def user_input():
    filename = input("Enter your file name:")
    name = input("Enter your first and last name:")
    address = input("Enter your address:")
    phone = input("Enter your phone number:")
    return filename, name, address, phone
def write_to_file(filename, name, address, phone):
  with open(filename, 'w') as file:
        file.write(f"{name},{address},{phone_number}")

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        return contents

def display_contents(contents):
    print("File contents:")
    print(contents)

filename, name, address, phone_number = user_input()

write_to_file(filename, name, address, phone_number)

file_contents = read_file(filename)
display_contents(file_contents)
  