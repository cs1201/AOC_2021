import sys
import os
import shutil
import fileinput
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs

here = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.dirname(here)
blank_py_file = os.path.join(here, "day_X.py")
data_dir = os.path.join(target_dir, "data")

if len(sys.argv) < 2:
    print("No day number given")
    sys.exit()

# Create empty py file
day_number = sys.argv[1]

# Day Directory
day_dirname = f"Day_{day_number}"
day_dir = os.path.join(target_dir, day_dirname)
os.makedirs(day_dir)
assert(os.path.isdir(day_dir))
print(f"Created new directory: {day_dir}")

# Day file
new_py_file = os.path.join(day_dir, f"day_{day_number}.py")
shutil.copyfile(blank_py_file, new_py_file)
with fileinput.FileInput(new_py_file, inplace=True, backup='.bak')as py_file:
    for line in py_file:
        print(line.replace("day_X_input.txt", f"day_{day_number}_input.txt"), end='')
os.remove(os.path.join(day_dir, f"day_{day_number}.py.bak"))
print(f"Created new python file: {new_py_file}")

# Description file
base_url = "https://adventofcode.com/2021/day/"
day_url = f"{base_url}{day_number}"
r = requests.get(day_url)
if (r.status_code != 200):
    print("ERROR: Could not obtain problemn description info from AOC website")
else:
    data = bs(r.content, 'html.parser')
    description = data.find("article", class_="day-desc")

    description_file = os.path.join(day_dir, f"day_{day_number}_desc.txt")
    with open(description_file, "w+") as f:
        for line in description.get_text().splitlines():
            f.write(line + os.linesep)
    print(f"Created new problem description file: {description_file}")

# Create empty data .txt file
input_file = os.path.join(day_dir, f"day_{day_number}_input.txt")
open(input_file, "a").close
print(f"Created empty file for input data: {input_file}")

print("READY TO GO!")
