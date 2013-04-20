print "MODELS"
from filereader import FileReader

instrucao_estagio1="addi R10, R0, 100"

fr = FileReader()
fr.read("./instructions/program.txt")
print "Arquivo program.txt carregado"

def instructionFetch(i, filereader):
	instructionCode = filereader.getInst(i)[0:6]
	return instructionCode

def instructionDecodeRegisterFetch(instructionCode, i, filereader):
	bits = filereader.getInst(i)
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
	# addu $d, $s, $t
	elif instructionCode == "000000" 
	pass

def instructionExecute():
	pass

def memoryAccess():
	pass

def writeBack():
	pass
