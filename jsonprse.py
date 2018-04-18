import sys
import json
import os


# Static Variables
menu_header = ["Main Menu", "Companies matching search", "Available Sectors:", "Most Popular Companies"]
menu_footer = ["  Q:  Exit/Quit", "  M:  Go back to main menu"]
main_menu = ["Lookup Company by Stock Symbol", "Find Company by Name", "Find Company by Sector", "Popular Companies"]
company_info = ["Company Name: ", "Stock Symbol: ", "Description: ", "CEO: ", "Website: "]


# Empty Global Dictonaries
symboldict = {}
namedict = {}
sectordict = {}
populardict = {}
currentmenu = {}


def main():
    cwd = getcwd()
    makedicts(cwd)

    menumodel = 0

    while True:
        header(menumodel)
        menu(menumodel)
        footer(menumodel)
        ui = userinput()
        menucontrol(ui)

    return 0


def menucontrol(ui, switcher=None):
    if switcher is None:
        switcher = {
            '1': lookup,
            '2': byname,
            '3': bysector,
            '4': bypopular,
            'Q': exitquit
        }

        # get function name
        process = switcher.get(ui)
        # execute correct function
        process()
    return

def lookup():
    currentmenu = symboldict
    for k, v in currentmenu.items():
        print("%s: %s" % (k, v))
    ui = userinput()
    print(company_info[0] + ": " + currentmenu[ui.casefold()])

def byname():
    print("byname")


def bysector():
    print("bysector")


def bypopular():
    print("bypopular")


def exitquit():
    sys.exit(0)


def userinput():
    choice = input("Enter your choice:   ")
    clearconsole()
    if choice in currentmenu:
        return choice
    else:
        print("Invalid selection, try again:")
        userinput()


def header(menumodel):
    print(menu_header[menumodel])


def footer(menumodel):
    if menumodel == 0:
        print(menu_footer[menumodel])
        currentmenu.update({"Q": ""})
    else:
        print(menu_footer[1])
        currentmenu.update({"M": ""})


# Menu creation model to work with all possible variations.
def menu(menumodel, menuopts=None):
    currentmenu.clear()
    # Went with enumerate since index variables are non-pythonic, but wanted to generate the menu values on the fly
    for index, opt in enumerate(menuopts if menuopts else main_menu):
        print("  " + str(index + 1) + ":  " + opt)
        currentmenu.update({str(index + 1): opt})


def getcwd():
    # get current working dir
    cwd = os.getcwd()
    # path join for correct folder
    cwd = os.path.join(cwd + '\companies')
    return cwd


# creates file list to search though for
def makedicts(cwd):
    global symboldict, namedict, sectordict

    # explain case use below
    from collections import defaultdict
    holder = defaultdict(list)

    # next will only search starting dir
    getjson = [next(os.walk(cwd))]

    for root, directory, files in getjson:
        for filename in files:
            # need to fix issues with the second period
            if filename.count(".") == 1:
                # grab json contents
                filejson = json.load(open(os.path.join(root, filename)))
                # update symbol key dict
                symboldict.update({filejson['symbol']: filejson})
                # update name key dict
                namedict.update({filejson['companyName']: filejson['symbol']})
                # Update popular key dict
                populardict.update({filejson['symbol']: 0})
                # update sector key dict as well as list internal lists using defaultdict. It supports an
                # additional argument at init: a function. If a key is attempted to be accessed with no value, the
                # the function is called with no arguments and return is default for the key.
                if filejson['sector'] is not None and filejson['sector'] is not '':
                    holder[filejson['sector']].append(filejson['companyName'])
    sectordict = holder


# Handle console clear on all systems
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    sys.exit(main())
