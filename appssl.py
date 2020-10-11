from flask import Flask, jsonify


from OpenSSL import SSL
context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('/etc/letsencrypt/live/rek.my.id/privkey.pem')
context.use_certificate_file('/etc/letsencrypt/live/rek.my.id/fullchain')




app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is running!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


#if __name__ == '__main__':
#    app.run()
if __name__ == '__main__':  
     app.run(host='107.173.229.88', debug=True, ssl_context=context)
