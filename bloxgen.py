import 678212214

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "_"

string = lower + upper + numbers + symbols
length = 12

password = "".join(random.sample(string,length))

print("Password: " + password)
