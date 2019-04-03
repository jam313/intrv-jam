#!/usr/bin/env python
import os
from os.path import splitext
import sys
from sqlalchemy import create_engine
import pandas as pd


def main(argv):
    try:
        file_name = argv[0]
        if file_name == 'test1.txt':
            delim = ','
            header = 'infer'
            names = None
        elif file_name == 'test2.txt':
            delim = '|'
            header = None
            names = ['Team', 'Home Field', 'Address', 'City', 'Phone', 'Website (En)', 'Website (Sp)']
        else:
            raise Exception('Unhandled file')

        working_dir = os.getcwd()

        engine = create_engine('sqlite:///{}\\db.sqlite'.format(working_dir))

        data_frame = pd.read_csv(file_name, sep=delim, header=header, names=names, skipinitialspace=True,
                                 engine='python', error_bad_lines=False)
        data_frame.to_sql(splitext(file_name)[0], con=engine, if_exists='replace')
    except Exception as e:
        print(e)
        print('Usage: intrv_jam.py [test1.txt|test2.txt]')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
