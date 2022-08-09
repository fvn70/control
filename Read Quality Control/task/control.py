import gzip

def read_gzip(fn):
    fn = input()
    with gzip.open(fn, 'r') as f:
        lines = f.read().decode('utf8').split('\n')
    return lines

def read_data():
    # fn = input()
    fn = 'test/test1.fastq'
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
    rez = proc_data(data)
    print(f'Reads in the file = {rez[0]}:')
    print(f'Reads sequence average length = {rez[1]}')
    print(f'Repeats = {rez[2]}')
    print(f'Reads with Ns = {rez[3]}')
    print(f'GC content average = {rez[4]}%')
    print(f'Ns per read sequence = {rez[5]}%')

def stage6():
    rez = []
    for i in range(3):
        fn = f'test/data{i + 1}.gz'
        data = read_gzip(fn)
        r = proc_data(data)
        rez.append(r)
    rez_list = [rez[0][3], rez[1][3], rez[2][3]]
    best = min(rez_list)
    best_i = rez_list.index(best)
    print(f'Reads in the file = {rez[best_i][0]}:')
    print(f'Reads sequence average length = {rez[best_i][1]}')
    print(f'Repeats = {rez[best_i][2]}')
    print(f'Reads with Ns = {rez[best_i][3]}')
    print(f'GC content average = {rez[best_i][4]}%')
    print(f'Ns per read sequence = {rez[best_i][5]}%')

def proc_data(data):
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
    aver_len = round(cnt_ch / cnt)
    rep = sum([v - 1 for v in dic.values() if v > 1])
    aver_gc = round(100 * r_gc / cnt, 2)
    aver_n = round(100 * r_n / cnt, 2)

    return [cnt, aver_len, rep, num_n, aver_gc, aver_n]

stage6()
