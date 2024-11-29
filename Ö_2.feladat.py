numbers=[]
szamok_osszege=0

while True:
    num=int(input('input(Adj meg egy egész számot a [-5,5] intervallumon! '))
    if num<-5 or num>5:
        break
    else:
        numbers.append(num)
        szamok_osszege+=num
print(f'Az alábbi számokat adtad meg: {numbers} és ezeknek az összege: {szamok_osszege}')

'''
intervallum=[] #[-5,5]

for i in range(-5,6):
    intervallum.append(i)
'''