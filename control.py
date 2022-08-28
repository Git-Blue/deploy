#! /usr/bin/env python

import argparse
import sys
import pwd

def foo(args):
    print("OK")
    with open(args.file, 'r') as file_object:
        line = file_object.readline()
        print(line)
    # print(len(args.file.readlines()))
    # args.file.close()

# main
def main():
    parser = argparse.ArgumentParser(prog='manager',
                                    usage='%(prog)s [actions]',
                                    description='service control command tools.')

    # group = parser.add_argument_group('group')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    subparsers = parser.add_subparsers(help='action [options]', dest='subparser_name')

    parser_a = subparsers.add_parser('start', help='start help')
    # parser_a.add_argument('bar', type=int, help='bar help')
    parser_a.add_argument('--file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=False)

    parser_b = subparsers.add_parser('stop', help='stop help')
    # parser_b.add_argument('bar', type=int, help='bar help', required=False)
    parser_b.add_argument('--file', required=False)

    # parser.print_help()
    parser_b.set_defaults(func=foo)
    args = parser.parse_args()
    print(vars(args))
    # parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
    # if vars(args).get("start") :
    #     print()
    args.func(args)

if '__main__' == __name__:
    main()