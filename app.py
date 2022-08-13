from flask import Flask,jsonify,request
import time
import os

app = Flask(__name__)
@app.route("/bot",method=["POST"])

port = int(os.environ.get('PORT', 5000))
#response
def response():
   query=dict(request.form)['query']
   result = query+ " " + time.ctime()
   return jsonify({"response":result})

if __name__ == "__main__":
   app.run(host="0.0.0.0",)


app.run(host='0.0.0.0', port=port, debug=True)