import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # Make a duplicate of an existing file
    if path.exists('textfile.txt'):
        # get path to the file in the current directory
        src = path.realpath('textfile.txt')

        # let's make a backup copy by appending 'bak' to the name.
        # dst = src + ".bak"
        # shutil.copy(src, dst)

        # rename original file
        # os.rename('textfile.txt', 'newfile.txt')

        # now put things into a zip file
        rootDir, tail = path.split(src)
        shutil.make_archive('archive', 'zip', rootDir)

        # more fine-grained control over ZIP files.
        with ZipFile('testzip.zip','w') as newzip:
            newzip.write('newfile.txt')
            newzip.write('textfile.txt.bak')
            newzip.close()


if __name__ == '__main__':
    main()