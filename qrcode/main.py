from mode import get_mode

class QRCODE:
    def __init__(self):
        self.data = ''
        self.mode = ''
    def __str__(self):
        return self.data + " " + self.mode
    def create(self,data):
        self.data = data
        self.mode = get_mode(data)