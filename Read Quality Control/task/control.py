def read_data():
    fn = input()
    # fn = 'test1.fastq'
    with open(fn, 'r') as f:
        lines = f.read().split('\n')
    return lines

def stage1():
    data = read_data()
    for i in range(4):
        print(data[i])

def stage2():
    data = read_data()
    r_cnt = 0
    i = 0
    dic = {}
    while i < len(data):
        if data[i][:4] == '@SRR':
            r_cnt += 1
            l = len(data[i + 1])
            dic[l] = dic.get(l, 0) + 1
            i += 4
        else:
            i += 1
    sum = 0
    n = 0
    print(f'Reads in the file = {r_cnt}:')
    for k in sorted(dic):
        sum += k * dic[k]
        n += dic[k]
        print(f'\twith length {k} = {dic[k]}')
    print(f'Reads sequence average length = {round(sum / n)}')

def stage3():
    data = read_data()
    n = 0
    k = 0
    r_cnt = 0
    i = 0
    while i < len(data):
        if data[i][:4] == '@SRR':
            dna = data[i + 1]
            n += len(dna)
            gc = dna.count('G') + dna.count('C')
            k += gc / len(dna)
            r_cnt += 1
            i += 4
        else:
            i += 1
    print(f'Reads in the file = {r_cnt}:')
    print(f'Reads sequence average length = {round(n / r_cnt)}')
    print(f'GC content average = {round(100 * k / r_cnt, 2)}%')


stage3()
