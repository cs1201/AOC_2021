#include <iostream>
#include <fstream>
#include <vector>
#include <string>

typedef struct instruction_t
{
    std::string direction;
    int         magnitude;
}instruction_t;

unsigned int part_1(std::vector<instruction_t> data)
{
    unsigned int x = 0, y = 0;
    for(auto const& instruction: data)
    {
        if (!instruction.direction.compare("forward"))
        {
            x += instruction.magnitude;
        }
        else if (!instruction.direction.compare("up"))
        {
            y -= instruction.magnitude;
        }
        else if (!instruction.direction.compare("down"))
        {
            y += instruction.magnitude;
        }
    }
    return x*y;
}

int part_2(std::vector<instruction_t> data)
{
    unsigned int x = 0, y = 0, a = 0;
    for(auto const& instruction: data)
    {
        if (!instruction.direction.compare("forward"))
        {
            x += instruction.magnitude;
            y += instruction.magnitude * a;
        }
        else if (!instruction.direction.compare("up"))
        {
            a -= instruction.magnitude;
        }
        else if (!instruction.direction.compare("down"))
        {
            a += instruction.magnitude;
        }
    }
    return x*y;
}

int main()
{
    std::string input_filename = "./day_2_input.txt";
    std::ifstream input(input_filename); 
    std::vector<instruction_t> data;

    for(std::string line; getline(input, line);)
    {   
        int split_point = line.find(" ");
        instruction_t ins = { line.substr(0, split_point), std::stoi(line.substr(split_point+1, line.size()))};
        data.push_back(ins);
    }

    std::cout << "Part 1: " << part_1(data) << std::endl;
    std::cout << "Part 2: " << part_2(data) << std::endl;

}