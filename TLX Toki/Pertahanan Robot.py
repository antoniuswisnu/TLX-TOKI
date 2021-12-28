s = input()
robot = [0,0]

for s in s:
    if s == "R":
        robot[0] += 1
    elif s == "L":
        robot[0] -= 1
    elif s == "U":
        robot[1] += 1
    elif s == "D":
        robot[1] -= 1
    else:
        pass

hasil = " ".join(str(robot) for robot in robot)
print(hasil)
    
