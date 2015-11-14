# DistMsg
DistMsg is a decentralized messaging protocol first prototyped at the Berlin Energy Hack Hackathon 2015

It is intended to bridge the gap in communications during a blackout event, or other similar catastrophe where communications will be lost

## Vectors of communication
The entire network is made of two kinds of nodes, users and servers. In a typical case, a user node is typically a PC or Mobile Phone, running the DistMsg app. The User may have cell, bluetooth, or wifi radios. The Server node is typically a battery-backed PC, such as a Raspberry Pi, which may have cell, bluetooth, HAM (APRS), Satellite, or long range point-to-point communication abilities.

Connections can be made user-to-user, server-to-user, or server-to-server.

## Message Types
There are three supported message types:

* Peer to Peer - This is from one user to a specific other user
* Broadcast message - This is from one user to any other user in a given area
* Official message - This is a message from one official source (hospital, fire services, government aid, etc.)

These messages are transported from user to user, user to server, and server to server whenever a connection occurs. 

## Message Prioritization
Due to the limited space to store messages on a Phone, PC, or Server, messages are kept based on priority, age, and location fencing. This allows the amount of data transferred to be lightweight, while still providing the most benefit possible
