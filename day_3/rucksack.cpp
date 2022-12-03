#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

// TODO: Clean this when I get time - lots of repeated code

std::set<char> find_common_elem(std::string str1, std::string str2) 
{
    std::set<char> str1_set; 
    std::set<char> str2_set; 
    std::set<char> common_set;
    for(char c : str1) 
    {
        str1_set.insert(c);
    }
    for (char c : str2) 
    {
        str2_set.insert(c);
    }
    std::set_intersection(str1_set.begin(), str1_set.end(), str2_set.begin(), str2_set.end(), std::inserter(common_set, common_set.begin()));
    return common_set;
}

std::set<char> find_common_three(std::string s1, std::string s2, std::string s3) 
{
    std::set<char> common_set  = find_common_elem(s1, s2);
    std::set<char> common_set2 = find_common_elem(s1, s3);
    std::set<char> common_set3 = find_common_elem(s2, s3);
    std::set<char> common_set4;
    std::set_intersection(common_set.begin(), common_set.end(), common_set2.begin(), common_set2.end(), std::inserter(common_set4, common_set4.begin()));
    std::set<char> common_set5;
    std::set_intersection(common_set3.begin(), common_set3.end(), common_set4.begin(), common_set4.end(), std::inserter(common_set5, common_set5.begin()));
    return common_set5; 
}

int calculate_pts(int orded_char) 
{
    int pts = 0; 
    if(orded_char >= 97 && orded_char <= 122) 
    {
        pts = orded_char % 96; 
    } else if (orded_char >= 65 && orded_char <= 90) 
    {
        pts = orded_char % 64 + 26; 
    }
    return pts; 
}
 

int main() 
{
    std::ifstream myFile ("rucksack.txt");
    std::string line;
    std::vector<std::string> all; 
    int chall_num = 2;
    if(myFile.is_open()) 
    {
        int total_pts = 0;; 
        while(std::getline(myFile, line)) 
        {
            if(chall_num == 1) 
            {
                int string_len = line.length();
                std::string s1 = line.substr(0, string_len/2);
                std::string s2 = line.substr(string_len/2, string_len);
                std::set<char> com = find_common_elem(s1, s2);
                int common = int(*com.begin());
                total_pts += calculate_pts(common);
            } else 
            {
                all.push_back(line);
            }
            
        }
        if(chall_num == 2)
        {
            for(int i = 0; i < all.size(); i+=3) 
            {
                std::set<char> com = find_common_three(all[i], all[i+1], all[i+2]);
                int common = int(*com.begin());
                total_pts += calculate_pts(common);
            }
        }
        printf("the total points are %d\n", total_pts);
    }
    myFile.close();

    return 0; 
}