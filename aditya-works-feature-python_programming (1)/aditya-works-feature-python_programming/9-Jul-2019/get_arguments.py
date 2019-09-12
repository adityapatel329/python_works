#Read readme for how to run this program
import argparse 
parser=argparse.ArgumentParser()
parser.add_argument("--operation","-o",help="Select the Operation to be performed",choices=["read","write","copy","re_name","delete_file","nlines","display"])
parser.add_argument("--filename","-fn",help="Write a file name")
parser.add_argument("--outputname","-on",help="Write a outputfile name")
parser.add_argument("--writing","-wn",help="Write a paragraph or word")
args=parser.parse_args()

