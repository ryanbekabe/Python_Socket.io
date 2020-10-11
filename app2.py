from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
   def index():
   return 'Flask is running!'
@app.route('/data')
   def names():
   data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
   return jsonify(data)
if __name__ == '__main__':
   app.run(ssl_context=('/etc/letsencrypt/live/rek.my.id/fullchain', '/etc/letsencrypt/live/rek.my.id/privkey.pem'))

#from flask import Flask
#app = Flask(__name__)
#app.run('107.173.229.88', debug=True, port=8100, ssl_context=('/etc/letsencrypt/live/rek.my.id/fullchain', '/etc/letsencrypt/live/rek.my.id/privkey.pem'))

