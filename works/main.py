import psycopg2
conn = psycopg2.connect(
    dbname='users_db',
    user='postgres',
    password='N17122010el',
    host='localhost',
    port='5432'
)
cur=conn.cursor()

def add_users():
    ism=input("Ismingizni kiriting: ")
    familiya=input("Familiyangizni kiriting: ")
    yosh=int(input("Yoshingizni kiriting: "))
    shahar=input("Shahringizni kiriting: ")
    cur.execute("""
        INSERT INTO users(ism,familiya,yosh,shahar) values(%s, %s, %s, %s)
    """, (ism,familiya,yosh,shahar))
    conn.commit()
    question=input("Foydalanuvchi muvaffaqiyatli qo'shildi, yana qo'shmoqchimisiz[Y/n]: ")
    if question == "Y":
        add_users()
    menu()

def list_of_users():
    print("==Foydalanuchilar ro'yhati==")
    cur.execute("select * from users")
    foydalanuvchilar = cur.fetchall()
    for index, user in enumerate(foydalanuvchilar):
        print(f"{index+1}. {user[0]} {user[1]} {user[2]} {user[3]}")
    menu()

def random_users():
    import random
    from faker import Faker
    faker=Faker()

    for i in range(1,51):
        ism = faker.first_name()[:50]
        familiya = faker.last_name()[:50]
        yosh = random.randint(1,100)
        shahar = faker.city()[:50]
        cur.execute("""
            INSERT INTO users(ism, familiya, yosh, shahar) VALUES(%s, %s, %s, %s)
        """, (ism,familiya,yosh,shahar))
        conn.commit()
    print("Random foydalanuvchilar muvaffaqiyatli qo'shildi")
    menu()

def del_users():
    cur.execute("""
        truncate table users;
    """)
    conn.commit()
    print("Hamma foydalanuvchilar muvaffaqiyatli o'chirildi")
    menu()

def menu():
    print("""
1. Foydalanuvchi qo'shish
2. Foydalanuvchilar ro'yhati
3. Random 50 ta foydalanuchi qo'shish
4. Hamma foydalanuvchilarni o'chirish
5. Dasturdan chiqish
""")
    tanlov=int(input("Tanlovni kiriting: "))
    if tanlov==1:
        add_users()
    elif tanlov==2:
        list_of_users()
    elif tanlov==3:
        random_users()
    elif tanlov==4:
        del_users()
    elif tanlov==5:
        print("Dastur to'xtatildi")
        cur.close()
        conn.close()
        exit()
menu()