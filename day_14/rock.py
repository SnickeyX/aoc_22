# a very messy sol, shoudl clean up later

def insert_sand(x, y, rock_coords, chall_num=1, abyss_threshold=0):
    sand_pos = (x,y)
    sand_not_resting = True
    while sand_not_resting:
        if(chall_num == 1 and sand_pos[1] > abyss_threshold):
            return (-1,-1)
        if (down := (sand_pos[0] ,sand_pos[1] + 1)) not in rock_coords:
            sand_pos = down
        elif (diagonal_left := (sand_pos[0]-1, sand_pos[1] + 1)) not in rock_coords:
            sand_pos = diagonal_left
        elif (diagonal_right := (sand_pos[0]+1, sand_pos[1] + 1)) not in rock_coords:
            sand_pos = diagonal_right
        else:
            if(chall_num == 2 and sand_pos == (500,0)):
                return (-1,-1)
            rock_coords.add(sand_pos)
            return sand_pos

with open("main_input.txt") as file:
    cleaned_data = [list(map( lambda x : tuple([int(y) for y in x.split(",")]), line.split("->"))) for line in file.read().splitlines()]
    rock_coords = set()
    for points in cleaned_data:
        for i in range(0, len(points)-1):
            p1 = points[i]
            p2 = points[i+1]
            #x value decreases
            if(p1[0] > p2[0]):
                for x in range(int(p1[0]), int(p2[0])-1, -1):
                    rock_coords.add((x, p1[1]))
            # x value increases
            elif(p1[0] < p2[0]):
                for x in range(int(p1[0]), int(p2[0])+1):
                    rock_coords.add((x, p1[1]))
            # y value decreases
            elif(p1[1] > p2[1]):
                for y in range(int(p1[1]), int(p2[1])-1, -1):
                    rock_coords.add((p1[0],y))
            # y value increases
            elif(p1[1] < p2[1]):
                for y in range(int(p1[1]), int(p2[1])+1):
                    rock_coords.add((p1[0],y))
                    
    abyss_threshold = max([coord[1] for coord in rock_coords])
    rock_coords_1 = rock_coords.copy()
   
    inserted_sand = []
    sand_pos = (500,0)
    while(sand_pos != (-1,-1)):
        sand_pos = insert_sand(500, 0, rock_coords_1, abyss_threshold=abyss_threshold)
        inserted_sand.append(sand_pos)
    # remove the last sand
    inserted_sand.pop()
    print("answer to part1", len(inserted_sand))  # 885

    for i in range(0,1000):
        rock_coords.add((i, abyss_threshold + 2))
        
    inserted_sand = []
    sand_pos = (500,0)
    while(sand_pos != (-1,-1)):
        sand_pos = insert_sand(500, 0, rock_coords, 2, abyss_threshold=abyss_threshold)
        inserted_sand.append(sand_pos)
    print("answer to part2", len(inserted_sand)) # 28691