def Hanoi(disk, start, middle, end):
    if disk == 1:
        print(f"Disk {disk} from {start} to {end}")
        return
    Hanoi(disk-1, start, end, middle)
    print(f"Disk {disk} from {start} to {end}")
    Hanoi(disk-1, middle, start, end)

Hanoi(3, "A", "B", "C")