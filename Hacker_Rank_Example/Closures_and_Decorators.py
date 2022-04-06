def wrapper(f):
    a=[]
    def fun(l):
        for i in l:
            a.append("+91 "+i[-10:-5]+" "+i[-5:]) 
        return f(a)     
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input("phone_number:") for _ in range(int(input("sayi")))]
    sort_phone(l) 

    