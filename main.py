#!/usr/bin/python2
import sys
sys.path.insert(0, './Helpers')
from NewsHelper import updateNewsDB
from DocHelper import saveToFile



if __name__ == "__main__":
    updateNewsDB()
    saveToFile()