# Import time library to have access to system time
import time
from socket import *

# Send 10 pings
for i in range(0,9):
    # Create a UDP socket for server
    clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set timeout for 1sec for reply
    clientSocket.settimeout(1)
    # Get hostname of localmachine
    host = socket.gethostname()
    # Reserve same port that server has binded to
    port = 12000
    # Start timer because round trip time starting
    t0 = time.time()

    # Set message 
    dayOfWeek = datetime.datetime.fromtimestamp(t0).strftime("%A")
    
    if dayOfWeek == "Monday":
        dayOfWeek = "M"
    elif dayOfWeek == "Tuesday":
        dayOfWeek = "T"
    elif dayOfWeek == "Wednesday":
        dayOfWeek = "W"
    elif dayOfWeek == "Thursday":
        dayOfWeek = "R"
    elif dayOfWeek == "Friday":
        dayOfWeek = "F"
    elif dayOfWeek == "Saturday":
        dayOfWeek = "S"
    elif dayOfWeek == "Sunday":
        dayOfWeek = "U"

    messagedate = datetime.datetime.fromtimestamp(t0).strftime("%Y-%m-%d")
    mesagetime = datetime.datetime.fromtimestamp(t0).strftime("%H:%M")
    message = "Ping" + " " + (i+1) + " " + messagedate + " " + dayOfWeek + " " + messagetime + " " + "UTC"
    # Send message
    clientSocket.sendto(message, (host, port))
    try:
        # Receive response from server
        modifiedMessage, server = clientSocket.recvfrom(1024)
        # Stop timer because round trip time done
        t1 = time.time()
        # Calculate print the round trip time in milliseconds of each packet if server respond
        rtt = t1 - t0
        # Abbreviate day of the week
        dayofweek = datetime.date.today().strftime("%A")
    
        # Print client ping + #, server response, and rtt
        print "%s\n" % (message)
        print "%s\n" % (modifiedMessage)
        print "RTT: %d\n" % (rtt)
    # If no response from server within timeout then print
    except socket.timeout:
        print "%s\n" % (message)
        print "Request timed out\n"
