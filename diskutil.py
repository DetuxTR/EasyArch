import parted
import os


class StorageDevice():
    def __init__(self, disklocation):
        self.disklocation = disklocation
        self.device = None
        self.disk = None

    def init(self):
        self.device = parted.getDevice(self.disklocation)
        self.disk = parted.newDisk(self.device)

    def clearPartitionTable(self):
        self.device.clobber()
        ipt = input("Do you want to set partition label to GPT(You must do it to continue.) : (Y/N,y/n)")
        if ipt.lower() == "y":
            self.setLabeltoGpt()

    def setLabeltoGpt(self):
        os.system("sudo parted -s {} mklabel gpt".format(self.disklocation))

    def getPartInfofromNumber(self,partNumber):
        partinfo= {}
        for partition in self.disk.partitions:
            if partition.number == partNumber:
                geo = partition.geometry
                partinfo["number"] = partition.number
                partinfo["lenght"] = partition.getLength()
                partinfo["active"] = partition.active
                partinfo["busy"] = partition.busy
                partinfo["path"] = partition.path
                partinfo["type"] = partition.type
                partinfo["geometry-start"] = geo.start
                partinfo["geometry-end"] = geo.end
                partinfo["geometry-lenght"] = geo.lenght

    def lastPartInfo(self):
        self.getPartInfofromNumber(self.disk.lastPartitionNumber)


