import sys

import pandas as pd
from halo import Halo

from core.choose_excel_file import choose_excel_file, show_info
from core.pars_input_chrome import login_user
from core.pars_input_chrome import test_args

if __name__ == "__main__":

    print(

        r"""
        
        _     ____   ____    ___   _      _   _  _____         ____      _     ____   ____
       / \   | __ ) / ___|  / _ \ | |    | | | ||_   _|       |  _ \    / \   |  _ \ / ___|
      / _ \  |  _ \ \___ \ | | | || |    | | | |  | |   _____ | |_) |  / _ \  | |_) |\___ \
     / ___ \ | |_) | ___) || |_| || |___ | |_| |  | |  |_____||  __/  / ___ \ |  _ <  ___) |
    /_/   \_\|____/ |____/  \___/ |_____| \___/   |_|         |_|    /_/   \_\|_| \_\|____/
    
    
        """
    )
    excel_file_path = choose_excel_file()

    if not excel_file_path:
        print("Файл не выбран. Программа завершается.")
        sys.exit()
    else:
        spinner = Halo(text='Загрузка', spinner='dots')
        spinner.start()
        df = pd.read_excel(excel_file_path)
        spinner.stop()
        spinner.start()
        login_user()
        spinner.stop()

        test_args(df)
        show_info()

        input("Импорт выполнен! Можете закрыть консоль или нажать 'ENTER'")
