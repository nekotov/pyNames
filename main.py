#!/usr/bin/python3

#  MIT License
#
#  Copyright (c) 2022 Dembytskyi Pavlo
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import threading
import requests


def selections(seq, n):
    if n == 0:
        yield []
    else:
        for i in range(len(seq)):
            for ss in selections(seq, n - 1):
                yield [seq[i]] + ss


iterable = '0123456789_abcdefghijklmnopqrstuvwxyz'


def run(first_char):
    print('Starting thread for {}'.format(first_char))
    sel = list(selections(iterable, 2))

    for item in sel:
        s = first_char+"".join(item)
        response = requests.get("https://api.mojang.com/users/profiles/minecraft/{0}".format(s))
        if response.status_code == 204:
            print("[INFO] {0} is not taken.".format(s))
        elif response.status_code == 404:
            return -1


threads = []
if __name__ == "__main__":
    for i in range(len(iterable)):
        t = threading.Thread(target=run, args=(iterable[i],))
        threads.append(t)
        t.start()

    threads[-1].join()
