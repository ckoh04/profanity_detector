'''

def split_txt():
    file = open("profanities.txt ", "r+")
    filepath = "profanities.txt"
    with open(filepath) as file:
        lines = file.read().splitlines()

    with open(filepath, "w") as file:
        for line in lines:
            file.write(line + ",\n")
            if line == "zipperhead":
                break





if __name__ == "__main__":
    split_txt()
'''