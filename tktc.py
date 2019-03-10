from tkinter import *
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText

sites = [
    "yandex.ru",
    "google.com"
]

class tktc():
	def __init__(self):
		self.root = Tk()
		self.root.title("Yet Anther Tag Counter")
		self.load_btn  = Button(self.root, text = 'Load from URL', width = 15 )
		self.view_btn  = Button(self.root, text = 'View from DB' , width = 15 )
		self.sites_cmb = ttk.Combobox(self.root, values=sites, height=3 )
		self.select_btn = Button(self.root, text='Select URL', width=11)
		self.entry_url = Entry(self.root, width=23)
		self.out_tags_field = ScrolledText(self.root, height=10, width=13, font='Arial 14', wrap=WORD)
		self.status_bar = Label(self.root, text="ready...", bd=1, relief=SUNKEN, anchor=W)			
		
		self.sites_cmb.pack()
		self.select_btn.pack()
		self.entry_url.pack()
		self.load_btn.pack()
		self.view_btn.pack()
		self.out_tags_field.pack()
		self.status_bar.pack(side = BOTTOM, fill = X)

	def run(self):
		self.root.mainloop()


