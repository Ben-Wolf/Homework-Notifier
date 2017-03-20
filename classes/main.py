import csci2300, csci2600, shelve, sys, holder, emailer, time

def main():
    test = False

    if len(sys.argv) == 2:
        # Add a user to the database
        if (sys.argv[1] == "-add"):
            email = raw_input("Enter user email --> ")
            classes = []
            while (True):
                x = raw_input("Enter class to get notifications for (2300/2600) --> ")
                # Makes sure command given is a class we can notify for.
                if (x == '2300' or x == '2600'):
                    classes.append(x)
                elif (x == '-1'):
                    break
                else:
                    print "Invalid choice: '-1' to exit..."

            # Open shelve to store new user data.
            x = shelve.open('users.db')
            data = x['data']
            data[email] = list(set(classes))    # lame check for duplicates
            x['data'] = data
            x.close()

            print "%s added to database, please rerun." %email
            sys.exit()

        # Reset the contents of the database
        if (sys.argv[1] == "-reset"):
            x = shelve.open('users.db')
            x['data'] = {}
            x.close()

        # Get contents of database
        if (sys.argv[1] == "-get"):
            x = shelve.open('users.db')
            if (x['data']):
                for key in x['data']:
                    print key
            x.close()
            sys.exit()

        # Returns all possible commands
        if (sys.argv[1] == "-help"):
            print "Recognized commands:\n"
            print "'-add' to add a new user to the database"
            print "'-get' to get all the users in the database"
            print "'-reset' to reset the contents of the database"
            print "'-test' to send a test email to all users"
            sys.exit()

    x = shelve.open('users.db')

    # Error checking: If no key 'data' in shelf, create empty dataset
    if 'data' not in x:
        x['data'] = {}

    # Saves all user data into variable data to go through and email.
    data = x['data']
    x.close()

    if len(sys.argv) == 2:
        # Send test email
        if (sys.argv[1] == "-test"):
            test = True
            for key in data:
                emailer.Emailer(key, data[key], {}, {}, test).sendEmail()
            sys.exit()

    while(True):
        # Check Algos for new assignments
        algos = csci2300.Csci2300()
        set2300 = algos.checkData()
        algos.addData()

        # Check PSoft for new assignments
        psoft = csci2600.Csci2600()
        set2600 = psoft.checkData()
        psoft.addData()

        for key in data:
            emailer.Emailer(key, data[key], set2300, set2600, test).sendEmail()

        print("Continuing to check once a day. CTRL + C to exit.")
        time.sleep(86400)

if __name__ == '__main__':
    main()
