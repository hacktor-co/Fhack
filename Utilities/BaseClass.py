import sys
from time import sleep

def ShowProgress(statement, len):
    for i in range(len):
        percentage = (i / float(len))
        time_msg = "\r" + statement + " => {0:.0%}".format(percentage)
        sys.stdout.write(time_msg)
        sys.stdout.flush()
