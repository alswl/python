""" Card Extension

Write every day note to user defined directory with your GUI editr.
"""

import os
from datetime import datetime
from subprocess import call

from albertv0 import iconLookup, Item, FuncAction

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Card"
__version__ = "0.1"
__trigger__ = "card"
__author__ = "alswl"
__dependencies__ = []

iconPath = iconLookup('gvim')

DIR_PATH = 'Desktop/md/card'
APP = "gvim"

def handleQuery(query):
    if not query.isTriggered:
        return
    results = []
    results.append(
        Item(
            id="card",
            icon=iconPath,
            text="Card",
            subtext="open today card",
            completion='card',
            actions=[
                FuncAction("Write", open_markdown),
            ]
        )
    )
    return results

def open_markdown():
    now = datetime.now()
    dir_name = "" + now.strftime('%Y-%m')
    dir_path = os.path.join(os.environ.get('HOME'), DIR_PATH, dir_name)
    file_name = now.strftime('%Y-%m-%d' + '.md')
    file_path = os.path.join(dir_path, file_name)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    os.chdir(dir_path)
    call(APP + " " + file_path, shell=True)

def test_open_markdown():
    open_markdown()

if __name__ == '__main__':
    test_open_markdown()
