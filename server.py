from flask import Flask, request, jsonify
import socket
import shlex, subprocess

app = Flask(__name__)

cache= {'num' : 0}

@app.route('/' , methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'GET':
      return socket.gethostname()
   else:
      subprocess.Popen(["python3", "stress_cpu.py"] ) 
      return "success"

if __name__ == '__main__':
   app.run(host='0.0.0.0')