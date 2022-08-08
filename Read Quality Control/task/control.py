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
            l_cnt = dic.get(l, 0)
            dic[l] = l_cnt + 1
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


stage2()
