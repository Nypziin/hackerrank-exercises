if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    runner_up = min(arr)
    for num in arr:
        if num > runner_up and num != max(arr):
            runner_up = num

    print(runner_up)









