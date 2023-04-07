import datasource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = ttk.LabelFrame(self,text="台北市行政區")
        # print(datasource.sarea_list)
        length = len(datasource.sarea_list)
        self.radioStringVar = tk.StringVar()
        for i in range(length):
            cols = i %3
            rows = i //3
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.radioStringVar,command=self.radio_Event).grid(column=cols,row=rows,sticky=tk.W,padx=10,pady=10)

        topFrame.pack()
        self.radioStringVar.set('信義區')

    def radio_Event(self):
        print(self.radioStringVar.get())
        area_name = self.radioStringVar.get()
        area_data = datasource.getInfoFromArea(area_name)
        for item in area_data:
            print(item)

def main():
    window = Window()
    window.title("台北市youbike2.0資訊")
    window.mainloop()

if __name__ == "__main__":
    main()