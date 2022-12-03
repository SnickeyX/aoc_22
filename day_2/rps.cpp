#include <fstream>

int calculate_total_pts_1(int opp_mv, int my_mv)
{
    // 1,2,3 for rock, papers and scissors
    int opp_ord_mv = opp_mv % 64;
    int my_ord_mv  = my_mv % 87;
    // x,y,z are worth 1,2,3 pts in that order
    int total_pts = my_ord_mv;
    if( (my_ord_mv % 3) == (1 + opp_ord_mv) % 3)
    {
        total_pts += 6;
    }
    else if( opp_ord_mv == my_ord_mv )
    {
        total_pts += 3;
    }
    else
    {
        total_pts += 0;
    }
    return total_pts;
}

int calculate_total_pts_2(int opp_mv, int my_mv)
{
    // 1,2,3 for rock, papers and scissors
    int opp_ord_mv = opp_mv % 64;
    int my_ord_mv  = my_mv % 88;
    // lose = 0, draw = 3, win = 6
    int total_pts = my_ord_mv * 3; 
    if(!my_ord_mv) 
    {
        total_pts += opp_ord_mv == 1 ? 3 : (opp_ord_mv - 1) % 3;
    } 
    else if (my_ord_mv == 1)
    {
        total_pts += opp_ord_mv; 
    } 
    else 
    {
        total_pts += opp_ord_mv == 2 ? 3 : (opp_ord_mv + 1) % 3;
    }
    return total_pts;
}

int main() 
{
    std::ifstream myFile ("rps.txt");
    std::string line;
    int total_score; 
    if(myFile.is_open()) 
    {
        // collects the ascii version
        char a,b; 
        while(myFile >> a >> b) 
        {
            total_score += calculate_total_pts_2(int(a),int(b));
        }
        printf("Total score: %d", total_score);
    }
    myFile.close();

    return 0; 
}