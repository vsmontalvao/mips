print "MODELS"
from filereader import FileReader


class Estagio:
    def __init__(self, num):
        self.num = num
        self.InstName = str(num)+":"
        self.SinControle = ""

    def desbloquear(self):
        self.bloqueado = True

    def bloquear(self):
        self.bloqueado = False

    def getStatusBloqueado(self):
        return self.bloqueado

class Mips:
    def __init__(self):
        self.fr = FileReader()
        self.inicio()

    def inicio(self):
        self.clock = -1
        self.pc = -1
        self.concluidas = 0
        self.produtividade = 0
        self.E1 = Estagio(1)
        self.E2 = Estagio(2)
        self.E3 = Estagio(3)
        self.E4 = Estagio(4)
        self.E5 = Estagio(5)

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

    def read(self, filePath):
        self.fr.read(filePath)
        # self.getInst(2)

    def setView(self, view):
        self.view = view

    def getInst(self, i):
        instruction = self.fr.getInst(i)[0:32]
        return instruction

    def instructionFetch(self, i):
        instructionCode = self.getInst(i)[0:6]
        return instructionCode

    def instructionDecodeRegisterFetch(self, instructionCode, i):
        bits = self.getInst(i)
        if instructionCode == "000010":
            self.address = bits[6:32]
        else:
            self.s = bits[6:11]
            self.t = bits[11:16]
            if instructionCode == "000000":
                self.d = bits(i)[16:21]
                self.shamt = bits(i)[21:26]
                if bits[26:32] == "100000":
                    self.instruction = "Add"
                elif bits[26:32] == "011000":
                    self.instruction = "Mul"
                elif bits[26:32] == "000000":
                    self.instruction = "Nop"
                elif bits[26:32] == "100010":
                    self.instruction = "Sub"
            else:
                self.immediate = bits[16:32]
                if instructionCode == "001000":
                    self.instruction = "Addi"
                elif instructionCode == "000101":
                    self.instruction = "Beq"
                elif instructionCode == "000111":
                    self.instruction = "Ble"
                elif instructionCode == "000100":
                    self.instruction = "Bne"
                elif instructionCode == "100011":
                    self.instruction = "Lw"
                elif instructionCode == "101011":
                    self.instruction = "Sw"

    def instructionExecute(self):
        pass

    def memoryAccess(self):
        pass

    def writeBack(self):
        pass

    def proxEstagio(self):
        self.clock = self.clock + 1
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

class InstrucaoR:
    def __init__(self, instrucao):
        self.rs = instrucao[6:11]
        self.rt = instrucao[11:16]
        self.rd = instrucao[16:21]
        self.shamt = instrucao[21:26]

class InstrucaoI:
    def __init__(self, instrucao):
        self.rs = instrucao[6:11]
        self.rt = instrucao[11:16]
        self.immediate = instrucao[16:32]

class InstrucaoJ:
    def __init__(self,instrucao):
        self.targetAddress = instrucao[6:32]



