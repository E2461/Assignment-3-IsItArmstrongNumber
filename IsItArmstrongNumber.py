numbers = [153, 370, 1,55, 371 ]
for number in numbers:
    str_number = str(number)
    toplam = 0
  
    
    for i in range(len(str_number)):
        toplam = toplam + int(str_number[i])**3
    if toplam == number:
        print(f"{number} is an Armstrong number")
    else :
         print(f"{number} is not an Armstrong number"
