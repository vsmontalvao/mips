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
# instrucao_estagio1="addi R10, R0, 100"

# fr = FileReader()
# fr.read("./instructions/program.txt")
# print "Arquivo program.txt carregado"






