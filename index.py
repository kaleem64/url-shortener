from flask import Flask, request, redirect
import string
import random
import json
import os

app = Flask(__name__)

# Load existing data
if os.path.exists("urls.json"):
    with open("urls.json", "r") as f:
        url_store = json.load(f)
else:
    url_store = {}

# Save data function
def save_urls():
    with open("urls.json", "w") as f:
        json.dump(url_store, f)

# Generate short code
def short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/')
def home():
    return "URL Shortener Running..."

# Create short link
@app.route('/shorten')
def shorten():
    url = request.args.get('url')

    if not url:
        return "Use ?url=yourlink"

    code = short_code()
    url_store[code] = url
    save_urls()   # IMPORTANT LINE

    return f"Short URL: http://127.0.0.1:5000/{code}"

# Redirect
@app.route('/<code>')
def redirect_url(code):
    if code in url_store:
        return redirect(url_store[code])
    else:
        return "Not found", 404

#if __name__ == "__main__":
 #   app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    

    