"""
This program tells you the probability of bankruptcy of at risk states.

cpd = cumulative probability of default, s = state, l = label, r = root, m = menu, n = name, b = button, t = text
"""

import sys
import tkinter as tk

cpd = {
	"PA" : 10.7,
	"FL" : 10.8,
	"OH" : 11.2,
	"MA" : 11.2,
	"RI" : 12.4,
	"NY" : 15.9,
	"NV" : 16.7,
	"NJ" : 17.1,
	"MI" : 18.8,
	"CA" : 20.9,
	"IL" : 21.0
	}
  
def button():
	cpdt.delete("1.0",tk.END)
	cpdt.insert("1.0",str(cpd[sn.get()])+'%')

r = tk.Tk()
r.title("Cumulative Probability of Default by State")
r.geometry("350x80")

sml =tk.Label(r,text='Select a State:')
sml.grid(row=0,column=0)
cpdl = tk.Label(r,text='Cumulative Probability of Default for the selected state is:')
cpdl.grid(row=2,column=0,columnspan=2)

cpdm = []

for s in cpd:
	cpdm.append(s)

sn = tk.StringVar(r)
sn.set('NY')
sm = tk.OptionMenu(r,sn,*cpdm)
sm.grid(row=0,column=1)

cpdt = tk.Text(r,width=10,height=1,borderwidth=2,relief='groove')
cpdt.grid(row=3,column=0)

b = tk.Button(r,text="Calc",command = button)
b.grid(row=0,column=2)

r.mainloop()
sys.exit(0)
