import pacmanwrapper
import diskutil
import sys
import os
import flet
import ui
if __name__ == "__main__":
    for argv in sys.argv:
        if argv == "testmode":
            print("I'm running at testmode. All of the operations will applied on disk.img")
            os.system("losetup -f disk.img")
            os.system("kpartx -a /dev/loop0")

    print("""Easy Arch v.0.1""")

    # disk=diskutil.StorageDevice("/dev/loop0")
    #
    # disk.init()
    # disk.getPartInfofromNumber(-1)
    # print(disk.lastPartInfo()["number"])
    #
    # disk.addPartition(48,"ext4","normal")
    # print(disk.lastPartInfo()["number"])

    # pac = pacmanwrapper.Pacman()
    # pres = pac.install_pkg("micro")
    #
    # print(pres)
    #
    # while True:
    #     if len(pres) < 2 and pres[0] == True:
    #         print("Package Installed")
    #         break
    #
    #     if pres[0] and pres[1]: #Package Already Installed,
    #         if pres[2]:
    #             print("Package Already Installed, Package Updated!!!")
    #             break
    #         else:
    #             print("Package is already installed and up to date")
    #             break
    #
    # pac.check_package("micro")
    # pac.remove_pkg("micro")
    # pacmanwrapper.add_pkg_to_txt("python","packagelist")
    # pacmanwrapper.check_package_exists("python","packagelist")
    flet.app(target=ui.main)

