print "MODELS"
from filereader import FileReader

class Mips():
	fr = FileReader()
	def read(self, filePath):
		self.fr.read(filePath)
		self.getInst(2)
	def getInst(self, i):
		instruction = self.fr.getInst(i)[0:32]
		return instruction
	def instructionFetch(i):
		instructionCode = self.getInst(i)[0:6]
		return instructionCode

	def instructionDecodeRegisterFetch(instructionCode, i):
		bits = self.getInst(i)
		if instructionCode == "000000": 
			s = bits[6:11]
			t = bits[11:16]
			if bits[21:32] == "00000100000"
				instruction = "add"
				d = bits(i)[16:21]
		elif instructionCode == "001000"
			s = bits[6:11]
			t = bits[11:16]
			imm = bits(i)[16:32]
		elif instructionCode == "000000" 
		
	def instructionExecute():
		pass

	def memoryAccess():
		pass

	def writeBack():
		pass
