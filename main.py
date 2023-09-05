import parted

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
    disk=diskutil.StorageDevice("/dev/loop0")
    disk.init()
    disk.getPartInfofromNumber(-1)
    print(disk.lastPartInfo()["number"])
    disk.addPartition(48,"ext4","normal")
