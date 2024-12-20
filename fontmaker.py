import tkinter
import sys

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
	print(resds)

def loadfile():
	global resd,resds,cbtns
	resd={}
	resds={}
	cbtns={}
	fname=saventval.get().strip()
	if not len(fname):return
	fx=open(fname).read().strip()
	if not len(fx):return
	dx=eval(fx)
	if not type(dx)==type({}):return
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
	f=open(saventval.get(),'w')
	if f:
		f.write(str(resd))
		f.close()
		
	

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
		
rows=int(sys.argv[1])
cols=int(sys.argv[2])
resx=sys.argv[3]


mw=tkinter.Tk()
entval=tkinter.StringVar()
lbxmsg=tkinter.StringVar()
saventval=tkinter.StringVar()
lbx=tkinter.Label(mw,textvariable=lbxmsg)
fmx=tkinter.Frame(mw)
btnsv=[]
r=0
for n in range(rows):
	bvrow=[]
	for m in range(cols):
		tvar=tkinter.IntVar()
		tmp=tkinter.Checkbutton(mw,variable=tvar)
		tmp.grid(row=m,column=n)
		bvrow.append(tvar)
	btnsv.append(bvrow)
	
	r+=1

ent=tkinter.Entry(mw,textvariable=entval,width=10)
ent.grid(row=0,column=cols+1)
dobtn=tkinter.Button(mw,text="Add Char",command=addchar)
dobtn.grid(row=1,column=cols+1)
dcbtn=tkinter.Button(mw,text="Del Char",command=lambda:clrch(entval.get()))
dcbtn.grid(row=2,column=cols+1)

clbtn=tkinter.Button(mw,text="Clear Btn",command=clrscr)
clbtn.grid(row=3,column=cols+1)
cabtn=tkinter.Button(mw,text="Clear All",command=clrall)
cabtn.grid(row=4,column=cols+1)
prnbtn=tkinter.Button(mw,text="Print All",command=prt)
prnbtn.grid(row=5,column=cols+1)
savent=tkinter.Entry(mw,textvariable=saventval,width=10)
savent.grid(row=6,column=cols+1)
savbtn=tkinter.Button(mw,text="Save File",command=savefile)
savbtn.grid(row=7,column=cols+1)
lodbtn=tkinter.Button(mw,text="Load File",command=loadfile)
lodbtn.grid(row=8,column=cols+1)
qtbtn=tkinter.Button(mw,text="Exit App",command=mw.destroy)
qtbtn.grid(row=9,column=cols+1)
lbx.grid(row=rows+1,columnspan=cols+1)
fmx.grid(row=rows+5,columnspan=cols+1)
mw.mainloop()
