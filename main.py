# This is just a Educational Projects, using this to brute force Gift Card codes is illegal and unethical.
#__  ______        _                      
#\ \/ / __ )  __ _| | __ _ _ __   ___ ___
# \  /|  _ \ / _` | |/ _` | '_ \ / __/ _ \
# /  \| |_) | (_| | | (_| | | | | (_|  __/
#/_/\_\____/ \__,_|_|\__,_|_| |_|\___\___/
# This is a simple script to generate Gift Card codes
# These are the Imports:
import random
# These are the Variables:
times = 99999
codes = []
# Now we will get to the main part of the code:


# !DISCLAIMER!
# This is not finished by far and Changes will be made in the future
# The script doesn't fulfill its purpose and I will have to change it later on.
# !DISCLAIMER!
zwichen = input("How many codes do you want to generate?")
if zwichen.isdigit():
    times = int(zwichen)
else:
    print("Please enter a valid number.")
    exit()
for i in range(times):
    code = ""
    for j in range(4):
        code += str(random.randint(0, 9))
        if j < 3:
            code += "-"
    codes.append(code)
print(f"Generated codes:\n {len(codes)}")
