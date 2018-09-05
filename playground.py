import requests

# Server to connect
server = "http://api.open-notify.org/"

# End point to connect
endpoint = "iss-now.json" 

# Generate the request
response = requests.get(server+endpoint)

# Print request
print(" - API PLAYGROUND | Request: ", response)