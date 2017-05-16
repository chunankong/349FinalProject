def main():
    entry_num = int(raw_input("Enter session count: "))
    while True:
        print "------- MESSAGE: enter summoner name or 'quit' to exit program -------"
        username = raw_input("Enter: ")
        if username == "quit":
            return

        if check_usernames(username) is False:
            while True:
                print "------- MESSAGE: enter attributes or 'format' for format -------"
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
            print("------- ERROR: summoner found in database -------")
            f.close()
    return found

def add_entry(entry):
    if entry == "format":
        print("@attribute 'preferred position' {top,jungle,mid,adc,support}\n" +
            "@attribute 'current rank(%of top)' numeric\n" +
            "@attribute 'recent P/kill' numeric\n" +
            "@attribute 'highest champ gold' numeric\n" +
            "@attribute 'highest champ cs' numeric\n" +
            "@attribute 'avg turrent' numeric\n" +
            "@attribute 'avg dmg' numeric\n" +
            "@attribute 'number of seasons' numeric\n" +
            "@attribute 'number of recent teammates' numeric\n" +
            "@attribute '# of games played with most played champion' numeric\n" +
            "@attribute 'overall winrate' {high,medium,low}")
        return False

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
