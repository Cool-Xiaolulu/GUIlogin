#登录程序
us=["admin"]
ps=["123456"]
chance=0
while chance<4:
    usin=input("请输入你的账号（若没有账号请输入“注册”）：")
    if usin in us:
        index=us.index(usin)
        psin=input("请输入你的密码：")
        psc=ps[index]
        if psin==psc:
            print("登录成功")
            break
        else:
            chance+=1
            if chance !=4:
                print("登录错误，你还有",4-chance,"次机会")
                continue
            else:
                print("登录失败，程序锁定")
    elif usin=="注册":
        nusin=input("请输入新账号：")
        npsin=input("请输入新密码：")
        us.append(nusin)
        ps.append(npsin)
        print("注册成功")
    else:
        print("找不到你的账号，请重新输入")

