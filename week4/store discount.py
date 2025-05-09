def read_file():
    with open("data.txt", 'r') as file:
        data = file.readlines()
        # return data
    for line in data:
        line_data= line.strip().split()
        
        print(f"{line_data[0]:<5}|{line_data[1]:<10}|{line_data[2]:<10}|{line_data[3]:<8}|{line_data[4]:<8}|{line_data[5]:<8}")

def id_username():
    identity = []
    first_name = []
    last_name = []
    with open("data.txt", 'r') as file:
        data = file.readlines()
    for line in data:
        line_data= line.strip().split()
        identity.append(line_data[0])
        first_name.append(line_data[1])
        last_name.append(line_data[2])

        print(f"{line_data[0]}- {line_data[1]} {line_data[2]}")

def main():
    while True:
        try:
            print("What info would you like to see?")
            print("1- Print transaction ID and username")
            print("2- Print username, total before and total after discount")
            print("3- Quit program")
            entry = int(input("which part of the data would you like to see 1/2/3: "))
            if entry == 1:
                id_username()
                break
            elif entry == 2:
                read_file()
                break
            elif entry == 3:
                print("Exiting program")
                break
            else:
                print("Invalid input, try again.")
        except ValueError:
            print("Invalid input, Try again.")
main()