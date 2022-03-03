'''
Author: moxi
Date: 2022-03-03 13:35:27
LastEditTime: 2022-03-03 14:56:14
Description: 

Copyright (c) 2022 by moxi/ICEJADE, All Rights Reserved. 
'''
# -*- coding: utf-8 -*-
from mod_log import logger as logger
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()

class TemplateClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        print('=================Client Running=======================')
        self.ListenEvents()

    def ListenEvents(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),"ClientItemUseOnEvent",self,self.OnClientItemUseOnEvent)                                                                                                
    
    def UnListenEvents(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),"ClientItemUseOnEvent",self,self.OnClientItemUseOnEvent)

    def OnClientItemUseOnEvent(self,args):
        pass

        

    def Destroy(self):
        self.UnListenEvents()
        pass