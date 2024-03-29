from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple
import pickle, mimetypes, socket
from time import sleep

import json
import os

#this is thread-unsafe (but this is a single thread server, so don't make it multithreaded)
#I'm not sure how this doesn't complain about never closing the file
def application(environ, start_response):
	request = Request(environ)
	sid = pickle.load(open("global"))
	if request.method == "POST":
		response = Response(str(sid))
		params = request.form["params"]
		email = request.form["email"]
		low_env = request.form["low_env"]
		high_env = request.form["high_env"]
		probedata = request.form["probedata"]
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_socket = sock.connect(('localhost', 8083))
		sock.sendall(pickle.dumps([sid,email,params,probedata,low_env,high_env]))
	else:
		response = Response(open("index.html",'rb').read(),mimetype=mimetypes.guess_type("index.html")[0])
	pickle.dump(sid+1,open("global","wb"))
	return response(environ, start_response)
	

if __name__ == '__main__':
	run_simple('0.0.0.0',8082, application)