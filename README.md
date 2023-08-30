# TCP Server with Protobuf Messages

This project demonstrates a simple TCP server that receives protobuf-encoded messages from clients and prints the message fields. 
The client application sends log messages using the `log_message_pb2` protobuf structure.

## Requirements

- Python 3.x
- Twisted library (for the server):</br>
  **pip install twisted**
- Protobuf installed with brew:</br>
**brew install protobuf**
- Downgrade protobuf using pip (to comply with task, which required using syntax = "proto2"):</br>
**pip install protobuf==3.20.***

## Project Structure

**server.py:**
Contains the Twisted server code that receives and processes incoming connections and protobuf-encoded messages.

**client.py:**
Contains the client code that sends log messages to the server using the log_message_pb2 structure.

**log_message.proto:**
The protobuf definition file for the LogMessage message structure.

**generated/:**
This directory contains the generated Python code from the log_message.proto file.
