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
		if instructionCode == "000010"
			self.address = bits[6:32]
		elif
			self.s = bits[6:11]
			self.t = bits[11:16]
			if instructionCode == "000000": 
				self.d = bits(i)[16:21]
				self.shamt = bits(i)[21:26]
				if bits[26:32] == "100000"
					self.instruction = "Add"
				elif bits[26:32] == "011000"
					self.instruction = "Mul"
				elif bits[26:32] == "000000"
					self.instruction = "Nop"
				elif bits[26:32] == "100010"
					self.instruction = "Sub"
			else
				self.immediate = bits[16:32]
				if instructionCode == "001000"
					self.instruction = "Addi"
				elif instructionCode == "000101"
					self.instruction = "Beq"
				elif instructionCode == "000111"
					self.instruction = "Ble"	
				elif instructionCode == "000100"
					self.instruction = "Bne"
				elif instructionCode == "100011"
					self.instruction = "Lw"
				elif instructionCode == "101011"
					self.instruction = "Sw"
		
	def instructionExecute():
		pass

	def memoryAccess():
		pass

	def writeBack():
		pass
