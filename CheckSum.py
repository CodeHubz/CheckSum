#Modulo_Check_better2
bc_num= input("Please enter your barcode numbers from 1 to 11  ")
even = 0
odd = 0
for x in range (0,11):
    if ( x%2 == 0):
        even= even + int(bc_num[x])
    else:
        odd = odd + int(bc_num[x])
total= (odd * 3) + even
if ((total % 10) > 0 ):
    print(f"The Modulo Check = {(((total/10 )+1) *10) - total}")
else:    
    print(f"The Modulo Check is 0")
