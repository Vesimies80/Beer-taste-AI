#######################################################
# THIS IS A SIMPLE TEXT FILE EDITOR AND READING PROGRAM
#######################################################

def string_list_of_string_to_string(original):
# Yes the name is funny
    slist = original.split(",")
    string = ""
    for item in slist:
        text = item.strip()
        if item == slist[-1]:
            string += text
        else:
            string += f"{text},"

    return string

def main():
    file_lines = []
    beer_name_list = []
    file = open("beer_data.txt", mode="r")
    for line in file:
        file_lines.append(line)
        line = line.split(";")
        beer_name_list.append(line[0])
    file = open("beer_data.txt", mode="w")
    print("This is a python script for adding and reviewing the current BEER DATA file.")
    print("If you do not know the answer to the question enter NO, if there are none answer with only enter")
    print("For multiple answers divide them with the , sign (whitespaces dont matter)")
    while True:
        command = input("Enter number 1 to add a new Beer, Enter number 2 to list all known beers, Enter 3 to remove a Beer, Enter q to quit the program: ")
        if command == "1":
            beer_name = input("Enter BEER NAME: ")
            if beer_name in beer_name_list:
                print("Beer already exists")
                continue
            beer_type = input("Enter BEER TYPE (IPA, wheat, lager etc.): ")
            malt_type = input("Enter MALT TYPE(s) (Pilsner, wheat, Caramel 50 etc.): ")
            hop_type = input("Enter HOP TYPE(s) (Citra, Tettnang etc.): ")
            alcohol = input("Enter alcohol amout in % (4.6 use dot not ,): ")
            bitterness = input("Enter BITTERNESS (IBU): ")
            malt_number = input("Enter how malty (1-5): ")
            hop_number = input("Enter how hoppy (1-5): ")
            grade = input("Enter GRADE for beer (1-10): ")
            
            print("################################################ \n")
            print("Beer name: ", beer_name)
            print("Beer type:",beer_type)
            print("Malt type(s):",malt_type)
            print("Hop type(s):", hop_type)
            print("Alcohol %:", alcohol)
            print("Bitterness (IBU):", bitterness)
            print("Malt amount (1-5):", malt_number)
            print("Hop amount (1-5):", hop_number)
            print("Total grade:", grade)
            correction = input("Is all the information above correct? If not write NO, else write YES (or anything but NO): ")
            if correction == "NO":
                continue
            else:
                malt_text = string_list_of_string_to_string(malt_type)
                hop_text = string_list_of_string_to_string(hop_type)
                beer_line = f"{beer_name};{beer_type};{malt_text};{hop_text};{alcohol};{bitterness};{malt_number};{hop_number};{grade}"
                file_lines.append(beer_line)
                beer_name_list.append(beer_name)
                print("Beer added\n")
        elif command == "2":
            for beer in file_lines:
                if beer == file_lines[0]:
                    continue
                beer = beer.split(";")
                print("\nBeer name:", beer[0],"\nBeer Type:", beer[1],"\nMalt type(s):", beer[2],"\nHop type(s):", beer[3], "\nAlcohol: ",beer[4],"\nBitterness",beer[5],"\nMalt grade (1-5):",beer[6],"\nHop grade (1-5):", beer[7],"\nOverall grade:",beer[8])
        elif command == "3":
            delete_this = input("Enter BEER NAME to be deleted: ")
            if delete_this not in beer_name_list:
                print("Name not found.\n")
            else:
                index = beer_name_list.index(delete_this)
                file_lines.pop(index)
                beer_name_list.pop(index)
        elif command == "q":
            print("Thank you for using this program")
            for new_line in file_lines:
                if new_line == file_lines[-1]:
                    file.write(f"{new_line}")
                else:
                    file.write(f"{new_line}\n")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()