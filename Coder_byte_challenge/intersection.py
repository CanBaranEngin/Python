strArr=["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
a = map(int, strArr[0].split(', '))
b = map(int, strArr[1].split(', '))
c = list(set(a) & set(b))
c.sort()  
if c==[]:
    print("False")
else:
    print(','.join(map(str, c)))

