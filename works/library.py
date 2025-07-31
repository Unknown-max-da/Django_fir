qayerda = False
login_fornow = ''

import psycopg2
def get_connection():
    database_rtx = psycopg2.connect(
        dbname = 'kutubxona_db',
        user = 'postgres',
        password = 'N17122010el',
        host = 'localhost',
        port = '5432'

    )
    return database_rtx

def kitob_qoshish():
    conn= get_connection()
    cur=conn.cursor()
    cur.execute("select * from kitoblar")
    kitoblar2=cur.fetchall()
    id = input('Kitobni id sini kiriting: ')
    for kitob in kitoblar2:
        if kitob[0] == id:
            print('Bunday id li kitob bazada bor! Boshqa ID kiriting')
            kitob_qoshish()
    nomi = input('kitobni nomini kiriting: ')
    author = input('Muallifini kiriting: ')
    narxi = int(input('Kitob narxini kiriting: '))

    cur.execute("""
        INSERT INTO kitoblar(id,nomi,author,narxi) values(%s, %s, %s, %s)
    """, (id,nomi,author,narxi))
    conn.commit()

    print('\033[92mKitob muvaffaqiyatli qo`shildi! ✅\033[0m')
    sorov = input('Yana kitob qoshishni istaysizmi [ha/yoq]? ')
    if sorov == 'ha':
        kitob_qoshish()
    else:
        admin_menu()

def kitob_tahrirlash():
    id = input('Tahrirlamoqchi bolgan kitobning ID sini kiriting: ')
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("select * from kitoblar")
    kitoblar2=cur.fetchall()
    for kitob in kitoblar2:
        if kitob[0] == id:
            print(f"{kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
            kitob_id = input("O'zgartirmoqchi bo'lgan ID-ni kiriting: ") or kitob[0]
            kitob_nomi = input("O'zgartirmoqchi bo'lgan nomini kiriting: ") or kitob[1]
            kitob_author = input("O'zgartirmoqchi bo'lgan authorni kiriting: ") or kitob[2]
            kitob_narxi = int(input("O'zgartirmoqchi bo'lgan narxini kiriting: ")) or kitob[3]
            cur.execute("UPDATE kitoblar SET id=%s, nomi=%s, author=%s, narxi=%s where id=%s", (kitob_id, kitob_nomi, kitob_author, kitob_narxi, id))
            conn.commit()
            print('kitob muvaffaqiyatli yangilandi! ✅')
            admin_menu()
    else:
        print('bunday ID li kitob topilmadi')
    admin_menu()

def kitob_ochirish():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from kitoblar")
    kitoblar2 = cur.fetchall()
    id = input('o`chirmoqchi bo`lgan kitobni ID sini kiriting: ')
    for kitob in kitoblar2:
        if kitob[0] == id:
            print(f"{kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
            sorov = input('Siz rostdan ham shu kitobni o`chirmoqchimisiz? [ha/yoq] ')
            if sorov == 'ha':
                cur.execute("delete from kitoblar where id=%s", (id,))
                conn.commit()
                print('kitob muvaffaqiyatli o`chirildi! ✅')
                admin_menu()
            else:
                admin_menu()
    admin_menu()


def kitob_detail():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from kitoblar")
    kitoblar2 = cur.fetchone()
    id = input('ko`rmoqchi bo`lgan kitobning ID sini kiriting: ')
    for kitob in kitoblar2:
        if kitob[0] == id:
            print(f"{kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
            admin_menu()
    admin_menu()

def kitoblar_royhati():
    print(' == Kitoblar ro`yxati == ')
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from kitoblar where mavjudmi=%s", (True,))
    kitobcha = cur.fetchall()

    for index, kitob in enumerate(kitobcha):
     print(f"{index+1}. {kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
    if qayerda:
        admin_menu()
    else:
        user_menu(login_fornow)

def kitob_search():
    nom = input('Izlamoqchi bo`lgan kitob nomini kiriting: ')
    count=0

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from kitoblar")
    kitoblar2 = cur.fetchall()
    for kitob in kitoblar2:
        if nom in kitob[1]:
            count+=1

    if count>0:
        print(f"{count} ta kitob topildi\n")
        count=0
        for kitob in kitoblar2:
            if nom in kitob[1]:
                count+=1
                print(f"{count}. {kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
        if qayerda:
            admin_menu()
        else:
            user_menu(login_fornow)
    else:
        print("Bunday kitob topilmadi! 🚫")
        if qayerda:
            admin_menu()
        else:
            user_menu(login_fornow)

def random_book():
    import random
    from faker import Faker
    conn = get_connection()
    cur = conn.cursor()
    faker = Faker()
    kitoblar_soni=int(input("Nechta kitob qo'shmoqchisiz?: "))
    cur.execute("select * from kitoblar")
    kitoblar2 = cur.fetchall()
    for i in range(1, kitoblar_soni + 1):
        while True:
            bormi=False
            id = str(random.randint(1, 999))
            for kitob in kitoblar2:
                if id != kitob[0]:
                    pass
                else:
                    bormi=True
            if bormi:
                pass
            else:
                break
        nomi=faker.street_name()
        author=faker.first_name()
        narxi=random.randint(10000,100000)
        cur.execute("""
            INSERT INTO kitoblar(id,nomi,author,narxi) values(%s,%s,%s,%s)
        """, (id,nomi,author,narxi))
        conn.commit()

    for index, kitob in enumerate(kitoblar2):
        print(f"{index+1}. {kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
    print("Kitoblar muvaffaqiyatli qo'shildi! ✅")
    admin_menu()


def kitob_detail_va_sotib_olish(login):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from userlar where login=%s", (login,))
    usercha=cur.fetchone()
    id = input('sotib olmoqchi bo`lgan kitob ID sini kiriting: ')
    cur.execute("select * from kitoblar where id=%s", (id,))
    kitob = cur.fetchone()
    if kitob:
        print(kitob)
        print(f"{kitob[0]} | {kitob[1]} | {kitob[2]} | {kitob[3]}")
        sorov = input('Rostdan ham shu kitobni sotib olmoqchimisiz? [ha/yoq] ')
        if sorov == 'ha':
            if usercha[2] >= kitob[3]:
                left_balance = usercha[2] - kitob[3]
                cur.execute("update userlar set balance=%s where login=%s", (left_balance, login))
                cur.execute("INSERT INTO xaridlar(user_login, kitob_id) values(%s, %s)", (login, id))
                cur.execute("UPDATE kitoblar set mavjudmi=%s where id=%s", (False, id))
                conn.commit()
                print('Siz kitobni sotib oldingiz')
                user_menu(login)
            else:
                print('Sizda yetarli mablag` mavjud emas')
                user_menu(login)
        else:
            print('Siz kitobni xarid qilmadingiz')
            user_menu(login)
    else:
        print("Bunday ID-li kitob mavjud emas!")

def dell_all():
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("""
        DELETE from kitoblar
    """)
    conn.commit()
    admin_menu()

def admin_menu():
    global qayerda
    qayerda = True
    print("""
1. Kitob qo'shish
2. Kitobni tahrirlash
3. Kitobni o'chirish
4. Kitobni detail
5. Kitoblar ro'yhati
6. Kitobni izlash
7. Random kitob qoshish
8. Hamma kitoblarni o'chirish
9. Orqaga
    """)
    tanlov = int(input('Tanlovni kiriting: '))
    if tanlov == 1:
        kitob_qoshish()
    elif tanlov == 2:
        kitob_tahrirlash()
    elif tanlov == 3:
        kitob_ochirish()
    elif tanlov == 4:
        kitob_detail()
    elif tanlov == 5:
        kitoblar_royhati()
    elif tanlov == 6:
        kitob_search()
    elif tanlov == 7:
        random_book()
    elif tanlov == 8:
        dell_all()
    elif tanlov == 9:
        main_manu()
    else:
        print('Bunday qiymat topilmadi')
        admin_menu()

def user_xaridlar(login):
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("select * from userlar where login=%s", (login,))
    usercha=cur.fetchone()
    if usercha:
        print("Sizning xaridlaringiz!")
        cur.execute("""
            select k.nomi, k.author, k.narxi from xaridlar x join kitoblar k on x.kitob_id=k.id where user_login=%s and k.mavjudmi=%s
        """, (login,False))
        kitobchalar = cur.fetchall()
        if kitobchalar:
            for index,kitob in enumerate(kitobchalar):
                print(f"{index+1}. {kitob[0]} |{kitob[1]} |{kitob[2]}")
            user_menu(login)
        else:
            print("\033[91mSizda hech qanday xaridlar yo'q\033[0m")
            user_menu(login)

def user_menu(login):
    global qayerda
    qayerda = False
    global login_fornow
    login_fornow = login
    conn = get_connection()
    cur=conn.cursor()
    print("""
1. Kitoblar ro'yhati
2. Kitob qidirish
3. Kitob detail va sotib olish
4. Balans
5. Xaridlar
6. Orqaga
    """)
    tanlov = int(input('Tanlovni kiriting: '))
    if tanlov == 1:
        kitoblar_royhati()
    elif tanlov == 2:
        kitob_search()
    elif tanlov == 3:
        kitob_detail_va_sotib_olish(login)
    elif tanlov == 4:
        cur.execute("select * from userlar where login=%s", (login,))
        usercha=cur.fetchone()
        print(f"Hisobingizdagi balans: {usercha[2]}")
        user_menu(login)
    elif tanlov==5:
        user_xaridlar(login)
    elif tanlov == 6:
        main_manu()
    else:
        print('Bunday qiymat mavjud emas')
        user_menu(login)

def admin_registration():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select * from adminlar")
    cur.fetchall()
    new_login = input('Yangi loginni kiriting: ')
    new_parol = input('Yangi parolni kiriting: ')
    cur.execute("INSERT INTO adminlar(login,parol) values(%s, %s)", (new_login,new_parol))
    conn.commit()
    print('Siz muvaffaqiyatli ro`yxatdan o`tdingiz ✅')
    admin_menu()

def user_registration():
    conn = get_connection()
    cur = conn.cursor()
    new_login = input('Logini kiriting: ')
    new_parol = input('Parolni kiriting: ')
    cur.execute("""
        INSERT INTO userlar(login,parol) values(%s,%s)
    """, (new_login, new_parol))
    print('Siz muvaffaqiyatli ro`yxatdan o`tdingiz ✅')
    main_manu()

def admin_panel():
    login = input('Loginni kiriting: ')
    parol = input('Parolni kiriting: ')
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("select * from adminlar where login=%s", (login,))
    admincha=cur.fetchone()

    if login == admincha[0]:
        if admincha[1] == parol:
            print('\033[92mAdmin muvaffaqiyatli topildi! ✅\033[0m')
            admin_menu()
        else:
            print('\033[91mParol noto`g`ri! 🚫\033[0m')
            admin_panel()
    else:
        print('\033[91mBunday admin topilmadi! 🚫\033[0m')
        admin_registration()

def user_panel():
    conn = get_connection()
    cur = conn.cursor()
    login = input('Logini kiriting: ')
    parol = input('Parolni kiriting: ')
    cur.execute("select * from userlar where login=%s and parol=%s", (login,parol))
    usercha = cur.fetchone()

    if login in usercha[0]:
        if usercha[1] == parol:
            print('\033[92mUser muvaffaqiyatli topildi! ✅\033[0m')
            user_menu(login)
        else:
            print('\033[91mParol noto`g`ri! 🚫\033[0m')
            user_panel()
    else:
        print('\033[91mBunday user mavjud emas! 🚫\033[0m')
        user_registration()

def main_manu():
    print("""
1. Admin panel
2. User panel
3. Dasturdan chiqish
    """)
    tanlov = int(input('Tanlovni kiriting: '))
    if tanlov == 1:
        admin_panel()
    elif tanlov == 2:
        user_panel()
    elif tanlov == 3:
        print('Dastur to`xtatildi')
        exit()
    else:
        print('Bunday qiymat mavjud emas')
        main_manu()

main_manu()
