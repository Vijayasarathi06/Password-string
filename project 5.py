
##Password string
import random
import string
lower_case=int(input("enter the lower value"))
upper_case=int(input("enter the upper value"))
digit=int(input("enter the number value")) 
symbol_len=int(input("enter the symbol value"))
password=lower_case+upper_case+digit+symbol_len
lower=string.ascii_lowercase
upper=string.ascii_uppercase
number=string.digits
symbol=string.punctuation
str=random.choices(lower,k=lower_case)+random.choices(upper,k=upper_case)+random.choices(number,k=digit)+random.choices(symbol,k=symbol_len)
random.shuffle(str)
y="".join(str)
print("password is",y)

