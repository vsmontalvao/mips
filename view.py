from Tkinter import *
import ImageTk

class Application(Frame):
    razao = 1.5
    linha_botoes = 28
    linha_instrucoes = 225
    linha_controle = 265
    coluna_dir=1150
    coluna_end=889
    coluna_valor=1028
    fonte_textos = "Arial 7"
    fonte_maior = "Arial 10"
    lblbgcolor = "white"
    linr0 = 465
    colr0 = 895
    reglindist = 28.5
    regcoldist = 84.3

    def say_hi(self):
        print "hi there, everyone!"
    def play(self):
        print "Play!"
    def pause(self):
        print "Pause!"
    def stop(self):
        print "Stop!"
    def next(self):
        print "Next!"
    def open(self):
        print "Open!"
    # Botoes e Imagens
    def createWidgets(self):
        canvas = Canvas(self, bg="white", width=1200, height=720)
        canvas.pack()
        canvas.create_image(600, 360, image=fundo)
        # QUIT = Button(self, text="QUIT", command=self.quit, fg="red", anchor= W)
        # QUIT.pack({"side": "left"})
        bplay = Button(self, text="Play", command=self.play, fg="darkgreen",
            width=25*self.razao, height=25*self.razao, image=bstart_img, bg="white")
        bplay_window = canvas.create_window(306, self.linha_botoes, anchor=NW, window=bplay)
        bpause = Button(self, text="Pause", command=self.pause, width=25*self.razao,
            height=25*self.razao, image=bpause_img, bg="white")
        bpause_window = canvas.create_window(357, self.linha_botoes, anchor=NW, window=bpause)
        bstop = Button(self, text="Stop", command=self.stop, width=25*self.razao,
            height=25*self.razao, image=bstop_img, bg="white")
        bstop_window = canvas.create_window(408, self.linha_botoes, anchor=NW, window=bstop)
        bnext = Button(self, text="Next", command=self.next, width=25*self.razao,
            height=25*self.razao, image=bnext_img, bg="white")
        bnext_window = canvas.create_window(459, self.linha_botoes, anchor=NW, window=bnext)
        bopen = Button(self, text="Open", command=self.open, width=35*self.razao,
            height=25*self.razao, image=bopen_img, bg="white")
        bopen_window = canvas.create_window(510, self.linha_botoes, anchor=NW, window=bopen)
        

        E1_instrucao = Label(self, text="l1:addi R10, R0, 100", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E1inst_window = canvas.create_window(51, self.linha_instrucoes, anchor=NW, window=E1_instrucao)

        E2_instrucao = Label(self, text="l2:sw R0, 24(R0)", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E2inst_window = canvas.create_window(215, self.linha_instrucoes, anchor=NW, window=E2_instrucao)
        E3_instrucao = Label(self, text="l3:sw R0, 28(R0)", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E3inst_window = canvas.create_window(379, self.linha_instrucoes, anchor=NW, window=E3_instrucao)
        E4_instrucao = Label(self, text="l4:lw R6,28(R0)", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E4inst_window = canvas.create_window(543, self.linha_instrucoes, anchor=NW, window=E4_instrucao)
        E5_instrucao = Label(self, text="l5:mul R7,R6,R6", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E5inst_window = canvas.create_window(707, self.linha_instrucoes, anchor=NW, window=E5_instrucao)

        E1_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E1cont_window = canvas.create_window(51, self.linha_controle, anchor=NW, window=E1_controle)
        E2_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E2cont_window = canvas.create_window(215, self.linha_controle, anchor=NW, window=E2_controle)
        E3_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E3cont_window = canvas.create_window(379, self.linha_controle, anchor=NW, window=E3_controle)
        E4_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E4cont_window = canvas.create_window(543, self.linha_controle, anchor=NW, window=E4_controle)
        E5_controle = Label(self, text="", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        E5cont_window = canvas.create_window(707, self.linha_controle, anchor=NW, window=E5_controle)

        lclock = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        clock_window = canvas.create_window(self.coluna_dir, 54, anchor=NW, window=lclock)
        lpc = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        pc_windowoncluidas = canvas.create_window(self.coluna_dir, 88, anchor=NW, window=lpc)
        lconcluidas = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        concluidas_window = canvas.create_window(self.coluna_dir, 122, anchor=NW, window=lconcluidas)
        lpipeline = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        pipeline_window = canvas.create_window(self.coluna_dir, 156, anchor=NW, window=lpipeline)

        lend1 = Label(self, text="24", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        end1_window = canvas.create_window(self.coluna_end, 274, anchor=NW, window=lend1)
        lval1 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        val1_window = canvas.create_window(self.coluna_valor, 274, anchor=NW, window=lval1)
        lend2 = Label(self, text="28", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        end2_window = canvas.create_window(self.coluna_end, 309, anchor=NW, window=lend2)
        lval2 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        val2_window = canvas.create_window(self.coluna_valor, 309, anchor=NW, window=lval2)
        lend3 = Label(self, text="28", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        end3_window = canvas.create_window(self.coluna_end, 344, anchor=NW, window=lend3)
        lval3 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        val3_window = canvas.create_window(self.coluna_valor, 344, anchor=NW, window=lval3)
        lend4 = Label(self, text="28", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        end4_window = canvas.create_window(self.coluna_end, 379, anchor=NW, window=lend4)
        lval4 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_maior)
        val4_window = canvas.create_window(self.coluna_valor, 379, anchor=NW, window=lval4)

        lr0 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r0_window = canvas.create_window(self.colr0, self.linr0, anchor=NW, window=lr0)
        lr1 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r1_window = canvas.create_window(self.colr0 , self.linr0 + self.reglindist, anchor=NW, window=lr1)
        lr2 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r2_window = canvas.create_window(self.colr0, self.linr0 + 2*self.reglindist, anchor=NW, window=lr2)
        lr3 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r3_window = canvas.create_window(self.colr0, self.linr0 + 3*self.reglindist, anchor=NW, window=lr3)
        lr4 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r4_window = canvas.create_window(self.colr0, self.linr0 + 4*self.reglindist, anchor=NW, window=lr4)
        lr5 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r5_window = canvas.create_window(self.colr0, self.linr0 + 5*self.reglindist, anchor=NW, window=lr5)
        lr6 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r6_window = canvas.create_window(self.colr0, self.linr0 + 6*self.reglindist, anchor=NW, window=lr6)
        lr7 = Label(self, text="0", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r7_window = canvas.create_window(self.colr0, self.linr0 + 7*self.reglindist, anchor=NW, window=lr7)

        lr8 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r8_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0, anchor=NW, window=lr8)
        lr9 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r9_window = canvas.create_window(self.colr0 + self.regcoldist , self.linr0 + self.reglindist, anchor=NW, window=lr9)
        lr10 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r10_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 2*self.reglindist, anchor=NW, window=lr10)
        lr11 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r11_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 3*self.reglindist, anchor=NW, window=lr11)
        lr12 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r12_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 4*self.reglindist, anchor=NW, window=lr12)
        lr13 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r13_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 5*self.reglindist, anchor=NW, window=lr13)
        lr14 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r14_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 6*self.reglindist, anchor=NW, window=lr14)
        lr15 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r15_window = canvas.create_window(self.colr0 + self.regcoldist, self.linr0 + 7*self.reglindist, anchor=NW, window=lr15)

        lr16 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r16_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0, anchor=NW, window=lr16)
        lr17 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r17_window = canvas.create_window(self.colr0 + 2*self.regcoldist , self.linr0 + self.reglindist, anchor=NW, window=lr17)
        lr18 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r18_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 2*self.reglindist, anchor=NW, window=lr18)
        lr19 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r19_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 3*self.reglindist, anchor=NW, window=lr19)
        lr20 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r20_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 4*self.reglindist, anchor=NW, window=lr20)
        lr21 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r21_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 5*self.reglindist, anchor=NW, window=lr21)
        lr22 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r22_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 6*self.reglindist, anchor=NW, window=lr22)
        lr23 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r23_window = canvas.create_window(self.colr0 + 2*self.regcoldist, self.linr0 + 7*self.reglindist, anchor=NW, window=lr23)

        lr24 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r24_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0, anchor=NW, window=lr24)
        lr25 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r25_window = canvas.create_window(self.colr0 + 3*self.regcoldist , self.linr0 + self.reglindist, anchor=NW, window=lr25)
        lr26 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r26_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 2*self.reglindist, anchor=NW, window=lr26)
        lr27 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r27_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 3*self.reglindist, anchor=NW, window=lr27)
        lr28 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r28_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 4*self.reglindist, anchor=NW, window=lr28)
        lr29 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r29_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 5*self.reglindist, anchor=NW, window=lr29)
        lr30 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r30_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 6*self.reglindist, anchor=NW, window=lr30)
        lr31 = Label(self, text="?", bg=self.lblbgcolor, anchor=NE, font=self.fonte_textos)
        r31_window = canvas.create_window(self.colr0 + 3*self.regcoldist, self.linr0 + 7*self.reglindist, anchor=NW, window=lr31)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
print "VIEW"
# Inicializa o Tkinter
root = Tk()
root.title("mips simulator")
root.geometry("1200x720")
# Carrega Imagens
fundo = ImageTk.PhotoImage(file="images/design_programa.png")
bstart_img = ImageTk.PhotoImage(file="images/start.png")
bstop_img = ImageTk.PhotoImage(file="images/stop.png")
bpause_img = ImageTk.PhotoImage(file="images/pause.png")
bnext_img = ImageTk.PhotoImage(file="images/next.png")
bopen_img = ImageTk.PhotoImage(file="images/open.png")
#Lanca o nosso app, seu loop principal e finaliza o programa
app = Application(master=root)
app.mainloop()
root.destroy()