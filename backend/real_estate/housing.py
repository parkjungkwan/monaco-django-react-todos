from real_estate.dataset import Dataset
import pandas as pd
class Housing(object):
    dataset = Dataset()

    # DF 생성하기
    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname + '.xlsx', sheet_name='평균전세')

    #

    # 시-도