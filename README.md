# Cheat
A cheatsheet manager

## What is cheat
Cheat is a command written in python to help you manage your cheatsheets. 
Cheat uses YAML, which makes the cheatsheets readable for humans as well as 
easy to interprate for machines.

## Features
- wildcard topics (You can use wildcards to search for topics)
- tags (You can filter out cheat cards using tags)
- YAML (You can easily read and write cheatsheets, as well as your machine)
- Other Cool Stuff you can maybe contribute here?

## What the hell are these things?

### Cheatsheet
A cheatsheet is a set of cheat cards written in YAML format in a file on your 
CHEATPATH...  We'll get through all of these in a second.

### Cheat Card
A cheat card is a single cheat or reminder, which includes three parts:
- Author: Something to give credit to the person who created it
- tags: An array of tags to help you filter out your cards
- text: The actual cheat or reminder

### YAML
> YAML: YAML Ain't Markup Language

> YAML is a human friendly data serialization standard for all programming 
languages.

Taken from [The Official YAML Web Site] (http://yaml.org/) Read more there.

We are using YAML 1.1 using PyYaml. You don't need to know YAML, if you want 
to create cheatsheet just see the cheatsheet on cheat.

You should install `pyYaml` on your `system` or `virtual-environment` in 
order to be able to use the project. you can either use:

    pip install -r requirements.txt

or use:

    pip install pyyaml

later would install latest version of `pyYaml` and first will install the 
latest tested compatible version.

### CHEATPATH
CHEATPATH is an optional Environmental Variable that you can set and point it 
to locations (yes, plural) of your cheatsheets. If none is provided the 
default `/usr/share/cheat/` will be used.

If you want to provide one, add something like this to your .bashrc or .zshrc:

    export CHEATPATH=/place/to/first/loc:/place/to/second/one

### wildcard
A Wildcard is a regular expression thingy that is there helping you find 
stuff. As an example, you may have these cheats:
- cheat1.yaml
- cheat2.yaml
- camel.yaml
- someotherstuff.yaml

Then you can provide these as your caption: `cheat\*` (yes, you have to 
escape special characters or your stupid shell will capture them)
- cheat1.yaml
- cheat2.yaml

`cheat`
- cheat1.yaml
- cheat2.yaml

(yes, by default we add * before and after your topic)

`c\*`
- cheat1.yaml
- cheat2.yaml
- camel.yaml


## MANUAL
Okay, enough about stuff. Here is how it all works...

#### Showing cheats
I'm assuming you have added cheat.py to your PATH.

    cheat.py topic

and that's it. 
Although we can use some flags...

### Show Author -a --author
You can use `-a` or `--author` to display authors. ex:

    cheat.py topic -a

### Show Tags -T --show_tags
See the list of tags for each card using this parameter. ex:

    cheat.py topic -T

### Limit results --count -c
You can limit the cards to certain numbers. ex:

    cheat.py topic -c 5 # Returns only the last 5


### Filter based on tags --tag -t
You can filter the cards by providing tags to look for. ex:

    cheat.py topic -t file

This will bring up any card containing file flag.

You can include more than one flag:

    cheat.py topic -t file -t tips

This will bring any card containing file or tips flags. Note that tags are 
not wildcardified (if that's a word) and you have to type the exact topic. 
Maybe in the future we can improve this somehow?

### Location --location -l
If you want to use a specefic location instead of CHEATPATH or the default 
one, you can present it here. ex:

    cheat.py topic -l /usr/share/cheats/:~/.config/cheat/

### Show --show -s
I really have no idea why I put it here; it's the default behaviour and the 
only way to disable it (so far) is by calling `--add`, which we'll cover in 
the next section.

## Add cards --add 
You can __interactively__ add a card to your cheatsheets using this flag. ex:

    cheat.py --add

### Author --author -a
If you pass this, the command will ask you to provide an author.

### Tags --tag -t
Tags are not added interactively! You have to pass your tags using the 
original commands. ex:

    cheat.py --add -t file -t stuff

### Other commands...
- the `-T` or `--show_tags` still works when printing the card at the end.
- the `--count` or `-c` won't throw any error, although it is ineffective.
- The `--location` or `-l` works as before.


## Contributing
Here are a few things you can contribute to at the moment:

- Improve this README.md file, I beg you!
- Check to see if there is any issue you can solve.
- Improve the code in any way, this has been a night's job
- **PLEASE write cheatsheets if you can, we'll appreciate it**
- Introduce us (and maybe brag a little?) to your friends and enemies. We are 
a pretty new and unknown thing.
- A MAKE file would also be very good!
- Add ideas to how one can contribute.

### Ideas for furthur improvement
You know, things. I'll add this later when I'm awake.

## License
As of now, this cheatsheet is distributed with MIT license.

## Author
Well, of course me, Sajjad Heydari.
