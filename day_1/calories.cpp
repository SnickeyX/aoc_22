#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

int main() 
{
    std::ifstream myFile ("calories.txt");
    std::string line;
    std::vector<int> calories;
    if(myFile.is_open()) 
    {
        int curr_cal_count; 
        while(std::getline(myFile, line)) 
        {
            if(line.empty())
            {
                printf("yo line empty\n");
                calories.push_back(curr_cal_count);
                curr_cal_count = 0;
            } else 
            {
                printf("heres the string yo %d\n", std::stoi(line));
                curr_cal_count += std::stoi(line);
            }
        }
        calories.push_back(curr_cal_count);
        std::nth_element(calories.begin(), calories.begin()+1, calories.end(), std::greater{});
        printf("the three highest calorie days are %d, %d, and %d\n", calories[0], calories[1], calories[2]);
        printf("their sum is %d\n", calories[0] + calories[1] + calories[2]);


    }
    myFile.close();

    return 0; 
}