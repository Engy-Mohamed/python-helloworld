from flask import Flask,json
import logging


app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('success Main request.')
    return "Hello World!"

@app.route("/status")
def status():
    app.logger.info('success status request.')
    return app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json')
   

@app.route("/metrics")
def metrics():
    app.logger.info('success metrics request.')
    return app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json')
    

if __name__ == "__main__":
    #config
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
