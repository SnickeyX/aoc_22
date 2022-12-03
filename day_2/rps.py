def cal_round_pts_1(opp_mv, our_mv):
    # 1,2,3 for rock, papers and scissors
    opp_ord_mv = ord(opp_mv) % 64
    our_ord_mv = ord(our_mv) % 87
    # x,y,z are worth 1,2,3 pts in that order
    total_pts = our_ord_mv
    if((our_ord_mv % 3) == (1 + opp_ord_mv) % 3): 
        total_pts += 6
    elif our_ord_mv == opp_ord_mv:
        total_pts += 3 
    else: 
        total_pts+= 0 
    return total_pts
    
# TODO: Clean up the messy nested ifs   
def cal_round_pts_2(opp_mv, our_mv):
    opp_ord_mv = ord(opp_mv) % 64
    our_ord_mv = ord(our_mv) % 88
    # lose = 0, draw = 3, win = 6
    total_pts = our_ord_mv * 3 
    if(not our_ord_mv):
        if(opp_ord_mv == 1):
            total_pts += 3
        else:
            total_pts += (opp_ord_mv - 1) % 3
    elif(our_ord_mv == 1):
        total_pts += opp_ord_mv
    else:
        if opp_ord_mv == 2:
            total_pts += 3
        else:
            total_pts += (opp_ord_mv + 1) % 3
    return total_pts

with open("rps.txt") as f: 
    rps_strat = [line for line in f]
    # r[0] is the opps move, r[2] is our move
    pts = 0
    for round in rps_strat:
        pts += cal_round_pts_2(round[0], round[2])
    print(pts)
        
    
    
