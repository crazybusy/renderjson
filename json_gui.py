from tkinter import *
from tkinter import filedialog
from json_cli import json_cli

class json_gui(json_cli):

    def __init__(self):
        self.main_window = Tk()

        self.row = 0

        self.filename = StringVar()
        self.main_frame= Frame(self.main_window)        
        Entry(self.main_frame, textvariable=self.filename).pack(side="left",fill="x")
        Button(self.main_frame,text = "Browse", command = self.browse_file).pack(side="left")
        Button(self.main_frame,text = "Show", command = self.show_file).pack(side="left")
        Button(self.main_frame,text = "Input", command = self.input_file).pack(side="left")
        Button(self.main_frame,text = "Dump", command = self.dump).pack(side="left")
        self.main_frame.pack(side="top", fill="x")
        return
    
    def browse_file(self):
        filename = filedialog.askopenfilename(title = "Select file",
            filetypes = (("json", "*.json"),("All files", "*.*")))
        
        self.filename.set(filename)
        self.main_frame.pack(side="top", fill="x")

        return

    def get_field(self, field):
        Label(self.data_frame,text=field['name']).grid(0,0)
        Entry(self.main_window).grid(0,1)
        self.data_frame.pack(fill="x")
              
    def render(self, level, type, key, value, path):
        label_name = "{}: {}({}): {}".format(level, path, type,  value)
        Label(self.data_frame,text=label_name).pack()
        self.data_frame.pack(fill="x")
        return

    def dump(self):
        #TODO Get the values from the child entry fields of the dataframe
        self.dump_file(str(self.filename))
    
    
    def show_file(self):
        self.setmode("SHOW")
        
        if hasattr(self, 'data_frame'):
            self.data_frame.destroy()
        self.data_frame = Frame(self.main_window)
        
        self.load_file(self.filename.get())
        return
    def input_file(self):
        self.setmode("READ")
        
        if hasattr(self, 'data_frame'):
            self.data_frame.destroy()
        self.data_frame =Frame(self.main_window) 
        
        self.load_file(self.filename.get())
        return
if __name__ == '__main__':
    clas = json_gui()
    clas.main_window.mainloop()
