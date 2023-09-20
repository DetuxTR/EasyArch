import utils

print("hello")
def install_pkg (package_name):
    if type(package_name) ==  str:
        res = utils.run_cmd(["sudo", "pacman","-Sy","--noconfirm",package_name])
        result = res.stderr.split("\n")
        print(result)


        if "is up to date -- reinstalling" in result[0]:
                return [True, True, False]

        for line in res.stdout.split("\n"):
                if "upgrading {}".format(package_name) in line:
                    return [True, True, True]

        if len(result) == 1:
            return [True]

    else:
        print("Package Name Must be String")

def remove_pkg(package_name):
    if type(package_name) == str:
        res = utils.run_cmd(["sudo","pacman","-R","--noconfirm",package_name])
        if len(res.stderr.split("\n")) < 2:
            return True
        else:
            return False
    else:
        print("Package Name Must be String")

def remove_deppkg(package_name):
    if type(package_name) == str:
        res = utils.run_cmd(["sudo","pacman","-Rdd","--noconfirm",package_name])
        if len(res.stderr.split("\n")) < 2:
            return True
        else:
            return False
    else:
        print("Package Name Must be String")

def install_from_txt(txtfile):
    f  = open(txtfile,"r")
    print(f.read())

def add_pkg_to_txt(package,txtfile):
    f = open(txtfile,"w")


    if check_package(package):
        print("Package Available")
        f.write("{}".format(package))
    else:
        print("Package not found")

def check_package(package_name):
    res=utils.run_cmd("sudo pacman -Si {}".format(package_name).split())

    if len(res.stderr) == 0:
        return True
