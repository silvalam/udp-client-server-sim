# Authors: Sylvia Lam, Brian LaBar

# Import time library to have access to system time
from datetime import datetime
from socket import *

# Send 10 pings
for i in range(0,9):
    # Create a UDP socket for server
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # Set timeout for 1sec for reply
    clientSocket.settimeout(1)
    # Get hostname of localmachine
    host = "127.0.0.1"
    # Reserve same port that server has binded to
    port = 12000
    # Start timer because round trip time starting
    t0 = (datetime.now()).microsecond
    # Set message 
    dayOfWeek = datetime.now().strftime("%A")
    
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

    messagedate = datetime.now().strftime("%Y-%m-%d")
    messagetime = datetime.now().strftime("%H:%M")
    message = "Ping" + " " + str((i+1)) + " " + messagedate + " " + dayOfWeek + " " + messagetime + " " + "UTC"
    # Send message
    clientSocket.sendto(message, (host, port))
    try:
        # Receive response from server
        modifiedMessage, server = clientSocket.recvfrom(1024)
        # Stop timer because round trip time done
        t1 = (datetime.now()).microsecond
        # Calculate print the round trip time in milliseconds of each packet if server respond
        rtt = float(t1 - t0) / 1000
        # Print client ping + #, server response, and rtt
        print "%s" % (message)
        print "%s" % (modifiedMessage)
        print "RTT: %.3f\n" % (rtt)
    # If no response from server within timeout then print
    except timeout:
        print "%s" % (message)
        print "Request timed out\n"
