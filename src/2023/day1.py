from utils import TextParser

output = 0
with open("C:\\Users\\matty\\PycharmProjects\\AdventOfCode\\input\\2023\\day1", "r") as input:
    for line in input:
        #output += int(TextParser.leaveNumbers(line))
        print(TextParser.leaveNumbers(line))

print("Answer: " + str(output))

#TODO:Get first and last digit, not all digits