if __name__ == '__main__':
    n = int(raw_input())
    # raw_input() returns a string, split() makes it a list
    t = tuple(map(int, raw_input().split()))
    print hash(t)
