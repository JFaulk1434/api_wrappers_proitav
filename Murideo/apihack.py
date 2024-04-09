import requests
import time

base_url = "http://10.0.10.96/do"

commands = [
    {"cmd": "c s eth0 static:010.000.010.096:255.255.255.000:010.000.010.001"},
    {"cmd": "c s eth0 dhcp"},
]

for command in commands:
    # Send POST request with the command
    response = requests.post(base_url, json=command)

    # Print the response status code and content
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.json())

    # Delay for 2 seconds before sending the next command
    time.sleep(3)
