from sys import argv
from simpleeval import simple_eval as se

# dict[var] = value
variables = {}

f"""
The '{variables}' variable is for all the variables I have in the Kood script
"""

def main(code): # this is the main loop of the kood scripting logic
    code_ = code.startswith # I just made this for short b/c I didn't want to type code.startswith 1M times
    if code_("*"):
        # command :
        # * this is a comment
        pass


    elif code_("addline:"):
        # command :
        # addline:"Hello world" + "abc"
        # addline:34+54
        # addline:my_number_var + 2
        text = code.removeprefix("addline:")
        text = se(text, names=variables)
        print(text)

with open(argv[1], "r", encoding="utf-8") as code_file:
    test_code = code_file.read()
    for code in test_code.splitlines():
        main(code)