import uuid


if __name__ == '__main__':
    with open('result.txt', 'w') as f:
        for i in range(200):
            code = str(uuid.uuid4()).replace('-','')[:13]
            f.write(code + '\n')
