# subzero
subzero.py is a quick/dirty Python script to subscribe to a 0MQ publisher feed and output it in JSON format.

# Command Options
-s SERVER, --server SERVER
    0MQ server address (default=localhost)
    
-p PORT, --port PORT
    0MQ server port (default=5555)
    
-t TOPICS, --topics TOPICS
    0MQ topics to subscribe to, comma delimited string, no spaces (default=all)
    
# Example
python3 subzero.py -s 192.168.1.1 -p 5566 -t topic1,topic2,topic3,topic4
