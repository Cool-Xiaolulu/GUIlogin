#登录程序GUI版
#主窗口
from tkinter import *
win=Tk()
win.title("登录程序")
win.geometry("300x100")
 
#用户名输入
txt=Label(win, text="输入用户名：")
txt.grid(column=0,row=0)
intxt1= Entry(win, width=10)
intxt1.grid(column=1, row=0)

#密码输入
txt=Label(win, text="   输入密码：")
txt.grid(column=0,row=2)
intxt2= Entry(win, width=10)
intxt2.grid(column=1, row=2)

#账户存储
us=["admin"]
ps=["123456"]    
chance=[]

#登录
def login():
    usin=intxt1.get()
    psin=intxt2.get()
    if usin in us:
        index=us.index(usin)
        psc=ps[index]
        if psin==psc:
            right=Tk()
            right.geometry("250x100")
            right.title(" ")
            txt=Label(right, text="登录成功",font=20)
            txt.pack(expand=True)
        else:
            chance.append(0)
            if len(chance)==5:
                txt=Label(win, text="次数过多，程序锁定",font=20)
                txt.grid(column=2,row=3)
                btn1.config(state="disabled")
                btn2.config(state="disabled")
            else:
                wrong=Tk()
                wrong.geometry("250x100")
                wrong.title(" ")
                txt=Label(wrong, text="登录失败",font=20)
                txt.pack(expand=True)
    else:
        unknown=Tk()
        unknown.geometry("250x100")
        unknown.title(" ")
        txt=Label(unknown, text="找不到你的账户，请重新输入",font=20)
        txt.pack(expand=True)

#注册
def register1():
        reg=Tk()
        reg.geometry("300x100")
        reg.title(" ")
        txt=Label(reg,text="请输入新账号：")
        txt.grid(column=0,row=0)
        txt=Label(reg,text="请输入新密码：")
        txt.grid(column=0,row=2)
        intxt1= Entry(reg, width=10)
        intxt1.grid(column=1, row=0)
        intxt2= Entry(reg, width=10)
        intxt2.grid(column=1, row=2)
        def register2():
            nusin=intxt1.get()
            npsin=intxt2.get()
            us.append(nusin)
            ps.append(npsin)
            txt=Label(reg,text="注册成功，你可以安全关闭此窗口")
            txt.grid(column=1,row=3)
        btn=Button(reg, text="  注册  ",command=register2)
        btn.grid(column=0, row=3)

#登录按钮
btn1=Button(win, text="  登录  ",command=login)
btn1.grid(column=0, row=3)

#注册按钮
btn2=Button(win, text="  注册  ",command=register1)
btn2.grid(column=1, row=3)

win.mainloop()

