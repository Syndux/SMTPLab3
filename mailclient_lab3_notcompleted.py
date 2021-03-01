from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'localhost'
mailPort = 25
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,mailPort))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM: <lab@teamlucid.com>'
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptTo = 'RCPT TO: <lab2@teamlucid.com>'
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = 'DATA'
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end
# Send message data.
# Fill in start
message = input('Lab3 by Team Lucid')
# Fill in end
# Message ends with a single period.
# Fill in start
endMessage = '.'
clientSocket.send(message.encode() + endMessage.encode())
recv5 = clientSocket.recv(1024).decode()
if recv5[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitCmnd = 'QUIT'
clientSocket.send(quitCmnd.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
clientSocket.close()
sys.exit()
# Fill in end