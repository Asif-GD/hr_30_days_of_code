phone_book = dict()


def build_phone_book(name_number: [str]) -> None:
    split_name_number = name_number.split()
    phone_book[split_name_number[0]] = int(split_name_number[1])


def search_phone_book(name: [str]) -> None:
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not found")


n = int(input("Enter the number of phone book entries: ").strip())
for number in range(n):
    phone_book_entry = input("Enter the name and number to be added [name 8_phone_number]: ").lower()
    build_phone_book(name_number=phone_book_entry)

# print(phone_book)
while True:
    try:
        name_to_find = input("Enter the name to look up: ").lower()
        search_phone_book(name=name_to_find)
    except EOFError:
        break