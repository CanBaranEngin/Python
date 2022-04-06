#Adam Asmaca Oyunu
import random
word_list=["baran","engin","lord","rings","game","mechanic","engineer","computer"]
o_g=random.choice(word_list)
baslangıç_liste=list(len(o_g)*"-")
print(baslangıç_liste)
a=0
b=0
c=len(o_g)
while a<len(o_g)-1:
  s=-1
  tahmin=input("Kelimeyi bulmak için bir harf giriniz: ")
  for harf in o_g:
    s+=1
    if harf in tahmin:
      b+=1
      baslangıç_liste.pop(s)
      baslangıç_liste.insert(s,harf)
  if tahmin not in o_g:
    a+=1
    c-=1
    print(f"yanlış, kalan hakkınız: {c}")
  print(baslangıç_liste)
  if b==len(o_g):
    print("Tebrikler Bildiniz")
    break
  if c==1:
    print("Malesef Hakkınız Bitti")  
