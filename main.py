# This is just a Educational Projects, using this to brute force Gift Card codes is illegal and unethical.
#__  ______        _                      
#\ \/ / __ )  __ _| | __ _ _ __   ___ ___
# \  /|  _ \ / _` | |/ _` | '_ \ / __/ _ \
# /  \| |_) | (_| | | (_| | | | | (_|  __/
#/_/\_\____/ \__,_|_|\__,_|_| |_|\___\___/
# This is a simple script to generate Gift Card codes
# These are the Imports:
import random
import string
# The variables:
codes = []
zwichen = 0
# This script generates random Gift Card codes in the format XXXX-XXXX-XXXX
times = 0
# Number of codes to generate
zwichen = input("How many codes do you want to generate? \n")
# Check if the input is a digit:
if zwichen.isdigit(): 
    times = int(zwichen)
else:
    print("Please enter a valid number.")
    exit()
# Main part of the code:
codes = []
for _ in range(times):
    code = ""
    for group in range(3):  # 3 groups
        part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        code += part
        if group < 2:
            code += "-"
    codes.append(code)

print(f"Generated codes ({len(codes)}):")
for c in codes:
    print(c)

# !DISCLAIMER!
# This Script is for educational purposes only.
# Using this script to brute force Gift Card codes is illegal and unethical.
# I am not responsible for any misuse of this script, as i do not condone or support any illegal activities.
# The inputting of the codes is not even included in this script.
# Even if you ust this to generate codes, you most probably wont be able to brute force one, as the codes are too long and complex.
# !DISCLAIMER!
