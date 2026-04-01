from connect import connect


def search():
    pattern = input("enter pattern: ")

    conn = connect()
    cur = conn.cursor()   #connect to base
    
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))   #вызываем
    rows = cur.fetchall()    #получаем все

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def upsert():
    name = input("enter name: ")
    phone = input("enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

    print("done")


def bulk_insert():
    names = input("Enter names: ").split(",")
    phones = input("Enter phones: ").split(",")

    conn = connect()
    cur = conn.cursor()

    cur.execute(    #передача массивов
        "CALL bulk_insert(%s, %s)",
        (names, phones)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("bulk insert done")


def pagination():  #разбиение данных
    limit_val = int(input("enter limit: "))
    offset_val = int(input("enter offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts(%s, %s)",
        (limit_val, offset_val)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete():
    value = input("enter name / phone to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()

    print("deleted")


def main():
    while True:
        print("1. Search")
        print("2. Insert/Update (Upsert)")
        print("3. Bulk Insert")
        print("4. Pagination")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search()
        elif choice == "2":
            upsert()
        elif choice == "3":
            bulk_insert()
        elif choice == "4":
            pagination()
        elif choice == "5":
            delete()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()