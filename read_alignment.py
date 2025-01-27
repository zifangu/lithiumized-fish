import pandas as pd
import numpy as np

def readAlignment(path: str):

    with open(path) as file:
        content = file.readlines()
        print(content)
        df = []
        for line in content:
            if line == '\n': 
                continue
            if '>' in line: 
                continue
            df.append(line[:-1])
    return df

def main():
    readAlignment('data/ProteinMPNN_sequences.txt')


# Using the special variable 
# __name__
if __name__=="__main__":
    main()
