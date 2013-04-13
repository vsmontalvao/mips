from Tkinter import *
import ImageTk

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"
    def play(self):
        print "Play!"
    def pause(self):
        print "Pause!"
    def next(self):
        print "Next!"
    def open(self):
        print "Open!"

    # Botoes e Imagens
    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.bplay = Button(self)
        self.bplay["text"] = "Play"
        self.bplay["fg"]   = "darkgreen"
        self.bplay["command"] = self.play
        self.bplay.pack({"side": "left"})

        self.bpause = Button(self)
        self.bpause["text"] = "Pause"
        self.bpause["command"] = self.pause
        self.bpause.pack({"side": "left"})

        self.bnext = Button(self)
        self.bnext["text"] = "Next"
        self.bnext["command"] = self.next
        self.bnext.pack({"side": "left"})

        self.bopen = Button(self)
        self.bopen["text"] = "Open"
        self.bopen["command"] = self.open
        self.bopen.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("mips simulator")
# root.geometry("640x510")

app = Application(master=root)
app.pack()

canvas = Canvas(app, bg="black")#, width=500, height=500
canvas.pack()

photoimage = ImageTk.PhotoImage(file="images/mips_color.png")
canvas.create_image(150, 150, image=photoimage)
canvas["bg"]="white"

app.mainloop()
root.destroy()