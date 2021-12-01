#include <iostream>
#include <fstream>
#include <vector>

int part_1(std::vector<int> data)
{
    int count = 0;

    for(std::size_t i = 1; i < data.size(); ++i) {
        if (data[i] > data[i - 1])
        {
            count += 1;
        }
    }
    return count;
}

int part_2(std::vector<int> data)
{
    int count = 0;
    
    for(std::size_t i = 3; i < data.size(); ++i) {
        if (data[i] > data[i - 3])
        {
            count += 1;
        }
    }
    return count;
}

int main()
{
    std::string input_filename = "./day_1_input.txt";
    std::ifstream input(input_filename); 
    std::vector<int> data;

    for(std::string line; getline(input, line);)
    {   
        data.push_back(std::stoi(line));
    }

    std::cout << "Part 1: " << part_1(data) << std::endl;
    std::cout << "Part 2: " << part_2(data) << std::endl;

}