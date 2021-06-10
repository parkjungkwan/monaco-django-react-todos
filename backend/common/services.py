import json

import pandas as pd
from models import DataTransferObject


class CommonService(object):

    dto = DataTransferObject()

    def print_dframe(self, this):
        print('*' * 100)
        print(f'1. Target type \n {type(this)} ')
        print(f'2. Target column \n {this.columns} ')
        print(f'3. Target 상위 1개 행\n {this.head()} ')
        print(f'4. Target null 의 갯수\n {this.isnull().sum()}개')
        print('*' * 100)

    def new_file(self) -> str:
        return self._context + self._fname

    def csv_to_dframe(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls_to_dframe(self, header, usecols) -> object:
        return pd.read_excel(self.new_file(), encoding='UTF-8', header=header, usecols=usecols)

    def json_to_dframe(self) -> object:
        return json.load(open(self.new_file(), encoding='UTF-8'))

    def create_gmaps(self):
        pass

