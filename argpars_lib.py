import argparse


#processes command line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # add a parameter to your script and help information about it
    parser.add_argument("--number1", type = int, help ="first number")
    parser.add_argument("--number2", type = int, help="second number")
    #parser.add_argument("--operation", help="operation to invoke")
    # restrict the choices of the --operation input
    parser.add_argument("--operation", help="operation", \
                        choices=["add", "subtract", "multiply"])
    #example how to add an optional parameter with --
    parser.add_argument("--optional_operation", help = " optional argument is passed with -- before the argument's name")
    args = parser.parse_args()
    #call from command line: python arpars_lib.py -h to get the help
    # supports positional and optional arguments

    print(args.number1)
    print(args.number2)
    print(args.operation)
    print(args.optional_operation)

    #pass param into the script
    #python argpars_lib.py 4 5 add from command line
    #all parameters are passed as a string
    # n1=int(args.number1)
    # n2=int(args.number2)
    result = None
    if args.operation == "add":
        result = args.number1 + args.number2
    elif args.operation == "subtract":
        result = args.number1 - args.number2
    elif args.operation == "multiply":
        result = args.number1 * args.number2
    else:
        result = args.number1/args.number2

    print('Result of the operation {0} is {1}'.format(args.operation,result))


    #function call from command prompt
    #python argpars_lib.py --number1 4 --number2 5 --operation add