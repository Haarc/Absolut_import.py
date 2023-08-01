from core.choose_excel_file import choose_excel_file
from core.pars_input_chrome import test_args
from core.pars_input_chrome import login_user
import pandas as pd

if __name__ == "__main__":
    print('ВЫБЕРИТЕ ФАЙЛ ДЛЯ ЗАГРУЗКИ ТОВАРОВ:".XLSX"')
    # Вызываем функцию для выбора файла Excel через диалоговое окно
    excel_file_path = choose_excel_file()

    if not excel_file_path:
        print("Файл не выбран. Программа завершается.")
    else:
        # Загружаем данные из файла Excel в DataFrame

        df = pd.read_excel(excel_file_path)


        # Вызываем функцию test_args и передаем DataFrame с данными
        login_user()
        test_args(df)

        input("Импорт выполнен, для закрытия консоли нажмите 'ENTER'")
