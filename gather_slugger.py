read_path = 'baseball_100_627.csv'
write_path = 'out_slugger.csv'

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

            if pitcher not in dic:
                dic[pitcher] = {batter: [bat, hit]}
            else:
                p = dic[pitcher]
                if batter not in p:
                    p[batter] = [bat, hit]
                else:
                    p[batter][0] += bat
                    p[batter][1] += hit

    print(dic)

    with open(write_path, mode='w') as f:
        f.writelines("no, from, to, weight\n")
        i = 0
        res = {}
        for p in dic:
            batters = []
            for b in dic[p]:
                if dic[p][b][0]> 3 and dic[p][b][1]/dic[p][b][0] > 0.3:
                    batters.append(b)

            for k in range(len(batters)):
                for l in range(k+1, len(batters)):
                    d = sorted([batters[k], batters[l]])
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