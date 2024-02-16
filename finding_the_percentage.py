if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average = [sum(v) / len(v) for k, v in student_marks.items() if k == query_name]
    print(f'{average[0]:.2f}')
