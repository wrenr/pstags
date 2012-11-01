#!/usr/bin/env python


class prompter:

    def getValidInput(self, prompt, valid):
        # Loops until we get input from the user prompt matching valid.
        # params:
        # prompt - the prompt to show the user during input.
        # valid - a list of valid responses (all lowercase)
        selection = ''
        first_time = True

        while selection not in [i.lower() for i in valid]:
            if not(first_time):
                print "Invalid Selection, please try again."
            else:
                first_time = False
            selection = raw_input(prompt)
            selection = selection.lower().strip()

        return selection
