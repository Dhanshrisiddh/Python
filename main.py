import os

if(not os.path.exists("data")):
    os.mkdir("data")              # Create a directory named "data"


# for i in range(0,100):              # Create 100 directories named "Day1", "Day2", ..., "Day100"
#     os.mkdir(f"data/Day{i+1}")       # The f-string is used to format the string with the current value of i


# os.mkdir("Dhanshree")                     
# os.rename(f"Tutorials",f"Dhanshree ")   # Rename the directory "Sanikaa" to "Tutorials"    