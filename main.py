#!/usr/bin/python2
import sys
sys.path.insert(0, './Helpers')
from NewsHelper import UpdateNewsDB, PrintNews

if __name__ == "__main__":
    UpdateNewsDB()
    PrintNews()