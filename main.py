import parted
import pacmanwrapper
import diskutil
import sys
import os
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
    # disk.deletePartitionbyNum(1)
    # print(disk.lastPartInfo()["number"])


    # pres = pacmanwrapper.install_pkg("micro")
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
