from db import find_all_users, add_user


def main():
    print("===== Welcome to CRM Application =====")
    print("[S]how all customers infomation")
    print("[A]dd new customer")
    print("[Q]uit")
    print("======================================")

    command = input("Your command > ")

    while command != "q":
        if command == "s":
            print("顧客一覧を表示します")

            for user in find_all_users():
                name = user[0]
                age = user[1]

                print(f"Name: {name} Age: {age}")

        elif command == "a":
            print("新規の顧客情報を追加します")
            name = input("New customer's name? > ")
            age = input("New customer's age? > ")

            add_user(name, age)
            print(f"Add new customer {name}")
        else:
            print(f"{command}: command not found")

        command = input("Your command > ")

    print('Bye')


if __name__ == "__main__":
    main()