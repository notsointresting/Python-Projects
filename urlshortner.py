import pyshorteners

url = "https://github.com/notsointresting/Python-Projects"

# Create a Shortener object
s = pyshorteners.Shortener()

# Use a specific service to shorten the URL
nw_url = s.tinyurl.short(url)

# Print the shortened URL
print(nw_url)
