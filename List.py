# List be mutable. It means we can do changes according to our need.
Fruits = ['Apple','Mango',"Orange","Papaya","Cherry","Grapes","Pineapple","Banana","Kiwi"]
print(Fruits,"\n")
#print(Fruits)
#for i in Fruits:
#    print(i)
print("\n".join(Fruits))  # In this ' "\n".join() ' will joined '\n' after each item during printing. It will not makes any changes into list.
Fruits.append('Guava')
print(Fruits)
Fruits.pop()                # Pop/Remove last item from the list.
print(Fruits)
Fruits.remove("Orange")       # Remove a specific item from the List.
print(Fruits)
print(" ".join(Fruits))