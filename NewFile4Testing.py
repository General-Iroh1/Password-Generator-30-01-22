with open("NewFileForTesting.txt",'r') as file:
    lines = file.readlines()

with open("NewFileForTesting.txt",'w') as file:
    for line in lines:
        # find() returns -1 if no match is found
        if line.find("diana") != -1:
            pass
        else:
            file.write(line)