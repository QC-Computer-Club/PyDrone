'''
Created on Mar 11, 2014

@author: zim
'''

import socket
import threading
import time

class ServerSendThread(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self, clientsocket, clientaddress, webcam):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.socket = clientsocket
        self.address = clientaddress
        
    def run(self):
        while True:
            time.sleep(1)