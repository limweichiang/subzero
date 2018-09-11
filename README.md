# Overview
subzero.py is a quick/dirty Python script to subscribe to a 0MQ publisher feed and output it in JSON format.

# Command Options
--zmq-server ZMQ_SERVER
    0MQ server address (default=localhost)

--zmq-port ZMQ_PORT
    0MQ server port (default=5555)

--zmq-topic ZMQ_TOPIC
    0MQ topics to subscribe to, comma delimited string, no spaces (default=all)

    
# Example
python3 subzero.py --zmq-server 192.168.1.1 --zmq-port 5566 --zmq-topic topic1,topic2,topic3,topic4
