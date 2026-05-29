import file1_1var
import file2_1var
import file3_1var


def main():
    choose = int(input('Первый: 0, Второй: 1, Третий: 2'))
    match choose:
        case 0:
            file1_1var.main()
        case 1:
            file2_1var.main()
        case 2:
            file3_1var.main()
        case _:
            print('Неверное значение')

if __name__ == '__main__':
     main()