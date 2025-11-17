from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/')
def proxy():
    url = "https://48c68b5c3059f281.chal.ctf.ae/flag.txt"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://48c68b5c3059f281.chal.ctf.ae/",
        "Origin": "https://48c68b5c3059f281.chal.ctf.ae/"
    }
    r = requests.get(url, headers=headers)
    return Response(r.content, status=r.status_code, content_type="text/plain")

app.run(host='0.0.0.0', port=3000)
