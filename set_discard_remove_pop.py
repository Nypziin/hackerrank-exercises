if __name__ == '__main__':
    n = int(input())
    data = set(map(int, input().split()))

    num_commands = int(input())
    for i in range(num_commands):
        command = input().split()
        try:
            if command[0] == 'pop':
                data.pop()
            elif command[0] == 'remove':
                data.remove(int(command[1]))
            else:
                data.discard(int(command[1]))
        except:
            continue

    print(sum(data))

