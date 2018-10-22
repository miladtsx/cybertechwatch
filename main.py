#!/usr/bin/python2
import sys, thread
sys.path.insert(0, './Helpers')
from NewsHelper import UpdateNewsDB, PrintNews, saveToFile
#from Model import baselineDate
import Model
import time
if __name__ == "__main__":
    # if((len(sys.argv) == 2) and int(sys.argv[1]) > 0 and int(sys.argv[1]) < 7) :
    #     baselineDate = int(sys.argv[1])
    UpdateNewsDB()
    saveToFile()
        #PrintNews()