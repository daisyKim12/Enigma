from tkinter import *

def main():
  
    #rotterA
    L1=[11, 8, 10, 24, 14, 3, 12, 9, 23, 26, 6, 25, 1, 21, 2, 17, 19, 18, 16, 13, 22, 5, 4, 15, 7, 20]
    #rotterB
    L2=[25, 17, 24, 11, 4, 3, 1, 9, 20, 22, 16, 14, 23, 18, 15, 13, 21, 10, 6, 19, 5, 12, 7, 26, 8, 2]
    #rotterC
    L3=[8, 24, 9, 3, 23, 2, 17, 1, 12, 26, 4, 20, 14, 6, 21, 19, 7, 16, 11, 13, 10, 25, 18, 15, 22, 5]
    #reflectorA
    R1=[8, 7, 25, 9, 21, 16, 2, 23, 17, 15, 20, 13, 19, 10, 3, 11, 6, 18, 26, 12, 1, 24, 22, 5, 4, 14]
    #reflectorB
    R2=[6, 25, 1, 10, 18, 22, 23, 21, 11, 19, 12, 13, 9, 3, 26, 17, 24, 2, 5, 8, 20, 15, 7, 4, 14, 16]
    #알파벳
    L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    mun1=0
    mun2=0
    mun3=0
    turn=eval(turns.get())
    for n in range(1,4):
        if Rot1.get(Rot1.curselection())[-1]==str(n):
            mun1=n
        if Rot2.get(Rot2.curselection())[-1]==str(n):
            mun2=n
    for n in range(1,3):
        if Ref.get(Ref.curselection())[-1]==str(n):
            mun3=n
    sentence=sentences.get()

    pos=0
    Output=[]

    for pos in range(0,len(sentence)):
        word=sentence[pos]
        num1=L.index(word)+1
    
#rotter1
        def rotter1(k):
       
            L=[L1,L2,L3]
            crotter=L[k-1]
            
            num2=crotter[num1-1]
            return num2


        num2=rotter1(mun1)+pos+turn
        if num2>=26:
            num2=num2%26
        if num2==0:
            num2=26   

   
#rotter2
        def rotter2(k):

            L=[L1,L2,L3]
            crotter=L[k-1]
            num3=crotter[num2-1]
            return num3

        num3=rotter2(mun2)

#reflectorA
        def reflectorA(k):
            L=[R1,R2]
            cref1=L.pop(k-1)
            cref2=cref1[:]
            cref2.reverse()
        
            a=cref1.index(num3)
            b=cref2[a]
            return b
    
        num4=reflectorA(mun3)

#rotter2역함수
        def irotter2(k):
            L=[L1,L2,L3]
            crotter=L[k-1]
            num5=crotter.index(num4)
            num5+=1
            return num5


        num5=irotter2(mun2)-pos-turn
        
        if num5<0:
            num5=num5%26
        
        if num5==0:
            num5=26
        print(num5)  
#rotter1역함수
        def irotter1(k):
            L=[L1,L2,L3]
            crotter=L[k-1]
            num6=crotter.index(num5)
            num6+=1
            return num6
    
        num6=irotter1(mun1)-1


        final=L[num6]
        Output.append(final)
        fOutput=''.join(Output)
    
    fOutputs.set(fOutput)

window=Tk()
window.title("Enigma Program")

Label(window,text="Rotter1").grid(row=0,column=0,padx=10,pady=8,sticky=EW)
Label(window,text="Rotter2").grid(row=0,column=1,padx=10,pady=8,sticky=EW)
Label(window,text="Reflector").grid(row=0,column=2,padx=10,pady=8,sticky=EW)

rotter1s=StringVar()
Rot1=Listbox(window,width=8,height=3,selectmode='single',exportselection=0,listvariable=rotter1s)
Rot1.grid(row=1,column=0,pady=10,padx=10)

A1=["Rotter1","Rotter2","Rotter3"]
rotter1s.set(tuple(A1))

rotter2s=StringVar()
Rot2=Listbox(window,width=8,height=3,selectmode='single',exportselection=0,listvariable=rotter2s)
Rot2.grid(row=1,column=1,pady=10,padx=10)

A2=["Rotter1","Rotter2","Rotter3"]
rotter2s.set(tuple(A2))

reflectors=StringVar()
Ref=Listbox(window,width=8,height=3,selectmode='single',exportselection=0,listvariable=reflectors)
Ref.grid(row=1,column=2,pady=10,padx=10)

A3=["Reflector1","Reflector2"]
reflectors.set(tuple(A3))

t1=Label(window, text="Today number: ")
t1.grid(row=4,column=0,pady=5,padx=15,sticky=W)

turns=StringVar()
t2=Entry(window,width=3,textvariable=turns)
t2.grid(row=4,column=1,padx=3,sticky=EW)

s1=Label(window, text="Input:")
s1.grid(row=6, column=0, padx=3, pady=5)

sentences=StringVar()
s2=Entry(window, width=20,textvariable=sentences)
s2.grid(row=6, column=1, padx=3, pady=5)

c=Button(window, text='coding', bg='light blue',command=main)
c.grid(row=7, column=1, padx=3, pady=5)

o1=Label(window,text='Output: ')
o1.grid(row=8, column=0, padx=3, pady=5)

fOutputs=StringVar()
o2=Entry(window, state="readonly",textvariable=fOutputs)
o2.grid(row=8, column=1, padx=3, pady=5)

window.mainloop()
