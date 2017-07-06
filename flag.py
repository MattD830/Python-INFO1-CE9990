'''
With apologies to Slovakia
'''

import sys
import tkinter as tk

def dp(x,y,w,color):
	"""
	Color the pixel at coordinates (x, y).
	"""
	assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
	c.create_rectangle(x, y, w, y + 1, width = 0, fill = color)
	
r = tk.Tk()
r.title("The Flag of Slovakia")
c = tk.Canvas(r,highlightthickness=0)

s = 175;h = 3 * s;w = int(h*3/2)
clr = {
	'white':'#FFF','blue':'#0b4ea2','red':'#ee1c25'
	}
	
k = 0;
for cr in clr:
	for i in range(s):
		dp(0,k,w,clr[cr])
		k += 1
		
aa = s*.75;bb=-(s*.7);cc=s*2;dd=s*2.15
c.create_arc(aa,bb,cc,dd,start=0,extent=-180,outline=clr['white'],fill=clr['red'],width=3)
a1 = s*1.35;b1=s*.88;c1=s*1.43;d1=s*1.75
c.create_rectangle(a1,b1,c1,d1,width=0,fill=clr['white'])
a2=s*1.14;b2=s*1.04;c2=s*1.62;d2=s*1.12
c.create_rectangle(a2,b2,c2,d2,width=0,fill=clr['white'])
a3=s*1.05;b3=s*1.26;c3=s*1.71;d3=s*1.34
c.create_rectangle(a3,b3,c3,d3,width=0,fill=clr['white'])
	
c.pack(expand = tk.YES,fill="both")
r.mainloop()
