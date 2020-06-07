import os

sandbox_url = "https://sandbox.iexapis.com/stable/"
sandbox_sse_url = "https://sandbox-sse.iexapis.com/stable/"

base_url = "https://cloud.iexapis.com/stable/"
base_sse_url = "https://cloud-sse.iexapis.com/stable"

url = base_url
url_sse = base_sse_url

token = os.getenv("IEX_TOKEN")