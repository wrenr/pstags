#!/usr/bin/env python
#
# pSTAGS Python Simple TAG Sorter
#
# Author: Wren Reynolds
# Author URL: https://github.com/wrenr/
# License: Creative Commons Attribution 3.0 Unported License
# License URL: http://creativecommons.org/licenses/by/3.0/

from os import chdir
from os import path
from os import walk
from re import split
from sys import argv
from shutil import move

import myfilejson
from prompter import prompter


class pstags:
    config_fname = "tag-sniff.json"
    tagmaps_fname = "tag-maps.json"
    prompter = prompter()
    verbose = False

    def __init__(self):
        self.setArgs()
        my_json = myfilejson.myfilejson(verbose=self.verbose)

        config = my_json.loadJSON(self.config_fname)
        tags = my_json.loadJSON(self.tagmaps_fname)

        self.validateDirs(config_fname=self.config_fname, tagmaps_fname=self.tagmaps_fname, directories=config["directories"], tags=tags)

        my_json.sortFileJSON(config, self.config_fname)
        my_json.sortFileJSON(tags, self.tagmaps_fname)

        self.sortByTag(config["directories"], tags)

    def setArgs(self):
        for arg in argv[1:]:
            if arg == "--verbose":
                self.verbose = True

    def sortByTag(self, directories, tags):
        # Moves files into their destinations by tag.
        # params:
        # directories - list of directories
        # tags - object of tags in { tag: path } format.

        for directory in directories:

            chdir(directory)
            if self.verbose:
                print "current directory is " + directory

            my_files = []
            # save a list all files in the directory root
            for (dirpath, dirname, filenames) in walk(directory):
                my_files.extend(filenames)
                # To get the top dir just break the first time it yields
                # http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
                break

            #go through each file and see if it has a tag
            for old_name in my_files:

                # Skip any system files
                if old_name[0] == ".":
                    continue

                if self.verbose:
                    print "Checking file " + old_name

                # break the filename for the tag
                tag_splits = split(r"^(.+)\-\>(.+)", old_name)

                if len(tag_splits) > 1:  # a match exists
                    tag_name = tag_splits[1]  # result at 0 is an empty string since it's at the start of the string
                    new_name = tag_splits[2]
                    if tag_name in tags:  # ensure the tag exists
                        self.moveWithWarning(directory + old_name, tags[tag_name] + new_name)

    def validateDirs(self, config_fname, tagmaps_fname, directories, tags):
        # Ensure all directory paths used are valid.

        if len(directories) < 1:
            raise invalidDir("No directories to scan in config file " + config_fname)

        for directory in directories:
            if not path.isdir(directory):
                raise invalidDir("Invalid path " + directory + " in config " + config_fname)

        for tag in tags:
            tagpath = tags[tag]
            if not path.isdir(tagpath):
                raise invalidDir("Invalid path " + tagpath + " in config " + tagmaps_fname)

    def moveWithWarning(self, old_location, new_location):
        # Ensures the file is not overwritten if it exists.

        if (path.exists(new_location)):
            selection = self.prompter.getValidInput(
                "File " + new_location + " Exists. Overwrite (Y/N)? ",
                ['y', 'n']
            )
            if (selection == 'y'):
                move(old_location, new_location)
                print old_location + " moved to " + new_location
        else:
            move(old_location, new_location)
            print old_location + " moved to " + new_location


class invalidDir(Exception):
    pass


my_sorter = pstags()
