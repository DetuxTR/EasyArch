import parted
import os

def getPartType(partstr):
    if partstr == "normal":
        return parted.PARTITION_NORMAL
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
                partinfo["geometry-lenght"] = geo.length
        return partinfo

    def lastPartInfo(self):
        last_partition = self.getPartInfofromNumber(self.disk.lastPartitionNumber)
        if last_partition:
            return last_partition
        else:
            return {"number": -1}


    def addPartition(self,length,fstype,pr_type):
        type = getPartType(pr_type)
        if self.lastPartInfo()["number"] == -1:
            start = 0
        else:
            start = self.lastPartInfo()["geometry-end"]
        geometry = parted.Geometry(start=start,
                                   length=parted.sizeToSectors(length, 'MiB', self.device.sectorSize),
                                   device=self.device
                                   )
        fs = parted.FileSystem(type=fstype,
                               geometry=geometry
                               )
        part = parted.Partition(disk=self.disk,
                                type=type,
                                fs=fs,geometry=geometry
                                )
        self.disk.addPartition(part, constraint=self.device.optimalAlignedConstraint)
        self.disk.commit()
