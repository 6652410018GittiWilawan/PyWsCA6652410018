def analyze_sentence(sentence):
    try:
        words = sentence.split()

        if not words:
            raise ValueError("ประโยคไม่ถูกต้อง")

        total_words = len(words)
        print(f"ประโยคนี้ประกอบด้วยคำทั้งหมด {total_words} คำ")

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        duplicate_words = sum(count > 1 for count in word_count.values())
        print(f"มีคำที่ซ้ำกัน {duplicate_words} คำ")

       
        if duplicate_words > 0:
            print("คำที่ซ้ำกันคือ:")
            for word, count in word_count.items():
                if count > 1:
                    print(f"{word}: ซ้ำ {count} ครั้ง")

    except ValueError as ve:
        print(f"เกิดข้อผิดพลาด: {ve}")

user_sentence = input("กรุณากรอกประโยคภาษาอังกฤษ: ")

analyze_sentence(user_sentence)