'''تحلیل متن
تابعی به نام analyze_text(text) بنویسید که موارد زیر را پیدا کند:
 تعداد کلمات
تعداد حروف
تعداد اعداد
پرتکرارترین حرف
پرتکرارترین کلمه
طولانی‌ترین کلمه
کوتاه‌ترین کلمه
تعداد کلمات Palindrome
تعداد حروف بزرگ
تعداد حروف کوچک
خروجی:
{"words": ...,
"letters": ...,
"digits": ...,
"most_common_letter": ...,
"most_common_word": ...,
"longest_word": ...,
"shortest_word": ...,
"palindrome_words": ...,
"uppercase": ...,
"lowercase": ...}'''

def analyze_text(text):
    text = input("enter your text: ")

    total_text = 0
    for i in text.split():
        total_text += 1

    total_words = 0
    for i in text:
        if i.isalpha():
            total_words += 1

    nums = 0
    for i in text:
        if i.isdigit():
            nums += 1

    most_word = {}
    for i in text.split():
        if i not in most_word:
            most_word[i] = 1
        else:
            most_word[i] += 1

    most = ''
    most_count = 0

    for i in most_word:
        if most_word[i] > most_count:
            most = i
            most_count = most_word[i]

    most_letter = {}
    for i in text:
        if i.isalpha():
            if i not in most_letter:
                most_letter[i] = 1
            else:
                most_letter[i] += 1

    most_letter_name = ''
    most_letter_count = 0

    for i in most_letter:
        if most_letter[i] > most_letter_count:
            most_letter_name = i
            most_letter_count = most_letter[i]

    l_word = ''

    for i in text.split():
        if len(i) > len(l_word):
            l_word = i

    sh_word = text.split()[0]

    for i in text.split():
        if len(i) < len(sh_word):
            sh_word = i

    palindromes = 0

    for i in text.split():
        if i == i[::-1]:
            palindromes += 1

    uppers = 0
    lowers = 0

    for i in text:
        if i.isupper():
            uppers += 1

        if i.islower():
            lowers += 1

    print("words:", total_text)
    print("letters:", total_words)
    print("digits:", nums)
    print("most common letter:", most_letter_name)
    print("most common word:", most)
    print("longest word:", l_word)
    print("shortest word:", sh_word)
    print("palindrom words:", palindromes)
    print("upper case:", uppers)
    print("lower case:", lowers)

analyze_text('')