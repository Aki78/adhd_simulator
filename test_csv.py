array = []
sub_array = []
sub_sub_array = []

with open('test.csv') as f:
    for line in f:
        if line == "\n":
            array.append(sub_array)
            sub_sub_array = []
            sub_array = []
            continue
        for x in line.split():
            sub_sub_array.append(x)
        sub_array.append(sub_sub_array)
        sub_sub_array = []
        

print(array)
