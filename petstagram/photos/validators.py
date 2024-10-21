class SizeImgValidator:
    def __init__(self, file_size_mb, message=None):
        self.file_size_mb = file_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"File size must be below or equal to {self.file_size_mb}MB"
        else:
            self.__message = value
