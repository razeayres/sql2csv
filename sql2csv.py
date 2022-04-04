# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)
# and Shawn Shao (shaoh@uoguelph.ca)

from sqlite3 import connect
from sys import argv
from os import path
from time import sleep

class main(object):
    def __init__(self, db, table):
        self.db = db
        self.table = table
        self.run()
    
    def connect(self):
        self.con = connect(self.db)
    
    def get_data(self):
        cur = self.con.cursor()
        self.data = cur.execute("SELECT * FROM " + self.table)
        self.colnames = list(map(lambda x: x[0], self.data.description))
    
    def export2csv(self):
        self.output = self.table + ".csv"
        with open(self.output, 'w') as writer:
            writer.write(",".join(self.colnames) + '\n')
            for i in list(self.data):
                i = ",".join(map(str, i)) + '\n'
                writer.write(i)

    def close(self):
        self.con.close()

    def wait(self):
        while not path.exists(self.output):
            sleep(1)
        sleep(5)

    def run(self):
        self.connect()
        self.get_data()
        self.export2csv()
        self.close()
        self.wait()

args = argv[1:]
main(args[0], args[1])
