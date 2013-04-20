print "MODELS"
from filereader import FileReader

class Mips():
	fr = FileReader()
	pc = 0
	def read(self, filePath):
		self.fr.read(filePath)
		# self.getInst(2)
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
		self.pc = self.pc + 1
		print self.pc

