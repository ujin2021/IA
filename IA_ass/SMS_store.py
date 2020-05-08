class SMS_store:

    def __init__(self):
        self.has_been_viewed = False # viewed : True, not_viewed : False
        self.smsList=[]

    def __str__(self):
        return f'{self.smsList}'

    def add_new_arrival(self, *args):
        self.from_number = args[0]
        self.time_arrived = args[1]
        self.text_of_SMS = args[2]
        self.smsTuple = (self.has_been_viewed, self.from_number, self.time_arrived, self.text_of_SMS)
        self.smsList.append(self.smsTuple)

    def message_count(self):
    # Returns the number of sms messages in my_inbox
        return len(self.smsList)

    def get_unread_indexes(self):
    # Returns list of indexes of all not-yet-viewed SMS messages
        unreadIdx = []
        for i in range(0, len(self.smsList)):
            if self.smsList[i][0] == False:
                unreadIdx.append(i)
        return unreadIdx

    def get_message(self, index):
    # Return (from_number, time_arrived, text_of_sms) for message[i]
    # Also change its state to "has been viewed".
    # If there is no message at position i, return None
        if index >= len(self.smsList):
            return None
        temp = (True, )
        self.smsList[index] = temp + self.smsList[index][1:]
        return self.smsList[index][1:]

    def delete(self, index):
    # Delete the message at index i
        if index >= len(self.smsList):
            return None
        self.smsList = self.smsList[0:index] + self.smsList[index+1:]
        return self.smsList

    def clear(self):
    # Delete all messages from in
        self.smsList = []
        return self.smsList






