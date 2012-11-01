#!/usr/bin/env python

import json


class myfilejson:
    verbose = False

    def __init__(self, verbose):
        self.verbose = verbose

    def loadJSON(self, fname):
        # Loads json from file, validates file and JSON.
        try:
            myfile = open(fname, 'r')
        except IOError:
            raise noFile("File " + fname + " does not exist.")

        json_str = myfile.read()

        if len(json_str) < 1:
            myfile.close()
            raise noJSON(myfile, "File " + fname + " has no JSON data.")

        try:
            config = json.loads(json_str)
        except Exception:
            myfile.close()
            raise invalidJSON(myfile, "JSON in " + fname + " is invalid.")

        if self.verbose:
            print "File " + fname + " loaded. File Data:"
            print json_str

        myfile.close()
        return config

    def sortFileJSON(self, json_data, fname):
        #Sorts JSON by key within a file and saves it.

        myfile = open(fname, 'w')

        json_output = json.dumps(json_data, indent=4, sort_keys=True)

        myfile.write(json_output)
        myfile.close()


class noFile(Exception):
    pass


class noJSON(Exception):
    pass


class invalidJSON(Exception):
    pass
