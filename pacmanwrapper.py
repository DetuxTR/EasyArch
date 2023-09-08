import utils

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


