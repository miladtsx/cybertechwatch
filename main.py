#!/usr/bin/python2
import sys, thread
sys.path.insert(0, './Helpers')
from NewsHelper import UpdateNewsDB, PrintNews, saveToFile
import Model


if __name__ == "__main__":
    UpdateNewsDB()
    saveToFile()