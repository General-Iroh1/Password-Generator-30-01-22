f = open("PrintingAndDeleting.txt", "a+")
f.write(("Test\n")*10)
with open('PrintingAndDeleting.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('PrintingAndDeleting.txt', 'w') as fout:
    fout.writelines(data[7:])