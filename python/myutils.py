class Utils:
    @staticmethod
    def getInt(*msg):
        while(True):
            try:
                value = int(input(*msg))
                return value
            except:
                print('Invalid input')

    @staticmethod
    def getFloat(*msg):
        while(True):
            try:
                value = float(input(*msg))
                return value
            except:
                print('Invalid input')