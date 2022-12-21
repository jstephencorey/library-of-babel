from Library import library

def get_integer_input(message):
    while True:
        try:
            print(message)
            num = input(message)
            num = int(num)
            return num
        except:
            continue

if __name__ == "__main__":
    lib = library()
    print("Hello, welcome to the Library of Babel, do you want to look up a book?")
    page_num = get_integer_input("What page number do you want?")
    print("Your page contains:")
    page = lib.get_page(page_num)
    print(page)
