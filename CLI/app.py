import sys
from os import listdir

from .utils import READ_PATH, handler

def run():
    args_1 = ["--file1", "-f1"]
    args_2 = ["--file2", "-f2"]
    args_3 = ["--vertical", "-v"]
    args_4 = ["--adapt-big", "-ab"]
    args_5 = ["--save", "-s"]
    args_6 = "--wf"

    filename_1, filename_2 = None, None
    vertical = False
    adapt_small = True
    save = False
    workflow = False

    if args_1[0] in sys.argv: filename_1 = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename_1 = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: filename_2 = sys.argv[sys.argv.index(args_2[0]) + 1]
    if args_2[1] in sys.argv: filename_2 = sys.argv[sys.argv.index(args_2[1]) + 1]

    if args_3[0] in sys.argv or args_3[1] in sys.argv: vertical = True
    if args_4[0] in sys.argv or args_4[1] in sys.argv: adapt_small = False
    if args_5[0] in sys.argv or args_5[1] in sys.argv:  save = True
    if args_6 in sys.argv: workflow = True

    assert filename_1 is not None, "Enter argument for --file1 | -f1"
    assert filename_2 is not None, "Enter argument for --file2 | -f2"

    assert filename_1 in listdir(READ_PATH), "File 1 Not Found"
    assert filename_2 in listdir(READ_PATH), "File 2 Not Found"

    image_1 = handler.read_image(READ_PATH + "/" + filename_1)
    image_2 = handler.read_image(READ_PATH + "/" + filename_2)
    
    image = handler.combine(image_1, image_2, vertical=vertical, adapt_small=adapt_small)

    if not save:
        if not workflow:
            handler.show(image)
    else:
        handler.save_image(image)
