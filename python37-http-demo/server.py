import time
from flask import Flask
from flask import request

app = Flask(__name__)

REQUEST_ID_HEADER = 'x-fc-request-id'


@app.route('/', methods=['GET'])
def hello_world():
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    # do your things
    print("FC Invoke End RequestId: " + rid)
    return 'Hello World!'

@app.route('/info', methods=['GET'])
def info():
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    # do your things
    print("FC Invoke End RequestId: " + rid)
    return 'test info'

@app.route('/event', methods=['POST'])
def event():
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)

    # do your things
    data = request.stream.read()
    print(data)
    # ...

    print("FC Invoke End RequestId: " + rid)

    return data

class CustomProxyFix(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        host = environ.get('HTTP_HOST', '')
        region = environ.get('HTTP_X_FC_REGION', '')
        uid = environ.get('HTTP_X_FC_ACCOUNT_ID', '')
        serviceName = environ.get('HTTP_X_FC_SERVICE_NAME', '')
        functionName = environ.get('HTTP_X_FC_FUNCTION_NAME', '')
        # print(" host=" + str(host) + 
        #     "; region=" + str(region) + 
        #     "; uid=" + str(uid) + 
        #     "; serviceName=" + str(serviceName) + 
        #     "; functionName=" + str(functionName)
        #     )
        if host == "{0}.{1}.fc.aliyuncs.com".format(uid, region):
            environ['SCRIPT_NAME'] = "/2016-08-15/proxy/{0}/{1}".format(serviceName, functionName)
            environ['PATH_INFO'] = environ['PATH_INFO'].replace(environ['SCRIPT_NAME'], "")
            print(environ)
        return self.app(environ, start_response)

app.wsgi_app = CustomProxyFix(app.wsgi_app)