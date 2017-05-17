import sys
def main():
    entry_num = int(raw_input("Enter session count: "))
    while True:
        print "\n------- MESSAGE: enter summoner name or 'quit' to exit program -------"
        username = raw_input("Enter: ")
        if username == "quit":
            return

        if check_usernames(username) is False:
            while True:
                print "------- MESSAGE: enter attributes or 'reset' for reset summoner name -------"
                entry = raw_input("Enter: ")
                if entry == "reset":
                    break
                if add_entry(entry) is True:
                    f = open("usernames.txt", "a")
                    f.write(username + "\n")
                    f.close()

                    entry_num += 1
                    print "------- MESSAGE: no." + str(entry_num) + " summoner " + username + " is added to database -------"
                    break

def check_usernames(username):
    f = open("usernames.txt")
    found = False
    for line in f.readlines():
        if username == line.strip():
            found = True
            print "------- ERROR: summoner found in database -------"
            f.close()
    return found

def add_entry(entry):
    entry_list = entry.split(',')
    if len(entry_list) != 11:
        print "------- ERROR: length of attributes is not correct -------"
        return False

    f = open("database.txt", "a")
    f.write(entry + "\n")
    f.close()
    return True

if __name__ == "__main__":
    main()
