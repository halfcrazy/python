if __name__ == '__main__':
    d = {}
    with open('in.txt', 'r') as f:
        text = ''.join(f.readlines())
        for word in text.split():
            if word in d.keys():
                d[word] = d[word] + 1
            else:
                d[word] = 1
    print d
