import trio
import sys
import logging
import grpc
import time
import requests

import UsersMicroservice_pb2
import UsersMicroservice_pb2_grpc

class Listener(UsersMicroservice_pb2_grpc.UsersServiceServicer):
    def __init__(self, config, logger):
        self.config = config
    
    def AuthFromVK(self, request, context): 
        pass

def run(config, logger):
    pass
