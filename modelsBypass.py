print "MODELS"
from filereader import FileReader

class Registrador:
	def __init__(self):
		self.valor = bin(0)
		self.bloqueado = False
		self.resultadoDisponivel = False

	def bloquear(self):
		self.bloqueado = True

	def desbloquear(self):
		self.bloqueado = False

class Instrucao:
	def decode(self):
		pass
	def execute(self):
		pass
	def memaccess(self):
		pass
	def writeback(self):
		pass

class InstrucaoR(Instrucao):
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.rs = bin(eval("0b"+instrucao[6:11]))
		self.rt = bin(eval("0b"+instrucao[11:16]))
		self.rd = bin(eval("0b"+instrucao[16:21]))
		self.shamt = bin(eval("0b"+instrucao[21:26]))
		self.isMul = False
		self.temLocalDestino = True

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			if (not self.mips.reg[eval(self.rs)].resultadoDisponivel) | (not self.mips.reg[eval(self.rt)].resultadoDisponivel):
				self.mips.E2.esperarClock()
			else:
				if self.mips.reg[eval(self.rs)].resultadoDisponivel:
					self.mips.A = self.mips.reg[eval(self.rs)].proxResultado
				else:
					self.mips.A = self.mips.reg[eval(self.rs)].valor
				if self.mips.reg[eval(self.rt)].resultadoDisponivel:
					self.mips.B = self.mips.reg[eval(self.rt)].proxResultado
				else:
					self.mips.B = self.mips.reg[eval(self.rt)].valor
				# self.mips.reg[eval(self.rd)].bloquear()
				self.mips.shamt = self.shamt
		else:
			self.mips.A = self.mips.reg[eval(self.rs)].valor
			self.mips.B = self.mips.reg[eval(self.rt)].valor
			# self.mips.reg[eval(self.rd)].bloquear()
			self.mips.shamt = self.shamt

	def writeback(self):
		self.mips.reg[eval(self.rd)].valor = self.mips.ULA
		self.mips.addDesbloqueio(self.mips.reg[eval(self.rd)])

	def localDestino(self):
		return self.mips.reg[eval(self.rd)]

class InstrucaoI(Instrucao):
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.rs = bin(eval("0b"+instrucao[6:11]))
		self.rt = bin(eval("0b"+instrucao[11:16]))
		self.immediate = bin(eval("0b"+instrucao[16:32]))	
		self.isMul = False
		self.temLocalDestino = False

class InstrucaoJ(Instrucao):
	
	def __init__(self, mips, instrucao):
		self.mips = mips
		self.targetAddress = bin(eval("0b"+instrucao[6:32]))
		self.isMul = False
		self.temLocalDestino = False

class Jmp(InstrucaoJ):
	
	def __init__(self, mips, instrucao):
		InstrucaoJ.__init__(self, mips, instrucao)

	def decode(self):
		self.mips.E1.bloquear()

	def memaccess(self):
		self.mips.pc = self.targetAddress
		self.mips.avancapc = False
		self.mips.addDesbloqueio(self.mips.E1)

	def texto(self):    
		return "jmp" + str(eval(self.targetAddress))

class Add(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)

	def execute(self):
		self.mips.ULA = bin(eval(self.mips.A) + eval(self.mips.B))
		self.mips.reg[eval(self.rd)].proxResultado = self.mips.ULA
		self.mips.reg[eval(self.rd)].resultadoDisponivel = True

	def texto(self):
		return "add R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Mul(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)
		self.isMul = True

	def execute(self):
		self.mips.ULA = bin(eval(self.mips.A) * eval(self.mips.B))
		self.mips.reg[eval(self.rd)].proxResultado = self.mips.ULA
		self.mips.reg[eval(self.rd)].resultadoDisponivel = True

	def texto(self):
		return "mul R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Nop(InstrucaoR):
	
	def __init__(self, mips, instrucao):
		InstrucaoR.__init__(self, mips, instrucao)
		self.temLocalDestino = False

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
		self.mips.ULA = bin(eval(self.mips.A) - eval(self.mips.B))
		self.mips.reg[eval(self.rd)].proxResultado = self.mips.ULA
		self.mips.reg[eval(self.rd)].resultadoDisponivel = True

	def texto(self):
		return "sub R" + str(eval(self.rd)) + ", R"+str(eval(self.rs)) + ", R" + str(eval(self.rt))

class Addi(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)
		self.temLocalDestino = True

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			if (not self.mips.reg[eval(self.rs)].resultadoDisponivel) | (not self.mips.reg[eval(self.rt)].resultadoDisponivel):
				self.mips.E2.esperarClock()
			else:
				if self.mips.reg[eval(self.rs)].resultadoDisponivel:
					self.mips.A = self.mips.reg[eval(self.rs)].proxResultado
				else:
					self.mips.A = self.mips.reg[eval(self.rs)].valor
				if self.mips.reg[eval(self.rt)].resultadoDisponivel:
					self.mips.B = self.mips.reg[eval(self.rt)].proxResultado
				else:
					self.mips.B = self.mips.reg[eval(self.rt)].valor
				self.mips.Imm = self.immediate
				# self.mips.reg[eval(self.rt)].bloquear()
		else:
			self.mips.A = self.mips.reg[eval(self.rs)].valor
			self.mips.B = self.mips.reg[eval(self.rt)].valor
			self.mips.Imm = self.immediate
			# self.mips.reg[eval(self.rt)].bloquear()

	def execute(self):
		self.mips.ULA = bin(eval(self.mips.A) + eval(self.mips.Imm))
		self.mips.reg[eval(self.rt)].proxResultado = self.mips.ULA
		self.mips.reg[eval(self.rt)].resultadoDisponivel = True

	def writeback(self):
		self.mips.reg[eval(self.rt)].valor = self.mips.ULA
		self.mips.addDesbloqueio(self.mips.reg[eval(self.rt)])

	def localDestino(self):
		return self.mips.reg[eval(self.rt)]

	def texto(self):
		return "addi R" + str(eval(self.rt)) + ", R"+str(eval(self.rs)) + ", " + str(eval(self.immediate))

class Beq(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			if (not self.mips.reg[eval(self.rs)].resultadoDisponivel) | (not self.mips.reg[eval(self.rt)].resultadoDisponivel):
				self.mips.E2.esperarClock()
			else:
				if self.mips.reg[eval(self.rs)].resultadoDisponivel:
					self.mips.A = self.mips.reg[eval(self.rs)].proxResultado
				else:
					self.mips.A = self.mips.reg[eval(self.rs)].valor
				if self.mips.reg[eval(self.rt)].resultadoDisponivel:
					self.mips.B = self.mips.reg[eval(self.rt)].proxResultado
				else:
					self.mips.B = self.mips.reg[eval(self.rt)].valor
				self.mips.Imm = self.immediate
				self.mips.E1.bloquear()
		else:
			self.mips.A = self.mips.reg[eval(self.rs)].valor
			self.mips.B = self.mips.reg[eval(self.rt)].valor
			self.mips.Imm = self.immediate
			self.mips.E1.bloquear()

	def execute(self):
		self.equal = False
		if eval(self.mips.A) == eval(self.mips.B):
			self.equal = True
			self.mips.ULA = bin(eval(self.mips.pc) + 4 + eval(self.mips.Imm))

	def memaccess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA
			self.mips.avancapc = False
		else:
			self.mips.avancapc = True
		self.mips.addDesbloqueio(self.mips.E1)

	def writeback(self):
		pass

	def texto(self):
		return "beq R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Ble(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			if (not self.mips.reg[eval(self.rs)].resultadoDisponivel) | (not self.mips.reg[eval(self.rt)].resultadoDisponivel):
				self.mips.E2.esperarClock()
			else:
				if self.mips.reg[eval(self.rs)].resultadoDisponivel:
					self.mips.A = self.mips.reg[eval(self.rs)].proxResultado
				else:
					self.mips.A = self.mips.reg[eval(self.rs)].valor
				if self.mips.reg[eval(self.rt)].resultadoDisponivel:
					self.mips.B = self.mips.reg[eval(self.rt)].proxResultado
				else:
					self.mips.B = self.mips.reg[eval(self.rt)].valor
				self.mips.Imm = self.immediate
				self.mips.E1.bloquear()
		else:
			self.mips.A = self.mips.reg[eval(self.rs)].valor
			self.mips.B = self.mips.reg[eval(self.rt)].valor
			self.mips.Imm = self.immediate
			self.mips.E1.bloquear()

	def execute(self):
		self.equal = False
		if eval(self.mips.A) <= eval(self.mips.B):
			self.equal = True
			self.mips.ULA = self.mips.Imm

	def memaccess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA
			self.mips.avancapc = False
		else:
			self.mips.avancapc = True
		self.mips.addDesbloqueio(self.mips.E1)

	def writeback(self):
		pass

	def texto(self):
		return "ble R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))  

class Bne(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			if (not self.mips.reg[eval(self.rs)].resultadoDisponivel) | (not self.mips.reg[eval(self.rt)].resultadoDisponivel):
				self.mips.E2.esperarClock()
			else:
				if self.mips.reg[eval(self.rs)].resultadoDisponivel:
					self.mips.A = self.mips.reg[eval(self.rs)].proxResultado
				else:
					self.mips.A = self.mips.reg[eval(self.rs)].valor
				if self.mips.reg[eval(self.rt)].resultadoDisponivel:
					self.mips.B = self.mips.reg[eval(self.rt)].proxResultado
				else:
					self.mips.B = self.mips.reg[eval(self.rt)].valor
				self.mips.Imm = self.immediate
				self.mips.E1.bloquear()
		else:
			self.mips.A = self.mips.reg[eval(self.rs)].valor
			self.mips.B = self.mips.reg[eval(self.rt)].valor
			self.mips.Imm = self.immediate
			self.mips.E1.bloquear()

	def execute(self):
		self.equal = False
		if eval(self.mips.A) != eval(self.mips.B):
			self.equal = True
			self.mips.pc = bin(eval(self.mips.pc) + 4 + eval(self.mips.Imm))

	def memaccess(self):
		if self.equal == True:
			self.mips.pc = self.mips.ULA
			self.mips.avancapc = False
		else:
			self.mips.avancapc = True
		self.mips.addDesbloqueio(self.mips.E1)

	def writeback(self):
		pass

	def texto(self):
		return "bne R" + str(eval(self.rs)) + ", R"+str(eval(self.rt)) + ", " + str(eval(self.immediate))

class Lw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)
		self.temLocalDestino = True

	def decode(self):
		if self.mips.reg[eval(self.rs)].bloqueado:
			if not self.mips.reg[eval(self.rs)].resultadoDisponivel:
				self.mips.E2.esperarClock()
			else:
				if self.mips.reg[eval(self.rs)].resultadoDisponivel:
					self.mips.A = self.mips.reg[eval(self.rs)].proxResultado
				else:
					self.mips.A = self.mips.reg[eval(self.rs)].valor
				self.destino = eval(self.mips.reg[eval(self.rs)].valor) + eval(self.immediate)
				if self.mips.mem[self.destino].bloqueado:
					if not self.mips.mem[self.destino].resultadoDisponivel:
						self.mips.E2.esperarClock()
					else:
						self.mips.resultado = self.mips.mem[self.destino].proxResultado
						# self.mips.reg[eval(self.rt)].bloquear()
						self.mips.addListaMemoria(self.destino)
						self.mips.reg[eval(self.rt)].proxResultado = self.resultado
						self.mips.reg[eval(self.rt)].resultadoDisponivel = True
		else:
			self.destino = eval(self.mips.reg[eval(self.rs)].valor) + eval(self.immediate)
			if self.mips.mem[self.destino].bloqueado:
				if not self.mips.mem[self.destino].resultadoDisponivel:
						self.mips.E2.esperarClock()
				else:
					self.mips.resultado = self.mips.mem[self.destino].proxResultado
					# self.mips.reg[eval(self.rt)].bloquear()
					self.mips.addListaMemoria(self.destino)
					self.mips.reg[eval(self.rt)].proxResultado = self.resultado
					self.mips.reg[eval(self.rt)].resultadoDisponivel = True
			else:
				self.mips.Imm = self.immediate
				self.resultado = self.mips.mem[self.destino].valor
				# self.mips.reg[eval(self.rt)].bloquear()
				self.mips.addListaMemoria(self.destino)
				self.mips.reg[eval(self.rt)].proxResultado = self.resultado
				self.mips.reg[eval(self.rt)].resultadoDisponivel = True

	def writeback(self):
		self.mips.reg[eval(self.rt)].valor = self.resultado
		self.mips.addDesbloqueio(self.mips.reg[eval(self.rt)])

	def localDestino(self):
		return self.mips.reg[eval(self.rt)]

	def texto(self):
		return "lw R" + str(eval(self.rt)) + ", " + str(eval(self.immediate)) + "(R" + str(eval(self.rs)) + ")"
class Sw(InstrucaoI):

	def __init__(self, mips, instrucao):
		InstrucaoI.__init__(self, mips, instrucao)
		self.temLocalDestino = True

	def decode(self):	
		if self.mips.reg[eval(self.rs)].bloqueado | self.mips.reg[eval(self.rt)].bloqueado:
			if (not self.mips.reg[eval(self.rs)].resultadoDisponivel) | (not self.mips.reg[eval(self.rt)].resultadoDisponivel):
				self.mips.E2.esperarClock()
			else:
				self.mips.Imm = self.immediate
				if self.mips.reg[eval(self.rs)].resultadoDisponivel:
					self.destino = 	eval(self.mips.reg[eval(self.rs)].valor) + eval(self.mips.Imm)
				else:
					self.mips.A = self.mips.reg[eval(self.rs)].valor
				if self.mips.reg[eval(self.rt)].resultadoDisponivel:
					self.resultado = self.mips.reg[eval(self.rt)].proxResultado
				else:
					self.resultado = self.mips.reg[eval(self.rt)].valor
		else:
			self.mips.Imm = self.immediate
			self.destino = 	eval(self.mips.reg[eval(self.rs)].valor) + eval(self.mips.Imm)
			# self.mips.mem[self.destino].bloquear()
			self.resultado = self.mips.reg[eval(self.rt)].valor
			self.mips.mem[self.destino].proxResultado = self.resultado
			self.mips.mem[self.destino].resultadoDisponivel = True

	def memaccess(self):
		self.mips.mem[self.destino].valor = self.resultado
		self.mips.addDesbloqueio(self.mips.mem[self.destino])
		self.mips.addListaMemoria(self.destino)

	def localDestino(self):
		return self.mips.mem[self.destino]

	def texto(self):
		return "sw R" + str(eval(self.rt)) + ", " + str(eval(self.immediate)) + "(R" + str(eval(self.rs)) + ")"

class Estagio:
	def __init__(self, num, mips):
		self.num = num
		self.SinControle = ""
		self.mips = mips
		self.bloqueado = False
		self.setNop()
		self.saida = 0
		self.desbloqueou = False

	def desbloquear(self):
		self.bloqueado = False

	def esperarClock(self):
		self.desbloqueou = True

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
		if i < self.mips.fr.count():
			inst = self.mips.fr.getInst(i)[0:32]
		else:
			inst = "0"*32
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
		self.instrucao.decode()

class InstructionExecute(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)
		self.cont = 0

	def do(self):
		if self.instrucao.isMul:
			if self.cont == 0:
				self.instrucao.execute()
				self.cont = 1
				self.esperarClock()
			else:
				self.cont = 0
		else:
			self.instrucao.execute()

class MemoryAccess(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self):
		self.instrucao.memaccess()

class WriteBack(Estagio):
	
	def __init__(self, num, mips):
		Estagio.__init__(self, num, mips)

	def do(self):
		self.instrucao.writeback()

class Mips:
	def __init__(self):
		self.inicio()
		self.fr = FileReader()   
		self.mem = []
		for i in range(0, 2**15):
			self.mem.append(Registrador())# vc pode checar o tamanho com len(self.mem) e acessar cada posicao
							   # independentemente com self.mips.mem[i] dai para manipular os 32 bits podemos
							   # mexer com os valores binarios e decimais
		self.reg = []
		for i in range(0, 2**5):
			self.reg.append(Registrador())
		self.avancapc = False
		self.listaDeDesbloqueio = []
		self.listaDeIndisponibilidade = []
		self.listaMemoria = []

	def addListaMemoria(self, endereco):
		self.listaMemoria.append([endereco, str(eval(self.mem[endereco].valor))])
		if len(self.listaMemoria) > 4:
			self.listaMemoria = self.listaMemoria[-4:]

	def getListaMemoria(self, i):
		if len(self.listaMemoria) < i:
			return ["", ""]
		else:
			return self.listaMemoria[-i]

	def addDesbloqueio(self, destino):
		self.listaDeDesbloqueio.append(destino)

	def addIndisponivel(self, destino):
		self.listaDeIndisponibilidade.append(destino)

	def ClockDesbloquear(self):
		for i in self.listaDeDesbloqueio:
			i.desbloquear()
		self.listaDeDesbloqueio = []

	def ClockIndisponivel(self):
		for i in self.listaDeIndisponibilidade:
			i.resultadoDisponivel = False
		self.listaDeIndisponibilidade = []

	def read(self, filePath):
		self.fr.read(filePath)

	def inicio(self):
		self.clock = 0
		self.pc = bin(0)
		self.concluidas = 0
		self.produtividade = 0
		self.E1 = InstructionFetch(1, self)
		self.E2 = InstructionDecodeRegisterFetch(2, self)
		self.E3 = InstructionExecute(3, self)
		self.E4 = MemoryAccess(4, self)
		self.E5 = WriteBack(5, self)

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
		self.ClockDesbloquear()
		self.ClockIndisponivel()
		if not self.E5.bloqueado:
			if not self.E5.desbloqueou:
				if self.E5.instrucao.__class__.__name__ != "Nop":
					self.concluidas = self.concluidas + 1
					if self.E5.instrucao.temLocalDestino:
						self.addIndisponivel(self.E5.instrucao.localDestino())
				if not self.E4.bloqueado:
					if not self.E4.desbloqueou:
						self.E5.setInstrucao(self.E4.instrucao)
						self.E5.do()
						if not self.E3.bloqueado:
							if not self.E3.desbloqueou:
								self.E4.setInstrucao(self.E3.instrucao)
								self.E4.do()
								if not self.E2.bloqueado:
									if not self.E2.desbloqueou:
										self.E3.setInstrucao(self.E2.instrucao)
										self.E3.do()
										if not self.E1.bloqueado:
											if not self.E1.desbloqueou:
												self.E2.setInstrucao(self.E1.instrucao)
												self.E2.do()
												if not self.avancapc:
													self.avancapc = True
												else:
													self.pc = bin(eval(self.pc) + 4)	
												self.E1.setInstrucao(self.E2.decodInst(self.E1.do(eval(self.pc)/4)))
											else:
												self.E2.setNop()
												self.E1.desbloqueou = False
												self.E1.do()
										else:
											self.E2.setNop()
									else:
										self.E3.setNop()
										self.E2.desbloqueou = False
										self.E2.do()
								else:
									self.E3.setNop()
							else:
								self.E4.setNop()
								self.E3.desbloqueou = False
								self.E3.do()
						else:
							self.E4.setNop()
					else:
						self.E5.setNop()
						self.E4.desbloqueou = False
						self.E4.do()
				else:
					self.E5.setNop()
			else:
				self.E5.desbloqueou = False
				self.E5.do()

		self.produtividade = float(self.concluidas)/self.clock
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
			self.view.lpc["text"] = str(eval(self.pc))
			self.view.lconcluidas["text"] = self.concluidas
			self.view.lprodutividade["text"] = "{0:.2f}".format(100*self.produtividade)+"%"

			self.setText(self.view.lend1, self.getListaMemoria(1)[0], "")
			self.setText(self.view.lval1, self.getListaMemoria(1)[1], "?")
			self.setText(self.view.lend2, self.getListaMemoria(2)[0], "")
			self.setText(self.view.lval2, self.getListaMemoria(2)[1], "?")
			self.setText(self.view.lend3, self.getListaMemoria(3)[0], "")
			self.setText(self.view.lval3, self.getListaMemoria(3)[1], "?")
			self.setText(self.view.lend4, self.getListaMemoria(4)[0], "")
			self.setText(self.view.lval4, self.getListaMemoria(4)[1], "?")

			self.view.lr0["text"] = str(eval(self.reg[0].valor))
			self.view.lr1["text"] = str(eval(self.reg[1].valor))
			self.view.lr2["text"] = str(eval(self.reg[2].valor))
			self.view.lr3["text"] = str(eval(self.reg[3].valor))
			self.view.lr4["text"] = str(eval(self.reg[4].valor))
			self.view.lr5["text"] = str(eval(self.reg[5].valor))
			self.view.lr6["text"] = str(eval(self.reg[6].valor))
			self.view.lr7["text"] = str(eval(self.reg[7].valor))
			self.view.lr8["text"] = str(eval(self.reg[8].valor))
			self.view.lr9["text"] = str(eval(self.reg[9].valor))
			self.view.lr10["text"] = str(eval(self.reg[10].valor))
			self.view.lr11["text"] = str(eval(self.reg[11].valor))
			self.view.lr12["text"] = str(eval(self.reg[12].valor))
			self.view.lr13["text"] = str(eval(self.reg[13].valor))
			self.view.lr14["text"] = str(eval(self.reg[14].valor))
			self.view.lr15["text"] = str(eval(self.reg[15].valor))
			self.view.lr16["text"] = str(eval(self.reg[16].valor))
			self.view.lr17["text"] = str(eval(self.reg[17].valor))
			self.view.lr18["text"] = str(eval(self.reg[18].valor))
			self.view.lr19["text"] = str(eval(self.reg[19].valor))
			self.view.lr20["text"] = str(eval(self.reg[20].valor))
			self.view.lr21["text"] = str(eval(self.reg[21].valor))
			self.view.lr22["text"] = str(eval(self.reg[22].valor))
			self.view.lr23["text"] = str(eval(self.reg[23].valor))
			self.view.lr24["text"] = str(eval(self.reg[24].valor))
			self.view.lr25["text"] = str(eval(self.reg[25].valor))
			self.view.lr26["text"] = str(eval(self.reg[26].valor))
			self.view.lr27["text"] = str(eval(self.reg[27].valor))
			self.view.lr28["text"] = str(eval(self.reg[28].valor))
			self.view.lr29["text"] = str(eval(self.reg[29].valor))
			self.view.lr30["text"] = str(eval(self.reg[30].valor))
			self.view.lr31["text"] = str(eval(self.reg[31].valor))
