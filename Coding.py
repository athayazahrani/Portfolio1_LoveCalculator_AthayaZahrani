# ======================================================== PORTOFOLIO PROJECT MODULE 1 ==============================================================================
# ========================================================= ATHAYA ZAHRANI IRMANSYAH ================================================================================
# ================================================================ JCDS - 0408 ======================================================================================
# ============================================================= LOVE CALCULATOR =====================================================================================

# HEADER ============================================================================================================================================================
print('='*100)
print(f"{'<3 LOVE CALCULATOR <3':^100}")
print('='*100)
print(f"{'The Love Calculator provides a score from 0% to 100%':^100}")
print(f"{'that is meant to be an indication of a match in terms of love':^100}")
print(f"{'based on the names of two people, age, zodiak,':^100}")
print(f"{'and both of them must answer all the questions!':^100}")
print(f"{'The higher the percentage, the better the match!':^100}")
print(f"{'LETS TRY!':^100}")
print('='*100)

# MAIN PROGRAM =======================================================================================================================================================

# Validation Function ================================================================================================================================================
def validasi_nama():
    while True:
        global input_nama
        input_nama = input('Your Name: ')
        if input_nama.replace(' ','').isalpha() == True:
            return(input_nama)
            break
        print('Invalid input.')

def validasi_nama2():
    while True:
        global input_nama2
        input_nama2 = input('Your Name: ')
        if input_nama2.replace(' ','').isalpha() == True:
            return(input_nama2)
            break
        print('Invalid input.')

def validasi_umur():
    while True:
        global age
        age = input('Your Age: ')
        if age.isnumeric() == True:
            return(int(age))
            break
        print('Invalid input.')

def validasi_answer1():
    while True:
        global angka
        answer1 = input('Your first answer is (a/b/c/d): ').lower()
        if answer1 == 'a':
            angka += 4
        elif answer1 == 'b':
            angka += 3
        elif answer1 == 'c':
            angka += 2
        elif answer1 == 'd':
            angka += 1 
        return angka

def validasi_answer2():
    while True:
        global angka
        answer2 = input('Your second answer is (a/b/c/d): ').lower()
        if answer2 == 'd':
            angka += 4
        elif answer2 == 'c':
            angka += 3
        elif answer2 == 'b':
            angka += 2
        elif answer2 == 'a':
            angka += 1 
        return angka 

def validasi_answer3():
    while True:
        global angka
        answer3 = input('Your third answer is (a/b/c/d): ').lower()
        if answer3 == 'a':
            angka += 4
        elif answer3 == 'c':
            angka += 3
        elif answer3 == 'b':
            angka += 2
        elif answer3 == 'd':
            angka += 1 
        return angka

def validasi_answer4():
    while True:
        global angka2
        answer4 = input('Your first answer is (a/b/c/d): ').lower()
        if answer4 == 'a':
            angka2 += 4
        elif answer4 == 'b':
            angka2 += 3
        elif answer4 == 'c':
            angka2 += 2
        elif answer4 == 'd':
            angka2 += 1 
        return angka2

def validasi_answer5():
    while True:
        global angka2
        answer5 = input('Your second answer is (a/b/c/d): ').lower()
        if answer5 == 'd':
            angka2 += 4
        elif answer5 == 'c':
            angka2 += 3
        elif answer5 == 'b':
            angka2 += 2
        elif answer5 == 'a':
            angka2 += 1 
        return angka2

def validasi_answer6():
    while True:
        global angka2
        answer6 = input('Your third answer is (a/b/c/d): ').lower()
        if answer6 == 'a':
            angka2 += 4
        elif answer6 == 'c':
            angka2 += 3
        elif answer6 == 'b':
            angka2 += 2
        elif answer6 == 'd':
            angka2 += 1 
        return angka2
 
# FEMALE TURN ========================================================================================================================================================
# Name Input =========================================================================================================================================================
print('=== Female Turn ===')
input_nama = validasi_nama().lower()
angka = 0
for i in range(len(input_nama)):
    if input_nama[i] == 'a' or input_nama[i] == 'f' or input_nama[i] == 'h' or input_nama[i] == 'i' or input_nama[i] == 't' or input_nama[i] == 'y' or input_nama[i] == 'z':
        angka += 5
    elif input_nama[i] == 'b' or input_nama[i] == 'g' or input_nama[i] == 'm' or input_nama[i] == 'q' or input_nama[i] == 'v':
        angka += 1
    elif input_nama[i] == 'c' or input_nama[i] == 'j' or input_nama[i] == 'n' or input_nama[i] == 'r' or input_nama[i] == 'w':
        angka += 2   
    elif input_nama[i] == 'd' or input_nama[i] == 'k' or input_nama[i] == 'o' or input_nama[i] == 's' or input_nama[i] == 'x':
        angka += 3 
    elif input_nama[i] == 'e' or input_nama[i] == 'l' or input_nama[i] == 'p' or input_nama[i] == 'u':
        angka += 4 

# Age Input ============================================================================================================================================================
age = validasi_umur()
if age < 24:
    angka += age
elif age == 24:
    angka += 35
elif age > 24 and age < 35:
    angka += age
elif age == 35:
    angka += 24
elif age > 35:
    angka += 1        

# Zodiak Input ==========================================================================================================================================================
tanggal_lahir = int(input('Your date of birth: '))
bulan_lahir = int(input('Your month of birth: ')) 
def cek_zodiak(tanggal, bulan):
    global angka
    if (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        angka += 7
        return "Capricorn"
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        angka += 6
        return "Aquarius"
    elif (bulan == 2 and tanggal >= 19) or (bulan == 3 and tanggal <= 20):
        angka +=5
        return "Pisces"
    elif (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
        angka += 4
        return "Aries"  
    elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
        angka += 3
        return "Taurus"
    elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
        angka += 2
        return "Gemini"
    elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
        angka += 1
        return "Cancer"
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        angka += 12
        return "Leo"
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        angka += 10
        return "Virgo"
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        angka += 11
        return "Libra"
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
        angka += 9
        return "Scorpio"
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
        angka += 8
        return "Sagittarius"
    else:
        return "Tanggal atau bulan tidak valid"

zodiak = cek_zodiak(tanggal_lahir, bulan_lahir)
print(f"Your zodiak for date of birth {tanggal_lahir} and month of birth {bulan_lahir} is {zodiak}")

# 3 Questions ===========================================================================================================================================================
confirm = input(f'\nContinue to the next challenge? Type "yes"! ').upper()
if confirm == 'YES':
    print('\nYour have to answer the question.')
    print('''
    NUMBER 1
    Do you trust him?
    a. Absolutely
    b. I think we are building a good foundation     
    c. There have been instances where I have had my doubts
    d. It's hard to get myself to trust him
    ''')
    answer1 = validasi_answer1()  

    print('''
    NUMBER 2
    How attracted are you both to each other?
    a. I don’t think we find each other attractive
    b. There is some level of attraction    
    c. We do feel attracted to each other
    d. Its like fireworks!
    ''')
    answer2 = validasi_answer2()

    print('''
    NUMBER 3
    How emotionally intimate are you both?
    a. Very, we share everything with each other
    b. We both have our guards up    
    c. We are opening up to each other at the right pace
    d. We barely talk about the deep things in life
    ''')
    answer3 = validasi_answer3()
else:
    print(f'Thank you for playing.')

# MALE TURN =============================================================================================================================================================
# Name Input ============================================================================================================================================================
print('\n\n=== Male Turn ===')
input_nama2 = validasi_nama2().lower()
angka2 = 0
for i in range(len(input_nama2)):
    if input_nama2[i] == 'a' or input_nama2[i] == 'f' or input_nama2[i] == 'h' or input_nama2[i] == 'i' or input_nama2[i] == 't' or input_nama2[i] == 'y' or input_nama2[i] == 'z':
        angka2 += 5
    elif input_nama2[i] == 'b' or input_nama2[i] == 'g' or input_nama2[i] == 'm' or input_nama2[i] == 'q' or input_nama2[i] == 'v':
        angka2 += 1
    elif input_nama2[i] == 'c' or input_nama2[i] == 'j' or input_nama2[i] == 'n' or input_nama2[i] == 'r' or input_nama2[i] == 'w':
        angka2 += 2   
    elif input_nama2[i] == 'd' or input_nama2[i] == 'k' or input_nama2[i] == 'o' or input_nama2[i] == 's' or input_nama2[i] == 'x':
        angka2 += 3 
    elif input_nama2[i] == 'e' or input_nama2[i] == 'l' or input_nama2[i] == 'p' or input_nama2[i] == 'u':
        angka2 += 4 

# Age Input ===============================================================================================================================================================
age = validasi_umur()
if age < 24:
    angka2 += age
elif age == 24:
    angka2 += 35
elif age > 24 and age < 35:
    angka2 += 24
elif age == 35:
    angka2 += 24
elif age > 35:
    angka2 += 1        

# Zodiak Input =============================================================================================================================================================
tanggal_lahir = int(input('Your date of birth: '))
bulan_lahir = int(input('Your month of birth: ')) 
def cek_zodiak(tanggal, bulan):
    global angka2
    if (bulan == 12 and tanggal >= 22) or (bulan == 1 and tanggal <= 19):
        angka2 += 7
        return "Capricorn"
    elif (bulan == 1 and tanggal >= 20) or (bulan == 2 and tanggal <= 18):
        angka2 += 6
        return "Aquarius"
    elif (bulan == 2 and tanggal >= 19) or (bulan == 3 and tanggal <= 20):
        angka2 +=5
        return "Pisces"
    elif (bulan == 3 and tanggal >= 21) or (bulan == 4 and tanggal <= 19):
        angka2 += 4
        return "Aries"  
    elif (bulan == 4 and tanggal >= 20) or (bulan == 5 and tanggal <= 20):
        angka2 += 3
        return "Taurus"
    elif (bulan == 5 and tanggal >= 21) or (bulan == 6 and tanggal <= 20):
        angka2 += 2
        return "Gemini"
    elif (bulan == 6 and tanggal >= 21) or (bulan == 7 and tanggal <= 22):
        angka2 += 1
        return "Cancer"
    elif (bulan == 7 and tanggal >= 23) or (bulan == 8 and tanggal <= 22):
        angka2 += 12
        return "Leo"
    elif (bulan == 8 and tanggal >= 23) or (bulan == 9 and tanggal <= 22):
        angka2 += 10
        return "Virgo"
    elif (bulan == 9 and tanggal >= 23) or (bulan == 10 and tanggal <= 22):
        angka2 += 11
        return "Libra"
    elif (bulan == 10 and tanggal >= 23) or (bulan == 11 and tanggal <= 21):
        angka2 += 9
        return "Scorpio"
    elif (bulan == 11 and tanggal >= 22) or (bulan == 12 and tanggal <= 21):
        angka2 += 8
        return "Sagittarius"
    else:
        return "Tanggal atau bulan tidak valid"

zodiak = cek_zodiak(tanggal_lahir, bulan_lahir)
print(f"Your zodiak for date of birth {tanggal_lahir} and month of birth {bulan_lahir} is {zodiak}")

# 3 Questions ==============================================================================================================================================================
confirm = input(f'\nContinue to the next challenge? Type "yes"! ').upper()
if confirm == 'YES':
    print('\nYour have to answer the question.')
    print('''
    NUMBER 1
    How do you feel being with her?
    a. I feel really happy when I am around her
    b. It is a good feeling meeting her     
    c. I am not sure how she makes me feel yet
    d. I do not enjoy her company
    ''')
    answer4 = validasi_answer4()  

    print('''
    NUMBER 2
    Where would you like to go with her?
    a. Doesn’t matter, I know it will be boring
    b. I would like to go on a very nice date    
    c. I would like to go to a fancy dinner with her
    d. Anywhere is fine, it is her company that matters
    ''')
    answer5 = validasi_answer5()

    print('''
    NUMBER 3
    What type of relationship are you looking for?
    a. I want to get married to her
    b. I am not sure
    c. I want a long term relationship and see where it goes
    d. I just don’t want to be alone
    ''')
    answer6 = validasi_answer6()
else:
    print(f'Thank you for playing.')

# CALCULATING ==============================================================================================================================================================
a = (angka / 286) * 100
b = (angka2 / 286) * 100
c = a + b

print('\nYour quiz is already calculated.')
result = input('Wanna see the result? Type "yes"! ').upper()
if result == 'YES':
    if c >= 75:
        print('\n')
        print("RESULT".center(100,'-'))
        print('<3 Stay away from candles - your relationship is hot enough already! <3'.center(100,'-'))
        print(f'Your match is {c:.2f}%'.center(100,'-'))
        print(f'{input_nama} & {input_nama2}'.center(100,'-'))
        print(f'CONGRATULATIONS!'.center(100,'-'))
        print('\n')
    elif c >= 50:
        print('\n')
        print("RESULT".center(100,'-'))
        print('You guys are most alive when youre in love with each other'.center(100,'-').center(100,'-'))
        print(f'Your match is {c:.2f}%'.center(100,'-'))
        print(f'{input_nama} & {input_nama2}'.center(100,'-'))
        print('Cheers!'.center(100,'-'))
        print('\n')
    elif c >= 25:
        print('\n')
        print("RESULT".center(100,'-'))
        print('You always have to find your way to make you happy'.center(100,'-'))
        print(f'Your match is {c:.2f}%'.center(100,'-'))
        print(f'{input_nama} & {input_nama2}'.center(100,'-'))
        print('Never give up on us!'.center(100,'-'))
        print('\n')
    else:
        print('\n')
        print("RESULT".center(100,'-'))
        print('There is no reason to stay...'.center(100,'-'))
        print(f'Your match is {c:.2f}%'.center(100,'-'))
        print(f'{input_nama} & {input_nama2}'.center(100,'-'))
        print('Stay strong!'.center(100,'-'))
        print('\n')
