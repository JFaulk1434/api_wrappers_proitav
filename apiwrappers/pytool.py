#!/usr/local/bin/python3

# pylint: disable=W0718:broad-exception-caught
# pylint: disable=C0301:line-too-long

"""
    This is a python query tool
"""

import sys
import os
import getopt
import socket
import select
import struct
import subprocess
import re
import platform

# Global constants
VERSION = "1.0.0"
QUERY_PORT = 3333
QUERY_ADDR = "225.1.0.0"


def find_all_ip():
    """Find all IP addresses in the OS"""
    _platform = platform.system()
    ip_str = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    if _platform == "Darwin" or _platform == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile(f"(inet {ip_str})")
        pattern = re.compile(ip_str)
        ip_list = []
        for ip_addr in re.finditer(ip_pattern, str(output)):
            ip_addr = pattern.search(ip_addr.group())
            if ip_addr.group() != "127.0.0.1":
                ip_list.append(ip_addr.group())
        return ip_list
    elif _platform == "Windows":
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile(f"IPv4 .*: {ip_str}")
        pattern = re.compile(ip_str)
        ip_list = []
        for ip_addr in re.finditer(ip_pattern, str(output)):
            ip_addr = pattern.search(ip_addr.group())
            if ip_addr.group() != "127.0.0.1":
                ip_list.append(ip_addr.group())
        return ip_list
    else:
        return []


def search_nodes(query_port=QUERY_PORT, regular_expression=None):
    """Search all units and store them in a dictionary"""
    nodes = {}
    sock_rcv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_rcv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_rcv.bind(("0.0.0.0", query_port + 1))
    sock_rcv.setblocking(0)  # Non-blocking

    i = 0
    while i < 3:
        # Send query from each local network interface
        for ip_addr in find_all_ip():
            sock_snd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock_snd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock_snd.bind((ip_addr, 0))
            try:
                sock_snd.sendto(struct.pack("ii", 0, 0), (QUERY_ADDR, query_port))
            except socket.error as err:
                print("send failed", err)
                exit(1)
            sock_snd.close()
        # Now wait for replies from all units
        while True:
            events = select.select([sock_rcv], [], [], 0.1)

            # Timeout
            if not events[0]:
                break

            # Reply received
            while True:
                try:
                    data, addr = sock_rcv.recvfrom(1024)
                except socket.error:  # Received all packets
                    break
                try:
                    struct_data = struct.unpack("ii32s64s32s16s144s", data)
                except Exception:
                    pass  # Not available packet
                else:
                    # key: dev_name, val: (dev_name, address, status, model, version)
                    try:
                        status = struct_data[2].split(b"\x00")[0].decode()
                    except UnicodeDecodeError:
                        status = "n/a"
                    if not status:
                        status = "n/a"

                    try:
                        dev_name = struct_data[3].split(b"\x00")[0].decode()
                    except UnicodeDecodeError:
                        dev_name = "n/a"
                    if not dev_name:
                        dev_name = "n/a"

                    try:
                        model = struct_data[4].split(b"\x00")[0].decode()
                    except UnicodeDecodeError:
                        model = "n/a"
                    if not model:
                        model = "n/a"

                    try:
                        version = struct_data[5].split(b"\x00")[0].decode()
                    except UnicodeDecodeError:
                        version = "n/a"
                    if not version:
                        version = "n/a"

                    if model == "n/a":
                        version = "n/a"

                    try:
                        if regular_expression and (
                            not re.search(rf"{regular_expression}", dev_name)
                        ):
                            continue
                        nodes[dev_name] = (
                            dev_name,
                            addr[0],
                            status,
                            model,
                            version,
                        )
                    except re.error as err:
                        print(f"Bad device type: {err}")
                        exit(-1)
        i += 1
    sock_rcv.close()
    return nodes


def printhelp():
    """Print the help/usage message"""
    print(f" usage: {os.path.split(sys.argv[0])[1]} [-hv] [-e REGEXP]")
    print("")
    print("        -h | --help          show this message")
    print("")
    print("        -v | --version       show the version message")
    print("")
    print("        -e REGEXP | --regular-expression=REGEXP")
    print("                             only show matching devices")
    print("")


def printversion():
    """Print the version message"""
    print(f"{os.path.split(sys.argv[0])[1]} version {VERSION}")


def getoptions(options):
    """Process the command line options"""
    regular_expression = ""
    for name, value in options:
        if name in ("-h", "--help"):
            printhelp()
            sys.exit()
        if name in ("-v", "--version"):
            printversion()
            sys.exit()
        if name in ("-e", "--regular-expression"):
            regular_expression = value
    return regular_expression


def main():
    """The main function"""
    regular_expression = ""

    try:
        options, args = getopt.getopt(
            sys.argv[1:],
            "hve:",
            [
                "help",
                "version",
                "regular-expression=",
            ],
        )
    except getopt.GetoptError as error:
        print(error.msg)
        print(
            f"use '{os.path.split(sys.argv[0])[1]}' -h' or '{os.path.split(sys.argv[0])[1]}' --help' for help information"
        )
        sys.exit()

    if args:
        print("unsupported args: ", args)
        print(
            f"use '{os.path.split(sys.argv[0])[1]}' -h' or '{os.path.split(sys.argv[0])[1]}' --help' for help information"
        )
        sys.exit()

    regular_expression = getoptions(options)

    nodes = search_nodes(QUERY_PORT, regular_expression)

    print("")
    print(
        "SEQ    HOSTNAME                ADDRESS            MODEL/ALIAS             VER           STATUS",
    )
    print(
        "===    ====================    ===============    ====================    ==========    ===========",
    )

    sorted_host = []
    seq = 0
    for key, val in sorted(nodes.items()):
        # key: dev_name, val: (dev_name, address, status, model, version)
        print(
            f"{seq:3}",
            f"   {key:<20}",
            f"   {val[1]:<15}",
            f"   {val[3]:<20}",
            f"   {val[4]:<10}",
            f"   {val[2]:<9}",
        )
        sorted_host.append(val)
        seq += 1

    print(
        "==================================================================================================="
    )
    print("")


if __name__ == "__main__":
    # main()
    print(search_nodes())
