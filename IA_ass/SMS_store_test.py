import time
import SMS_store

 # get the current time in seconds since Epoch

my_inbox = SMS_store.SMS_store()
time_stamp = time.time()
my_inbox.add_new_arrival('010-1111-2222', time.ctime(time_stamp), 'Peng')
time_stamp = time.time()
my_inbox.add_new_arrival('010-3333-4444', time.ctime(time_stamp), 'Soo')
time_stamp = time.time()
my_inbox.add_new_arrival('010-5555-6666', time.ctime(time_stamp), 'Hi!')

print(my_inbox)
print("message count: ",my_inbox.message_count()) #3
print("\nunread indexes list : ", my_inbox.get_unread_indexes()) #[0, 1, 2]
print("\nread index1 message: ",my_inbox.get_message(1))
print("if index is out of bound : ", my_inbox.get_message(5))
print("\n<my_inbox after get index1 message>\n", my_inbox) #change index 1 state to True
print("\nunread indexes list : ", my_inbox.get_unread_indexes()) #[0, 2]
my_inbox.delete(1)
print("\n<my_inbox after delete index1 message>\n", my_inbox)
time_stamp = time.time()
my_inbox.add_new_arrival('010-7777-8888', time.ctime(time_stamp), 'How are you?')
print(my_inbox)
print("\nunread indexes list : ", my_inbox.get_unread_indexes())
my_inbox.clear()
print("\n<my_inbox after clear>\n", my_inbox)