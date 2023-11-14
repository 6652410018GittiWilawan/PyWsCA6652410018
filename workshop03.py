import math

def menu():
    print("Area & Cube")
    print("1.พื้นที่4เหลี่ยม")
    print("2.พื่นที่วงกลม")
    print("3. ปริมาตรทรงสี่เหลี่ยม")
    print("4. ปริมาตรทรงกลม")
    print("0. ออกจากการทำงาน")

 
    def recArea():
        
            W = float(input("ป้อนความกว้าง: "))
            L = float(input("ป้อนความยาว"))
            A = W * L
            print(f"พื้นที่4เหลี่ยมที่คำนวณได้คือ: {A:.2f} ")

    def circleArea():
            Rad = float(input("ป้อนรัศมี :"))
            A = math.pi * Rad **2 
            print(f"พื้นที่วงกลมที่คำนวณได้คือ: {A:.2f}")

    def recvolume():
            w = float(input("ป้อนความกว้าง: "))
            l = float(input("ป้อนความยาว: "))
            h = float(input("ป้อนความสูง: "))
            v = w * l * h
            print(f"ปริมาตรทรง4เหลี่ยมที่คำนวณได้คือ: {v:.2f}")

    def spvolume():
            r = float(input("ป้อนรัศมี: "))
            v = (4/3) * math.pi * r**3
            print(f"ปริมาตรทรงกลมที่คำนวณได้คือ: {v:.2f}")

    if __name__ == "__main__":
        while True:
            menu()
            choice = input("เลือกเมนู : ")

            if choice == "1":
                recArea()
            elif choice == "2":
                circleArea()
            elif choice == "3":
                recvolume()
            elif choice == "4":
                spvolume()
            elif choice == "0":
                print("ทำคำนวณเสร็จสิ้น บายบาย!")
                break
            else:
                print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")