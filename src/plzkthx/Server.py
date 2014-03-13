'''
Created on Mar 11, 2014

@author: zim
'''
import pygame
import pygame.camera
import socket
import threading
import plzkthx.ServerSendThread
import sys

class Server(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.hostname = "localhost"
        self.port = 45002
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.serversocket.bind((self.hostname, self.port))
            self.serversocket.listen(5)
            pygame.init()
            pygame.camera.init()
            cam_list = pygame.camera.list_cameras()
            self.webcam = pygame.camera.Camera(cam_list[0],(800,600))
            self.webcam.start()
        except:
            self.serversocket.close()
            self.webcam.stop()
            raise
            sys.exit()
        
    def run(self):
        while True:
            (clientsocket, clientaddress) = self.serversocket.accept()
            t = plzkthx.ServerSendThread.ServerSendThread(clientsocket, clientaddress, self.webcam)
            t.start()
            
        