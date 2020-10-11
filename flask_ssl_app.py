from flask import Flask
from flask_sslify import SSLify

"""
Option 1 : (pip install pyopenssl)
from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('web.key')
context.use_certificate_file('web.crt')

Option 2 : (OOB : No install)
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('web.crt', 'web.key')

Option 3 : Native Flask (No imports needed)
"""

app = Flask(__name__)

context = ('/etc/letsencrypt/live/rek.my.id/fullchain', '/etc/letsencrypt/live/rek.my.id/privkey.pem')
sslify = SSLify(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    context = ('/etc/letsencrypt/live/rek.my.id/fullchain', '/etc/letsencrypt/live/rek.my.id/privkey.pem')
    app.run( debug = True, ssl_context = context)
    #app.run( debug = True, ssl_context = 'adhoc')  # Generate Adhoc Certs
