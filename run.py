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
        QUIT = Button(self)
        QUIT["text"] = "QUIT"
        QUIT["fg"]   = "red"
        QUIT["command"] =  self.quit
        QUIT.pack({"side": "left"})

        bplay = Button(self)
        bplay["text"] = "Play"
        bplay["fg"]   = "darkgreen"
        bplay["command"] = self.play
        bplay.config(image=bstart_img)
        bplay.pack({"side": "left"})

        bpause = Button(self)
        bpause["text"] = "Pause"
        bpause["command"] = self.pause
        bpause.config(image=bpause_img)
        bpause.pack({"side": "left"})

        bstop = Button(self)
        bstop["text"] = "Stop"
        bstop["command"] = self.stop
        bstop.config(image=bstop_img)
        bstop.pack({"side": "left"})

        bnext = Button(self)
        bnext["text"] = "Next"
        bnext["command"] = self.next
        bnext.config(image=bnext_img)
        bnext.pack({"side": "left"})

        bopen = Button(self)
        bopen["text"] = "Open"
        bopen["command"] = self.open
        bopen.config(image=bopen_img)
        bopen.pack({"side": "left"})

        canvas = Canvas(self, bg="black", width=537, height=321)
        canvas.pack()
        
        canvas.create_image(537, 321, image=mips_blocks)
        canvas["bg"]="white"

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


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