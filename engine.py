from tools import DatabaseHelper, Connections
from time import sleep

# if error
# case invalid / expired details
# switch to next details
# case radius server & # case unavailable
# sleep, retry
# if succesful
# parse time left
# set restart timer


class App:

    def __init__(self):
        self.conn = Connections()
        self.user_details = DatabaseHelper.load_data()
        self.user_details_bak = self.user_details.copy()
        self.sep = '=='*20

    def login(self):
        server_reply = self.conn.post(self.user_details)
        self.parse_response(server_reply, self.user_details)

    def parse_response(self, server_reply, details):
        username = details.keys()[0]

        # case 1 - Unable to connect
        if not server_reply:
            print "Connection Error! "
            print "Check connection settings or gateway is down"
            print "Retrying in 30: "
            sleep(30)
            self.login()

        # case 2 - Radius
        elif 'radius' in server_reply:
            print "Radius server is not responding, retrying in 60..."
            sleep(60)
            self.login()

        # case 3
        if 'invalid' in server_reply:
            print "%s is invalid! " % username
            if self.remove(username):
                self.login()

        # case 4
        elif 'confirm' or 'maximum' in server_reply:
            print self.sep
            print "%s time usage exceeded \n " % username
            print self.sep
            print "Switching to a different account... \n\n"
            self.remove(username)
            print self.sep
            print "sleeping for 30 secs"
            sleep(30)
            self.login()

        # case 5
        elif 'logged in' in server_reply:
            print "%s is already logged in, switching account..."
            self.remove(username)
            self.login()

        # case 6
        elif 'success' in server_reply:
            print 'Sucessfully logged in as %s' % username
            self.remove(username)
            self.monitor_connection()

        else:
            raise TypeError("Unhandled exception!\n" + server_reply)

    def remove(self, user_detail):
        try:
            self.user_details.pop(user_detail)
            print self.sep
            print 'i removed {}'.format(user_detail)
            print self.sep
        except IndexError:
            raise IndexError("You ran out of accounts! ")
        if self.user_details == {}:
            self.user_details = self.user_details_bak.copy()

    def monitor_connection(self):
        while self.conn.is_active():
            sleep(120)
            continue
        self.login()

if __name__ == '__main__':
    test = App()
    test.login()
