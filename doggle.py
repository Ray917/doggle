import os
import sys
import random
import string
import getpass

os.system("title 睿集团 加密狗 v1.1.0 Preview")
print("睿集团 加密狗 v1.1.0.00T70800202.1 Preview\nRayGroup Doggle v1.1.0.00T70800202.1 Preview\n版权所有 睿集团 2020。保留所有权利。\n")

print("让您的U盘或移动硬盘成为您的计算机的唯一凭证。")
print("让您的U盘或移动硬盘成为您的计算机的“钥匙”，")
print("如果没有这把“钥匙”，您的计算机就会 爆 掉 ！\n")

print("/--------------------开始初始化--------------------/\n正在检测加密狗服务是否开启...")
if(os.path.exists("C:\\Users\\"+getpass.getuser()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\raygroupdoggleprocess.exe")==True):
    print("检测成功：已开启")
    check=True
else:
    print("检测成功：未开启")
    check=False
print("/--------------------结束初始化--------------------/")

if(check==False):
    while True:
        start=str(input("\n是否开始开启加密狗服务？(Y/n) "))
        if(start=="Y" or start=="y"):break
        elif(start=="N" or start=="n"):sys.exit()
        else:print("错误：输入不合法。")
    
    print("\n/--------------------开始创建向导--------------------/")
    print("注意：加密狗服务仅会应用到您现在登录的本地用户上，\n其他用户并不会受到影响。\n")
    pa=str(input("1/3:\n我们需要在您的U盘或移动硬盘中创建验证文件以和您的计算机匹配。\n输入将要存放验证文件的U盘路径：\n>> "))
    if(len(pa)==0):
        print("\n发生了一个致命的错误：输入不合法。\n错误：向导1/3\n")
        os.system("pause")
        sys.exit()
    if(pa[0]==chr(34)):pa=pa[1:len(pa)]
    if(pa[len(pa)-1]==chr(34)):pa=pa[0:len(pa)-1]
    if(pa[len(pa)-1]!=chr(92)):pa=pa+chr(92)
    mode=str(input("\n2/3:\n选择模式：\n1：当您登录这台计算机的这个用户时检测，检测完毕后弹出U盘也能继续使用。\n2：持续检测，使用时必须插着U盘，弹出U盘计算机就会 爆 掉 。\n>> "))
    if(mode!="1" and mode!="2"):
        print("\n发生了一个致命的错误：输入不合法。\n错误：向导2/3\n")
        os.system("pause")
        sys.exit()
    boom=str(input("\n3/3:\n选择“爆掉”的动作：\n1：锁定\n2：关机\n>> "))
    if(mode!="1" and mode!="2"):
        print("\n发生了一个致命的错误：输入不合法。\n错误：向导3/3\n")
        os.system("pause")
        sys.exit()
    print("\n/--------------------结束创建向导--------------------/")

    print("\n/--------------------开始设置--------------------/")
    print("开始生成验证文件至 "+pa+" ...")
    vert=str(''.join(random.sample(string.ascii_letters + string.digits, 62)))
    file = open('.\\temp.txt','w')
    file.write(vert)
    file.close()
    os.system("ren temp.txt verifyfile.raydoggle")
    a=os.system("move verifyfile.raydoggle "+chr(34)+pa+chr(34))
    if(a==1):
        os.system("del verifyfile.raydoggle")
        print("\n这是一个致命的错误，已停止并撤销设置。\n错误：向导1/3\n")
        os.system("pause")
        sys.exit()
    print("已生成验证文件至 "+pa+" 。")

    print("正在编写代码...")
    file = open('.\\temp.txt','w')
    file.write("@echo off\n:start\ncls\nif not exist "+chr(34)+pa+"verifyfile.raydoggle"+chr(34)+" ")
    if(boom=="1"):file.write("rundll32.exe user32.dll LockWorkStation\n")
    else:file.write("shutdown -s -t 0\n")
    file.write("for /f "+chr(34)+"delims="+chr(34)+" "+chr(37)+chr(37)+"a in ('type "+chr(34)+pa+"verifyfile.raydoggle"+chr(34)+"') do set a="+chr(37)+chr(37)+"a\n")
    file.write("if not "+chr(37)+"a"+chr(37)+"=="+vert+" ")
    if(boom=="1"):file.write("rundll32.exe user32.dll LockWorkStation\n")
    else:file.write("shutdown -s -t 0\n")
    if(mode=="2"):file.write("timeout /t 1\ngoto start\n")
    file.write("exit\n")
    file.close()
    os.system("ren temp.txt temp.bat")
    print("编写代码已完成。")

    print("正在编译代码至可执行文件...")
    os.system(".\\Convert\\Bat_To_Exe_Converter.exe /bat .\\temp.bat /exe .\\raygroupdoggleprocess.exe /invisible /x64")
    os.system("del temp.bat")
    print("\n编译代码至可执行文件已完成。")

    print("正在添加自启动...")
    a=os.system("move .\\raygroupdoggleprocess.exe "+chr(34)+"%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"+chr(34))
    if(a==0):print("添加自启动已完成。")
    else:
        os.system("del raygroupdoggleprocess.exe")
        os.system("del "+pa+"verifyfile.raydoggle")
        print("\n这是一个致命的错误，已停止并撤销设置。\n错误：自启被阻止\n")
        print("您可以尝试：以管理员方式运行此程序、关闭杀毒软件。\n")
        os.system("pause")
        sys.exit()

    print("正在启动...")
    os.system("start "+chr(34)+chr(34)+" "+chr(34)+"%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\raygroupdoggleprocess.exe"+chr(34))
    print("启动已完成。")

    print("\n/--------------------结束设置--------------------/\n")

    print("已结束设置，您现在可以体验由睿集团加密狗带来的安全与便携。")
    print("卸载此程序并不会影响加密狗的运行，卸载后可重新安装此程序来关闭加密狗。")
    print("如需关闭加密狗，请重新打开此程序来操作。\n")
    print("如果您想在没有设置的U盘或移动磁盘的情况下关闭加密狗，请联系我们的技术支持：")
    print("邮箱：ray_group@126.com")
    print("B站私信：https://space.bilibili.com/476881495")
    print("以上两种联系方式都必须标记【客服】，并提供手机号码。\n")
    os.system("pause")
    sys.exit()

else:
    while True:
        start=str(input("\n是否开始关闭加密狗服务？(Y/n) "))
        if(start=="Y" or start=="y"):break
        elif(start=="N" or start=="n"):sys.exit()
        else:print("错误：输入不合法。")

    print("\n/--------------------开始关闭向导--------------------/")
    print("注意：只会关闭计算机的服务，U盘或移动硬盘内的验证文件并不会被删除。")
    print("您可以手动删除。\n")
    os.system("pause")
    print("\n/--------------------结束关闭向导--------------------/")

    print("\n/--------------------开始设置--------------------/")
    print("正在关闭...")
    a=os.system("taskkill -f -im raygroupdoggleprocess.exe")
    if(a==1):
        print("\n这是一个致命的错误。\n错误：进程无法结束\n")
        print("您可以尝试：以管理员方式运行此程序、关闭杀毒软件。\n")
        os.system("pause")
        sys.exit()
    print("关闭已完成。")

    print("正在删除...")
    a=os.system("del "+chr(34)+"%USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\raygroupdoggleprocess.exe"+chr(34))
    if(a==1):
        print("\n这是一个致命的错误。\n错误：进程无法结束\n")
        print("您可以尝试：以管理员方式运行此程序、关闭杀毒软件。\n")
        os.system("pause")
        sys.exit()
    print("删除已完成。")
    print("\n/--------------------结束设置--------------------/")

    print("\n需要重启您的计算机以关闭加密狗。")
    while True:
        start=str(input("\n是否重启？(Y/n) "))
        if(start=="Y" or start=="y"):os.system("shutdown -r -t 0")
        elif(start=="N" or start=="n"):break
        else:print("错误：输入不合法。")

    print("现在加密狗仍在运行，您可以稍后重启以关闭。\n")
    os.system("pause")
    sys.exit()