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

# def get_option():
#     print("1: Get text of a page")
#     print("2: Get the number of a page containing a certain text")
#     while True:
#         inp = input()
#         if inp in ('1','2'):
#             return 

if __name__ == "__main__":
    lib = library()
    print("Hello, welcome to the Library of Babel, Here are your options:")
    # option = get_option()
    page_num = get_integer_input("What page number do you want?")
    print("Your page contains:")
    page = lib.get_page(page_num)
    print(page)
