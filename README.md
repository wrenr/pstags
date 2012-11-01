Python STAGS - Simple TAG Sorter (pSTAGS)
======

Save your files with a simple tag prefix, run this script, and your files are in their proper places.

**This script is pre-alpha. Use at your own risk.**


## What does it do?

Your Desktop folder is so full, you forgot what your Desktop picture looks like. Your Downloads folder is a messy pile of thousands -

You roll up your sleeves and slog through the mess, and after two grueling hours you've finally moved every single file to its rightful place. If only you had a quick, simple way to stop that from *ever* happening again...

**Python Simple TAG Sorter (pSTAGS)** to the rescue! Save your files with a simple tag prefix, run the **pSTAGS** script, and your files are in their proper places.

## What do I need to run it?

I've only tested this with Python 2.7.3. If you have an earlier version of Python it might work, and if it doesn't you can upgrade.

You need to know how to run Python scripts from the command line ([Windows](http://docs.python.org/2/faq/windows.html#how-do-i-run-a-python-program-under-windows), [Mac OS X](http://docs.python.org/2/using/mac.html)), and also know how to make [a simple JSON-formatted file](http://www.w3schools.com/json/default.asp) for configuration.

As of Nov. 1st, 2012, you'll also need a Mac OS X or Unix-based computer to run it, I haven't tested it with anything else.

## How do I use it?

### One-time Setup

**pSTAGS** needs to know where to sniff for tagged files with a JSON configuration file. Make a new text file called `tag-sniff.json` that's in the same directory as the `pstags.py` script. Be sure that all of the directories exist on your file system. (If they don't, **pSTAGS** will warn you!) You can also view this example at `tag-sniff.json.default` in the Git repo.

For example: `tag-sniff.json`

```json
    {
        "directories": [
            "/Users/wren/Downloads/",
            "/Users/wren/Desktop/",
            "/Users/wren/Documents/unsorted/"
        ]
    }
```

Declare your list of tags in another JSON config file called `tag-maps.json`.  You can view this example at `tag-maps.json.default` in the Git repo. The JSON key is the tag, and the JSON value is the destination directory:

```json
{
    "errands": "/User/wren/Documents/errands/",
    "pic-cool": "/Users/wren/Pictures/cool/",
    "work": "/Users/wren/Documents/work/",
    "mus-theory": "/Users/wren/Music/theory/"
}
```

### Saving Files with Tags

When you save a file in one of your **pSTAGS** sniffed directories, save the filenames with this structure (no spaces):

* `tagname`
* `->` (separator)
* `file-name.txt`

For example:

    pic-cool->dog-on-a-skateboard-wearing-sunglasses.jpg
    work->BossChristmasFlyer3MonthsTooEarly.doc

Before running the **pSTAGS** script, your files will be sitting in your sniffed directories, looking woefully out of place.

    FILES BEFORE pSTAGS...
    /Users/wren/Downloads/pic-cool->dog-on-a-skateboard-wearing-sunglasses.jpg
    /Users/wren/Documents/work/unsorted/work->BossChristmasFlyer3MonthsTooEarly.doc

### Running the pSTAGS script

Open up the command line. Navigate to the pstags directory and run `python pstags.py`.

Your files are now in the right places, with those clunky tags removed!

    FILES AFTER pSTAGS!
    /Users/wren/Documents/work/BossChristmasFlyer3MonthsTooEarly.doc
    /Users/wren/Pictures/cool/dog-on-a-skateboard-wearing-sunglasses.jpg

#### Script Arguments

`--verbose`
Verbose output

**TODO:** Make the script use the `argparse` python module to make it a proper command line script with more options.

### Does it actually work?

This is a simple script I put together, and it hasn't been exhaustively tested in different environments. It works for the file sorting tasks I've given it, and has some exception handling.

### What are the system requirements?
Tested with the following setup:

* Python 2.7.3
* OS X

This **may** work on other OSes and previous versions of Python, but they have not been tested. Proceed at your own risk.

## Troubleshooting

### Why does it say "File does not exist?"

Create the `tag-sniff.json` and `tag-maps.json` files in the same directory as your `pstags.py` script. You can use the sample files `tag-sniff.json.default` and `tag-maps.json.default` as guides.

### What if I move the directories around?

When the script loads it scans all of the directories given to it and makes sure they all exist before proceeding. You'll have to manually update the `tag-maps.json` file if your directories change.

### What if the file I tagged already exists?

The script will bring up an input prompt confirming if you want to overwrite the file before moving it to its new destination.

## What's next for pSTAGS?

Later on I may add a unit testing suite. I'll also make the script use the [argparse python module](http://docs.python.org/dev/library/argparse.html) so it has a few more command line options.


## License and Warranty

This work is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit [http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/).

Attribute work to name: **Wren Reynolds**

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
