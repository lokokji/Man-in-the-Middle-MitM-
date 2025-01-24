import requests

# Monitor atau log request dan response
def log_request_response(url):
    response = requests.get(url)
    print(f"Request URL: {url}")
    print(f"Response: {response.text}")

log_request_response('http://example.com')
