from flask import Flask, request, make_response

import requests

app = Flask(__name__)

def add_cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "accept, authorization"


@app.route('/<path:path>', methods=['OPTIONS'])
def opts(path):
    resp = make_response()
    add_cors(resp)
    return resp

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route(path):

    url = "https://spreadsheets.google.com/" + path
    r = requests.request(request.method, url, data=request.data, headers = {
        "Authorization": request.headers["Authorization"],
        "Accept": request.headers["Accept"]
    })

    print
    print
    print "*********"
    print "%s: %s" % (request.method, path)
    print
    print request.headers

    print "Requesting %s" % url

    print
    print "Response: %s" % r.status_code

    print "*********"
    print
    print

    resp = make_response(r.text, r.status_code)

    for k in r.headers:
        resp.headers[k] = r.headers[k]

    add_cors(resp)

    return resp
if __name__ == "__main__":
    app.run(debug=True)