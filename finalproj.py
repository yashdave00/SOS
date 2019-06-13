

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:45:49 2019

@author: vidisha
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:37:06 2019

@author: vidisha
"""

import tkinter as tk



global count
global ccount
global userlist
userlist=[]
global sublist
sublist=[]
global chaplist
chaplist=[]
global vlist
vlist=[]
global results
results=" "
global tcount
tcount=0
global tsname
tsname=None
global tchap
tchap=0
global tlist
global v
v=0
global gcount
gcount=0
class User:

    def __init__(self):
        self.tgpa=0.0
        self.nsub=0
        self.name=""
        self.subs=[]
    

    def makeknap(self):
        for i in range(0,self.nsub):
            self.subs[i].knapsub()
    
    def putdatainfile():
        f = open("UserData.txt","w+")
        f.write("Name of Student:  "+name+"\n")
        f.write("Target GPA : "+tgpa+"\n")
        f.write("Number of Subjects: "+nsub+"\n")
        f.write("***************************************************************************************")
        f.close()

    def inputus(self):
        global userlist
        '''print("Are you a Student or a Teacher?")
        st=input()
        if st=='s' or st=='S':'''
        #print("Enter Name of user:")
        self.name=userlist[0]
        #print("Enter Number of Subjects:")
        #nsubs=int(input())
        self.nsub=userlist[2]
        #print("Enter Target GPA:")
        self.tgpa=float(userlist[1])
        
    def inputut(self):
        global tsname
        for i in range(0,self.nsub):

            if(tsname==self.subs[i].name):
                break
            self.subs[i].getintmarks()
            
            
        '''
        self.nchap=tlist[0]
        for i in range(0,self.nchap):
            self.subs[i].getintmarks()
        '''
    
    def insub(self,s):
        self.subs.append(s)
        
        #for i in range(self.nsub):
           # S=Subject()
           # S=S.inputs()


global U
U= User()







mainwindow = tk.Tk()
mainwindow.title("Main Page")
mainwindow.configure(background='#fefdca')
mainwindow.geometry("1200x600+100+100")






    
        


def openteacher():
    teacherwindow = tk.Toplevel()
    teacherwindow.title("Teacher Page")
    teacherwindow.configure(background='#fefdca')
    teacherwindow.geometry("1200x600+100+100")
     
    six=tk.Canvas(teacherwindow,background="#fefdca")
    six.pack(expand=True,side='top',fill='both')
    global tcount
    global tsname
    global tchap
    global gcount
    sname=tk.StringVar(value=tsname)
    nchapt=tk.IntVar(value=tchap)
    cname=tk.StringVar(value=None)
    prevwt=tk.IntVar(value=None)
    l10=tk.Label (six,text="Enter Subject Name: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=50,y=50)
    e10=tk.Entry(six,relief='ridge',font='Consolas 16 italic',textvariable=sname).place(x=300,y=55)

    l11=tk.Label(six,text="Enter Number of Chapters: ",font='Consolas 14 italic ',padx=4,pady=4,background='#ffde7d').place(x=650,y=50)
    e11=tk.Entry(six,relief='ridge',font='Consolas 16 italic',textvariable=nchapt).place(x=940,y=55)

    

    def submit1():
        global tlist
        global U
        tlist=[cname.get(),prevwt.get()]
        U.inputut()

    def submit():
        global tcount
        global tchap
        global tsname
        global U
        

        tsname=sname.get()
        tcount=nchapt.get()
        tchap=tcount
        #tcount-=1
        #tlist=[cname.get(),prevwt.get()]
        #U.inputut()

    if gcount==0:
        gcount+=1
        bsubmit= tk.Button(six,text="Submit",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda :submit())
        bsubmit.place(x=250,y=500)
    elif gcount!=0:
        gcount+=1
        
        l13=tk.Label (six,text="Chapter Name ",font='Consolas 14 italic bold',padx=4,pady=4,background='#fefdca').place(x=550,y=250)
        e13=tk.Entry(six,relief='ridge',font='Consolas 16 italic',textvariable=cname).place(x=500,y=290)

        l14=tk.Label(six,text="Previous weightage ",font='Consolas 14 italic bold',padx=4,pady=4,background='#fefdca').place(x=530,y=380)
        e14=tk.Entry(six,relief='ridge',font='Consolas 16 italic',textvariable=prevwt).place(x=500,y=420)
        
        bsubmit= tk.Button(six,text="Submit",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda :submit1())
        bsubmit.place(x=250,y=500)
        
        
    
    global U
    
    def makeknapandres():
        global U
        U.makeknap()
        openresult()


    

    if tcount==1 :
        bnext =tk.Button(six,text="End",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=makeknapandres)
        bnext.place(x=750,y=500)
    elif tcount!=1:
        tcount-=1
        bnext= tk.Button(six,text="Next",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=openteacher)
        bnext.place(x=750,y=500)

    

    
        

    
    
def openresult():
    reswindow = tk.Toplevel()
    reswindow.title("Result Page")
    reswindow.configure(background='#fefdca')
    reswindow.geometry("1200x600+100+100")

    five=tk.Canvas(reswindow,background='#fefdca')
    five.pack(expand=True,side='top',fill='both')
    global results
    l = tk.Label (five,text="Follow this and you're all set!! ",font="Consolas 18 bold", background='#fefdca',foreground='#3c415e',padx=4,pady=4)
    l.place(x=600,y=100,anchor='center')
    
    lres = tk.Label (five,text=results,font="Consolas 18 bold", background='#ffde7d',foreground='#3c415e',padx=4,pady=4,relief='ridge',bd=5,width=40,height=10,justify=tk.LEFT)
    lres.place(x=600,y=300,anchor='center')
    
    bend= tk.Button(five,text="End",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda : clearresults())
    bend.place(x=800,y=550)


    def clearresults():
        global results
        results=""
        mainwindow.destroy()
    
        
        

    
        
              


'''
'''
###########################################################################################################################################################################
def openmain():

    one=tk.Canvas(mainwindow,background='#fefdca')
    one.pack(expand=True,side='top',fill='both')

    l = tk.Label (one,text="Enter as a Student or a Teacher? ",font="Consolas 18 bold", background='#fefdca',foreground='#3c415e',padx=4,pady=4)




    l.place(x=600,y=300,anchor='center')
    '''
    '''

    b1= tk.Button(one,text="Student",background='#ffde7d',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=openstu)
    b1.place(x=350,y=400)
    b2 = tk.Button(one,text="Teacher",background='#ffde7d',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=openteacher)
    b2.place(x=650,y=400)
    mainwindow.mainloop()
#############################################################################################################################################    
    

def openchap(s):
    chapwindow= tk.Toplevel()
    chapwindow.title("Chapter Page")
    chapwindow.geometry("1200x600+100+100")
    cname=tk.StringVar()
    wname=tk.DoubleVar()
    kb=tk.IntVar()
    tb=tk.IntVar()
    ib=tk.IntVar()
    db=tk.IntVar()

    four=tk.Canvas(chapwindow,background="#fefdca")
    four.pack(expand=True,side='top',fill='both')

    l8=tk.Label (four,text="Enter Chapter Name: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=50,y=50)
    e7=tk.Entry(four,relief='ridge',font='Consolas 16 italic',textvariable=cname).place(x=300,y=55)

    l9=tk.Label(four,text="Enter Weightage: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=650,y=50)
    e8=tk.Entry(four,relief='ridge',font='Consolas 16 italic',textvariable=wname).place(x=850,y=55)

    l10=tk.Label (four,text="How much do you know?: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=160)
    w10=tk.Scale(four,orient='horizontal',resolution=1.0,from_=1,to=10,length=200).place(x=500,y=160)

    l11=tk.Label (four,text="How difficult do you find this?: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=160,y=260)
    w11=tk.Scale(four,orient='horizontal',resolution=1.0,from_=1,to=10,length=200).place(x=510,y=260)

    l12=tk.Label (four,text="How time consuming is this chapter?: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=150,y=360)
    w12=tk.Scale(four,orient='horizontal',resolution=1.0,from_=1,to=10,length=200).place(x=535,y=360)

    l13=tk.Label (four,text="How interested are you? : ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=460)
    w13=tk.Scale(four,orient='horizontal',resolution=1.0,from_=1,to=10,length=200).place(x=530,y=460)

    bsubmit= tk.Button(four,text="Submit",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda :submit())
    bsubmit.place(x=250,y=550)

    def submit():
        global chaplist
        global vlist
        chaplist=[cname.get(),wname.get()]
        vlist=[kb.get(),tb.get(),ib.get(),db.get()]
        c=Chapters()
        c.getinput()
        s.inchap(c)
    
        
    
    global ccount
    global count
    '''
    if(ccount==0) and count>0:
        
        
        
        bnext= tk.Button(four,text="Next",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda : opensub())
        
        print("subject")
        
        print(count)
        count-=1
        bnext.place(x=800,y=550)
        
    elif ccount>0 and count>0:
        ccount-=1 
        bnext= tk.Button(four,text="Next",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda : openchap())
       
        print("chapter")
        print(ccount)
        bnext.place(x=800,y=550)
        
    elif ccount>0 and count==0:
        bnext= tk.Button(four,text="End",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda : openresult())
        bnext.place(x=800,y=550)'''
    
        
    if count==1 and ccount==1:
        bnext= tk.Button(four,text="End",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=openteacher)
        bnext.place(x=800,y=550)
    elif ccount==1 and count!=1:
        count-=1
        bnext= tk.Button(four,text="Next Subject",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda : opensub())
        bnext.place(x=800,y=550)
    elif ccount!=1 and count!=1:
        ccount-=1
        bnext= tk.Button(four,text="Next Chapter",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda : openchap(s))
        bnext.place(x=800,y=550)
    
    elif count==1 and ccount!=1:
        ccount-=1
        bnext= tk.Button(four,text="Next Chapter",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda : openchap(s))
        bnext.place(x=800,y=550)
    
        
        
    
'''    
def coordinate():
    global count
    global ccount
    for i in range(count,0,-1):
        for j in range(ccount,0,-1):
            return 'openchap()'
        if i==0:
            return 'openresult()'
        else:
            return 'opensub()'
    
   '''
def opensub():
    
    
    subwindow= tk.Toplevel()
    subwindow.title("Subject Page")
    subwindow.geometry("1200x600+100+100")
    global ccount
    global U
    global sublist
    three=tk.Canvas(subwindow,background="#fefdca")
    three.pack(expand=True,side='top',fill='both')

    sname=tk.StringVar(value=None)
    maxm=tk.IntVar(value=None)
    tscore=tk.IntVar(value=None)
    l4=tk.Label (three,text="Enter Subject Name: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=200)
    e4=tk.Entry(three,relief='ridge',font='Consolas 16 italic',textvariable=sname).place(x=475,y=205)
    l5=tk.Label(three,text="Enter Maximum Marks: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=250)
    e5=tk.Entry(three,relief='ridge',font='Consolas 16 italic',textvariable=maxm).place(x=480,y=255)
    nchap=tk.IntVar(value = None)
    l6=tk.Label(three,text="Enter Number of Chapters: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=300)
    e6=tk.Entry(three,relief='ridge',font='Consolas 16 italic',textvariable=nchap).place(x=530,y=305)
    l7=tk.Label(three,text="Target Score: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=350)
    e7=tk.Entry(three,relief='ridge',font='Consolas 16 italic',textvariable=tscore).place(x=410,y=355)

    s=Subject()

    

    def submit():
        global ccount
        global sublist
        global U
        ccount=int(nchap.get())
        sublist=[str(sname.get()),maxm.get(),nchap.get(),tscore.get()]
        
        
        
        print("chapter and subject")
        print(ccount)
        print(count)
        U.insub(s.inputs())

        
        
        
        
        
        #s.inputs()
    
    

    bsubmit= tk.Button(three,text="Submit",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda :submit())
    bsubmit.place(x=300,y=450) 


    

    bnext= tk.Button(three,text="Next",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda :openchap(s))
    bnext.place(x=800,y=450)

    
    
    
    
    
    
        
        
    
        
        
    
    


def openstu():
    
    userwindow= tk.Toplevel()
    userwindow.title("User Page")
    userwindow.geometry("1200x600+100+100")
    global count
    global U
    two=tk.Canvas(userwindow,background="#fefdca")
    two.pack(expand=True,side='top',fill='both')
    tgpa=tk.DoubleVar(value=None)
    nsub=tk.IntVar(value=None)
    sname=tk.StringVar(value=None)
    l1=tk.Label (two,text="Enter Name: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=200)
    e1=tk.Entry(two,relief='ridge',font='Consolas 16 italic',textvariable=sname).place(x=400,y=205)
    l2=tk.Label(two,text="Enter Target GPA: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=250)
    e2=tk.Entry(two,relief='ridge',font='Consolas 16 italic',textvariable=tgpa).place(x=450,y=255)
    l3=tk.Label(two,text="Enter Number of Subjects: ",font='Consolas 14 italic',padx=4,pady=4,background='#ffde7d').place(x=250,y=300)
    e3=tk.Entry(two,relief='ridge',font='Consolas 16 italic',textvariable=nsub).place(x=530,y=305)
    
    def submit():
        global count
        global userlist
        global U
        count = int(nsub.get())
        print("subject")
        print(count)
        userlist=[sname.get(),tgpa.get(),nsub.get()]
        U.inputus()
        
        #print(nsub.get())
    
    
    bsubmit= tk.Button(two,text="Submit",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda :submit())
    bsubmit.place(x=300,y=450)
    
    bnext= tk.Button(two,text="Next",background='#738598',font="Consolas 14 italic",width=15,relief='ridge',padx=4,pady=4,command=lambda :opensub())
    bnext.place(x=800,y=450)





        
 
class Stack:
    def  __init__(self):
        self.top=-1
        self.data=[]
        self.s=[]
        self.stackname=""
        
    def pop(self):
        global results
        #results=self.stackname+"  \n         "
        if(self.top==-1) :
            print("NO DATA!")
        else :
            
            self.top-=1
          #  print(data[top+1])
            results= results + self.s[self.top+1]+"\n"
            print(results)
            
    def push(self,arr):
            self.top+=1
            #self.data[self.top]=d
            self.s.insert(self.top,arr)
    
    def getstackname(self,name):
        self.stackname=name
             
class Value:
    
    
    def __init__(self):
        self.knowledge=0
        self.time=0
        self.difficulty=0
        self.interest=0
        
        
    def calcv(self):
        global vlist
        print("How much do you know about this chapter on a scale of 1-10? \n")
        knowledge=vlist[0]
        print(vlist[0])
        print("How difficult  is this chapter on a scale of 1-10? \n")
        difficulty=vlist[3]
        
        print("How interesting is this chapter on a scale of 1-10?  \n")
        interest=vlist[2]
        
        print("How time consuming is this chapter on a scale of 1-10? \n")
        time=vlist[1]
        
        return ((0.4*knowledge)+(0.1*interest)+(0.3*time)+(0.2*difficulty))
    
    
class Chapters:
    
    
    def __init__(self):
        self.weightage=0
        self.wbyv=0
        self.v=1
        self.intmarks=0
        self.cname=""
        
    def accintmarks(self,m):
        self.intmarks=m

    def getweight(self):
        return self.weightage
    
    def getwbyv(self):
        self.wbyv=self.weightage/self.v
        
    def accwbyv(self):
        return self.wbyv
        
    def getvalue(self):
        c=Value()
        v=c.calcv()
        v=(v*0.7)+(0.3*self.intmarks)
        self.getwbyv()
        
    def getname(self):
        return self.cname
    
    
    def getinput(self):
        global chaplist
        #print("Enter the name of the Chapter \n")
        self.cname= chaplist[0]
        
        #print("Enter the weightage\n")
        self.weightage=chaplist[1]
        self.getvalue()
        return self
        
        

            
        
        
        
         
        
        
           

    

        
class Subject:

    


    def __init__(self):
        self.maxm=0
        self.tscore=0
        self.nchap=0
        self.name=""
        self.knaparr=[]
        self.c=[]
        self.s=Stack()


    def knapsub(self):
        for i in range(0,self.nchap):
           self.knaparr.append(self.c[i].accwbyv())
        self.sortknap()
    
    def findresult(self):
        sum=0.0
        i=0
        while sum <= self.tscore:
            sum=sum+self.c[i].getweight()
            self.s.pop()
            i+=1
            
    def sortknap(self):
        #global results
        #results=results+self.name+"\n"
        global v
        global results
        v+=1
        results=results+str(v)+") \n"
        
        
        self.knaparr.sort()
        for i in range(0,self.nchap):
            #self.s.getstackname(self.name)
            self.s.push(self.c[i].getname())

        self.findresult()

    

    def getnumber(self):
        k=self.nchap
        return k
    
    def inchap(self,cx):
        self.c.append(cx)
        

                    
    def inputs(self):
        global sublist
        #print("Enter Name of Subject:")
        self.name=str(sublist[0])
        #print("Enter Maximum marks of Subject:")
        self.maxm=int(sublist[1])
        #print("Enter Target Score for Subject:")
        self.tscore=int(sublist[3])
        #print("Enter Number of chapters :")
        self.nchap=int(sublist[2])
        
            
        
        return self
        
        #for i in range(nchap):
         #   self.c[i].getinput()


    def getintmarks(self):
        m=0.0
        global tlist
            #print("Enter the marks this chapter has been asked for in the internals:")
        m=float(tlist[1])
        m=(m/self.maxm)*100
        m=int(m/10)
        chapname=tlist[0]
        for i in range(0,self.nchap):
            if(chapname==self.c[i].cname):
                break;
        self.c[i].accintmarks(m)        
            

      
def main():
    openmain()

if __name__=="__main__":
    main()
    
        
        
    
    
    
    
    
    
    
  
        
        
    
    
    
    
    
    
    
    














