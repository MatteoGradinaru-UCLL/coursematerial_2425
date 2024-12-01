class Tweet:
    def __init__(self, message, max_length):
        self.message = message
        self.max_length = max_length
    
    @property
    def max_length(self):
        return self.__max_length
    
    @max_length.setter
    def max_length(self, value):
        if value <= 0:
            raise ValueError("max lenght moet groter zijn dan 0")
        self.__max_length = value

    @property
    def message(self):
        if len(self.__message) > self.max_length:
            return self.__message[:self.max_length]
        return self.__message

    @message.setter
    def message(self,value):
        self.__message = value

tweet = Tweet("abc", 2)
print(tweet.message)

tweet.max_length = 1
print(tweet.message)



'''class Tweet:
    def __init__(self, message, max_length):
        self.message = message
        self.max_length = max_length
        

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
'''