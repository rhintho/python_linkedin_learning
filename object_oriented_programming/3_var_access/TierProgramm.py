from Katze import *


class TierProgramm:
    def __init__(self):
        TierProgramm.main()

    @staticmethod
    def main():
        susi = Katze(1)
        print(susi.alter)
        susi.alter = 3
        print(susi.alter)



TierProgramm()
