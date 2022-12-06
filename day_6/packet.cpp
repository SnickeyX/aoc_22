#include <fstream>
#include <string>

bool is_unique_str(std::string str)
{
    // 32 bits - enough for 26 letters
    // props to geeks4geeks for this idea
    int checker = 0;
    for (int i = 0; i < str.length(); i++) {
 
        int bits_at_index = str[i] - 'a';
        if ((checker & (1 << bits_at_index)) > 0) {
            return false;
        }
        checker = checker | (1 << bits_at_index);
    }
    return true;
}

int find_index_of_unique_seq(std::string s, int num_unique_len)
{
    for(int i = 0; i < s.length() - num_unique_len; i++) {
        std::string sub = s.substr(i, num_unique_len);
        if(is_unique_str(sub)) {
            return i + num_unique_len;
        }
    }
    // if no consec unique substr found
    return -1; 
}

int main() 
{
    std::ifstream myFile ("packet.txt");
    std::string segment;
    if(myFile.is_open()) 
    {
        // set to 4 for part 1 and 14 for part 2
        int num_consecutive_chars = 14;
        int index; 
  
        while(std::getline(myFile, segment)) 
        {
            index = find_index_of_unique_seq(segment, num_consecutive_chars);
        }
        if(index != -1) 
        {
            printf("index of the end of consec seq is: %d\n", index);
        } 
        else {
            printf("no consec unique substr found\n");
        }
    }
    myFile.close();
    return 0; 
}