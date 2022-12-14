import pickle

bfilename = 'd:/bbb/test.bin'
tfilename = 'd:/bbb/test.txt'

data1 = 77
data2 = "Hello, World!"
data3 = ["car","apple","house"]

with open(bfilename, "wb") as f:
    pickle.dump(data1,f)
    pickle.dump(data2,f)
    pickle.dump(data3,f)

with open(tfilename, "wt") as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))
    f.write('\n')

with open(bfilename, 'rb') as f:
    b = pickle.load(f)
    print(type(b), ' Binary Read1 | ', b)
    b = pickle.load(f)
    print(type(b), ' Binary Read2 | ', b)
    b = pickle.load(f)
    print(type(b), ' Binary Read3 | ', b)

with open(tfilename, 'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), 'Text Read' + str(i) + '|', line, end='')
