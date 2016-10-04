#!/usr/bin/env python3
# Copyright (c) 2016 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

'''
This checks if the HEAD commit's diff is properly formatted
Return value is 0 to indicate no error.

Author: @MarcoFalke
'''

from subprocess import check_call
import os

FOLDER_SCRIPT = os.path.dirname(os.path.abspath(__file__))
CMD_CLANG_FORMAT_DIFF = 'git diff -U0 HEAD~ | {}/clang-format-diff.py -p1 -i -v'.format(FOLDER_SCRIPT)
CMD_GIT_DIFF = ['git', 'diff', '--exit-code']

def main():
  if os.getenv("TRAVIS_PULL_REQUEST", "false") == "false":
    print("No TRAVIS_PULL_REQUEST request")
    exit(0)
  check_call(CMD_CLANG_FORMAT_DIFF, shell=True)
  check_call(CMD_GIT_DIFF)

if __name__ == "__main__":
    main()
