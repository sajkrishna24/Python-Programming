def TowerOfHanoi(n,source,destination,intermediate):
    if n==1:
        print(f"Move Disk 1 fron {source} to {destination}")
        return
    TowerOfHanoi(n-1,source,intermediate,destination)
    print(f"Move Disk {n} from {source} to {destination}")
    TowerOfHanoi(n-1,intermediate,destination,source)
n=3
TowerOfHanoi(n,'A','B','C')