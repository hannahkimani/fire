print("Grades calculator")

math = int(input("math: "))
eng = int(input("eng: "))
phy = int(input("phy: "))
kisw = int(input("kisw: "))
histo = int(input("histo: "))
total = math + eng + phy + kisw + histo
print(total)
average = total / 5
print(average)

if average >100:
    print("invalid")
elif average < 0:
    print("out of range")


elif average < 39:
    print("Grade=E")

elif average < 39  :
     print("Grade=D")

elif average < 50 :
    print("Grade=C")

elif average < 60  :
    print("Grade=B")

elif  average > 79  :
    print("Grade=A")

else:

   print("invalid input")

   print("grades")

