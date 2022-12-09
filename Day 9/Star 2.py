# Day 9

def main():
    
    # Check for maximum size of the grid, results below
    file = open("Data.txt", "r")
    lines = file.readlines()
    dimensions = [0,0,0,0]
    for line in lines:
        line = line.replace("\n","")
        sections = line.split(" ")
        if sections[0] == "U":
            dimensions[0] = dimensions[0] + int(sections[1])
        elif sections[0] == "D":
            dimensions[1] = dimensions[1] + int(sections[1])
        elif sections[0] == "L":
            dimensions[2] = dimensions[2] + int(sections[1])
        elif sections[0] == "R":
            dimensions[3] = dimensions[3] + int(sections[1])
    
    print(dimensions)
    # required width approx 6000
    # required height approx 6000
    
    # Setting up the map
    mapp = []
    for i in range(0,6000):
        mappp = []
        for a in range(0,6000):
            mappp.append(".")
        mapp.append(mappp)
    #      X     Y
    S = [3000, 3000] # Starting point
    # Knots, Head: i = 0, Tail: i = 9
    K = [[3000, 3000],[3000, 3000],[3000, 3000],[3000, 3000],[3000, 3000],[3000, 3000],[3000, 3000],[3000, 3000],[3000, 3000],[3000, 3000]] 
    mapp[S[0]][S[0]] = "#"
    
    
    for line in lines:
        line = line.replace("\n","")
        sections = line.split(" ")
        head_move_amount = int(sections[1])
        head_move_dir = sections[0]

        for i in range(0, head_move_amount):
            K[0] = newPosHead(K[0], head_move_dir)
            for i in range(1,10):
                K[i] = newPosTail(K[i-1], K[i])
            a = K[9][0]
            b = K[9][1]
            if mapp[a][b] == ".":
                mapp[a][b] = "#"
    result = countmarks(mapp)
    print("#-marks: ", result)

# Moves head by one tick using head's current coordinates and direction.
def newPosHead(head, direction):
    if direction == "U":
        head[1] = head[1] + 1
    elif direction == "D":
        head[1] = head[1] - 1
    elif direction == "R":
        head[0] = head[0] + 1
    elif direction == "L":
        head[0] = head[0] -1
    return head

# Finds a new position for any tail knot by comparing the knot's position to the next knot's (head) position.
def newPosTail(head, tail):
    if tail[0] == head[0]:
        if abs(tail[1] - head[1]) > 1:
            if head[1] > tail[1]:
                tail = newPosHead(tail, "U")
            else:
                tail = newPosHead(tail, "D")
    elif tail[1] == head[1]:
        if abs(tail[0] - head[0]) > 1:
            if head[0] > tail[0]:
                tail = newPosHead(tail, "R")
            else:
                tail = newPosHead(tail, "L")
    else:
        if abs(tail[0] - head[0]) > 1:
            if head[0] > tail[0]:
                tail = newPosHead(tail, "R")
            else:
                tail = newPosHead(tail, "L")

            if head[1] > tail[1]:
                tail = newPosHead(tail, "U")
            else:
                tail = newPosHead(tail, "D")
        elif abs(tail[1] - head[1]) > 1:
            if head[1] > tail[1]:
                tail = newPosHead(tail, "U")
            else:
                tail = newPosHead(tail, "D")

            if head[0] > tail[0]:
                tail = newPosHead(tail, "R")
            else:
                tail = newPosHead(tail, "L")
    return tail

# Counts the number of #-marks on the map. These are the points that the end tail has visited at least once.
def countmarks(mapp):
    count = 0
    for i in range(0,6000):
        for a in range(0,6000):
            if mapp[i][a] == "#":
                count = count + 1
    return count

main()
