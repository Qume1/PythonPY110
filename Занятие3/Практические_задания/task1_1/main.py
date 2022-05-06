def task():
    # filename = r"C:\Users\semyo\PycharmProjects\PythonPY110\Занятие3\Практические_задания\task1_1\input.txt"
    filename = "input.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            # line = line.strip()
            print(line, end="")


if __name__ == "__main__":
    task()
