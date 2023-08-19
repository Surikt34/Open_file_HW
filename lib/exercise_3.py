file_names = ["1.txt", "2.txt", "3.txt"]
file_data = []

# Считываем данные из файлов и храним их в списке вместе с количеством строк и именем файла
for file_name in file_names:
    with open(file_name, "r") as file:
        lines = file.readlines()
        file_data.append((file_name, len(lines), lines))

# Сортируем список на основе количества строк
file_data.sort(key=lambda x: x[1])

# Записываем данные в результирующий файл
with open("result.txt", "w") as result_file:
    for data in file_data:
        result_file.write(f"{data[0]}\n")
        result_file.write(f"{data[1]}\n")
        result_file.writelines(data[2])

with open('result.txt') as f:
    print(f.read())