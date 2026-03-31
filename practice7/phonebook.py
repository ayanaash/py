import csv
from connect import connect


#1 insert from CSV
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                (row["first_name"], row["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV!")


#2 insert from cons(input)
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added!")


#3 update
def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (Enter to skip): ")
    new_phone = input("New phone (Enter to skip): ")

    conn = connect()
    cur = conn.cursor()

    if new_name:
        cur.execute(
            "UPDATE phonebook SET first_name=%s WHERE first_name=%s",
            (new_name, name)
        )

    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE first_name=%s",
            (new_phone, name)
        )

    conn.commit()
    cur.close()
    conn.close()
    print("Updated!")


#4 search
def search_contacts():
    keyword = input("Enter name or phone prefix: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone LIKE %s",
        (f"%{keyword}%", f"{keyword}%")
    )

    results = cur.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No results")

    cur.close()
    conn.close()


#5 delete
def delete_contact():
    choice = input("Delete by (1) name or (2) phone: ")

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE first_name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted!")



def main():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Import from CSV")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Search")
        print("5. Delete")
        print("0. Exit")

        choice = input("Choose: ")

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


if __name__ == "__main__":
    main()