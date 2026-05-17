import sys
import os
import shutil

# Diese App ist für Mich selber gebaut, Wenn dein PC oder OS anders ist als meins
# müsstest du den code *ändern*

def err(id: int, type: int, args: dict = None):
    if args is None:
        args = {}
    if type == 1:
        print(f"Couldnt create Version:\n")
    if type == 2:
        version = args.get("version")
        print(f"Couldnt update Version {version}:\n")
    if type == 3:
        print(f"Couldnt delete Version:\n")
    if id == 201:
        version = args.get("version")
        agrv4 = args.get("agrv4")
        agrv3 = args.get("agrv3")
        print(f"Version already exists.\n   loisgit create {version} {agrv3} {agrv4}\n"
                  f"{" "*len(f"loisgit create {version}")} {'^'*len(version)}\nUse --overwrite to overwrite existing version or use 'loisgit update'\nError: 201 DirectoryExistsError")
    elif id == 202:
        print(f"Not enough values to create Version\nError: 202 ValueError")
    elif id == 198:
        print("Version doesnt exist; use 'loisgit create' to create an version.\nError: 198 FileNotFoundError")


def create():
    if len(sys.argv) < 2:
        err(202, 1)
        sys.exit(202)

    if len(sys.argv) < 3:
        err(202, 1)
        sys.exit(202)
    version = sys.argv[2]

    if len(sys.argv) > 3:
        if sys.argv[3].startswith(r"C:/"):
            path = sys.argv[3]
            inThisCWD = False
        else:
            inThisCWD = True
            path = os.getcwd()

        if inThisCWD:
            if sys.argv[3] == "--overwrite":
                overwrite = True
            else:
                overwrite = False

        argv3 = sys.argv[3:]
        if len(sys.argv) > 4:
            argv4 = sys.argv[4:]
    else:
        argv3 = ""
        argv4 = ""
        overwrite = False
        inThisCWD = True
        path = os.getcwd()



    if not os.path.exists(os.path.join(path, ".loisgit")):
        print("Creating .loisgit directory")
        os.mkdir(os.path.join(path, ".loisgit"))
        
    ignore = [".loisgit",".venv",".vscode",".idea"]
    try:
        with open(os.path.join(path, ".gitignore"), "r") as f:
            for line in f.readlines():
                if line.isspace() or line == "":
                    continue
                if line.startswith("*"):
                    continue
                else:
                    ignore.append(line.strip())
    except FileNotFoundError:
        pass

    root = path

    path = os.path.join(path, ".loisgit")

    if os.path.exists(os.path.join(path, version)):
        if not overwrite:
            err(201, 1, {"version": version, "agrv3": argv3, "agrv4": argv4})
            sys.exit(201)
        shutil.rmtree(os.path.join(path, version))

    shutil.copytree(root, os.path.join(path, version), ignore=shutil.ignore_patterns(*ignore))

def update():
    if len(sys.argv) < 2:
        err(202, 1)
        sys.exit(202)

    if len(sys.argv) > 3:
        path = sys.argv[3]
    else:
        path = os.getcwd()

    version = sys.argv[2]

    ignore = [".loisgit", ".venv", ".vscode", ".idea"]
    try:
        with open(os.path.join(path, ".gitignore"), "r") as f:
            for line in f.readlines():
                if line.isspace() or line == "":
                    continue
                if line.startswith("#"):
                    continue
                else:
                    ignore.append(line.strip())
    except FileNotFoundError:
        pass

    root = path
    path = os.path.join(path, ".loisgit")

    try:
        shutil.rmtree(os.path.join(path, version))
    except FileNotFoundError:
        err(198, 2, {"version": version})
        sys.exit(198)

    shutil.copytree(root, os.path.join(path, version), ignore=shutil.ignore_patterns(*ignore))

def delete():
    if len(sys.argv) < 2:
        err(202, 3)
        sys.exit(202)

    if len(sys.argv) > 3:
        path = sys.argv[3]
    else:
        path = os.getcwd()

    path = os.path.join(path, ".loisgit")
    version = sys.argv[2]

    shutil.rmtree(os.path.join(path, version))

def help_():
    print("""
    
    Possible Commands:
    
    -   loisgit create
    -   loisgit update
    -   loisgit delete
    """)

if len(sys.argv) == 1:
    print("""
    Loisgit Version 1.1:

    An Update System for people that only want backups and not complex stuff.


    Written in Python, Opensource https://github.com/kerimkiraz15-hash/loisgit

    - loisgit help

    """)
    sys.exit(1)

elif sys.argv[1] == "create":
    create()
elif sys.argv[1] == "update":
    update()
elif sys.argv[1] == "delete":
    delete()
elif sys.argv[1] == "help" or sys.argv[1] == "?":
    help_()
