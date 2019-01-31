import window

# TODO tests which run with -O off, all warnings on, for max debug
# TODO always use -O when running application
# TODO key to switch screen

def main():
    win = window.create()
    window.main_loop(win)

if __name__ == "__main__":
    main()

