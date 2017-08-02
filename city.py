"""
This program tells you which cities are in demand and which are not.

You can uncomment the rest list "City" to view all the cities, but it takes way too long to load.
"""


import sys
import urllib.request as ur
import json
import tkinter as tk
from tkinter import messagebox

url = 'https://www.quandl.com/api/v3/datasets/ZILLOW/C4{}_ZHVITT.json?api_key={}'
api_key = 'wborJm5zx5u4r8PS9JLy'
City = [100,102,103,105,106,107,109,110]#,111,113,114,115,116,117,118,120,121,122,123,125,126,127,128,131,132,133,134,135,137,138,140,141,143,144,145,146,147,148,149,150,151,152,153,154,156,157,158,159,160,161,162,163,164,165,166,168,169,170,171,172,175,176,177,178,179,180,181,183,184,185,186,187,190,191,192,193,194,195,198,199,200,201,202,203,204,205,206,209,210,212,213,214,215,216,217,219,220,222,223,224,225,226,227,228,229,230,231,233,234,235,236,237,238,241,242,243,244,247,248,249,250,254,255,257,258,259,260,261,262,263,264,265,266,267,268,270,271,272,273,274,275,276,277,279,282,283,284,285,286,287,288,289,290,292,293,294,295,296,297,298,299,300,301,302,303,304,305,307,308,310,311,313,315,316,317,318,319,320,321,322,323,324,325,328,329,330,331,332,333,334,335,338,339,340,341,342,344,345,346,348,349,352,353,355,358,359,360,361,362,363,364,365,366,368,369,371,372,374,375,376,377,378,379,380,381,382,383,384,385,386,387,390,391,392,393,394,395,396,397,399,400,401,402,403,404,405,406,407,408,409,410,412,413,414,415,416,417,418,419,421,422,423,425,426,427,428,429,430,431,433,434,435,436,437,438,439,440,441,442,443,445,446,447,448,449,450,451,452,454,456,457,458,460,461,463,465,466,467,468,469,470,472,473,476,477,478,479,480,481,482,483,485,487,488,489,490,491,492,494,495,496,498,499,500,501,502,503,504,505,506,507,508,509,511,512,513,514,515,517,518,519,520,521,523,524,525,526,528,530,532,533,535,536,537,538,540,541,542,544,545,546,547,548,549,551,553,554,558,559,560,561,562,564,567,568,569,570,571,572,574,575,576,577,580,581,582,584,586,587,589,590,591,592,594,595,596,598,599,600,601,602,603,604,605,606,610,611,612,613,616,618,619,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,642,643,647,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,665,666,667,669,670,672,673,674,675,676,678,681,682,683,686,687,688,689,691,692,693,695,696,698,699,700,704,705,706,707,708,711,712,713,714,715,716,717,718,719,720,721,722,725,726,729,731,733,734,737,738,739,740,741,743,745,747,748,749,750,751,753,754,755,756,757,758,759,760,761,762,763,764,766,767,771,772,773,774,775,776,779,780,781,783,784,785,788,790,792,793,794,795,796,798,800,801,802,804,805,806,808,809,810,811,813,814,815,817,819,821,822,823,824,825,826,827,828,829,831,832,833,834,835,837,840,843,844,845,846,848,849,850,852,853,855,856,857,858,861,862,864,865,866,867,868,870,871,872,873,874,875,876,879,883,884,886,887,888,889,890,891,892,893,894,895,896,898,899,900,901,903,904,905,907,908,909,910,911,912,913,914,915,916,917,918,920,921,922,923,924,926,928,929,930,931,932,933,936,937,938,939,940,941,942,944,945,946,947,948,949,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,969,971,972,973,974,975,977,978,979,980,982,983,984,986,987,988,990,991,992,993,995,996,997,999]
Data = []
City_Name = []
n=[]
cityavgs = {}

for c in City:
	u = ur.urlopen(url.format(c, api_key))
	f = u.read().decode('utf-8')
	u.close()
	f = json.loads(f)
	Data.append(f)
	
num = len(City)

for i in range(num):
	a = 0
	Housing_Price_Data = Data[i]['dataset']['data']
	for d,p in Housing_Price_Data:
		n.append(p)
		a += p
	avg = int(a / len(Housing_Price_Data))
	city_name = Data[i]['dataset']['name'].split('- Top Tier - ')[1]
	if avg >= n[0]:
		cityavgs[city_name] = "Everyone seems to want to live in "+city_name+" as prices are on the rise"
	elif avg < n[0]:
		cityavgs[city_name] = "Prices are low in "+city_name+" Is it a good deal? Or will it be the next Detroit?"
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
