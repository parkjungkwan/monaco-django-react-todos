from common.models import DataTransferObject
import pandas as pd
import xlwings as xw


class HousingService(object):
    dto = DataTransferObject()

    # DF 생성하기
    def new_model(self, payload):

        this = self.dto
        this.context = './data/'
        this.fname = payload
        '''
        df = pd.read_excel(this.context + this.fname + '.xlsx', sheet_name='매매종합')
        '''
        sheet = xw.Book(this.context + payload + '.xlsx').sheets['매매종합']
        row_num = sheet.range(1,1).end('down').end('down').end('down').row
        data_range = 'A2:GE' + str(row_num)
        df = sheet[data_range].options(pd.DataFrame, index=False, header=True).value
        return df

    @staticmethod
    def import_data_make_list(this):
        sido = list(this.columns)
        gugun = list(this.iloc[0])
        return {sido, gugun}

    @staticmethod
    def remove_none_in_gugun(this):

        for i, j in enumerate(gugun):
            if j == None:
                gugun[i] = sido[i]
        bignames = '서울 대구 부산 대전 광주 인천 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주도 6개광역시 5개광역시 수도권 기타지방 구분 전국'
        bigname_list = bignames.split(' ')
        sido_col = list(this.columns)
        gugun_col = list(this.iloc[0])

        for num, gu_data in enumerate(gugun_col):
            if gu_data == None:
                gugun_col[num] = sido_col[num]

            check = num
            while True:
                if sido_col[check] in bigname_list:
                    sido_col[num] = sido_col[check]
                    break
                else:
                    check = check - 1
        # [예제 2.6] small_col, big_col 예외 부분 수정하기

        sido_col[129] = '경기'
        sido_col[130] = '경기'
        gugun_col[185] = '서귀포'

        # [예제 2.7] 새로운 컬럼 입력하기

        this.columns = [sido_col, gugun_col]
        new_col_data = this.drop([0, 1])
        return new_col_data

    @staticmethod
    def date_list_for_index(this):

        print('[예제 2.9] 인덱스를 위한 날짜 리스트 만들기')

        index_list = list(this['구분']['구분'])

        new_index = []

        for num, raw_index in enumerate(index_list):
            temp = str(raw_index).split('.')
            if int(temp[0]) > 12:
                if len(temp[0]) == 2:
                    new_index.append('19' + temp[0] + '.' + temp[1])
                else:
                    new_index.append(temp[0] + '.' + temp[1])
            else:
                new_index.append(new_index[num - 1].split('.')[0] + '.' + temp[0])

        # [예제 2.10] 만들어진 날짜 리스트를 인덱스로 설정

        new_col_data.set_index(pd.to_datetime(new_index), inplace=True)
        cleaned_data = new_col_data.drop(('구분', '구분'), axis=1)

        # [예제 2.11] 전처리 함수화

        def KBpriceindex_preprocessing(path, data_type):
            # path : KB 데이터 엑셀 파일의 디렉토리 (문자열)
            # data_type : ‘매매종합’, ‘매매APT’, ‘매매연립’, ‘매매단독’, ‘전세종합’, ‘전세APT’, ‘전세연립’, ‘전세단독’ 중 하나

            wb = xw.Book(path)
            sheet = wb.sheets[data_type]
            row_num = sheet.range(1, 1).end('down').end('down').end('down').row
            data_range = 'A2:GE' + str(row_num)
            raw_data = sheet[data_range].options(pd.DataFrame, index=False, header=True).value

            bignames = '서울 대구 부산 대전 광주 인천 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주도 6개광역시 5개광역시 수도권 기타지방 구분 전국'
            bigname_list = bignames.split(' ')
            big_col = list(raw_data.columns)
            small_col = list(raw_data.iloc[0])

            for num, gu_data in enumerate(small_col):
                if gu_data == None:
                    small_col[num] = big_col[num]

                check = num
                while True:
                    if big_col[check] in bigname_list:
                        big_col[num] = big_col[check]
                        break
                    else:
                        check = check - 1

            big_col[129] = '경기'
            big_col[130] = '경기'
            small_col[185] = '서귀포'

            raw_data.columns = [big_col, small_col]
            new_col_data = raw_data.drop([0, 1])

            index_list = list(new_col_data['구분']['구분'])

            new_index = []

            for num, raw_index in enumerate(index_list):
                temp = str(raw_index).split('.')
                if int(temp[0]) > 12:
                    if len(temp[0]) == 2:
                        new_index.append('19' + temp[0] + '.' + temp[1])
                    else:
                        new_index.append(temp[0] + '.' + temp[1])
                else:
                    new_index.append(new_index[num - 1].split('.')[0] + '.' + temp[0])

            new_col_data.set_index(pd.to_datetime(new_index), inplace=True)
            cleaned_data = new_col_data.drop(('구분', '구분'), axis=1)
            return cleaned_data

            # [예제 2.12] 전처리 함수 사용 예제

            # [예제 2.13] matplotlib 불러오고 한글폰트 설정
            import matplotlib.pyplot as plt
            from matplotlib import font_manager, rc


            font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
            rc('font', family=font_name)
            # 맥OS 인 경우 위 두 줄을 입력하지 말고 아래 코드를 입력하세요
            # rc('font', family='AppleGothic')
            plt.rcParams['axes.unicode_minus'] = False

            # [예제 2.14] 종합 매매가격 지수 그래프 그리기
            path = r' 여러분이 받은 파일의 디렉터리를 넣으세요 \ KB엑셀 파일명.xls'
            data_type = '매매종합'
            new_data = KBpriceindex_preprocessing(path, data_type)
            new_data['전국']['전국'].plot(legend='전국')
            plt.show()

            # [예제 2.15] 특정 지역에 원하는 시간대의 데이터를 가져와 그래프 그리기

            new_data['전국']['전국']['2008-01':].plot(legend='전국')
            plt.show()

            # [예제 2.16] subplot을 이용해 서울과 대구 그래프 그리기

            plt.figure(figsize=(10, 5))

            plt.subplot(1, 2, 1)
            plt.title('서울')
            plt.plot(new_data['서울']['서울']['2008-01':])

            plt.subplot(1, 2, 2)
            plt.title('대구')
            plt.plot(new_data['대구']['대구']['2008-01':])

            plt.show()

            # [예제 2.17] for 문을 이용해 여러 개의 subplot을 그리는 코드

            spots = '전국 서울 대구 부산'
            start_date = '2008-1'
            spot_list = spots.split(' ')
            num_row = int((len(spot_list) - 1) / 2) + 1

            plt.figure(figsize=(10, num_row * 5))
            for i, spot in enumerate(spot_list):
                plt.subplot(num_row, 2, i + 1)
                plt.title(spot)
                plt.plot(new_data[spot][spot][start_date:])

            plt.show()

            # [예제 2.18] 시-도 안의 구 지역 가격지수까지 subplot으로 그래프 그리기

            spots = '서울 서울,마포구 서울,강남구 부산 경기'
            start_date = '2008-1'
            spot_list = spots.split(' ')
            num_row = int((len(spot_list) - 1) / 2) + 1

            plt.figure(figsize=(10, num_row * 5))
            for i, spot in enumerate(spot_list):
                plt.subplot(num_row, 2, i + 1)
                plt.title(spot)
                if ',' in spot:
                    si, gu = spot.split(',')
                else:
                    si = gu = spot
                plt.plot(new_data[si][gu][start_date:])

            plt.show()

            # [예제 2.19] 특정 날짜의 전 지역 가격지수 데이터 가져오기

            new_data.loc['2018-1-1']

            # [예제 2.20] 두 날짜 사이의 부동산 가격지수 증감률 구하기

            (new_data.loc['2018-1-1'] - new_data.loc['2016-1-1']) / new_data.loc['2016-1-1'] * 100

            # [예제 2.21] 가격지수 증감률 정렬하기

            diff = (new_data.loc['2018-1-1'] - new_data.loc['2016-1-1']) / new_data.loc['2016-1-1'] * 100
            diff.sort_values()

            # [예제 2.22] 누락된 지역 삭제 및 상위, 하위 10개만 출력

            diff = ((new_data.loc['2018-1-1'] - new_data.loc['2016-1-1']) / new_data.loc['2016-1-1'] * 100).dropna()
            print("하위 10개")
            print(diff.sort_values()[:10])
            print(' ')
            print("상위 10개")
            print(diff.sort_values(ascending=False)[:10])

            # [예제 2.23] 가격지수 증감률을 막대그래프로 시각화

            import numpy as np
            from matplotlib import style
            style.use('ggplot')

            fig = plt.figure(figsize=(13, 7))
            ind = np.arange(20)

            ax = fig.add_subplot(1, 3, 1)
            plt.title('2016.1~2018.1 가격 변화율 최하위 20')
            rects = plt.barh(ind, diff.sort_values()[:20].values, align='center', height=0.5)
            plt.yticks(ind, diff.sort_values()[:20].index)
            for i, rect in enumerate(rects):
                ax.text(0.95 * rect.get_width(),
                        rect.get_y() + rect.get_height() / 2.0,
                        str(round(diff.sort_values()[:20].values[i], 2)) + '%',
                        ha='left', va='center', bbox=dict(boxstyle="round", fc=(0.5, 0.9, 0.7), ec="0.1"))

            ax2 = fig.add_subplot(1, 3, 3)
            plt.title('2016.1~2018.1 가격 변화율 최상위 20')
            rects2 = plt.barh(ind, diff.sort_values()[-20:].values, align='center', height=0.5)
            plt.yticks(ind, diff.sort_values()[-20:].index)
            for i, rect in enumerate(rects2):
                ax2.text(0.95 * rect.get_width(),
                         rect.get_y() + rect.get_height() / 2.0,
                         str(round(diff.sort_values()[-20:].values[i], 2)) + '%',
                         ha='right', va='center', bbox=dict(boxstyle="round", fc=(0.5, 0.9, 0.7), ec="0.1"))

            plt.show()

            # [예제 2.24] 특정 지역만 선택해서 가격지수 증감률을 막대그래프로 시각화

            loca = '전국 서울 부산 경기 대구 광주 울산 대전'

            temp_list = loca.split(" ")
            loca_list = []
            for temp in temp_list:
                if ',' in temp:
                    temp_split = temp.split(",")
                    loca_list.append((temp_split[0], temp_split[1]))
                else:
                    loca_list.append((temp, temp))

            diff = ((new_data.loc['2018-1-1', loca_list] - new_data.loc['2016-1-1', loca_list]) / new_data.loc[
                '2016-1-1', loca_list] * 100).sort_values()

            num = len(loca_list)
            fig = plt.figure(figsize=(13, 7))
            ind = np.arange(num)

            ax = fig.add_subplot(1, 3, 1)
            plt.title('2016.1~2018.1 가격지수 변화율')
            rects = plt.barh(ind, diff.head(num).values, align='center', height=0.5)
            plt.yticks(ind, diff.head(num).index)
            for i, rect in enumerate(rects):
                ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height() / 2.0,
                        str(round(diff.head(20).values[i], 2)) + '%',
                        ha='left', va='center', bbox=dict(boxstyle="round", fc=(0.5, 0.9, 0.7), ec="0.1"))

            plt.show()



















    #

    # 시-도