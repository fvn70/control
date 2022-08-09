def read_data():
    fn = input()
    # fn = 'test/test1.fastq'
    # fn = 'srr16506265_1.fastq'
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

def stage4():
    data = read_data()
    i = 0
    dic = {}
    while i < len(data):
        if data[i][:4] == '@SRR':
            dna = data[i + 1]
            dic[dna] = dic.get(dna, 0) + 1
            i += 4
        else:
            i += 1
    n = 0
    r = 0
    for k, v in dic.items():
        n += len(k) * v
        gc = k.count('G') + k.count('C')
        r += gc / len(k) * v

    cnt = sum(dic.values())
    rep = sum([v - 1 for v in dic.values() if v > 1])
    print(f'Reads in the file = {cnt}:')
    print(f'Reads sequence average length = {round(n / cnt)}')
    print(f'Repeats = {rep}')
    print(f'GC content average = {round(100 * r / cnt, 2)}%')

def stage5():
    data = read_data()
    i = 0
    dic = {}
    while i < len(data):
        if data[i][:4] == '@SRR':
            dna = data[i + 1]
            dic[dna] = dic.get(dna, 0) + 1
            i += 4
        else:
            i += 1
    cnt_ch = 0
    r_n = 0
    r_gc = 0
    num_n = 0
    for k, v in dic.items():
        cnt_ch += len(k) * v
        cnt_n = k.count('N')
        if cnt_n > 0:
            num_n += v
            r_n += cnt_n / len(k) * v
        gc = k.count('G') + k.count('C')
        r_gc += gc / len(k) * v

    cnt = sum(dic.values())
    rep = sum([v - 1 for v in dic.values() if v > 1])
    print(f'Reads in the file = {cnt}:')
    print(f'Reads sequence average length = {round(cnt_ch / cnt)}')
    print(f'Repeats = {rep}')
    print(f'Reads with Ns = {num_n}')
    print(f'GC content average = {round(100 * r_gc / cnt, 2)}%')
    print(f'Ns per read sequence = {round(100 * r_n / cnt, 2)}%')


stage5()
