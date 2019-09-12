import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--number1","-n1",help="FirstNumber",type=int)
parser.add_argument("--number2","-n2",help="SecondNUmber",type=int)
parser.add_argument("--operation","-o",help="Operation to be performed",choices=["add","sub","mul"])
args=parser.parse_args()
