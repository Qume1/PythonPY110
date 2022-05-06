OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as file_:
        for count_aster in range(1, 11):
            file_.write(f"{count_aster * '*':>10}\n")  # TODO записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
