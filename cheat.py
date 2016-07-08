#!/bin/python3
import yaml
import os
import sys
import argparse
import fnmatch

class Card():
    def __init__(self, dic):
        if 'author' in dic:
            self.author = dic['author']
        else:
            self.author = 'N/A'
        if 'tags' in dic:
            self.tags = dic['tags']
        else:
            self.tags = ['default']
        self.text = dic['text']

    def print(self, args):
        ans = ""
        if args.author:
            ans += 'author: ' + self.author + '\n'
        if args.show_tags:
            ans += 'tags: '
            for t in self.tags:
                ans += t + ', '
            ans=ans[:-2] + '\n'
        ans += self.text
        print (ans)

def add(args):
    dic = {}
    if args.author:
        dic.update({'author': input('Author: ')})
    if args.tag:
        dic.update({'tags': args.tag})
    print ("enter your text, empty line to stop: ")
    text = input()
    while not text:
        print("You have to enter at least one line")
        text = input()
    text +=  '\n'
    new_line = input()
    while new_line:
        text += new_line + '\n'
        new_line = input()
    text = text[:-1]
    class literal(str): pass
    def literal_presenter(dumper, data):
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    yaml.add_representer(literal, literal_presenter)
    dic.update({'text': literal(text)})
    c = Card(dic)
    loc = args.location.split(':')[-1]
    with open(os.path.join(loc, args.topic + '.yaml'), 'a') as f:
        f.write(yaml.dump(dic, default_flow_style=False, explicit_start=True))
    c.print(args)

def show(args):
    locs = args.location.split(':')
    cards = []
    pat = '*' + args.topic + '*.yaml'
    for loc in locs:
        for root, dirs, files in os.walk(loc):
            for file in files:
                if fnmatch.fnmatch(file, pat):
                    with open(os.path.join(root, file), 'r') as f:
                        t = yaml.load_all(f)
                        for a in t:
                            cards.append(Card(a))
    if args.tag:
        tag = set(args.tag)
        new_cards = []
        for c in cards:
            if (set(c.tags) & tag): #Intersect
                new_cards.append(c)
        cards = new_cards

    if args.count:
        for i,c in enumerate(cards):
            if i == args.count:
                return
            c.print(args)
        return
    for c in cards:
        c.print(args)

if __name__ == "__main__":
    os.environ.setdefault('CHEATPATH', '/usr/share/cheat/')
    #DEBUG
    #os.environ.setdefault('CHEATPATH', 'cheats/')
    path = os.environ['CHEATPATH'].split(':')
    parser = argparse.ArgumentParser(prog = 'cheats')
    parser.add_argument('topic', help='topic to search for')
    parser.add_argument('--tag', '-t', help='specify tags to search for, could be used more than once', action='append')
    parser.add_argument('--location', '-l', default=os.environ['CHEATPATH'])
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--show','-s', action='store_true',help = 'show cards, optional')
    group.add_argument('--add',  action='store_true', help = 'add a card interactively')
    parser.add_argument('--author', '-a', help='show authors', action='store_true')
    parser.add_argument('--show_tags','-T', help='show tagss', action='store_true')
    parser.add_argument('--count' , '-c',type=int,help='limit the number of results, 0 for unlimited')
    parser.description = "a cheatsheet manager" 
    parser.epilog = "by Sajjad Heydari (MCSHemail@gmail.com), for more info look at the docs!"
    args = parser.parse_args()
    if args.add:
        add(args)
    else: #arg.show
        show(args)

