from common.models import FileDTO
from common.services import Printer, Reader
from common.abstracts import ReaderBase


class CrimeService(ReaderBase):

    def csv(self, payload):
        printer = Printer()
        reader = Reader()
        file = FileDTO()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.csv(file))

    def xls(self):
        pass

    def json(self):
        pass

    def new_file(self):
        pass

    # 추상클래스에 정의되지 않은 추가 메소드 
    def test(self):
        pass





