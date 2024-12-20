import tkinter
import sys

#TODO
"""
Widget layout can be a lot cleaner than the adhoc!
More error catching
File ops can use a file selection dialog

"""

fmver="0.21"

resd={} #[1001,1010]... int represntation of the character as a dict
resds={} # ['100...','1001..' ...], COLS wide string representation of 1's and 0s for reloading the check boxes
cbtns={} # buttons that go in the current char set frame at the bottom, allows to load/delete/reload the check boxes
fmxr=0
fmxc=0


if len(sys.argv)<4:
	print("fontmake.py ROWS COLS RESOLUTION")
	raise SystemExit

def addchar():
	global resd,resds,lbxmsg,fmx
	outd={}
	tmpd=[]
	tmpds=[]
	chx=entval.get()
	if not len(chx):
		lbxmsg.set("No char!")
		return
		
	for n in btnsv:
		s=""
		for m in n:
			s+=str(m.get())
		tmpd.append(int(s[::-1],2))
		tmpds.append(s)
	resd[entval.get()]=tmpd
	resds[entval.get()]=tmpds
	lbstr=entval.get()
	tmpbtn=tkinter.Button(fmx,text=entval.get())
	tmpbtn.bind("<Button-1>",loadbtn)
	if not lbstr in cbtns:
		puttoframe(tmpbtn)
		cbtns[lbstr]=tmpbtn


def loadfile():
	global resd,resds,cbtns
	resd={}
	resds={}
	cbtns={}
	fname=saventval.get().strip()
	if not len(fname):
		lbxmsg.set("No file!")
		return
	fx=open(fname).read().strip()
	if not len(fx):
		lbxmsg.set("Empty file!")
		return
	dx=eval(fx)
	if not type(dx)==type({}):
		lbxmsg.set("Wrong filetype!")
		return
	for n in dx:
		lbstr=str(n)
		resd[n]=dx[n]
		tmps=[]
		for m in dx[n]:
			tmps.append(format(m,'0'+str(resx)+'b')[::-1])
		resds[n]=tmps
		tbtn=tkinter.Button(fmx,text=n)
		tbtn.bind("<Button-1>",loadbtn)
		puttoframe(tbtn)
		cbtns[n]=tbtn




def puttoframe(widg):
	global frmx,fmxr,fmxc
	widg.grid(row=fmxr,column=fmxc)
	fmxc+=1
	if fmxc>4:
		fmxr+=1
		fmxc=0
		
	
def loadbtn(e):
	global resds,btnsv
	param=e.widget.cget("text")
	clrscr()
	entval.set(param)
	if param in resds:
		for n in range(len(resds[param])):
			for m in range(len(resds[param][n])):
				btnsv[n][m].set(int(resds[param][n][m]))
	
def savefile():
	global saventval,resd
	if not len(saventval.get().strip()):
		lbxmsg.set("No file!")
		return
	f=open(saventval.get(),'w')
	if f:
		f.write(str(resd))
		f.close()
	else:
		lbxmsg.set("Couln't open file")
		return
		
	

def prt():
	print(resd)

def clrch(param):
	global resd,cbtns,mx
	if param in resd:
		clrscr()
		resd.pop(param)
	if param in cbtns:
		cbtns[param].destroy()
	entval.set("")
	
def clrscr():
	global btnsv,lbxmsg
	for n in btnsv:
		for m in n:
			m.set(0)

def clrall():
	global resd,resds,cbtns
	clrscr()
	resd={}
	resds={}
	cbtns={}
	entval.set("")
	saventval.set("")
	for n in fmx.winfo_children():
		n.destroy()

def set_col(param):
	for n in btnsv[int(param.widget.cget("text"))]:
		n.set(1)
	
def unset_col(param):
	for n in btnsv[int(param.widget.cget("text"))]:
		n.set(0)
		
def set_row(param):
	for n in btnsv:
		n[int(param.widget.cget("text"))].set(1)
	
def unset_row(param):
	for n in btnsv:
		n[int(param.widget.cget("text"))].set(0)

def set_grid(x):
	for n in btnsv:
		for m in n:
			m.set(1)
	
def unset_grid(x):
	for n in btnsv:
		for m in n:
			m.set(0)


rows=int(sys.argv[1])
cols=int(sys.argv[2])
resx=sys.argv[3]


mw=tkinter.Tk()
mw.title("Font Maker "+fmver)
entval=tkinter.StringVar()
lbxmsg=tkinter.StringVar()
saventval=tkinter.StringVar()
lbx=tkinter.Label(mw,textvariable=lbxmsg)
fmx=tkinter.Frame(mw)
ftx=tkinter.Frame(mw)
ftx.grid(row=0,columnspan=cols+1)
btnsv=[]
r=0

cornerbtn=tkinter.Button(ftx,text="..")
cornerbtn.pack(side="left")
cornerbtn.bind("<Button-1>",set_grid)
cornerbtn.bind("<Button-3>",unset_grid)

for n in range(rows):
	bvrow=[]
	
	head=tkinter.Button(ftx,text=str(n))
	head.bind("<Button-1>",set_col)
	head.bind("<Button-3>",unset_col)
	head.pack(side="left")#(row=0,column=n+1)
	
	pad=tkinter.Button(mw,text=str(n))
	pad.bind("<Button-1>",set_row)
	pad.bind("<Button-3>",unset_row)
	pad.grid(row=n+1,column=0)
	
	
	for m in range(cols):
		tvar=tkinter.IntVar()
		tmp=tkinter.Checkbutton(mw,variable=tvar)
		#tmp.grid(row=m,column=n+1)
		tmp.grid(row=m+1,column=n+1)
		bvrow.append(tvar)
	btnsv.append(bvrow)
	
	r+=1

bfrm=tkinter.Frame(mw)
bfrm.grid(row=0,rowspan=rows+4,column=cols+1)

elbl=tkinter.Label(bfrm,text="Char:")
ent=tkinter.Entry(bfrm,textvariable=entval,width=10)
elbl.grid(row=0,column=cols+1)
ent.grid(row=1,column=cols+1)

acbtn=tkinter.Button(bfrm,text="Add Char",command=addchar)
acbtn.grid(row=2,column=cols+1)

dcbtn=tkinter.Button(bfrm,text="Del Char",command=lambda:clrch(entval.get()))
dcbtn.grid(row=3,column=cols+1)

clbtn=tkinter.Button(bfrm,text="Clear Btn",command=clrscr)
clbtn.grid(row=4,column=cols+1)

cabtn=tkinter.Button(bfrm,text="Clear All",command=clrall)
cabtn.grid(row=5,column=cols+1)

prnbtn=tkinter.Button(bfrm,text="Print All",command=prt)
prnbtn.grid(row=6,column=cols+1)

flbl=tkinter.Label(bfrm,text="File:")
savent=tkinter.Entry(bfrm,textvariable=saventval,width=10)
flbl.grid(row=7,column=cols+1)
savent.grid(row=8,column=cols+1)

savbtn=tkinter.Button(bfrm,text="Save File",command=savefile)
savbtn.grid(row=9,column=cols+1)

lodbtn=tkinter.Button(bfrm,text="Load File",command=loadfile)
lodbtn.grid(row=10,column=cols+1)

qtbtn=tkinter.Button(bfrm,text="Exit App",command=mw.destroy)
qtbtn.grid(row=11,column=cols+1)

lbx.grid(row=rows+4,columnspan=cols+1)
fmx.grid(row=rows+5,columnspan=cols+1)
mw.mainloop()
