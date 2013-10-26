from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple
import pickle, mimetypes, socket
from time import sleep

import json
import os

def application(environ, start_response):
	request = Request(environ)
	response = Response(open("viz.html",'rb').read(),mimetype=mimetypes.guess_type("index.html")[0])
	return response(environ, start_response)
	

if __name__ == '__main__':
	run_simple('0.0.0.0', 8888, application)