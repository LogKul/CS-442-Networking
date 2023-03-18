import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

# Not required, but indicates server is running
print("Server initialized, listening for requests...")

while True:

    try:

        # Generate random number and capitalize client message
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()

        # Drop message if random number is 3 or lower
        if rand < 4:
            continue

        # Send response to client
        serverSocket.sendto(message, address)

    except:
        # This error-catching wasn't required, but I like it
        print("Internal server error. Closing...")
        break

# Close connection when while loop is finished
serverSocket.close()
