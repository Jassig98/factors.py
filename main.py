# Author: Jasmine Singh
# Github username: Jassig98
# Date: October 12, 2022
# Description: Project 3B

num_1=int(input("Please enter a positive integer:"))
print("The factors of" ,num_1, "are:")
for i in range(1,num_1+1):
    if(num_1%i==0):
        print(i)


