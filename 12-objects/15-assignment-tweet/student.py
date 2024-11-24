class Tweet:
    def __init__(self, message, max_length):
        self.__max_length = max_length
        self.message = message

    @property
    def message(self):
        return self.__message
    
    @message.setter
    def message(self, value):
        if len(value) > self.__max_length:
            self.__message = value[:self.__max_length]
            self.__message = value
    
    @property
    def max_length(self):
        return self.__max_length
    
    @max_length.setter
    def max_length(self, value):
        if value < 1:
            raise ValueError("max_length must be at least 1!")
        self.__max_length = value

        if len(self.__message) > self.__max_length:
            self.__message = self.__message[:self.__max_length]

my_tweet = Tweet("1234567", 5)
print(my_tweet.message)
