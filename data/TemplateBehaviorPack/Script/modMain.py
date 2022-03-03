# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi



@Mod.Binding(name="NeteaseMod_Temp", version="0.0.1")
class NeteaseMod_Temp(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def NeteaseMod_TempServerInit(self):
		serverApi.RegisterSystem("Template","TemplateServerSystem","Script.templateServerSystem.TemplateServerSystem")


	@Mod.DestroyServer()
	def NeteaseMod_TempServerDestroy(self):
		pass

	@Mod.InitClient()
	def NeteaseMod_TempClientInit(self):
		clientApi.RegisterSystem("Template","TemplateClientSystem","Script.templateClientSystem.TemplateClientSystem")

	@Mod.DestroyClient()
	def NeteaseMod_TempClientDestroy(self):
		pass
