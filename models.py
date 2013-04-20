print "MODELS"
from filereader import FileReader

class Estagio:
	def __init__(self, num):
		self.num = num
		self.InstName = str(num)+":"
		self.SinControle = ""

class Mips():
	fr = FileReader()
	clock = -1
	pc = -1
	E1 = Estagio(1)
	E2 = Estagio(2)
	E3 = Estagio(3)
	E4 = Estagio(4)
	E5 = Estagio(5)
	def read(self, filePath):
		self.fr.read(filePath)
		# self.getInst(2)
	def setView(self, view):
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
		self.clock = self.clock + 1
		self.pc = self.pc + 1
		print self.pc
		self.atualizarLabels()

	def atualizarLabels(self):
		if self.view != None:
			self.view.lclock["text"] = self.clock
			self.view.E1_instrucao["text"] = self.E1.InstName
			self.view.E2_instrucao["text"] = self.E2.InstName
			self.view.E3_instrucao["text"] = self.E3.InstName
			self.view.E4_instrucao["text"] = self.E4.InstName
			self.view.E5_instrucao["text"] = self.E5.InstName
			self.view.E1_controle["text"] = self.E1.SinControle
			self.view.E2_controle["text"] = self.E2.SinControle
			self.view.E3_controle["text"] = self.E3.SinControle
			self.view.E4_controle["text"] = self.E4.SinControle
			self.view.E5_controle["text"] = self.E5.SinControle		


