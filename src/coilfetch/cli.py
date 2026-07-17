from coilfetch.info_collector import InfoCollector
from coilfetch.printer import Printer


def main():
    collector = InfoCollector()
    printer = Printer()
    printer.print(collector.get_info_dict())
