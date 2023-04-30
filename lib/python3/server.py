import asyncio
import sys
import logging
import grpc
import time
import requests
import json
import aiohttp
import jwt
import datetime
import vk_api

import database as db
import UsersMicroservice_pb2 as pb2
import UsersMicroservice_pb2_grpc as pb2_grpc

class Listener(pb2_grpc.UsersServiceServicer):
    def __init__(self, config: dict, logger: logging.Logger):
        self.config = config
        self.logger = logger
        self.db = db.DatabaseManager(logger,
                              db_name=config["DataBase"]["name"],
                              db_user=config["DataBase"]["user"],
                              db_pass=config["DataBase"]["password"],
                              db_host=config["DataBase"]["host"],
                              db_port=config["DataBase"]["port"]
                              )

    async def AuthFromVK(self, request, context): 
        self.logger.info("AuthFromVK")
        
        uri_parts = self.config['AuthFromVK']
        requested_uri = uri_parts['getAccessTokenBaseURL'] + \
            	'?client_id=' + uri_parts['clientID'] + \
				'&client_secret=' + uri_parts['clientSecret']  + \
				'&redirect_uri=' + uri_parts['redirectURI'] + \
				'&code=' + request.authCode
        
        vk_resp = None
        async with aiohttp.ClientSession() as session:
            try:
                vk_resp = await session.get(requested_uri)
                vk_content = await vk_resp.text(encoding='UTF-8')
            except Exception as e:
                return pb2.AuthResponse(status=pb2.ExitStatus.FAILED_DEPENDENCY)

        self.logger.info("Recieved from VK: %s" % str(vk_resp.text))
        self.logger.info("Recieved content from VK: %s" % vk_content)
        if vk_resp.status == 200:
            try:
                vk_content_dict = json.loads(vk_content)
                
                vk_access_token = vk_content_dict['access_token']
                vk_user_id = vk_content_dict['user_id']

                user_id = self.db.getUserIDFromVKID(vk_user_id)
                
                self.logger.info(str(vk_user_id))

                if not user_id:
                    self.logger.info("Non-existent user with %d VK ID, registration." % vk_user_id)
                    vk = vk_api.VkApi(token=vk_access_token)
                    vk_user = vk.method("users.get", {"user_ids": vk_user_id})
                    vk_user_name = vk_user[0]['first_name']
                    
                    self.logger.debug("Received vk name: %s" % vk_user_name)

                    user_id = self.db.createUserAndReturnID(vk_user_name, vk_user_id)

                access_token = createJWT(user_id, self.config['Token']['secret'],
                                         self.config['Token']['algorithm'],
                                         self.config['Token']['accessTokenDuringLife']
                                         )
               
                refresh_token = createJWT(user_id, self.config['Token']['secret'],
                                          self.config['Token']['algorithm'],
                                          self.config['Token']['refreshTokenDuringLife'],
                                          True
                                          )
                
                token_pair = pb2.TokenPair(accessToken=access_token, 
                                           refreshToken=refresh_token)
                user_info = pb2.User(ID=user_id,
                                     nickname='Player1',
                                     isGuest=False,
                                     rating=100)

                self.logger.debug("Created JWT pair: %s(access) and %s(refresh)" % (access_token ,refresh_token))
                return pb2.AuthResponse(tokens=token_pair, userInfo=user_info)
            except Exception as e:
                self.logger.error("Creating JWT failed: %s" % str(e))
                return pb2.AuthResponse(status=pb2.ExitStatus.CODING_ERROR)
        else:
            return pb2.AuthResponse(status=pb2.ExitStatus.FAILED_DEPENDENCY)


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
