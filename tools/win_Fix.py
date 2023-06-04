import sysconfig

if not sysconfig.system_W :
    print("无须运行此应用或没有修改sysconfig.py \nneedn't run this or make sure you has changed sysconfig.py")
    exit(0)
else :
    data = '''
    @echo off
    '''+sysconfig.py_Path+'python.exe ../Server.py'
    with open('../bin/open.bat', 'w+') as file :
        file.write(str(data))
    print("已根据 sysconfig.py 中的内容重新生成了一个 open.bat\nhas already created new open.bat from infomation ofsysconfig.py")
    exit(0)
