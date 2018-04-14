import sys
import json
import os

menu_header = ["Main Menu", "Companies matching search", "Available Sectors:"]
menu_footer = ["  Q:  Exit/Quit", "  M:  Go back to main menu", "  M:  Go back to main menu"]
main_menu = ["Lookup Company by Stock Symbol", "Find Company by Name", "Find Company by Sector", "Popular Companies"]


def main():
    datamodel = ('symbol', 'name', 'sector', 'popular')
    menumodel = 0
    run = True
    while run:
        header(menumodel)
        menu(menumodel)
        footer(menumodel)
        ui = userinput(menumodel)
    return 0


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
