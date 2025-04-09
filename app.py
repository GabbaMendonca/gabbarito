import sys

from gabbarito.main import main, main_debug

if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "--debug":
        main_debug()
    else:
        main()
