# Overview

This program sends and recievces data with a client server network. The client inputs a file that they want to transfer and then is sent to the server that stores the file. To start the client we run the client file that will display the GUI that can connect and choose the file to send. The server is started by running the server file that will then listen for any ip address that is trying to connect. When the server sees the client it connects and the file transfer process begins and when it is done the connection is closed. 

I wrote this software to learn more about the way that networking works and how I could utilize it to transfer files. I also wanted to see how I could use networking so that two computers could communicate with each other over a private network connection. 


[Software Demo Video](https://youtu.be/8ocXWQbdRlc)

# Network Communication

## Architecture
* client/server

## Protocol and Port used
* TCP 
* PORT Number 5500

## Message Format
* The format of the messages is byte code that is encoded with the client and then decoded when the server receive the file. 

# Development Environment

* Visual Studio Code

* Python 3.9.5
* socket libarary

# Useful Websites

* [Tutorials Point](https://www.tutorialspoint.com/python/python_networking.htm)
* [Real Python](https://realpython.com/python-sockets/)

# Future Work

* Add a server side GUI that displays the file that was transfered
* Add more UI elements that improve the look of the GUI
* Explore other ways to send files and what the best method is