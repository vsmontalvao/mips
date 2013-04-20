print "MODELS"
from filereader import FileReader

class Mips():
	fr = FileReader()
	def read(self, filePath):
		self.fr.read(filePath)
		# self.getInst(2)
	def setView(view):
		self.view = view
	def getInst(self, i):
		instruction = self.fr.getInst(i)[0:32]
		return instruction
	def instructionFetch(i):
		pass

	def instructionDecodeRegisterFetch():
		pass

	def instructionExecute():
		pass

	def memoryAccess():
		pass

	def writeBack():
		pass

	def proxEstagio(self):
		if self.clock == None:
			self.clock = 0
		else:
			self.clock = self.clock + 1
		if self.pc == None:
			self.pc = 0
		else:
			self.pc = self.pc + 1
		print self.pc
		self.atualizarLabels()

	def atualizarLabels(self):
		if view != None:
			view.lclock["text"] = self.clock

