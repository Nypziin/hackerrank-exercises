if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    runner_up = max([i for i in arr if i != max(arr)])

    print(runner_up)










