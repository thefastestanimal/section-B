x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) # this code combine set y to x by adding only one appearance of the item.  

print(x)   # the out put will be { "apple", "banana", "cherry", "google", "microsoft"}
