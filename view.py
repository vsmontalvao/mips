from Tkinter import *
import ImageTk, time
import tkFileDialog
import tkFont
from threading import Thread
from filereader import FileReader
import os

class geradorDeClock(Thread):
    def __init__(self, metodo):
        Thread.__init__(self)
        self.metodo = metodo
        self.contando = True
        self.terminado = False

    def pausar(self):
        self.contando = False

    def continuar(self):
        self.contando = True

    def terminar(self):
        self.terminado = True

    def run(self):
        try:
            while not self.terminado:
                if self.contando:
                    self.metodo()
                time.sleep(1)
        except:
            None
class Application(Frame):
    razao = 1.5
    # grid
    linha_botoes = 30
    linha_instrucoes = 225
    linha_controle = 265
    coluna_dir=1150
    coluna_end=889
    coluna_valor=1028
    lblbgcolor = "white"
    linr0 = 464
    colr0 = 890
    reglindist = 28.5
    regcoldist = 84.3

    # pendulo?
    pendulo = None

    # fonts
    fonte_negrito = "Arial 8 bold"
    fonte_textos = "Arial 8"
    fonte_maior = "Arial 14"

    def setMips(self, mips):
        self.mips = mips
    # button actions
    def quit(self):
        if pendulo != None:
            self.pendulo.terminar()
        self.quit

    def play(self):
        print "Play!"
        # Para agilizar a execucao - Remover depois
        # self.FileName["text"] = "C:/Users/vsmon_000/Documents/code/mips/mips/instructions/program_addi.txt"
        self.FileName["text"] = os.getcwd().replace("\\","/")+"/instructions/program.txt"
        self.mips.read(self.FileName["text"])

        if self.pendulo == None:
            self.pendulo = geradorDeClock(self.next)
            self.pendulo.start()
        else:
            if not self.pendulo.contando:
                self.pendulo.continuar()
        
    def pause(self):
        print "Pause!"
        if self.pendulo != None:
            if self.pendulo.contando:
                self.pendulo.pausar()

    def stop(self):
        print "Stop!"
        if self.pendulo != None:
            if not self.pendulo.terminado:
                self.pendulo.terminar()
                self.pendulo = None
        self.zerar_labels()
        if self.mips != None:
            self.mips.inicio()

    def next(self):
        print "next!"
        if self.mips != None:
            self.mips.proxEstagio()

    def open(self):
        print "Open!"

        # file choosing
        master = Tk()
        master.withdraw() # hiding tkinter window

        file_path = tkFileDialog.askopenfilename(title="Open file", filetypes=[("txt file",".txt")])

        if file_path != "":
            print "You chose file with path:", file_path
        else:
            print "You should have chosen a file."
        self.FileName["text"] = file_path
        self.mips.read(file_path)

    def zerar_labels(self):
        self.lclock["text"] = "?"
        self.lpc["text"] = "?"
        self.lconcluidas["text"] = "?"
        self.lprodutividade["text"] = "?"
        self.E1_instrucao["text"] = "l1:addi R10, R0, 100"
        self.E1_controle["text"] = ""
        self.E2_instrucao["text"] = "l2:sw R0, 24(R0)"
        self.E2_controle["text"] = ""
        self.E3_instrucao["text"] = "l3:sw R0, 28(R0)"
        self.E3_controle["text"] = ""
        self.E4_instrucao["text"] = "l4:lw R6,28(R0)"
        self.E4_controle["text"] = ""
        self.E5_instrucao["text"] = "l5:mul R7,R6,R6"
        self.E5_controle["text"] = ""
        self.lval1["text"] = "24"
        self.lend1["text"] = "?"
        self.lval2["text"] = "28"
        self.lend2["text"] = "?"
        self.lval3["text"] = "28"
        self.lend3["text"] = "?"
        self.lval4["text"] = "28"
        self.lend4["text"] = "?"
        self.lr0["text"] = "0"
        self.lr1["text"] = "0"
        self.lr2["text"] = "0"
        self.lr3["text"] = "0"
        self.lr4["text"] = "0"
        self.lr5["text"] = "0"
        self.lr6["text"] = "0"
        self.lr7["text"] = "0"
        self.lr8["text"] = "?"
        self.lr9["text"] = "?"
        self.lr10["text"] = "?"
        self.lr11["text"] = "?"
        self.lr12["text"] = "?"
        self.lr13["text"] = "?"
        self.lr14["text"] = "?"
        self.lr15["text"] = "?"
        self.lr16["text"] = "?"
        self.lr17["text"] = "?"
        self.lr18["text"] = "?"
        self.lr19["text"] = "?"
        self.lr20["text"] = "?"
        self.lr21["text"] = "?"
        self.lr22["text"] = "?"
        self.lr23["text"] = "?"
        self.lr24["text"] = "?"
        self.lr25["text"] = "?"
        self.lr26["text"] = "?"
        self.lr27["text"] = "?"
        self.lr28["text"] = "?"
        self.lr29["text"] = "?"
        self.lr30["text"] = "?"
        self.lr31["text"] = "?"

    def labels_iniciais(self):
        canvas = self.canvas
        
        self.E1_instrucao = E1_instrucao = Label(self, text="l1:addi R10, R0, 100", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E1inst_window = canvas.create_window(51, self.linha_instrucoes, anchor=NW, window=E1_instrucao)
        self.E2_instrucao = E2_instrucao = Label(self, text="l2:sw R0, 24(R0)", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E2inst_window = canvas.create_window(215, self.linha_instrucoes, anchor=NW, window=E2_instrucao)
        self.E3_instrucao = E3_instrucao = Label(self, text="l3:sw R0, 28(R0)", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E3inst_window = canvas.create_window(379, self.linha_instrucoes, anchor=NW, window=E3_instrucao)
        self.E4_instrucao = E4_instrucao = Label(self, text="l4:lw R6,28(R0)", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E4inst_window = canvas.create_window(543, self.linha_instrucoes, anchor=NW, window=E4_instrucao)
        self.E5_instrucao = E5_instrucao = Label(self, text="l5:mul R7,R6,R6", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E5inst_window = canvas.create_window(707, self.linha_instrucoes, anchor=NW, window=E5_instrucao)
        
        self.FileNameLabel = FileNameLabel = Label(self, text="Choosen file:", bg=self.lblbgcolor, anchor=NW, font=self.fonte_negrito, width=40)
        FileNameLabel_window = canvas.create_window(340, 30, anchor=NW, window=FileNameLabel)
        self.FileName = FileName = Label(self, text="No file chosen yet.", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=60)
        FileName_window = canvas.create_window(340, 50, anchor=NW, window=FileName)

        self.E1_controle = E1_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E1cont_window = canvas.create_window(51, self.linha_controle, anchor=NW, window=E1_controle)
        self.E2_controle = E2_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E2cont_window = canvas.create_window(215, self.linha_controle, anchor=NW, window=E2_controle)
        self.E3_controle = E3_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E3cont_window = canvas.create_window(379, self.linha_controle, anchor=NW, window=E3_controle)
        self.E4_controle = E4_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E4cont_window = canvas.create_window(543, self.linha_controle, anchor=NW, window=E4_controle)
        self.E5_controle = E5_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=18)
        E5cont_window = canvas.create_window(707, self.linha_controle, anchor=NW, window=E5_controle)

        self.lclock = lclock = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_maior, width=10)
        clock_window = canvas.create_window(992, 48, anchor=NW, window=lclock)
        self.lpc = lpc = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_maior, width=10)
        pc_windowoncluidas = canvas.create_window(887, 82, anchor=NW, window=lpc)
        self.lconcluidas = lconcluidas = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_maior, width=10)
        concluidas_window = canvas.create_window(1052, 116, anchor=NW, window=lconcluidas)
        self.lprodutividade = lprodutividade = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_maior, width=7)
        pipeliNW_window = canvas.create_window(1089, 150, anchor=NW, window=lprodutividade)

        self.lend1 = lend1 = Label(self, text="24", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        end1_window = canvas.create_window(self.coluna_end, 264, anchor=NW, window=lend1)
        self.lval1 = lval1 = Label(self, text="?", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        val1_window = canvas.create_window(self.coluna_valor, 264, anchor=NW, window=lval1)
        self.lend2 = lend2 = Label(self, text="28", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        end2_window = canvas.create_window(self.coluna_end, 299, anchor=NW, window=lend2)
        self.lval2 = lval2 = Label(self, text="?", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        val2_window = canvas.create_window(self.coluna_valor, 299, anchor=NW, window=lval2)
        self.lend3 = lend3 = Label(self, text="28", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        end3_window = canvas.create_window(self.coluna_end, 334, anchor=NW, window=lend3)
        self.lval3 = lval3 = Label(self, text="?", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        val3_window = canvas.create_window(self.coluna_valor, 334, anchor=NW, window=lval3)
        self.lend4 = lend4 = Label(self, text="28", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        end4_window = canvas.create_window(self.coluna_end, 369, anchor=NW, window=lend4)
        self.lval4 = lval4 = Label(self, text="?", bg=self.lblbgcolor, anchor=CENTER, font=self.fonte_maior, width=10)
        val4_window = canvas.create_window(self.coluna_valor, 369, anchor=NW, window=lval4)

        self.lr0 = lr0 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r0_window = canvas.create_window(self.colr0, self.linr0, anchor=NW, window=lr0)
        self.lr1 = lr1 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r1_window = canvas.create_window(self.colr0 , self.linr0 + self.reglindist, anchor=NW, window=lr1)
        self.lr2 = lr2 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r2_window = canvas.create_window(self.colr0, self.linr0 + 2*self.reglindist, anchor=NW, window=lr2)
        self.lr3 = lr3 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r3_window = canvas.create_window(self.colr0, self.linr0 + 3*self.reglindist, anchor=NW, window=lr3)
        self.lr4 = lr4 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r4_window = canvas.create_window(self.colr0, self.linr0 + 4*self.reglindist, anchor=NW, window=lr4)
        self.lr5 = lr5 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r5_window = canvas.create_window(self.colr0, self.linr0 + 5*self.reglindist, anchor=NW, window=lr5)
        self.lr6 = lr6 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r6_window = canvas.create_window(self.colr0, self.linr0 + 6*self.reglindist, anchor=NW, window=lr6)
        self.lr7 = lr7 = Label(self, text="0", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r7_window = canvas.create_window(self.colr0, self.linr0 + 7*self.reglindist, anchor=NW, window=lr7)

        self.lr8 = lr8 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r8_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0, anchor=NW, window=lr8)
        self.lr9 = lr9 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r9_window = canvas.create_window(self.colr0 + self.regcoldist , self.linr0 + self.reglindist, anchor=NW, window=lr9)
        self.lr10 = lr10 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r10_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 2*self.reglindist, anchor=NW, window=lr10)
        self.lr11 = lr11 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r11_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 3*self.reglindist, anchor=NW, window=lr11)
        self.lr12 = lr12 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r12_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 4*self.reglindist, anchor=NW, window=lr12)
        self.lr13 = lr13 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r13_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 5*self.reglindist, anchor=NW, window=lr13)
        self.lr14 = lr14 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r14_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 6*self.reglindist, anchor=NW, window=lr14)
        self.lr15 = lr15 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r15_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 7*self.reglindist, anchor=NW, window=lr15)

        self.lr16 = lr16 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r16_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0, anchor=NW, window=lr16)
        self.lr17 = lr17 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r17_window = canvas.create_window(self.colr0 + 2*self.regcoldist , self.linr0 + self.reglindist, anchor=NW, window=lr17)
        self.lr18 = lr18 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r18_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 2*self.reglindist, anchor=NW, window=lr18)
        self.lr19 = lr19 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r19_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 3*self.reglindist, anchor=NW, window=lr19)
        self.lr20 = lr20 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r20_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 4*self.reglindist, anchor=NW, window=lr20)
        self.lr21 = lr21 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r21_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 5*self.reglindist, anchor=NW, window=lr21)
        self.lr22 = lr22 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r22_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 6*self.reglindist, anchor=NW, window=lr22)
        self.lr23 = lr23 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r23_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 7*self.reglindist, anchor=NW, window=lr23)

        self.lr24 = lr24 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r24_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0, anchor=NW, window=lr24)
        self.lr25 = lr25 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r25_window = canvas.create_window(self.colr0 + 3*self.regcoldist , self.linr0 + self.reglindist, anchor=NW, window=lr25)
        self.lr26 = lr26 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r26_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 2*self.reglindist, anchor=NW, window=lr26)
        self.lr27 = lr27 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r27_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 3*self.reglindist, anchor=NW, window=lr27)
        self.lr28 = lr28 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r28_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 4*self.reglindist, anchor=NW, window=lr28)
        self.lr29 = lr29 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r29_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 5*self.reglindist, anchor=NW, window=lr29)
        self.lr30 = lr30 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r30_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 6*self.reglindist, anchor=NW, window=lr30)
        self.lr31 = lr31 = Label(self, text="?", bg=self.lblbgcolor, anchor=NW, font=self.fonte_textos, width=2)
        r31_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 7*self.reglindist, anchor=NW, window=lr31)

        # Botoes e Imagens
    def createWidgets(self):
        # Carrega Imagens
        self.fundo = ImageTk.PhotoImage(file="images/design_programa.png")
        self.bstart_img = ImageTk.PhotoImage(file="images/start.png")
        self.bstop_img = ImageTk.PhotoImage(file="images/stop.png")
        self.bpause_img = ImageTk.PhotoImage(file="images/pause.png")
        self.bnext_img = ImageTk.PhotoImage(file="images/next.png")
        self.bopen_img = ImageTk.PhotoImage(file="images/open.png")
        

        self.canvas = canvas = Canvas(self, bg="white", width=1200, height=720)
        canvas.pack()
        canvas.create_image(600, 360, image=self.fundo)

        bplay = Button(self, text="Play", command=self.play, fg="darkgreen",
            width=25*self.razao, height=25*self.razao, image=self.bstart_img, bg="white", bd=0, activebackground="white")
        bplay_window = canvas.create_window(43, self.linha_botoes, anchor=NW, window=bplay)
        bpause = Button(self, text="Pause", command=self.pause, width=25*self.razao,
            height=25*self.razao, image=self.bpause_img, bg="white", bd=0, activebackground="white")
        bpause_window = canvas.create_window(94, self.linha_botoes, anchor=NW, window=bpause)
        bstop = Button(self, text="Stop", command=self.stop, width=25*self.razao,
            height=25*self.razao, image=self.bstop_img, bg="white", bd=0, activebackground="white")
        bstop_window = canvas.create_window(145, self.linha_botoes, anchor=NW, window=bstop)
        bnext = Button(self, text="next", command=self.next, width=25*self.razao,
            height=25*self.razao, image=self.bnext_img, bg="white", bd=0, activebackground="white")
        bnext_window = canvas.create_window(196, self.linha_botoes, anchor=NW, window=bnext)
        bopen = Button(self, text="Open", command=self.open, width=35*self.razao,
            height=25*self.razao, image=self.bopen_img, bg="white", bd=0, activebackground="white")
        bopen_window = canvas.create_window(247, self.linha_botoes, anchor=NW, window=bopen)

        self.labels_iniciais()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
def GUI(mips):
    print "VIEW"
    # Inicializa o Tkinter
    root = Tk()
    root.title("mips simulator")
    root.geometry("1200x720")

    #Lanca o nosso app, seu loop principal e finaliza o programa
    app = Application(master=root)
    mips.setView(app)
    app.setMips(mips)
    app.mainloop()
