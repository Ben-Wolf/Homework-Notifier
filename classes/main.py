import csci2300, shelve, sys, holder
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def main():
    # Check Algos for new assignments
    algos = csci2300.Csci2300()
    sendSet = algos.checkData()

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

    print data

    if len(data) == 0:
        print "No users, please run with -add flag"

    if len(sendSet) == 0:
        print "No assignments"

    else:
        for key in sendSet:
            print "%s : %s" %(key, sendSet[key])

    print holder.Holder().email



if __name__ == '__main__':
    main()
