with open("NewFile4Testing.txt", "rt") as fin:
    with open("out.txt", "wt") as fout:
        for line in fin:
            fout.write(line.replace("python", "\n"))