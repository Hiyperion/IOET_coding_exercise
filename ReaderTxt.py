def singleton(cls):
    instances = dict()
    def wrap(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap
@singleton
class ReaderTxt:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
    def readFile(self):
        with open(self.file_name) as file:#TODO: should convert the hour in 00:00 format to a decimal format
            pass
