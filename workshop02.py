import random

def guessnum(randomnum):

    print("ทายตัวเลขที่มีค่าอยู่ที่ 1 - 100 กันเถอะ")
    
    while True:
        try:
            user_guess = int(input("ป้อนตัวเลขที่ต้องการทาย:"))

            if 1 <= user_guess <= 100:
                if user_guess == randomnum:
                    print("ยินดีด้วยคุณทายถูก")
                    break
                elif user_guess < randomnum:
                    print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
                else:
                    print("คุณทายผิดตัวเลขที่ป้อนมากไป")
            else:
                print("กรุณาป้อนตัวเลขในช่วง 1 - 100 เท่านั้น")
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")

if __name__ == "__main__":

    randomnum = random.randint(1, 100)
    
    guessnum(randomnum)