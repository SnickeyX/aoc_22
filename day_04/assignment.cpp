#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

// a bit ugly but space efficient
int overlap(std::vector<int> bounds, bool complete_overlap_only = false)
{
    int a = bounds[0], b = bounds[1], c = bounds[2], d = bounds[3];
    if(c >= a && d <= b) {
        return 1;
    } else if (a >= c && b <= d) {
        return 1;
    // for complete overlap only, we stop looking here
    } else if (complete_overlap_only) {
        return 0;                     
    } else if (b >= c && b <= d) {
        return 1;
    } else if (a >= c && a <= d) {
        return 1;
    } else if (c >= a && c <= b) {
        return 1;
    } else if( d >= a && d <= b) {
        return 1;
    } else {
        return 0; 
    } 
}
 
int main() 
{
    std::ifstream myFile ("assignment.txt");
    std::string segment;
    // should be array - could refactor later
    std::vector<int> numbers;
    if(myFile.is_open()) 
    {
        int total_complete_overlaps = 0;
        int num_any_overlaps = 0;
        while(std::getline(myFile, segment)) 
        {
            // quite hacky, but does the job
            std::replace(segment.begin(), segment.end(), ',' , ' ');
            std::stringstream ss(segment);
            for(int i = 0; ss >> i; ) {
                numbers.push_back(abs(i)); 
            }
            total_complete_overlaps += overlap(numbers, true); 
            num_any_overlaps += overlap(numbers);
            // clearning for next set of numbers
            numbers.clear();
        }
        printf("total overlap: %d\n", total_complete_overlaps);
        printf("num any overlap: %d\n", num_any_overlaps);
    
    }
    myFile.close();
    return 0; 
}