print "MODELS"
from filereader import FileReader

class Registrador:
	def __init__(self):
		self.valor = 0
		self.bloqueado = False

	def bloquear(self):
		self.bloqueado = True

	def desbloquear(self):
		self.bloqueado = False

class InstrucaoR:
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.rs = bin(eval("0b"+instrucao[6:11]))
		self.rt = bin(eval("0b"+instrucao[11:16]))
		self.rd = bin(eval("0b"+instrucao[16:21]))
		self.shamt = bin(eval("0b"+instrucao[21:26]))

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			self.mips.E2.bloquear()
		else:
			self.mips.A = self.mips.reg[eval(self.rs)].valor
			self.mips.B = self.mips.reg[eval(self.rt)].valor
			self.mips.reg[eval(self.rd)].bloquear()
			self.mips.shamt = self.shamt

	def memaccess(self):
		pass

	def writeback(self):
		self.mips.reg[eval(self.rd)].valor = self.mips.ULA
		self.mips.reg[eval(self.rd)].desbloquear()
		if self.mips.E2.bloqueado:
			self.mips.E2.desbloquear()

class InstrucaoI:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.rs = bin(eval("0b"+instrucao[6:11]))
		self.rt = bin(eval("0b"+instrucao[11:16]))
		self.immediate = bin(eval("0b"+instrucao[16:32]))	

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			self.mips.E2.bloquear()
		else:
			self.mips.A = self.mips.reg[eval(self.rs)].valor
			self.mips.B = self.mips.reg[eval(self.rt)].valor
			self.mips.Imm = self.immediate

class InstrucaoJ:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.targetAddress = bin(eval("0b"+instrucao[6:32]))

class Jmp(InstrucaoJ):
	
	def __init__(self, mips, instrucao):
		InstrucaoJ.__init__(self, mips, instrucao)

	def decode(self):
		mips.E1.bloquear()
		mips.E1.avancapc = False

	def execute(self):
		pass

	def memaccess(self):
		mips.pc = self.targetAddress
		mips.E1.desbloquear()

	def writeback(self):
		pass

	def texto(self):    
		return "jmp" + str(eval(self.targetAddress))

class Add(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = bin(self.mips.A + self.mips.B)

	def texto(self):
		return "add R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Mul(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = bin(self.mips.A * self.mips.B)

	def texto(self):
		return "mul R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Nop(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def decode(self):
		pass

	def execute(self):
		pass

	def memaccess(self):
		pass

	def writeback(self):
		pass 

	def texto(self):
		return "nop"

class Sub(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = bin(self.mips.A - self.mips.B)

	def texto(self):
		return "sub R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Addi(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		InstrucaoI.decode()
		self.mips.reg[eval(self.rt)].bloquear()

	def execute(self):
		self.mips.ULA = bin(self.mips.A + self.mips.Imm)

	def memaccess(self):
		pass

	def writeback(self):
		self.mips.reg[eval(self.rt)].valor = self.mips.ULA
		self.mips.reg[eval(self.rt)].desbloquear()

	def texto(self):
		return "addi R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Beq(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		mips.E1.bloquear()
		InstrucaoI.decode()

	def execute(self):
		self.equal = False
		if eval(self.mips.reg[eval(self.mips.A)].valor) == eval(self.mips.reg[eval(self.mips.B)].valor):
			self.equal = True
			self.mips.ULA = bin(eval(self.mips.pc) + 4 + eval(self.mips.Imm))

	def memacess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA
			mips.E1.avancapc = False
		else:
			mips.E1.avancapc = True
		mips.E1.desbloquear()

	def writeback(self):
		pass

	def texto(self):
		return "beq R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Ble(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		mips.E1.bloquear()
		InstrucaoI.decode()

	def execute(self):
		self.equal = False
		if eval(self.mips.reg[eval(self.mips.A)].valor) <= eval(self.mips.reg[eval(self.mips.B)].valor):
			self.equal = True
			self.mips.ULA = bin(eval(self.mips.Imm))      

	def memacess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA
			mips.E1.avancapc = False
		else:
			mips.E1.avancapc = True
		mips.E1.desbloquear()

	def writeback(self):
		pass

	def texto(self):
		return "ble R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))  

class Bne(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		mips.E1.bloquear()
		InstrucaoI.decode()

	def execute(self):
		self.equal = False
		if eval(self.mips.reg[eval(self.mips.A)].valor) != eval(self.mips.reg[eval(self.mips.B)].valor):
			self.equal = True
			self.mips.pc = bin(eval(self.mips.pc) + 4 + eval(self.mips.Imm))

	def memacess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA
			mips.E1.avancapc = False
		else:
			mips.E1.avancapc = True
		mips.E1.desbloquear()

	def writeback(self):
		pass

	def texto(self):
		return "bne R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Lw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		InstrucaoI.decode()
		if self.mips.reg[eval(self.rt)].bloqueado:
			self.mips.E2.bloquear()
		else:
			self.mips.reg[eval(self.rt)].bloquear()
			self.resultado = self.mips.mem[eval(self.mips.reg[eval(self.rs)]) + self.mips.Imm]

	def execute(self):
		pass

	def writeback(self):
		self.mips.reg[eval(self.rt)].valor = self.resultado
		self.mips.reg[eval(self.rt)].desbloquear()

	def texto(self):
		return "lw R" + str(eval(self.rs)) + ", "+str(eval(self.immediate))+"("+str(eval(self.rt)) + ")"
class Sw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):	
		InstrucaoI.decode()
		self.destino = 	self.mips.reg[eval(self.rs)] + self.mips.Imm
		if self.mips.mem[self.destino].bloqueado:
			self.mips.E2.bloquear()
		else:
			self.mips.mem[self.destino].bloquear()
			self.resultado = self.mips.reg[eval(self.rt)]

	def execute(self):
		pass

	def memaccess(self):
		self.mips.mem[self.destino].valor = self.resultado
		self.mips.mem[self.destino].desbloquear()

	def texto(self):
		return "sw R" + str(eval(self.rs)) + ", "+str(eval(self.immediate))+"("+str(eval(self.rt)) + ")"

class Estagio:
	def __init__(self, num, mips):
		self.num = num
		self.SinControle = ""
		self.mips = mips
		self.bloqueado = False
		self.setNop()
		self.saida = 0
		self.passarInstrucao = True

	def desbloquear(self):
		self.bloqueado = False

	def bloquear(self):
		self.bloqueado = True

	def setNop(self):
		self.setInstrucao(Nop(self.mips, "0"*32))

	def setInstrucao(self, instrucao):
		self.instrucao = instrucao
		self.InstName = "l" + str(self.num) + ": " + self.instrucao.texto()

class InstructionFetch(Estagio):

	def __init__(self, num, mips):
		Estagio.__init__(self, num,  mips)

	def do(self, i):
		self.bloquear()
		inst = self.mips.fr.getInst(i)[0:32]
		self.desbloquear()
		return inst

class InstructionDecodeRegisterFetch(Estagio):

	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def decodInst(self, instrucao):
		instructionCode = instrucao[0:6]
		if instructionCode == "000010":
			instrucaoDecodificada = Jmp(self.mips, instrucao) 
		else:
			if instructionCode == "000000":
				if instrucao[26:32] == "100000":
					instrucaoDecodificada = Add(self.mips, instrucao)
				elif instrucao[26:32] == "011000":
					instrucaoDecodificada = Mul(self.mips, instrucao)
				elif instrucao[26:32] == "000000":
					instrucaoDecodificada = Nop(self.mips, instrucao)
				elif instrucao[26:32] == "100010":
					instrucaoDecodificada = Sub(self.mips, instrucao)
			else:
				if instructionCode == "001000":
					instrucaoDecodificada = Addi(self.mips, instrucao)
				elif instructionCode == "000101":
					instrucaoDecodificada = Beq(self.mips, instrucao)
				elif instructionCode == "000111":
					instrucaoDecodificada = Ble(self.mips, instrucao)
				elif instructionCode == "000100":
					instrucaoDecodificada = Bne(self.mips, instrucao)
				elif instructionCode == "100011":
					instrucaoDecodificada = Lw(self.mips, instrucao)
				elif instructionCode == "101011":
					instrucaoDecodificada = Sw(self.mips, instrucao)

		return instrucaoDecodificada

	def do(self):
		self.bloquear()
		self.instrucao.decode()
		self.desbloquear()
		return self.instrucao

class InstructionExecute(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)
		self.cont = 0

	def do(self):
		self.bloquear()
		if self.instrucao.__class__.__name__ == 'Mul':
			if self.cont == 0:
				self.instrucao.execute()
				self.cont = 1
			else:
				self.desbloquear()

class MemoryAccess(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self):
		self.bloquear()
		self.instrucao.memaccess()
		self.desbloquear()

class WriteBack(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self):
		self.bloquear()
		self.instrucao.writeback()
		self.debloquear()

class Mips:
	def __init__(self):
		self.inicio()
		self.fr = FileReader()   
		self.mem = [Registrador()] * 2**15 # vc pode checar o tamanho com len(self.mem) e acessar cada posicao
							   # independentemente com self.mips.mem[i] dai para manipular os 32 bits podemos
							   # mexer com os valores binarios e decimais
		self.reg = [Registrador()] * 2**5
		self.ULAbloqueada = False
		self.avancapc = False

	def bloquearULA():
		self.ULAbloqueada = True

	def desbloquearULA():
		self.ULAbloqueada = False

	def read(self, filePath):
		self.fr.read(filePath)

	def inicio(self):
		self.clock = -1
		self.pc = bin(0)
		self.concluidas = 0
		self.produtividade = 0
		self.E1 = InstructionFetch(1, self)
		self.E2 = InstructionDecodeRegisterFetch(2, self)
		self.E3 = InstructionExecute(3, self)
		self.E4 = MemoryAccess(4, self)
		self.E5 = WriteBack(5, self)

		self.E1.bloquear() #para manter o pc em 0
		self.E1.setNop()
		self.E2.setNop()
		self.E3.setNop()
		self.E4.setNop()
		self.E5.setNop()

		self.end1 = None
		self.val1 = None
		self.end2 = None
		self.val2 = None
		self.end3 = None
		self.val3 = None
		self.end4 = None
		self.val4 = None

	def setView(self, view):
		self.view = view

	def memoryAccess(self):
		pass

	def writeBack(self):
		pass

	def proxEstagio(self):
		self.clock = self.clock + 1

		if not self.E5.bloqueado:
			if not self.E4.bloqueado & self.E4.passarInstrucao:
				self.E5.setInstrucao(self.E4.instrucao)
				self.E5.do()
				if not self.E3.bloqueado & self.E3.passarInstrucao:
					self.E4.setInstrucao(self.E3.instrucao)
					self.E4.do()
					if not self.E2.bloqueado & self.E2.passarInstrucao:
						self.E3.setInstrucao(self.E2.instrucao)
						self.E3.do()
						if not self.E1.bloqueado & self.E1.passarInstrucao:
							self.E2.setInstrucao(self.E1.instrucao)
							self.E2.do()
							if not self.avancapc:
								self.avancapc = True
							else:
								self.pc = bin(eval(self.pc) + 4)	
							self.E1.setInstrucao(self.E2.decodInst(self.E1.do(eval(self.pc)/4)))						
						else:
							self.E1.setNop()
							self.E2.setNop()
					else:
						self.E3.setNop()
				else:
					self.E4.setNop()
			else:
				self.E5.setNop()

		self.atualizarLabels()


	def setText(self, label, ori, none):
		if ori is not None:
			label["text"] = ori
		else:
			label["text"] = none

	def atualizarLabels(self):
		if self.view is not None:
			self.setText(self.view.E1_instrucao, self.E1.InstName, "")
			self.setText(self.view.E2_instrucao, self.E2.InstName, "")
			self.setText(self.view.E3_instrucao, self.E3.InstName, "")
			self.setText(self.view.E4_instrucao, self.E4.InstName, "")
			self.setText(self.view.E5_instrucao, self.E5.InstName, "")
			self.setText(self.view.E1_controle, self.E1.SinControle, "")
			self.setText(self.view.E2_controle, self.E2.SinControle, "")
			self.setText(self.view.E3_controle, self.E3.SinControle, "")
			self.setText(self.view.E4_controle, self.E4.SinControle, "")
			self.setText(self.view.E5_controle, self.E5.SinControle, "")

			self.view.lclock["text"] = self.clock
			self.view.lpc["text"] = self.pc[2:]
			self.view.lconcluidas["text"] = self.concluidas
			self.view.lprodutividade["text"] = self.produtividade

			self.setText(self.view.lend1, self.end1, "")
			self.setText(self.view.lval1, self.val1, "?")
			self.setText(self.view.lend2, self.end2, "")
			self.setText(self.view.lval2, self.val2, "?")
			self.setText(self.view.lend3, self.end3, "")
			self.setText(self.view.lval3, self.val3, "?")
			self.setText(self.view.lend4, self.end4, "")
			self.setText(self.view.lval4, self.val4, "?")

			self.view.lr0["text"] = str(self.reg[0].valor)
			self.view.lr1["text"] = str(self.reg[1].valor)
			self.view.lr2["text"] = str(self.reg[2].valor)
			self.view.lr3["text"] = str(self.reg[3].valor)
			self.view.lr4["text"] = str(self.reg[4].valor)
			self.view.lr5["text"] = str(self.reg[5].valor)
			self.view.lr6["text"] = str(self.reg[6].valor)
			self.view.lr7["text"] = str(self.reg[7].valor)
			self.view.lr8["text"] = str(self.reg[8].valor)
			self.view.lr9["text"] = str(self.reg[9].valor)
			self.view.lr10["text"] = str(self.reg[10].valor)
			self.view.lr11["text"] = str(self.reg[11].valor)
			self.view.lr12["text"] = str(self.reg[12].valor)
			self.view.lr13["text"] = str(self.reg[13].valor)
			self.view.lr14["text"] = str(self.reg[14].valor)
			self.view.lr15["text"] = str(self.reg[15].valor)
			self.view.lr16["text"] = str(self.reg[16].valor)
			self.view.lr17["text"] = str(self.reg[17].valor)
			self.view.lr18["text"] = str(self.reg[18].valor)
			self.view.lr19["text"] = str(self.reg[19].valor)
			self.view.lr20["text"] = str(self.reg[20].valor)
			self.view.lr21["text"] = str(self.reg[21].valor)
			self.view.lr22["text"] = str(self.reg[22].valor)
			self.view.lr23["text"] = str(self.reg[23].valor)
			self.view.lr24["text"] = str(self.reg[24].valor)
			self.view.lr25["text"] = str(self.reg[25].valor)
			self.view.lr26["text"] = str(self.reg[26].valor)
			self.view.lr27["text"] = str(self.reg[27].valor)
			self.view.lr28["text"] = str(self.reg[28].valor)
			self.view.lr29["text"] = str(self.reg[29].valor)
			self.view.lr30["text"] = str(self.reg[30].valor)
			self.view.lr31["text"] = str(self.reg[31].valor)  