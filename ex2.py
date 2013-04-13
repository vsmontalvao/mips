from Tkinter import *
import ImageTk

class Application(Frame):
	print "Started"

root = Tk()
root.title("mips simulator")
root.geometry("640x510")

app = Application(master=root)
app.pack()

canvas = Canvas(app, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="images/mips_frompdf.gif")
canvas.create_image(150, 150, image=photoimage)

app.mainloop()
root.destroy()