path = 'baseball_100_627.csv'

def main():
    dic = {}
    with open(path) as f:
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

if __name__ == '__main__':
    main()