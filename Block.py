import hashlib
import datetime


class Structure:
    def __init__(self, datas, previous_hash):
        self.datas = datas
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        self.TimeStamp = datetime.datetime.now()

    def calculate_hash(self):
        block_header = str(self.datas) + str(self.previous_hash)
        return hashlib.sha256(block_header.encode()).hexdigest()
