str = input("enter a string: ")
maxchar = tmp = 0
for x in str:
  tmp = str.count(x)
  if maxchar < tmp:
    maxchar = tmp
    c = x
print(c)
