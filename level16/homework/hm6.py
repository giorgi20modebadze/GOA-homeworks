# თქვენ დაგპატიჟეს პატარა ბავშვის დაბადების დღეზე გასართობ ცენტრში, თქვენთან ერთად ამ გასართობ ცენტრში დაპატიჟეს 10 ადამიანი და ამ 10 ადამიანიდან ერთ ერთი ნიკოლოზია. ნიკოლოზს უთხრეს რომ მას შეუძლია ბავშებთან ერთად გაერთოს თუ ის ფეხსაცმელებს გაიხდის და ქურთუკს საკიდზე ჩამოკიდებს (True და False-ს გამოყენება დაგჭირდებათ). თქვენი მიზანია გაარკვიოთ ნიკოლოზმა შეასრულა ეს წესები თუ არა, ანუ შეუძლია თუ არა მას ბავშებთან ერთად გართობა.

qurtuki = input("acvia qurtuki?: ")
pexsacmeli = input("acvia pexsacmeli?: ")

if qurtuki == "True" and pexsacmeli == "false":
    print("ნიკოლოზს არ შეუძლია გართობა")

elif qurtuki == "True" and pexsacmeli == "True":
    print("ნოკოლოზს შეუძლია გართობა")

elif qurtuki == "False" and pexsacmeli == "True":
    print("ნიკოლოზს არ შეუძლია გართობა")

elif qurtuki == "false" and pexsacmeli == "False":
    print("ნიკოლოზს არ შეუძლია გართობა")