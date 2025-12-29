# Python TCP Socket Group Chat App

A simple **TCP-based group chat application** built using **Python sockets**.  
The project focuses on **network fundamentals** such as TCP full-duplex communication, connection handling, and message broadcasting — without using high-level async frameworks.

---

## Features

- TCP full-duplex communication
- Multiple clients supported
- Group chat (broadcast messages)
- Persistent TCP connections
- No external libraries
- No `asyncio` or frameworks
- Clear separation of server and client logic

---

## Technologies Used

- Python 3
- TCP sockets
- Thread-based concurrency (server-side)

---

---

## How It Works

- The **server** listens on a TCP port and accepts multiple client connections.
- Each client connection runs independently.
- When a client sends a message, the server **broadcasts** it to all connected clients.
- TCP provides reliable, ordered, full-duplex communication.Note: TCP natively supports full-duplex communication on a single connection.
> This project uses separate ports to simplify input/output handling and  demonstrate independent data flow management.
> Separate  port used in client side to avoide blocking input 
---

## Running the Application

### 1 Start the server

```bash
python messageserver.py
### 2 Start the client

```bash
python clientserver.py
