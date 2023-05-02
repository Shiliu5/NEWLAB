import ping3

hostname = "www.google.com"
response_time = ping3.ping(hostname)

if response_time is not None:
    print(f"Response time for {hostname}: {response_time} ms")
else:
    print(f"No response from {hostname}")
