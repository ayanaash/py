import csv  #to read data from file
from connect import connect  #connect to database


#1 insert from CSV
def insert_from_csv():
    conn = connect()   #соеденение с базой
    cur = conn.cursor()   #инструмент для выполнения sql запросво

    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)   #csv читается как dictionary
        for row in reader:
            cur.execute(    #выполняем запрос
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",   #transfer data (передача значений)
                (row["first_name"], row["phone"])
            )

    conn.commit()    #save changes
    cur.close()
    conn.close()
    print("data inserted from CSV")


#2 insert from cons(input)
def insert_from_console():
    name = input("enter name: ")
    phone = input("enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("added")


#3 update
def update_contact():
    name = input("enter name to update: ")   #person/name who we are updating (кого обновляем)
    new_name = input("new name: ")  
    new_phone = input("new phone: ")   

    conn = connect()
    cur = conn.cursor()

    if new_name:   #обновляем имя
        cur.execute(
            "UPDATE phonebook SET first_name=%s WHERE first_name=%s",
            (new_name, name)
        )

    if new_phone:    #обновляем номер тел
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE first_name=%s",
            (new_phone, name)
        )

    conn.commit()
    cur.close()
    conn.close()
    print("updated")


#4 search
def search_contacts():
    keyword = input("enter name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone LIKE %s",     #ilike = name, like = phone
        (f"%{keyword}%", f"{keyword}%")   # %...% - содержит,  ...% - начинается с
    )

    results = cur.fetchall()   #получаем все найденные строки

    if results:
        for row in results:
            print(row)
    else:
        print("No results")

    cur.close()
    conn.close()


#5 delete
def delete_contact():
    choice = input("Delete by (1) name or (2) phone: ")   #выбор пользователя (по имени или по номеру)

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name=%s", (name,))   #удалить по имени
    elif choice == "2":
        phone = input("enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))    #удалить по номеру

    conn.commit()
    cur.close()
    conn.close()
    print("deleted")



def main():
    while True:
        print("1. import from CSV")
        print("2. add contact")
        print("3. update contact")
        print("4. search")
        print("5. delete")
        print("0. exit")

        choice = input("choose: ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break


if __name__ == "__main__":    #файл запущен напрямую
    main()