print "MODELS"
from filereader import FileReader

class Estagio:
	def __init__(self, num):
		self.num = num
		self.InstName = str(num)+":"
		self.SinControle = ""

class Mips():
	fr = FileReader()
	clock = -1
	pc = -1
	concluidas = 0
	produtividade = 0
	E1 = Estagio(1)
	E2 = Estagio(2)
	E3 = Estagio(3)
	E4 = Estagio(4)
	E5 = Estagio(5)

	end1 = None
	val1 = None
	end2 = None
	val2 = None
	end3 = None
	val3 = None
	end4 = None
	val4 = None

	r0 = 0
	r1 = 0
	r2 = 0
	r3 = 0
	r4 = 0
	r5 = 0
	r6 = 0
	r7 = 0
	r8 = 0
	r9 = 0
	r10 = 0
	r11 = 0
	r12 = 0
	r13 = 0
	r14 = 0
	r15 = 0
	r16 = 0
	r17 = 0
	r18 = 0
	r19 = 0
	r20 = 0
	r21 = 0
	r22 = 0
	r23 = 0
	r24 = 0
	r25 = 0
	r26 = 0
	r27 = 0
	r28 = 0
	r29 = 0
	r30 = 0
	r31 = 0

	def read(self, filePath):
		self.fr.read(filePath)
		# self.getInst(2)
	def setView(self, view):
		self.view = view
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
		self.clock = self.clock + 1
		
		self.atualizarLabels()

	def setText(self, dest, ori, none):
		if ori != None:
			dest = ori
		else:
			dest = none

	def atualizarLabels(self):
		if self.view != None:			
			self.setText(self.view.E1_instrucao["text"], self.E1.InstName, "")
			self.setText(self.view.E2_instrucao["text"], self.E2.InstName, "")
			self.setText(self.view.E3_instrucao["text"], self.E3.InstName, "")
			self.setText(self.view.E4_instrucao["text"], self.E4.InstName, "")
			self.setText(self.view.E5_instrucao["text"], self.E5.InstName, "")
			self.setText(self.view.E1_controle["text"], self.E1.SinControle, "")
			self.setText(self.view.E2_controle["text"], self.E2.SinControle, "")
			self.setText(self.view.E3_controle["text"], self.E3.SinControle, "")
			self.setText(self.view.E4_controle["text"], self.E4.SinControle, "")
			self.setText(self.view.E5_controle["text"], self.E5.SinControle, "")

			self.view.lclock["text"] = self.clock
			self.view.lpc["text"] = self.pc
			self.view.lconcluidas["text"] = self.concluidas
			self.view.lprodutividade["text"] = self.produtividade

			self.setText(self.view.lend1["text"], self.end1, "")
			self.setText(self.view.lval1["text"], self.val1, "?")
			self.setText(self.view.lend2["text"], self.end2, "")
			self.setText(self.view.lval2["text"], self.val2, "?")
			self.setText(self.view.lend3["text"], self.end3, "")
			self.setText(self.view.lval3["text"], self.val3, "?")
			self.setText(self.view.lend4["text"], self.end4, "")
			self.setText(self.view.lval4["text"], self.val4, "?")

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