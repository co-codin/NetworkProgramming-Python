import socket
import threading
from queue import Queue

target = 'flatium.ru'
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port  = queue.get()
        if portscan(port):
            print("Port {} is open.".format(port))
            open_ports.append(port)

