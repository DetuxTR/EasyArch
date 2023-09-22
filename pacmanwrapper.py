import utils

print("hello")

class Pacman():
    def __init__(self,root="",cachedir="",):
        if type(root) and type(cachedir) == str:
            if len(root) == 0:
                self.root = "/"
            if len(cachedir) == 0:
                self.cachedir= root + "/var/cache/pacman/pkg"
            self.pacmanstr= "sudo pacman -r {} --cachedir {}".format(self.root,self.cachedir)


    def install_pkg (self,package_name):
        if type(package_name) ==  str:
            res = utils.run_cmd(self.pacmanstr.split()+["-Sy","--noconfirm",package_name])
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

    def remove_pkg(self,package_name):
        if type(package_name) == str:
            res = utils.run_cmd(self.pacmanstr.split()+["-R","--noconfirm",package_name])
            if len(res.stderr.split("\n")) < 2:
                return True
            else:
                return False
        else:
            print("Package Name Must be String")

    def remove_deppkg(self,package_name):
        if type(package_name) == str:
            res = utils.run_cmd(self.pacmanstr.split()+["-Rdd","--noconfirm",package_name])
            if len(res.stderr.split("\n")) < 2:
                return True
            else:
                return False
        else:
            print("Package Name Must be String")

    def install_from_txt(self,txtfile,):
        f  = open(txtfile,"r")
        print(f.read())

    def add_pkg_to_txt(package,txtfile,self):
        try:
            if open(txtfile,"r"):
                print("packagelist file is found")

        except:
            open(txtfile,"x")

        if type(package) == str:
            f = open(txtfile,"a+")
            if self.check_package(package):
                print("Package Available")
                # f.writelines("{}".format(package))
                f.seek(0)


                if len(f.read()) == 0:
                    f.seek(0, 2)
                    f.writelines("{}".format(package))
                    f.seek(0)
                else:
                    f.seek(0,2)
                    f.writelines("\n{}".format(package))
                    f.seek(0)
            else:
                print("Package not found")
        else:
            print("Package Name Must be String")

    def check_package(self,package_name):
        res=utils.run_cmd(self.pacmanstr.split()+["-Si",package_name])
        print(res.stdout)
        if len(res.stderr) == 0:
            return True

    def check_package_exists(self,package,txtfile):
        fa = open(txtfile,"r")
        for line in fa.read().split("\n"):
            pass
