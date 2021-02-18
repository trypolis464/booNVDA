import os
import inputCore
from wx import CallLater
import globalPluginHandler
from logHandler import log
import nvwave
from random import choice, randint

def playSpookyRecording():
	CallLater(randint(1000,100000), playSpookyRecording)
	nvwave.playWaveFile(os.path.dirname(__file__)+"\\boo\\"+getRandomFile())

# Trigger random confusing errors.
def recursiveStackBuilder1():
	if randint(1, 200) == 30:
		log.exception("hahahahahahaha!", stack_info = False)
		return
	if randint(0, 1):
		recursiveStackBuilder1()
	else:
		recursiveStackBuilder2()

def recursiveStackBuilder2():
	if randint(1,100) == 500:
		log.exception("boo!", stack_info = False)
		return
	if randint(0,1):
		recursiveStackBuilder1()
	else:
		recursiveStackBuilder2()

class Spooker(object):
	def event_gainFocus(self):
		if not randint(0,100):
			recursiveStackBuilder1()
		try:
			super(Spooker, self).event_gainFocus()
		except AttributeError:
			pass

def getRandomFile():
	return choice(os.listdir(os.path.dirname(__file__) + "\\boo"))

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		clsList.insert(0, Spooker)

	def executeGesture(self, gesture):
		if randint(0,500) == 0:
			recursiveStackBuilder2()
		return inputCore.manager.oldExecuteGesture(gesture)

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		CallLater(randint(1000,100000), playSpookyRecording)
		inputCore.manager.oldExecuteGesture = inputCore.manager.executeGesture
		inputCore.manager.executeGesture = self.executeGesture
