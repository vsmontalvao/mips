from Tkinter import *
import ImageTk

class Application(Frame):
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
        canvas = Canvas(self, bg="white", width=800, height=600)
        canvas.pack()
        # QUIT = Button(self, text="QUIT", command=self.quit, fg="red", anchor= W)
        # QUIT.pack({"side": "left"})
        bplay = Button(self, text="Play", command=self.play, fg="darkgreen",
            width="25", height="25", image=bstart_img)
        bplay_window = canvas.create_window(307, 20, anchor=NW, window=bplay)
        bpause = Button(self, text="Pause", command=self.pause, width="25",
            height="25", image=bpause_img)
        bpause_window = canvas.create_window(344, 20, anchor=NW, window=bpause)
        bstop = Button(self, text="Stop", command=self.stop, width="25",
            height="25", image=bstop_img)
        bstop_window = canvas.create_window(381, 20, anchor=NW, window=bstop)
        bnext = Button(self, text="Next", command=self.next, width="25",
            height="25", image=bnext_img)
        bnext_window = canvas.create_window(418, 20, anchor=NW, window=bnext)
        bopen = Button(self, text="Open", command=self.open, width="35",
            height="25", image=bopen_img)
        bopen_window = canvas.create_window(455, 20, anchor=NW, window=bopen)
        canvas.create_image(290, 420, image=mips_blocks)
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
print "VIEW"
# Inicializa o Tkinter
root = Tk()
root.title("mips simulator")
root.geometry("800x600")
# Carrega Imagens
mips_blocks = ImageTk.PhotoImage(file="images/mips_color.png")
bstart_img = ImageTk.PhotoImage(file="images/start.png")
bstop_img = ImageTk.PhotoImage(file="images/stop.png")
bpause_img = ImageTk.PhotoImage(file="images/pause.png")
bnext_img = ImageTk.PhotoImage(file="images/next.png")
bopen_img = ImageTk.PhotoImage(file="images/open.png")
#Lanca o nosso app, seu loop principal e finaliza o programa
app = Application(master=root)
app.mainloop()
root.destroy()