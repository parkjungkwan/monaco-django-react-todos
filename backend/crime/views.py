from crime.services import CrimeService

class Crime_API(object):

    @staticmethod
    def main():
        util = CrimeService()
        while 1:
            menu = input('0-Exit\n1-서울CCTV DF\n2-서울범죄 DF\n'
                             '3-경찰서위치 DF\n4-실업율 DF\n5-엑셀POP')
            if menu == '0':
                break
            elif menu == '1':
                this = util.new_model_csv('cctv_in_seoul')
                util.print_dframe(this)
            elif menu == '2':
                this = util.new_model_csv('crime_in_seoul')
                util.print_dframe(this)
            elif menu == '3':
                this = util.new_model_csv('police_position')
                util.print_dframe(this)
            elif menu == '4':
                this = util.new_model_csv('us_unemployment')
                util.print_dframe(this)
            elif menu == '5':
                this = util.new_model_exel('pop_in_seoul')
                util.print_dframe(this)
            else:
                continue

Crime_API.main()