import csci2300, csci2600, shelve, sys, holder, emailer
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def main():
    # Check Algos for new assignments
    algos = csci2300.Csci2300()
    set2300 = algos.checkData()

    # Check PSoft for new assignments
    psoft = csci2600.Csci2600()
    set2600 = psoft.checkData()

    if len(sys.argv) == 2:
        if (sys.argv[1] == "-add"):
            email = raw_input("Enter user email --> ")
            classes = []
            while (True):
                x = raw_input("Enter class to get notifications for (2300/2600) --> ")
                # Makes sure command given is a class we can notify for.
                if (x == '2300' or x == '2600'):
                    classes.append(x)
                elif (x == '-1'):
                    print "Exiting loop...\n"
                    break
                else:
                    print "Invalid choice: '-1' to exit..."

            # Open shelve to store new user data.
            x = shelve.open('users.db')
            data = x['data']
            data[email] = list(set(classes))    # lame check for duplicates
            x['data'] = data
            x.close()

    x = shelve.open('users.db')

    # Error checking: If no key 'data' in shelf, create empty dataset
    if 'data' not in x:
        x['data'] = {}

    # Saves all user data into variable data to go through and email.
    data = x['data']
    x.close()

    for key in data:
        emailer.Emailer(key, data[key], set2300, set2600).sendEmail()

    if len(data) == 0:
        print "No users, please run with '-add' flag"

    if len(set2600) == 0:
        print "No assignments"

    else:
        for key in set2600:
            print "%s : %s" %(key, set2600[key])

    print holder.Holder().email



if __name__ == '__main__':
    main()
