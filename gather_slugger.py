path = 'baseball_100_627.csv'

def main():
    with open(path) as f:
        _ = f.readline()
        for line in f:
            print(line)

if __name__ == '__main__':
    main()