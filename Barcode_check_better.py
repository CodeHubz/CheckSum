#Modulo_Check_better

bc_num= input("Please enter your barcode numbers from 1 to 11")
odd_num1=(bc_num[0])
even_num2=(bc_num[1])
odd_num3=(bc_num[2])
even_num4=(bc_num[3])
odd_num5=(bc_num[4])
even_num6=(bc_num[5])
odd_num7=(bc_num[6])
even_num8=(bc_num[7])
odd_num9=(bc_num[8])
even_num10=(bc_num[9])
odd_num11=(bc_num[10])

total_odd= int(odd_num1) + int(odd_num3) + int(odd_num5) + int(odd_num7) + int(odd_num9) + int(odd_num11)
total_even= int(even_num2) + int(even_num4) + int(even_num6) + int(even_num8) + int(even_num10)
total2_odd= int(total_odd) * 3
total_bn= int(total_even) + int(total2_odd)
y= int(total_bn) % 10
z= int(total_bn) / 10

if y> 0 :
    b = int(z)+1
    a = int(b)*10
    j = int(a) - int(total_bn)
    print(f"The Modulo Check = {j}")
else:
    x= int(total_bn)
    k= int(total_bn) - int(x)
    print(f"The Modulo Check is {k}")
    
 






