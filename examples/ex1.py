import sys, os
from Tkinter import *
import Tkinter as tk
import tkFileDialog
from tkFileDialog import askopenfile , asksaveasfile   # Open dialog box
import tkMessageBox
import ttk

class Window():

    def __init__(self):
        "Initialisation for empty table in window"

        self.root = Tk()                              # Create window
        self.root.title("Window")               # Window title
        self.mycolour = self.root.cget('bg')          # Get main window bg colour for default colour
        self.s = ttk.Style()
        self.s.theme_use('xpnative')
        self.s.configure("Black.TLabel", background="black")

        self.win1 = Frame(self.root)
        self.win1.pack(side="top", fill="both", expand=True)
        self.win1.grid_columnconfigure(0, weight=1) # Column 0
        self.menu1 = Menu(self.root)

        # Menu
        filemenu = Menu(self.menu1, tearoff=0)
        filemenu.add_command(label="Import", command=self.import_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        self.menu1.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=self.menu1)

        self.frame_table = ttk.Frame(self.win1, style="Black.TLabel", relief='sunken', borderwidth=1)
        self.frame_table.grid(row=2, column=0, padx=1, pady=1, sticky= "nsew")
        self.frame_table.grid_columnconfigure(0, weight=1)
        self.frame_table.grid_rowconfigure(1, weight=1)

        text_table1 = Label(self.frame_table, text='Number 1', bg='white', borderwidth=0)
        text_table1.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)
        text_table2 = Label(self.frame_table, text='Number 2', bg='white', borderwidth=0, width=12)
        text_table2.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)
        text_table3 = Label(self.frame_table, text='Points', bg='white', borderwidth=0, width=10)
        text_table3.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)
        text_table4 = Label(self.frame_table, text='Type', bg='white', borderwidth=0, width=15)
        text_table4.grid(row=1, column=3, sticky="nsew", padx=1, pady=1)
        text_table5 = Label(self.frame_table, text='Value', bg='white', borderwidth=0, width=10)
        text_table5.grid(row=1, column=4, sticky="nsew", padx=1, pady=1)
        text_table6 = Label(self.frame_table, text='Unit', bg='white', borderwidth=0, width=10)
        text_table6.grid(row=1, column=5, sticky="nsew", padx=1, pady=1)

        # Empty boxes (1 row)
        self.empty1 = Entry(self.frame_table, bg='white', borderwidth=0, fg='grey', justify="center")

        self.empty1.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)
        self.empty2 = Entry(self.frame_table, bg='white', borderwidth=0)
        self.empty2.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
        self.empty3 = Entry(self.frame_table, bg='white', borderwidth=0)
        self.empty3.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
        self.empty5 = Entry(self.frame_table, bg='white', borderwidth=0)
        self.empty5.grid(row=2, column=4, sticky="nsew", padx=1, pady=1)

        # Dropdown menu preload type
        self.variable = StringVar(self.win1)
        self.variable.set("None")
        self.preload_type = OptionMenu(self.frame_table, self.variable, "None", "1", "2", "3", command=self.VarMenu)
        self.preload_type.grid(row=2, column=3, sticky="ew", padx=1, pady=1) # To fit what's above

        # Dropdown menu units
        self.variableunit = StringVar(self.frame_table)
        self.variableunit.set("mm")
        self.unit = OptionMenu(self.frame_table, self.variableunit, "mm", "m", command=self.VarMenu)
        self.unit.grid(row=2, column=5, sticky="ew", padx=1, pady=1)

        # Set of drop down menus - Fixed, list, interval, optimisation

        text_table7 = Label(self.frame_table, text='Choice', bg='white', borderwidth=0, width=10)
        text_table7.grid(row=1, column=6, sticky="nsew", padx=1, pady=1)
        variablelist = StringVar(self.frame_table)
        variablelist.set('Fixed')
        self.list1 = OptionMenu(self.frame_table, variablelist, 'Fixed', 'List', 'Min', 'Max', command=self.ChoiceBox)
        self.list1.grid(row=2, column=6, sticky="ew", padx=1, pady=1)

        # Start button
        frame_but = ttk.Frame(self.win1)
        frame_but.grid(sticky=S, padx=1, pady=1)
        frame_but.grid_columnconfigure(0, weight=1)
        frame_but.grid_rowconfigure(1, weight=1)
        but1 = ttk.Button(frame_but, text='Start', command=None)#numberwritten)
        but1.grid(row=3, column=0, padx=2, pady=1, sticky="S")

        # Quit button
        but2 = ttk.Button(frame_but, text='Quit', command = self.root.destroy)
        but2.grid(row=3, column=1, padx=2, pady=1, sticky="S")

        #self.mycolour = '#%02x%02x%02x' % (224, 226, 235)
        self.clicked = []
        self.column = 7

    def VarMenu(self, selection):

        if selection == "3":
            self.variableunit.set("m")
            self.unit.config(state=DISABLED)
        else:
            self.variableunit.set("mm")
            self.unit.config(state=NORMAL)

    def ChoiceBox(self, choice):

        #print self.list1.grid_info()
        co_ord = str(self.frame_table.grid_size())
        col, rows = map(float, co_ord.strip('()').split(','))
        rows = int(rows)
        griddy = str(self.list1.grid_info())
        self.row_list = int(griddy[-3])

        if choice == "Fixed":

            for i in xrange(self.number_boxes):

                self.box[i].grid_remove()
                self.choice_title.grid_remove()
                self.frame_table.grid_columnconfigure(7, weight=0)
                # Search row number chosen (row_list)
                # Delete from column 7/8 onwards in that row
                #self.frame_table.grid_forget()
                tkMessageBox.showinfo("Message", "Value fixed.")
        elif choice == "List":
            self.win2 = tk.Toplevel(self.root)
            self.win2.title("List")
            self.list_text = Label(self.win2, text="Please enter number of values to be used:")
            self.list_text.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
            self.value = StringVar()
            self.list_values = Entry(self.win2, textvariable=self.value, justify="center")
            self.list_values.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)

            list_button = ttk.Button(self.win2, text="Enter", command=self.ValueBox)
            list_button.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
            self.win2.mainloop()

            column = 7
            self.number_boxes = int(self.number_boxes)
            self.numbers = [StringVar() for i in xrange(self.number_boxes) ]  
            self.box = []

            for i in xrange(self.number_boxes):
                self.clicked.append(False)
                self.choice_title = Label(self.frame_table, bg=self.mycolour, borderwidth=0, width=10) 
                self.choice_title.grid(row=1, column=self.column, columnspan=self.number_boxes, sticky="nsew", padx=1, pady=1) 
                self.box.append(Entry(self.frame_table,bg='white',borderwidth=0, width=10, justify="center", textvariable=self.numbers[i], fg='grey'))
                self.box[i].grid(row=self.row_list,column=self.column+i, sticky='nsew', padx=1, pady=1) 
                self.box[i].insert(0, "Value %g" % float(i+1))
                self.box[i].bind("<Button-1>", lambda event, index=i : self.callback(event, index))

                self.total_boxes = self.number_boxes * ( rows - 2 )
                self.boxes=[]
                self.boxes.append(self.box[i])

            tkMessageBox.showinfo("Message", "Please fill in list values.")

            for i in self.numbers: 
                i.trace('w',lambda index=i: self.numberwritten(index) ) 

        elif choice == "Min" or "Max":

            self.numbers = [StringVar() for i in xrange(2) ] #Name available in global scope. 
            self.number_boxes = 2
            self.box = []
            for i in xrange(2): 
                self.clicked.append(False)
                self.choice_title = Label(self.frame_table, bg=self.mycolour, borderwidth=0)
                self.choice_title.grid(row=1, column=self.column, columnspan=2, sticky="nsew", padx=1, pady=1)
                self.box.append(Entry(self.frame_table,bg='white',borderwidth=0,textvariable=self.numbers[i], justify='center', fg='grey'))
                self.box[i].grid(row=self.row_list, column=self.column+i, sticky='nsew', padx=1, pady=1) 
                if i == 0:
                    self.box[0].insert(0, "Min value")
                elif i == 1:
                    self.box[1].insert(0, "Max value")
                self.box[i].bind("<Button-1>", lambda event, index=i : self.callback(event, index))
                self.boxes=[]
                self.boxes.append(self.box[i])

            tkMessageBox.showinfo("Message", "Enter Min/Max values.")

            for i in self.numbers: 
                i.trace('w',lambda a,b,n=i: self.numberwritten(n) ) 

    def ValueBox(self):

        self.number_boxes = self.list_values.get()
        self.win2.quit()
        return self.number_boxes

    def numberwritten(self, index):
        """Example of how to get info in Entry fields"""
        if (choice is not None):
            for k, v in choice.boxes.items():
                print ("boxnum (%d) : value (%s)" % (k,v.get()))
        self.after(1000, lambda : print_boxes(self))

    def callback(self, event, index):

        if (self.clicked[index] == False):
            self.box[index].delete(0, END)
            self.box[index].config(fg='black')
            self.clicked[index] = True

    #for i,j in enumerate(self.box):
        #print ("%ith element: %s" % (i,j.get()))


    def import_file(self):
        print teste
    # Create blocks for each starting with *
    def parse_file(ff): 
        out={} 
        block=None 
        for i,line in enumerate(ff):  
            line=line.strip() 
            if(line.startswith('*')): 
                block=out[line.strip()[1:]]=[] 
            elif (block is not None) and line: 
                try: 
                    block.append((line.split()))
                except Exception: 
                    # If problem in a block
                    sys.stderr.write("Parsing datafile choked on line %d '%s'n"%(i+1,line.rstrip())) 
                    raise 
        return out 

    # Import file window
    with askopenfile(filetypes=[(".txt files","*.txt")], title='Import', mode='r') as f: 
        data_dict=parse_file(f) 

    # Get information from '*apload' block: 
    info=data_dict['three'] 
    i = 2
    for row in info:
        # Create row in 'table' for each output
        no_1, code, value = row             # Obtain results
        def three( code ):
            c = { "1" : "1",
                  "2" : "2",
                  "3" : "3" }
            try:
                return c[code]
            except KeyError:
                return "None"

        if code == "1" or "2":
            value = int(value) * (1E-03)     # Change units     

        self.empty1 = Label(self.frame_table, text=no_1, bg='white', borderwidth=0, width=20)    # Bearing no.
        self.empty1.grid(row=i, column=0, sticky="nsew", padx=1, pady=1)
        self.empty5 = Label(self.frame_table, text=value, bg='white', borderwidth=0, width=10) # Preload value
        self.empty5.grid(row=i, column=4, sticky="nsew", padx=1, pady=1)

        # Preload type drop down menu
        self.variable = StringVar(self.frame_table)                                # Preload code --> Type
        self.variable.set(three(code))
        self.type = OptionMenu(self.frame_table, self.variable, "None", "1", "2", "3", command=self.VarMenu)
        self.type.grid(row=i, column=3, sticky="nsew", padx=1, pady=1)

        # Unit drop down menu
        self.unit = OptionMenu(self.frame_table, self.variableunit, "mm", "m")
        self.unit.grid(row=i, column=5, sticky="nsew", padx=1, pady=1)

        # Choice drop down menu
        variablelist = StringVar(self.frame_table)
        variablelist.set("Fixed")
        self.list1 = OptionMenu(self.frame_table, variablelist, "Fixed", "List", "Min", "Max", command=self.ChoiceBox)
        self.list1.grid(row=i, column=6, sticky="nsew", padx=1, pady=1)
        i = i + 1

    info=data_dict['geo'] 
    j = 2
    for row in info:
        if no_1 in row:
            number1 = row[3]                  # Only the 4th number in each row
            number2 = row[4]               # 5th no.
            text_table2 = Label(self.frame_table, text=number1, bg='white', borderwidth=0, width=12)
            text_table2.grid(row=j, column=1, sticky="nsew", padx=1, pady=1)
            text_table3 = Label(self.frame_table, text=number2, bg='white', borderwidth=0, width=10)
            text_table3.grid(row=j, column=2, sticky="nsew", padx=1, pady=1)
            j = j + 1


    def save_file(self):

        savedfile = asksaveasfile(filetypes=[(".sho files","*.sho")], initialfile="test.sho", mode='w')
        savedfile.write("h") # Change once got correct outputs etc.
        savedfile.close()

    #if savedfile == True:
        tkMessageBox.showinfo("Save message", "Save successful")

main_window = Window()
main_window.root.wm_geometry("")
mainloop()
