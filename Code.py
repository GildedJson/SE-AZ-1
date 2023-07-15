def main():
    q = input('Ask a math question')
    splitq = q.split(' ')
    if splitq[1] == '+':
        print (int(splitq[0]) + int(splitq[2]))


if __name__ == '__main__':
    main()