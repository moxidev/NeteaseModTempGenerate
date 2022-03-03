'''
Author: moxi
Date: 2022-03-03 13:35:27
LastEditTime: 2022-03-03 14:56:17
Description: 

Copyright (c) 2022 by moxi/ICEJADE, All Rights Reserved. 
'''
# -*- coding: utf-8 -*-
from mod_log import logger as logger
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()


class TemplateServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        print('=================Server Running=======================')
        self.ListenEvents()

    def ListenEvents(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(
        ), "ServerItemUseOnEvent", self, self.OnServerItemUseOnEvent)

    def UnListenEvents(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(
        ), "ServerItemUseOnEvent", self, self.OnServerItemUseOnEvent)


    def Destroy(self):
        self.UnListenEvents()
