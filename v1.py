
import random
from sys import argv
from os import system as cmd
from time import sleep as wait

"I started making this project at 2026/January/6 2:05 pm"

# MIT License

# Copyright (c) 2025 KMK virtual

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# dict[var] = value
variables = {}

def main(code):
    code_ = code.startswith
    if code == "":
        pass


    elif code_("*"):
        # command :
        # * this is a comment
        pass


    elif code == "clear":
        # command :
        # clear
        try:
            cmd("cls")
        except:
            cmd("clear")


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        if text.startswith("\""):
            print(text.replace('\"', ''))
        else:
            print(variables[text])


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = eval(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        item_1, operator, item_2 = var_value.split(' ', 2)

        if item_1.replace('.', '').isdigit():
            item_1 = eval(item_1)
        elif item_1.startswith('\"'):
            item_1 = item_1.strip('\"')
        else:
            item_1 = variables[item_1]


        if item_2.replace('.', '').isdigit():
            item_2 = eval(item_2)
        elif item_2.startswith('\"'):
            item_2 = item_2.strip('\"')
        else:
            item_2 = variables[item_2]

        if operator == '+':
            variables[var_name] = item_1 + item_2
        elif operator == '-':
            variables[var_name] = item_1 - item_2
        elif operator == '*':
            variables[var_name] = item_1 * item_2
        elif operator == '/':
            variables[var_name] = item_1 / item_2


    elif code_("getline:"):
        # command :
        # getline:my_var="enter your name :  "
        code = code.removeprefix("getline:")
        var_name, user_input = code.split('=')

        var_name = var_name.replace('\"', '')
        user_input = user_input.replace('\"', '')

        variables[var_name] = input(user_input)


    elif code_("timer:"):
        # command :
        # timer:2
        code = code.removeprefix("timer:")
        seconds = eval(code)
        wait(seconds)


    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            variables[value] = eval(variables[value])
        elif conv_type == 'num-str':
            variables[value] = str(variables[value])


    elif code_("random:"):
        # command :
        # random:my_var=1,10
        code = code.removeprefix("random:")
        var_name, var_value = code.split('=')
        num1, num2 = var_value.split(',')
        variables[var_name.strip(' ')] = random.randint(int(num1.strip(' ')), int(num2.strip(' ')))


    elif code_("make_file:"):
        # command :
        # make_file:my_text.txt="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        value = value.strip('\" ')

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:my_text.txt
        code = code.removeprefix("read_file:")
        file_name = code
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')
        

        if value.startswith("\""):
            code = code.strip('\" ')
            with open(file_name, 'w') as f:
                f.write(value)
        else:
            code = code.strip('\" ')
            with open(file_name, 'w') as f:
                f.write(variables[value])




    elif code_("if "):
        # command :
        # if my_var = "hello world"::addline:"my_var is hello world"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_, my_function = arg3_.split('::')

        if arg1_.startswith('"') and arg1_.endswith('"'):
            arg1_ = arg1_.replace('\"', '')
        elif arg1_.isdigit():
            arg1_ = eval(arg1_)
        else:
            arg1_ = variables[arg1_]

        
        if arg3_.startswith('"') and arg3_.endswith('"'):
            arg3_ = arg3_.replace('\"', '')
        elif arg3_.isdigit():
            arg3_ = eval(arg3_)
        else:
            arg3_ = variables[arg3_]


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        
        if is_true:
            main(my_function)


if len(argv) == 1:
    print("usage: kood -v | kood -h | kood <code.kd>")
elif argv[1] == '-v':
    print("kood v0.1.0 by KMK virtual ©")
elif argv[1] == '-h':
    print("""
`*` : a comment

`clear` : to clear all text on screen  

`addline:<my_text>` : to print text to the screen  

`item:<my_var>="my text"` : to make a variable  

`m_item:<my_var>=<my_hello_world> + <number or text>` : a math version of `item:` to do simple math like adding 1 to a variable intager of 10 resulting in 11 or adding text like "Tom" to a variable that has text like "hi, " resulting in "hi, Tom"  

`getline:<my var>="my question to user running"` : to ask the user a question and store the answer inn a variable  

`timer:<time to wait in seconds>` : to set a timer to wait and do nothing  

`conv:<str-num|num-str>:<my var>` : to convert text to float/integer, and to convert float/integer to text like "9" (text) to 9 (number)  

`random:<my_var>=<1st number>, <2nd number>` : to get a random number in the range of the first number and the second number  

`make_file:<my_file_name>="<file contents>"` : to make a file in the current folder the script is in and add file contants  

`read_file:"<my_file_name>"` : to read a file in the current folder the script is in  

`write_file:<my_file_name>=<file contents>` : "make_file" but instead of creating, you would write  

`if <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::<funtion to do if conditions are true>` : to do a command if a condition is true  
          


To run code : kood my_code.kd
""")
    
else:
    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            main(code)



