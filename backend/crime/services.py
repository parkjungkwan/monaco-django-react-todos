from common.models import FileDTO
from common.services import Printer, Reader


class CrimeService(Printer, Reader):

    def show_file(self, payload):
        printer = Printer()
        reader = Reader()
        file = FileDTO()
        file.context = payload.get('context')
        file.fname = payload.get('fname')
        printer.dframe(reader.csv(file))



