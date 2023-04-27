import asyncio
import sys
import logging
import grpc
import time
import requests
import json
import aiohttp
import jwt

import UsersMicroservice_pb2 as pb2
import UsersMicroservice_pb2_grpc as pb2_grpc

class Listener(pb2_grpc.UsersServiceServicer):
    def __init__(self, config: dict, logger: logging.Logger):
        self.config = config
        self.logger = logger

    async def AuthFromVK(self, request, context): 
        self.logger.info("AuthFromVK")
        
        uri_parts = config['AuthFromVK']
        requested_uri = uri_parts['getAccessTokenBaseURL'] + \
            	'?client_id=' + uri_parts['clientID'] + \
				'&client_secret=' + uri_parts['clientSecret']  + \
				'&redirect_uri=' + uri_parts['redirectURI'] + \
				'&code=' + request.authCode
        
        vk_resp = None
        async with aiohttp.ClientSession() as session:
            try:
                vk_resp = await session.get(requested_uri)
            except Exception as e:
                return pb2.AuthResponse(statusCode=3)

        logger.info("Recieved from vk %s" % str(vk_resp.text))
        if vk_resp.status_code == 200:
            try:
                vk_resp_dict = json.loads(vk_resp.text(encoding='UTF-8'))
                
                user_id = vk_resp_dict['user_id']

                access_token = createJWT(user_id, self.config['Token']['secret'],
                                         self.config['Token']['algorithm'],
                                         self.config['Token']['accessTokenDuringLife']
                                         )
               
                refresh_token = createJWT(user_id, self.config['Token']['secret'],
                                          self.config['Token']['algorithm'],
                                          self.config['Token']['refreshTokenDuringLife'],
                                          True
                                          )

                logger.debug("Created JWT pair: %s(access) and %s(refresh)" % (access_token ,refresh_token))
                return pb2.AuthResponse(statusCode=0, tokens=pb2.TokenPair(accessToken=access_token, refreshToken=refresh_token))

            except Exception as e:
                logger.error("Creating JWT failed: %s" % str(e))
                return pb2.AuthResponse(statusCode=2)
        else:
            return pb2.AuthResponse(statusCode=1)


def createJWT(user_id: int, secret: str, algorithm: str, time_units: int, is_refresh: bool = False):
    delta = datetime.timedelta(minutes=time_units if not is_refresh else 0,
                               days=time_units if is_refresh else 0)
    now = datetime.datetime.now()
    expires_at = (now + delta).strftime('%m/%d/%Y %H:%M:%S')

    payload = {'userID': user_id, 
               'expiresAt': expires_at, 
               'type': 'refresh' if is_refresh else 'access'
    }
    
    return jwt.encode(payload, secret, algorithm)


async def serve(config: dict, logger: logging.Logger) -> None:
    server = grpc.aio.server()
    listener = Listener(config, logger)
    pb2_grpc.add_UsersServiceServicer_to_server(listener, server)
    listen_addr = '[::]:' + str(config['gRPC']['port'])
    server.add_insecure_port(listen_addr)
    logger.info('Starting server on %s', listen_addr)
    await server.start()
    await server.wait_for_termination()


def run(config: dict, logger: logging.Logger) -> None:
    asyncio.run(serve(config, logger))
