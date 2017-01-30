import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('board', metavar='N', type=str)

    args = parser.parse_args()

    input = args.board
    input_len = len(input)
    max_crash = input_len * (input_len-1) / 2
    max_crash = int(max_crash)

    crash = 0
    for i in range(input_len):
        for j in range(i+1,input_len):
            ii = int(input[i])
            jj = int(input[j])
            bad = False
            bad = bad or ii == jj
            bad = bad or (ii-i+j == jj)
            bad = bad or (ii+i-j == jj)
            if bad:
                crash+=1
    
    print(max_crash-crash)
