import socket
import time


def send_udp_message(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(5)  # Set a timeout for waiting for a response
        sock.sendto(message.encode(), (ip, port))
        print(f"Sent message to {ip}:{port}")
        try:
            data, addr = sock.recvfrom(1024)
            print(f"Received response from {addr}: {data.decode()}")
        except socket.timeout:
            print(f"No response received from {ip}:{port}")


def main():
    device_ip = "10.0.50.31"  # Device IP address
    ports = [
        59101,
        63714,
        3334,
        3333,
        3335,
        6968,
        24,
    ]  # Ports identified from netstat output
    test_message = hex(0000000000000000)

    for port in ports:
        send_udp_message(device_ip, port, test_message)


if __name__ == "__main__":
    main()
