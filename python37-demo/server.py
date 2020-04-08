import time
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/invoke', methods=['POST'])
def event_invoke():
    rid = request.headers.get('x-fc-request-id')
    print("FC Invoke Start RequestId: " + rid)
    
    # do your things
    data = request.stream.read()
    print(data)
    # ...
    
    print("FC Invoke End RequestId: " + rid)

    return data
