import os
import getpass

n = 0
up = ""
download = input("Would you like to be able to directly open files with PRIME?")
if download == "Y":
    print("Downloading '/Prime [Warp].bat [0.004625 KB]")
    os.mkdir(f"C:/Users/{getpass.getuser()}/Desktop/PRIME")
    up = "@echo off\necho Opening..\nstart Prime.py"
    for line in up:
          os.system(f"echo {line} > C:/Users/{getpass.getuser()}/Desktop/PRIME/Prime [Warp].bat")
print("Downloading Prime.py [5.112 KB]
up = """
import getpass
import os

os.system("title Prime Script: read.prime")
errors = ""
script = []
floc = 0
cloc = 0
while not ".prime" in os.listdir(f"C:/Users/{getpass.getuser()}/Desktop/PRIME/")[floc]:
    floc += 1
file = os.listdir(f"C:/Users/{getpass.getuser()}/Desktop/PRIME/")[floc]
os.system(f"title Prime Script: {file}")
sysinput = ""
f = open(f"C:/Users/{getpass.getuser()}/Desktop/PRIME/{file}", "r")
for line in f:
    script.append(line)

vlist = []
n = 0
i = script[n]
itm = ""
loc = 0
ref = 0
dou = []
while not n == len(script):
    n += 1
    i = script[n-1]
    itm = ""
    loc = 0
    if "system.display(" in i:
        loc = 0
        loc = 15
        itm = ""
        if not i[15] == ">":
            while not i[loc+1] == "\"":
                loc += 1
                itm = itm + i[loc]
            if itm == "":
                errors = errors + f"\nERR [Ln {n-1}]: Nothing to Print."
            else:
                if "import system\n" in script:
                    print(itm)
                else:
                    errors = errors + f"\nERR [Ln {n-1}]: Define \"system\""
        else:
            while not i[loc+1] == ")":
                loc += 1
                itm = itm + i[loc]
            if itm == "system.input":
                print(sysinput)
            if itm == "system.username":
                print(getpass.getuser())
            if not "." in itm:
                if itm in vlist:
                    print(vlist[vlist.index(itm)+1])
                else:
                    errors = errors + f"\nERR [Ln {n-1}]: Variable \"{itm}\" does Not Exist."
            if "+" in itm or "-" in itm or "*" in itm or "/" in itm:
                loc = 15
                itm = ""
                while i[loc+1] in "1234567890":
                    loc += 1
                    itm = itm + i[loc]
                dou.append(itm)
                loc += 1
                itm = ""
                while i[loc+1] in "1234567890":
                    loc += 1
                    itm = itm + i[loc]
                dou.append(itm)
                if "+" in i:
                    print(int(dou[0]) + int(dou[1]))
                if "-" in i:
                    print(int(dou[0]) - int(dou[1]))
                if "*" in i:
                    print(int(dou[0]) * int(dou[1]))
                if "/" in i:
                    print(int(dou[0]) / int(dou[1]))
                
    if "system.input(" in i:
        loc = 0
        loc = 13
        itm = ""
        while not i[loc+1] == "\"":
            loc += 1
            itm + itm + i[loc]
        if "import system\n" in script:
            sysinput = input(itm)
        else:
            errors = errors + f"\nERR [Ln {n-1}]: Define \"system\""
    if "system.clear(" in i:
        if not "()" in i:
            errors = f"\nERR [Ln {n-1}]: Function built for no args"
        else:
            if "import system\n" in script:
                os.system("cls")
            else:
                errors = errors + f"\nERR [Ln {n-1}]: Define \"system\""
    if "system.file.direct(" in i:
        loc = 0
        loc = 19
        itm = ""
        while not i[loc+1] == "\"":
            loc += 1
            itm = itm + i[loc]
        if itm == "":
            errors = errors + f"\nERR [Ln {n-1}]: Path empty"
        else:
            if "import system\n" in script:
                f = open(itm, "r")
                script = []
                n = 0
                os.system("cls")
                os.system(f"title {itm}")
                for line in f:
                    script.append(line)
            else:
                errors = errors + f"\nERR [Ln {n-1}]: Define \"system\""
    if "system.color(" in i:
        loc = 0
        loc = 13
        itm = ""
        while not i[loc+1] == "\"":
            loc += 1
            itm = itm + i[loc]
        if "import system\n" in script:
            os.system(f"color {itm}")
        else:
            errors = errors + f"\nERR [Ln {n-1}]: Define \"system\""

    if i == "/*":
        while not script[n-1] == "*/":
            n += 1

    if "var " in i:
        loc = 3
        itm = ""
        while not i[loc+1] == " ":
            loc += 1
            itm = itm + i[loc]
        if not itm in vlist:
            vlist.append(itm)
            vlist.append("")
        dou = [itm]
        if "\"" in i:
            loc = i.index("\"")
            itm = ""
            while not i[loc+1] == "\"":
                loc += 1
                itm = itm + i[loc]
            vlist[vlist.index(dou[0])+1] = itm
        else:
            print("Func WIP")

    if "arr " in i:
        loc = 3
        itm = ""
        while not i[loc+1] == " ":
            loc += 1
            itm = itm + i[loc]
        if not itm in vlist:
            vlist.append(itm)
            vlist.append("")
        dou = [itm]
        while not "};" in script[n]:
            if not "};" in script[n]:
                vlist[vlist.index(dou[0])+1] = vlist[vlist.index(dou[0])+1] + script[n]
            n += 1

        
    
if not errors == "":
    os.system("cls")
    os.system("color 4")
print(errors)
os.system("pause")
"""
for line in up:
      os.system(f"echo {line} > C:/Users/{getpass.getuser()}/Desktop/PRIME/Prime.py")
      print("Finished!")
