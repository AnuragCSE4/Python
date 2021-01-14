# for i in range(stop)
# for i in range(start,stop)
# for i in range(start,stop,increment count)

a=0
for i in range(5):
    a=a+1
    print("a = ",a)

for i in range(0,5):    #In this the value of i will be increment till 4 and when it be 5 then loop will be terminate. so i increase 0,1,2,3,4 
    a=a+1
    print("a = ",a)
# we can iterate for loop into any string, list, tuple and disctionary too.

variable = "My name is Anurag Kushwaha."
for i in variable:
    print(i,end="")   # In this statement ' end="" ' is used for non-line-breaking. If I remove it then it print each letter in a new line.
