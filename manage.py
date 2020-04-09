import sys
import utils



print("This is argv:", sys.argv)

try:
    command = sys.argv[1]
    print(command)
    if command == "build":
        print("Build was specified")
        utils.main()
        utils.makePage()
    elif command == "new":
        print("New page was specified")
        utils.newPage()

except IndexError:  # error results in no arguent given
    print("Please specify 'manage.py build' or 'manage.py new'")