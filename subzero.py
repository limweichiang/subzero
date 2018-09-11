#!/usr/bin/python3
#
#   Copyright 2018 Lim Wei Chiang
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import json
import argparse
import zmq

# Set up CLI options and input
parser = argparse.ArgumentParser(description="0MQ client")
parser.add_argument("--zmq-server", help="0MQ server address (default=localhost)")
parser.add_argument("--zmq-port", help="0MQ server port (default=5555)")
parser.add_argument("--zmq-topic", help="0MQ topics to subscribe to, comma delimited string, no spaces (default=all)")
args = parser.parse_args()

# Set 0MQ connection targets
zmq_server = args.zmq_server if args.zmq_server is not None else "localhost"
zmq_port = args.zmq_port if args.zmq_port is not None else "5555"
zmq_connect_target = "tcp://" + zmq_server + ":" + zmq_port

# Compile 0MQ topics for subscription
if args.zmq_topic is not None:
	zmq_topic = args.zmq_topic.split(",")
else:
	zmq_topic = [""]

#  Prepare 0MQ context and sockets
context = zmq.Context()
zmq_socket = context.socket(zmq.SUB)
zmq_socket.connect(zmq_connect_target)

for t in zmq_topic:
	zmq_socket.subscribe(t)

# Start reading
while zmq_socket.closed is not True:
	try:
		msg = zmq_socket.recv()	
		(msg_topic, msg_payload) = msg.decode("utf-8").split("\n", 1)
		msg_json = json.loads(msg_payload)
		print(json.dumps(msg_json, indent=4))
	except KeyboardInterrupt:
		zmq_socket.disconnect(zmq_connect_target)
		zmq_socket.close()

# The end
print("\nShutting down, goodbye!")

