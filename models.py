print "MODELS"
from filereader import FileReader

class InstrucaoR:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.rs = bin(eval("0b"+instrucao[6:11]))
		self.rt = bin(eval("0b"+instrucao[11:16]))
		self.rd = bin(eval("0b"+instrucao[16:21]))
		self.shamt = bin(eval("0b"+instrucao[21:26]))

	def decode(self):
		self.mips.A = self.mips.reg[eval(self.rs)]
		self.mips.B = self.mips.reg[eval(self.rt)]
		# self.mips.rd = self.rd
		# self.mips.shamt = self.shamt

	def memacess(self):
		pass

	def writeback(self):
		self.mips.reg[eval(self.rd)] = self.mips.ULA

class InstrucaoI:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.rs = bin(eval("0b"+instrucao[6:11]))
		self.rt = bin(eval("0b"+instrucao[11:16]))
		self.immediate = bin(eval("0b"+instrucao[16:32]))	

	def decode(self):
		self.mips.A = self.mips.reg[eval(self.rs)]
		self.mips.B = self.mips.reg[eval(self.rt)]
		self.mips.Imm = self.immediate

class InstrucaoJ:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.targetAddress = bin(eval("0b"+instrucao[6:32]))

	def decode(self):
		self.mips.targetAddress = self.targetAddress

class Jmp(InstrucaoJ):
	
	def __init__(self, mips, instrucao):
		InstrucaoJ.__init__(self, mips, instrucao)

	def decode(self):
		pass

	def execute(self):
		pass

	def memacess(self):
		mips.pc = self.mips.targetAddress

	def writeback(self):
		pass

	def texto(self):    
		return "jmp" + str(eval(self.targetAddress))

class Add(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)


	def execute(self):
		self.mips.ULA = self.mips.A + self.mips.B

	def texto(self):
		return "add R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Mul(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = self.mips.A * self.mips.B

	def texto(self):
		return "mul R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Nop(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def decode(self):
		pass

	def execute(self):
		pass

	def memacess(self):
		pass

	def writeback(self):
		pass 

	def texto(self):
		return "nop"

class Sub(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = self.mips.A - self.mips.B

	def texto(self):
		return "sub R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Addi(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = self.mips.A + self.mips.Imm

	def memacess(self):
		pass

	def writeback(self):
		self.mips.reg[eval(self.rt)] = self.mips.ULA

	def texto(self):
		return "addi R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Beq(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self):
		self.equal = False
		if self.mips.reg[eval(self.mips.A)] == self.mips.reg[eval(self.mips.B)]:
			self.equal = True
			self.mips.ULA = bin(eval(self.mips.pc) + 4 + eval(self.mips.Imm))

	def memacess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA

	def writeback(self):
		pass

	def texto(self):
		return "beq R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Ble(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self):
		self.equal = False
		if self.mips.reg[eval(self.mips.rs)] <= self.mips.reg[eval(self.mips.rt)]:
			self.equal = True
			self.mips.ULA = bin(eval(self.mips.immediate))      

	def memacess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA

	def writeback(self):
		pass

	def texto(self):
		return "ble R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))  

class Bne(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self):
		self.equal = False
		if self.mips.reg[eval(self.mips.rs)] != self.mips.reg[eval(self.mips.rt)]:
			self.equal = True
			self.mips.pc = bin(eval(self.mips.pc) + 4 + eval(self.mips.immediate))

	def memacess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA

	def writeback(self):
		pass

	def texto(self):
		return "bne R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Lw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = bin(eval(self.mips.rs) + eval(self.mips.immediate))

	def memacess(self):
		self.mips.rt = self.mips.reg[eval(self.mips.ULA)]

	def writeback(self):
		pass

	def texto(self):
		return "lw R" + str(eval(self.rs)) + ", "+str(eval(self.immediate))+"("+str(eval(self.rt)) + ")"

class Sw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = bin(eval(self.mips.rs) + eval(self.mips.immediate))

	def memacess(self):
		self.mips.reg[eval(self.mips.ULA)] = bin(eval(self.mips.rt))

	def writeback(self):
		pass

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
		return self.mips.fr.getInst(i)[0:32]

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

		self.instrucao.decode()
		return self.instrucao

class InstructionExecute(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self):
		self.instrucao.execute()

class MemoryAccess(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self):
		pass #escrever no local da memoria

class WriteBack(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self):
		pass #escrever novamente no registrador do mips

class Mips:
	def __init__(self):
		self.inicio()
		self.fr = FileReader()   
		self.mem = [0] * 2**15 # vc pode checar o tamanho com len(self.mem) e acessar cada posicao
							   # independentemente com self.mips.mem[i] dai para manipular os 32 bits podemos
							   # mexer com os valores binarios e decimais
		self.reg = [0] * 2**5


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

		self.r0 = 0
		self.r1 = 0
		self.r2 = 0
		self.r3 = 0
		self.r4 = 0
		self.r5 = 0
		self.r6 = 0
		self.r7 = 0
		self.r8 = 0
		self.r9 = 0
		self.r10 = 0
		self.r11 = 0
		self.r12 = 0
		self.r13 = 0
		self.r14 = 0
		self.r15 = 0
		self.r16 = 0
		self.r17 = 0
		self.r18 = 0
		self.r19 = 0
		self.r20 = 0
		self.r21 = 0
		self.r22 = 0
		self.r23 = 0
		self.r24 = 0
		self.r25 = 0
		self.r26 = 0
		self.r27 = 0
		self.r28 = 0
		self.r29 = 0
		self.r30 = 0
		self.r31 = 0

	def setView(self, view):
		self.view = view

	def memoryAccess(self):
		pass

	def writeBack(self):
		pass

	def proxEstagio(self):
		self.clock = self.clock + 1

		if not self.E5.bloqueado:
			if not self.E4.bloqueado:
				self.E5.setInstrucao(self.E4.instrucao)
				self.E5.do()
				if not self.E3.bloqueado:
					self.E4.setInstrucao(self.E3.instrucao)
					self.E4.do()
					if not self.E2.bloqueado:
						self.E3.setInstrucao(self.E2.instrucao)
						self.E3.do()
						if not self.E1.bloqueado:
							self.E2.setInstrucao(self.E1.instrucao)
							self.E2.do()
							self.pc = bin(eval(self.pc) + 4)							
						else:
							self.E2.setNop()
							self.E1.desbloquear()
						self.E1.setInstrucao(self.E2.decodInst(self.E1.do(eval(self.pc)/4)))
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

			self.view.lr0["text"] = str(self.r0)
			self.view.lr1["text"] = str(self.r1)
			self.view.lr2["text"] = str(self.r2)
			self.view.lr3["text"] = str(self.r3)
			self.view.lr4["text"] = str(self.r4)
			self.view.lr5["text"] = str(self.r5)
			self.view.lr6["text"] = str(self.r6)
			self.view.lr7["text"] = str(self.r7)
			self.view.lr8["text"] = str(self.r8)
			self.view.lr9["text"] = str(self.r9)
			self.view.lr10["text"] = str(self.r10)
			self.view.lr11["text"] = str(self.r11)
			self.view.lr12["text"] = str(self.r12)
			self.view.lr13["text"] = str(self.r13)
			self.view.lr14["text"] = str(self.r14)
			self.view.lr15["text"] = str(self.r15)
			self.view.lr16["text"] = str(self.r16)
			self.view.lr17["text"] = str(self.r17)
			self.view.lr18["text"] = str(self.r18)
			self.view.lr19["text"] = str(self.r19)
			self.view.lr20["text"] = str(self.r20)
			self.view.lr21["text"] = str(self.r21)
			self.view.lr22["text"] = str(self.r22)
			self.view.lr23["text"] = str(self.r23)
			self.view.lr24["text"] = str(self.r24)
			self.view.lr25["text"] = str(self.r25)
			self.view.lr26["text"] = str(self.r26)
			self.view.lr27["text"] = str(self.r27)
			self.view.lr28["text"] = str(self.r28)
			self.view.lr29["text"] = str(self.r29)
			self.view.lr30["text"] = str(self.r30)
			self.view.lr31["text"] = str(self.r31)  