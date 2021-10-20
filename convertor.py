
distance =int(input('the distance: ')) 
unit = input("in M or K:  ").upper()

if unit =='K':
    res = distance * 1000
    print(f' the distance is {res} K')

elif unit =="M":
    res = distance / 1000
    print(f'the distance is {res} M') 
else:
    print('select M for metter or K for kilometer')




