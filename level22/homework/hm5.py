#მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ნამრავლი

num = int(input("enter number: "))

sum = 1

for i in range(1, num + 1):
    sum = sum * i

print(sum)