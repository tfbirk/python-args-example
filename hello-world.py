""" Sample Hello World script with input parameters """

from optparse import OptionParser
import sys

def process_options():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option(
                        "-n",
                        "--name",
                        type="string",
                        dest="person_name",
                        help="name to say hello to", 
                        metavar="PERSON_NAME")
    parser.add_option("-d",
                      "--debug",
                      action="store_true",
                      dest="debug",
                      help="print debug statements")
    (options, args) = parser.parse_args()
    
    if options.debug:
        print "[DEBUG] Options: ", options
        print "[DEBUG] Args: ", args
    return options

def main():
    print "[DEBUG] sys.argv[1:] = {}\n".format(sys.argv[1:])
    options = process_options()
    if options.person_name:
        print "\nHello {}!".format(options.person_name)
    else:
        print "\nHello World!"

if __name__ == "__main__":
    main()