files = []
def merge_files(file_names):
    sorted_files = sorted(((name, len(open(name, encoding='utf-8').readlines()))for name in file_names), key=lambda x: x[1])

    with open("result.txt", "w") as result_file:
        for file_name, line_count in sorted_files:
            file = open(file_name, 'r')
            result_file.write(f'Имя файла: {file_name}\n')
            result_file.write(f'Количество строк: {line_count}\n')
            result_file.write(file + '\n\n')