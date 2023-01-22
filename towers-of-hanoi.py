# source, a
# middle, b
# destination, c

# disk w/ index 0 is smallest and 2 is largest

def hanoi(disk, source, middle, destination):

    # BASE CASE - 0 is always the smallest plate
    if disk == 0:
        print('Disk %s from %s to %s' %(disk,source, destination))
        return
    
    hanoi(disk-1, source, destination, middle)
    print('Disk %s from %s to %s' %(disk,source, destination))
    hanoi(disk-1, middle, source, destination)

hanoi(3, 'A', 'B', 'C')




