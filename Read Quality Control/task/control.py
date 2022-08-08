def read_data():
    fn = input()
    # fn = 'test.fastq'
    with open(fn, 'r') as f:
        lines = f.read().split('\n')
    return lines[:4]

data = read_data()
for i in range(4):
    print(data[i])
