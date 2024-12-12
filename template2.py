example1 = """"""
example2 = """"""
puzzle = """"""

import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tests', 
                        action='store_true', 
                        help='Run all tests')
    
    parser.add_argument('--test1', 
                        action='store_true', 
                        help='Run test 1')
    
    parser.add_argument('--test2', 
                        action='store_true', 
                        help='Run test 2')
    parser.add_argument('--solve', 
                        action='store_true', 
                        help='Solve all')
    
    parser.add_argument('--solve1', 
                        action='store_true', 
                        help='Solve 1')
    
    parser.add_argument('--solve2', 
                        action='store_true', 
                        help='Solve 2')
    
    return parser.parse_args()


from color import Color

def solve1(p) -> int:
    pass

def solve2(p) -> int:
    pass

if __name__ == '__main__':
    args = get_args()
    if args.test1 or args.tests:
        print(solve1(example1))
        # print(solve1(example2))

    if args.solve1 or args.solve:
        print(solve1(puzzle))

    if args.test2 or args.tests:
        print(solve2(example1))
        # print(solve2(example2))

    if args.solve2 or args.solve:
        print(solve2(puzzle))

