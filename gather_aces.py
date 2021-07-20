read_path = 'baseball_100_627.csv'
write_path = 'out_aces.csv'

def main():
    dic = {}
    with open(read_path) as f:
        _ = f.readline()
        for line in f:
            batter, pitcher, res = line.rstrip().split(",")
            res = int(res)

            # box = 0
            bat = 0
            hit = 0
            if res > 0:
                bat += 1
            if res > 1:
                hit += 1

            if batter not in dic:
                dic[batter] = {pitcher: [bat, hit]}
            else:
                b = dic[batter]
                if pitcher not in b:
                    b[pitcher] = [bat, hit]
                else:
                    b[pitcher][0] += bat
                    b[pitcher][1] += hit

    print(dic)

    with open(write_path, mode='w') as f:
        f.writelines("no, from, to, weight\n")
        i = 0
        res = {}
        for b in dic:
            pitchers = []
            for p in dic[b]:
                if dic[b][p][0]> 3 and dic[b][p][1]/dic[b][p][0] < 0.3:
                    pitchers.append(p)

            for k in range(len(pitchers)):
                for l in range(k+1, len(pitchers)):
                    d = sorted([pitchers[k], pitchers[l]])
                    if d[0] not in res:
                        res[d[0]] = {d[1]: 1}
                    else:
                        r = res[d[0]]
                        if d[1] not in r:
                            r[d[1]] = 1
                        else:
                            r[d[1]] += 1

        for node1 in res:
            for node2 in res[node1]:
                m = str(i) + ", " + str(node1) + ", " + str(node2) + ", " + str(res[node1][node2]) + "\n"
                f.writelines(m)
                i += 1

if __name__ == '__main__':
    main()