#TOWER OF AN i 
def(disk,source,destination,aux):
    if(disk==1):
        print("move the disk 1 from source to dest:")
        return
    else:
        tower(disk-1,A,B,C)
        print("move {} from {} to {}".format(disk, A,B)
        tower(disk-1,A,B,C)


disk=int(input("enter the input"))
print("steps involved in the process")
tower(disk,'A','B','C')