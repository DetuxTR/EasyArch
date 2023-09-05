import diskutil
import sys
import os
if __name__ == "__main__":
    for argv in sys.argv:
        if argv == "testmode":
            print(argv)
            os.system("losetup -f disk.img")
            os.system("kpartx -a /dev/loop0")

    print("""Easy Arch v.0.1""")
    disk=diskutil.StorageDevice("/dev/loop0")
    disk.init()
    disk.getPartInfofromNumber(-1)
    disk.lastPartInfo()