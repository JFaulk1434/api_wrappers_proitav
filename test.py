import time
import socket
from zeroconf import ServiceBrowser, Zeroconf, ServiceStateChange, ServiceInfo


class MyListener:
    def __init__(self):
        self.devices = {}

    def remove_service(self, zeroconf, type, name):
        print(f"Service {name} removed")

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info:
            print(f"Service {name} added, service info: {info}")
            self.devices[name] = info

    def update_service(self, zeroconf, type, name):
        print(f"Service {name} updated")


def discover_brightsign_devices(duration=5):
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

    time.sleep(duration)
    zeroconf.close()

    devices_info = {}
    for name, device in listener.devices.items():
        ip_addresses = [socket.inet_ntoa(addr) for addr in device.addresses]
        properties = {
            key.decode("utf-8"): value.decode("utf-8")
            for key, value in device.properties.items()
        }
        serial_number = properties.get("serialnumber")
        devices_info[serial_number] = {
            "name": name,
            "addresses": ip_addresses,
            "properties": properties,
        }

    return devices_info


# Example usage
bright_sign_devices = discover_brightsign_devices()
print("Discovered BrightSign devices:")
for serial_number, device in bright_sign_devices.items():
    print(f"Serial Number: {serial_number}")
    print(f"Name: {device['name']}")
    print(f"Addresses: {device['addresses']}")
    print(f"Properties: {device['properties']}")
    print("-" * 40)
