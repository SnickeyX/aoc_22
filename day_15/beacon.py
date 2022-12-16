import re 

def get_manhattan_dist(p,q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])

def add_points_within_manhattan(p : tuple, q : tuple, points : set, y_coord : int, chall_num : int = 1):
    man_dist = get_manhattan_dist(p,q)
    if(p[1] == y_coord):
        points.add(p)
    for i in range(p[0] - man_dist, p[0] + man_dist + 1):
            if(get_manhattan_dist(p,(i,y_coord)) <= man_dist and (i, y_coord) != q):
                points.add((i,y_coord))  
    return points 

# find all ranges of possible x values for every sensor/beacon pair
# then find the one x value that is not in any of the ranges for a particular y value
def get_distress_x(sensors, becons, y_coord):
    ranges = []
    for s,b in zip(sensors, becons):
        dy = abs(y_coord - s[1])
        dist = get_manhattan_dist(s,b)
        if dy > dist:
            continue
        dx = dist - dy
        ranges.append((s[0] - dx, s[0] + dx))
    ranges.sort()
    prev_range_max = ranges[0][1]
    for curr_range_min, curr_range_max in ranges[1:]:
        if curr_range_min > prev_range_max:
            return prev_range_max + 1
        prev_range_max = max(curr_range_max, prev_range_max)
    return False
     

with open("main_input.txt") as f:
    cleaned_data = [re.findall(r'(-?\d+)', line) for line in f.read().splitlines()]
    sensor_locations = []
    beacon_locations = []
    points_seen = set()
    for line in cleaned_data:
        sensor_locations.append((int(line[0]), int(line[1])))
        beacon_locations.append((int(line[2]), int(line[3])))

    for p,q in zip(sensor_locations, beacon_locations):
        add_points_within_manhattan(p,q,points_seen, y_coord = 2000000)
    print("part1: ", len(points_seen))
    
    points = set()
    for row in range(0, 4000000):
        if(missing_x := get_distress_x(sensor_locations, beacon_locations, row)):
            print("part2: ", missing_x * 4000000 + row)