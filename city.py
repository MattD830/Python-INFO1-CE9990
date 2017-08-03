"""
This program tells you which cities are in demand and which are not.


"""


import sys
import urllib.request as ur
import json
import tkinter as tk
from tkinter import messagebox

url = 'https://www.quandl.com/api/v3/datasets/ZILLOW/C4{}_ZHVITT.json?api_key={}'
api_key = 'wborJm5zx5u4r8PS9JLy'
City = [100,102,103,105,106,107,109,110,111,113,114,115,116,117,118,120]
Data = []
cityavgs = {}

for c in City:
	try:
		u = ur.urlopen(url.format(c, api_key))
		f = u.read().decode('utf-8')
	except:
		print("Something went wrong.")
		sys.exit(1)
	u.close()
	try:
		f = json.loads(f)
	except:
		print("Something went wrong.")
		sys.exit(1)
	Data.append(f)
	
num = len(City)

for i in range(num):
	a = 0;n = []
	Housing_Price_Data = Data[i]['dataset']['data']
	for d,p in Housing_Price_Data:
		n.append(p)
		a += p
	avg = int(a / len(Housing_Price_Data))
	city_name = Data[i]['dataset']['name'].split('- Top Tier - ')[1]
	if avg >= n[0]:
		cityavgs[city_name] = "Everyone seems to want to live in "+city_name+" as prices are on the rise."
	elif avg < n[0]:
		cityavgs[city_name] = "Prices are low in "+city_name+". Is it a good deal? Or will it be the next Detroit?"
	else:
		cityavgs[city_name] = None

r=tk.Tk()
r.title("Select city")
l = tk.Frame(r)

lb = tk.Listbox(l, relief='groove')

for c, key in enumerate(cityavgs.keys()):
	lb.insert(c, key)

def dia():
	messagebox.showinfo("City desirability", cityavgs[lb.get(lb.curselection())])

b = tk.Button(l, text="Press me", command=dia)

b.pack(padx=10, side=tk.RIGHT)
lb.pack()
l.pack(pady=5, padx=5)
		
r.mainloop()
sys.exit(0)
