import sys
import json
import os
from collections import defaultdict

# Static Variables
menu_header = ["Main Menu", "Companies matching search", "Available Sectors:"]
menu_footer = ["  Q:  Exit/Quit", "  M:  Go back to main menu", "  M:  Go back to main menu"]
main_menu = ["Lookup Company by Stock Symbol", "Find Company by Name", "Find Company by Sector", "Popular Companies"]
company_info = ["Company Name: ", "Stock Symbol: ", "Description: ", "CEO: ", "Website: "]

# Empty Global Dictonaries
symboldict = {}
namedict = {}
sectordict = {}
populardict = {}


def main():
    cwd = getcwd()
    makedicts(cwd)
    for k, v in populardict.items():
        print("%s: %s" % (k, v))

# Company Name (Key) with Stock Symbol as secondary
# Sectors (Key) with Company Names as lists

    menumodel = 0
    run = True
    while run:
        header(menumodel)
        menu(menumodel)
        footer(menumodel)
        ui = userinput(menumodel)
    return 0


def getcwd():
    # get current working dir
    cwd = os.getcwd()
    # path join for correct folder
    cwd = os.path.join(cwd + '\companies')
    return cwd


# creates file list to search though for
def makedicts(cwd):
    global symboldict, namedict, sectordict

    from collections import defaultdict
    holder = defaultdict(list)

    # next will only search starting dir
    getjson = [next(os.walk(cwd))]

    for root, directory, files in getjson:
        for filename in files:
            if filename.count(".") == 1:
                # grab json contents
                filejson = json.load(open(os.path.join(root, filename)))
                # update symbol key dict
                symboldict.update({filejson['symbol']: filejson})
                # update name key dict
                namedict.update({filejson['companyName']: filejson['symbol']})
                # Update popular key dict
                populardict.update({filejson['symbol']: 0})
                # update sector key dict as well as list internal lists
                if filejson['sector'] is not None and filejson['sector'] is not '':
                    for sector, companyName in sectordict:
                        holder[filejson['sector']].append((filejson['companyName']))
    print(sectordict)


# Menu creation model to work with all possible variations.
def menu(menumodel, menuopts=None):

    # Went with enumerate since index variables are non-pythonic, but wanted to generate the menu values on the fly
    for index, opt in enumerate(menuopts if menuopts else main_menu):
        print("  " + str(index + 1) + ":  " + opt)


def header(menumodel):
    print(menu_header[menumodel])


def footer(menumodel):
    print(menu_footer[menumodel])


def userinput(menumodel):
    userinput = input("Enter your choice:   ")
    clearconsole()
    return userinput


# Handle console clear on all systems
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    sys.exit(main())
