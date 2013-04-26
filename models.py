print "MODELS"
from filereader import FileReader

class InstrucaoR:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		mips.rs = bin(eval("0b"+instrucao[6:11]))
		mips.rt = bin(eval("0b"+instrucao[11:16]))
		mips.rd = bin(eval("0b"+instrucao[16:21]))
		mips.shamt = bin(eval("0b"+instrucao[21:26]))

class InstrucaoI:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		mips.rs = bin(eval("0b"+instrucao[6:11]))
		mips.rt = bin(eval("0b"+instrucao[11:16]))
		mips.immediate = bin(eval("0b"+instrucao[16:32]))

class InstrucaoJ:
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		mips.targetAddress = bin(eval("0b"+instrucao[6:32]))

class Jmp(InstrucaoJ):
	
	def __init__(self, mips, instrucao):
		InstrucaoJ.__init__(self, mips, instrucao)

	def execute(self, mips):
		mips.pc = bin(eval(self.mips.pc) + eval(self.mips.targetAddress)) #REVISAR acho que nao precisa reler o pc

	def texto(self):    
		return "jmp" + str(eval(self.mips.targetAddress))

class Add(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self, mips):
		self.mips.rd = bin(eval(self.mips.rs) + eval(self.mips.rt))

	def texto(self):
		return "add R" + str(eval(self.mips.rd)) + ", R"+str(eval(self.mips.rs)) + ", R" + str(eval(self.mips.rt))

class Mul(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self, mips):
		self.mips.rd = bin(eval(self.mips.rs)*eval(self.mips.rt))

	def texto(self):
		return "mul R" + str(eval(self.mips.rd)) + ", R"+str(eval(self.mips.rs)) + ", R" + str(eval(self.mips.rt))

class Nop(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self, mips):
		pass

	def texto(self):
		return "nop"

class Sub(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self, mips):
		self.mips.rd = bin(eval(self.mips.rs) - eval(self.mips.rt))

	def texto(self):
		return "sub R" + str(eval(self.mips.rd)) + ", R"+str(eval(self.mips.rs)) + ", R" + str(eval(self.mips.rt))

class Addi(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self, mips):
		mips.rt = bin(eval(mips.rs) + eval(mips.immediate))

	def texto(self):
		return "addi R" + str(eval(self.mips.rs)) + ", R"+str(eval(self.mips.rt)) + ", " + str(eval(self.mips.immediate))

class Beq(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self, mips):
		if self.mips.rs == self.mips.rt:
			self.mips.pc = bin(eval(self.mips.pc) + 4 + eval(self.mips.immediate))

	def texto(self):
		return "beq R" + str(eval(self.mips.rs)) + ", R"+str(eval(self.mips.rt)) + ", " + str(eval(self.mips.immediate))

class Ble(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self, mips):
		if self.mips.rs <= self.mips.rt:
			self.mips.pc = bin(eval(self.mips.immediate))      

	def texto(self):
		return "ble R" + str(eval(self.mips.rs)) + ", R"+str(eval(self.mips.rt)) + ", " + str(eval(self.mips.immediate))  

class Bne(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self, mips):
		if self.mips.rs != self.mips.rt:
			self.mips.pc = bin(eval(self.mips.pc) + 4 + eval(self.mips.immediate))

	def texto(self):
		return "bne R" + str(eval(self.mips.rs)) + ", R"+str(eval(self.mips.rt)) + ", " + str(eval(self.mips.immediate))

class Lw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self, mips):
		pass

	def texto(self):
		return "lw R" + str(eval(self.mips.rs)) + ", "+str(eval(self.mips.immediate))+"("+str(eval(self.mips.rt)) + ")"

class Sw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def execute(self, mips):
		pass

	def texto(self):
		return "sw R" + str(eval(self.mips.rs)) + ", "+str(eval(self.mips.immediate))+"("+str(eval(self.mips.rt)) + ")"

class Estagio:
	def __init__(self, num, mips):
		self.num = num
		self.InstName = str(num)+":"
		self.SinControle = ""
		self.mips = mips
		self.bloqueado = False

	def desbloquear(self):
		self.bloqueado = False

	def bloquear(self):
		self.bloqueado = True

class InstructionFetch(Estagio):

	def __init__(self, num, mips):
		Estagio.__init__(self, num,  mips)

	def do(self, i):
		self.instruction = self.mips.fr.getInst(i)[0:32]
		return self.instruction

class InstructionDecodeRegisterFetch(Estagio):

	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self, instrucao):
		instructionCode = instrucao[0:6]
		if instructionCode == "000010":
			self.instrucaoDecodificada = Jmp(self.mips, instrucao) 
		else:
			if instructionCode == "000000":
				if instrucao[26:32] == "100000":
					self.instrucaoDecodificada = Add(self.mips, instrucao)
				elif instrucao[26:32] == "011000":
					self.instrucaoDecodificada = Mul(self.mips, instrucao)
				elif instrucao[26:32] == "000000":
					self.instrucaoDecodificada = Nop(self.mips, instrucao)
				elif instrucao[26:32] == "100010":
					self.instrucaoDecodificada = Sub(self.mips, instrucao)
			else:
				self.immediate = instrucao[16:32]
				if instructionCode == "001000":
					self.instrucaoDecodificada = Addi(self.mips, instrucao)
				elif instructionCode == "000101":
					self.instrucaoDecodificada = Beq(self.mips, instrucao)
				elif instructionCode == "000111":
					self.instrucaoDecodificada = Ble(self.mips, instrucao)
				elif instructionCode == "000100":
					self.instrucaoDecodificada = Bne(self.mips, instrucao)
				elif instructionCode == "100011":
					self.instrucaoDecodificada = Lw(self.mips, instrucao)
				elif instructionCode == "101011":
					self.instrucaoDecodificada = Sw(self.mips, instrucao)
		return self.instrucaoDecodificada

class InstructionExecute(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self, instrucaoDecodificada):
		instrucaoDecodificada.execute(self.mips)

class Mips:
	def __init__(self):
		self.inicio()
		self.fr = FileReader()   
		self.mem = [0] * 2**15 #vc pode checar o tamanho com len(self.mem) e acessar cada posicao
							   # independentemente com self.mips.mem[i] dai para manipular os 32 bits podemos
							   # mexer com os valores binarios e decimais


	def read(self, filePath):
		self.fr.read(filePath)

	def inicio(self):
		self.clock = -1
		self.pc = -1
		self.concluidas = 0
		self.produtividade = 0
		self.E1 = InstructionFetch(1, self)
		self.E2 = InstructionDecodeRegisterFetch(2, self)
		self.E3 = InstructionExecute(3, self)
		self.E4 = Estagio(4, self)
		self.E5 = Estagio(5, self)

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
		if not self.E1.bloqueado:         
			self.pc = self.pc + 1   
		else:
			self.E1.desbloquear()
		inst_bin = self.E1.do(self.pc)
		print inst_bin    
		if not self.E2.bloqueado:
			inst_decod = self.E2.do(inst_bin)
			print inst_decod.texto()
		# else:
		#     self.E1.bloquear()
		# if not self.E3.bloqueado:
		#     self.E3.do(inst_decod)
		# else:
		#     self.E1.bloquear()
		#     self.E2.bloquear()

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
			self.view.lpc["text"] = self.pc
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