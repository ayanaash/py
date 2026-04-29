import json
import csv
from connect import get_connection

#add contact
def add_contact(name, email, birthday, group_name):
    conn = get_connection()
    cur = conn.cursor()

    #group
    cur.execute("SELECT id FROM groups WHERE name=%s", (group_name,))  #ищем группу
    g = cur.fetchone()

    if g is None:
        cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group_name,))  #создаём 
        group_id = cur.fetchone()[0]
    else:
        group_id = g[0]

    #contact
    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)   
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (name, email, birthday, group_id))

    conn.commit()
    cur.close()
    conn.close()


#search + filter + sort + pagination
def search_contacts_console():
    conn = get_connection()
    cur = conn.cursor()

    query = input("Search: ")
    group = input("Group (optional): ")
    sort = input("Sort (name/birthday/created_at): ")

    page = 0
    limit = 3   #пагинация (3 записи на страницу)

    while True:
        offset = page * limit

        sql = """
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        WHERE (c.name ILIKE %s OR c.email ILIKE %s)
        """

        params = [f"%{query}%", f"%{query}%"]

        if group:   #фильтр по группе
            sql += " AND g.name = %s"
            params.append(group)

        if sort in ["name", "birthday", "created_at"]:
            sql += f" ORDER BY c.{sort}"

        sql += " LIMIT %s OFFSET %s"
        params.extend([limit, offset])

        cur.execute(sql, params)
        rows = cur.fetchall()

        if not rows:
            print("No results")
            break

        print("\n--- PAGE", page, "---")
        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            page += 1
        elif cmd == "prev" and page > 0:
            page -= 1
        else:
            break

    cur.close()
    conn.close()


#export json
def export_json():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    """)

    rows = cur.fetchall()

    data = {}

    for r in rows:
        name = r[0]

        if name not in data:   #создание структуры контакта
            data[name] = {
                "email": r[1],
                "birthday": str(r[2]),
                "group": r[3],
                "phones": []
            }

        if r[4]:
            data[name]["phones"].append({    #добавление телефона в список
                "number": r[4],
                "type": r[5]
            })

    with open("contacts.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Exported to contacts.json")

    cur.close()
    conn.close()


#import json
def import_json():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for name, info in data.items():

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))   #проверка есть ли уже контакт
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")  #поиск, ввод
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))  #удаление старого контакта

        add_contact(name, info["email"], info["birthday"], info["group"])

        for p in info["phones"]:   #теперь добавляем телефоны
            cur.execute("CALL add_phone(%s,%s,%s)", (name, p["number"], p["type"]))

    conn.commit()
    cur.close()
    conn.close()


#import csv
def import_csv():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            add_contact(
                row["name"],
                row["email"],
                row["birthday"],
                row["group"]
            )

            cur.execute(
                "CALL add_phone(%s::varchar, %s::varchar, %s::varchar)",
                (row["name"], row["phone"], row["type"])
            )
            

    conn.commit()
    cur.close()
    conn.close()


#menu
def main():
    while True:
        print("\n1.Add Contact")
        print("2.Search")
        print("3.Export JSON")
        print("4.Import JSON")
        print("5.Import CSV")
        print("6.Exit")

        choice = input("> ")

        if choice == "1":
            add_contact(
                input("Name: "),
                input("Email: "),
                input("Birthday (YYYY-MM-DD): "),
                input("Group: ")
            )
        elif choice == "2":
            search_contacts_console()
        elif choice == "3":
            export_json()
        elif choice == "4":
            import_json()
        elif choice == "5":
            import_csv()
        elif choice == "6":
            break


if __name__ == "__main__":
    main()