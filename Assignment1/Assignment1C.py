# Queens College
# Internet and Web Technology  (CSCI 355)
# Winter 2024
# Assignment 1c - Socket Program Client
# Brandon Prophete
# Worked with Class

import sys
import socket

# [2] Define a function binary_address() to convert your IP Address from “dotted decimal notation” to a 32-bit binary string.
# First, split the dotted decimal notation into four numbers, then find the binary equivalent of each and concatenate them back together. Be sure to remove the "0b" prefix of the binary numbers and to pad each component to 8 binary digits. When you are done, your binary address should be exactly 32  characters long.
# See https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
# and https://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python

def binary_address(ip_address):
    octets = ip_address.split('.')
    binary = "".join([bin(int(octet))[2:].zfill(8) for octet in octets])
    return binary

# [3] Write a function to determine if the address is Class A, B, C, D or E by examining the first few bits of the 32-bit string.
# See https://en.wikipedia.org/wiki/Classful_network

def get_class(bin_address):
      cls = ""
      if bin_address[0:1] == "0":
          cls = "A"
      elif bin_address[0:2] == "10":
          cls = "B"
      elif bin_address[0:3] == "110":
          cls = "C"
      elif bin_address[0:4] == "1110":
          cls = "D"
      elif bin_address[0:4] == "1111":
          cls = "E"
      return cls

# [4] Define a function port_type(port) to determine the type of port number. The options are:
# 0-1023: Well-Known
# 1024-49151: Registered
# 49152-65535: Dynamic/Private
# See https://en.wikipedia.org/wiki/Port_(computer_networking)
def port_type(port):
    pt = "?"
    if 0 <= port < 1024:
        pt = "Well-Known"
    elif 1024 <= port < 49152:
        pt = "Registered"
    elif 49152 <= port < 65536:
        pt = "Dynamic/Private"
    return pt

# [5] Write a function to connect to the Google server
# https://www.geeksforgeeks.org/socket-programming-python/
# An example script to connect to Google using socket programming in Python import socket # for socket
def connect_to_server(domain_name, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    try:
        host_ip = socket.gethostbyname(domain_name)
    except socket.gaierror:
        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()

    # connecting to the server
    s.connect((host_ip, port))

    print("The socket has successfully connected to", domain_name, "on port", port)
    s.close()

# [7] Write a programs Assignment2Client.py that will talk to that server

def connect_to_server_v2(ip_addr, port):
    s = socket.socket()
    if ip_addr.count(".") != 3:
        ip_addr = socket.gethostbyname(ip_addr)
    s.connect((ip_addr, port))
    msg = s.recv(2048).decode()
    print(msg)
    s.close()


# [1] Define a function get_host_info() to determine your computer's IP address.
def get_host_info():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    binary = binary_address(ip_addr)
    cls = get_class(binary)
    port_num = 125
    pt = port_type(port_num)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + ip_addr)
    print("The binary version is", binary, len(binary))
    print("The class type is", cls)
    print("The port number is", port_num, "The port type", pt)

def main():
    get_host_info()
    # Connecting to Web server
    connect_to_server("www.google.com", 80)
    # Quote of the day: returns a quote
    connect_to_server_v2("djxmmx.net", 17)
    # Looks to server to ge the date
    connect_to_server_v2("ntp-b.nist.gov", 13)
    # Connects to our server
    connect_to_server_v2("192.168.1.183", 12345)

if __name__ == "__main__":
    main()