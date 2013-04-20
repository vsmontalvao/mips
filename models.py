print "MODELS"
from filereader import FileReader

instrucao_estagio1="addi R10, R0, 100"

fr = FileReader()
fr.read("./instructions/program.txt")
print "Arquivo program.txt carregado"

def InstructionFetch(i, filereader):
	instruction = filereader.getInst(i)[0:6]
	return instruction


