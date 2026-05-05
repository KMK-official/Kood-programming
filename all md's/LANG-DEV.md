# Day 1 / 2026/01/06

I made my folder for the code files  

I created main.py (the code for the language)  

I created code.bk (the code to test)  

I added my first code to do simple tasks like print text on the screen and I started making the if statement logic in `main.py`  

## my code:

`main.py`:

```
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
with open('code.bk', "r", encoding="utf-8") as code_file:
    test_code = code_file.read()
    for code in test_code.splitlines():
        code_ = code.startswith
        if code == "":
            pass
        elif code_("addline:"):
            text = code.removeprefix("addline:")
            print(text)
        elif code_("if "):
            if_, arg1_, arg2_, arg3_ = code.split(' ')
            print(arg1_)
            print(arg2_)
            print(arg3_)
```

## Challenges
making the if statment logic  










# Day 2 / 2026/01/15

I edited my code to have new commands:

`*` : a comment

`clear` : to clear all text on screen  

`addline:<my_text>` : to print text to the screen  

`item:<my_var>="my text"` : to make a variable  

`getline:<my var>="my question to user running"` : to ask the user a question and store the answer inn a variable  

`timer:<time to wait in seconds>` : to set a timer to wait and do nothing  

`conv:<str-num|num-str>:<my var>` : to convert text to float/integer, and to convert float/integer to text like "9" (text) to 9 (number)  

`if <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::<funtion to do if conditions are true>` : to do a command if a condition is true  


## my code:

`main.py`:

```
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
        from os import system as cmd
        try:
            cmd("cls")
        except:
            cmd("clear")


    elif code_("addline:"):
        # command :
        # addline:hello world
        text = code.removeprefix("addline:")
        print(text.replace('\"', ''))


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = eval(var_value)


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
        from time import sleep as wait
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


    elif code_("if "):
        # command :
        # if my_var = "hello world"::addline:"my_var is hello world"
        if_, arg1_, arg2_, arg3_ = code.split(' ')
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



with open('code.bk', "r", encoding="utf-8") as code_file:
    test_code = code_file.read()
    for code in test_code.splitlines():
        main(code)



```

## Challenges
Learning how to print multiple characters to screen  










# Day 3 / 2026/01/16

I edited my code to have new commands:

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


## my code:

`main.py`:

```

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
        # addline:hello world
        text = code.removeprefix("addline:")
        print(text.replace('\"', ''))


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
        item_1, operator, item_2 = var_value.split(' ')

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
        if_, arg1_, arg2_, arg3_ = code.split(' ')
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
```

## Challenges
the file logic was giving a huge ammount of errors to fix  









# Day 4, 5, 6, 7 / 2026/01/17-18-19-20

I added a function to make functions and made a Visual Studio Code extension (The Visual Studio Code extension is made from AI)

## my code:

`main.py`:

```

import random
from sys import argv, exit as exit_
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
lines = {}
line_num = 0
current_line = ""
marks_code = {}

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:"hello"

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line
    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        exit_()


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')
        for _ in var_a:
            if _ != "":
                main(_)


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
            try:
                variables[value] = eval(variables[value])
            except:
                variables[value] = 0
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


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        

        if value.startswith("\""):
            code = code.strip('\" ')
            with open(file_name, 'a') as f:
                f.write(value)
        else:
            code = code.strip('\" ')
            with open(file_name, 'a') as f:
                f.write(variables[value])



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
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

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
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



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
    
    line_nu = 0
    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            lines[line_nu] = code

    line_num = 0



    
    line_nu = 0
    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            find_goto(lines[line_nu])

    line_num = 0



    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_num += 1
            if not code.startswith('    '):
                current_line = code
                try:
                    main(code)
                except:
                    up_value = '\u21E7' * len(lines[line_num])
                    print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                    print(f'           \033[96m{up_value}\033[0m')




```

## Challenges
making the function to make functions (repeatable blocks of code) and making an error system to get errors instead of python getting the errors









# Day 8 / 2026/01/21

I updated my `main.py` to have while loops  

I started working on run.bat (windows batch file) to run commands to turn my code into an app  

## my code:

`main.py`:

```

import random
from sys import argv, exit as exit_
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
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_ in variables:
        return variables[value_]
    elif value_.startswith('\"'):
        return str(value_)

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:"hello"

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line
    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        exit_()


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')
        for _ in var_a:
            if _ != "":
                main(_)


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
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        item_1, operator, item_2 = var_value.split(' ', 2)

        if item_1.replace('.', '').isdigit():
            item_1 = find_type(item_1)
        elif item_1.startswith('\"'):
            item_1 = item_1.strip('\"')
        else:
            item_1 = variables[item_1]


        if item_2.replace('.', '').isdigit():
            item_2 = find_type(item_2)
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
        seconds = find_type(code)
        wait(seconds)


    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        

        if value.startswith("\""):
            code = code.strip('\" ')
            with open(file_name, 'a') as f:
                f.write(value)
        else:
            code = code.strip('\" ')
            with open(file_name, 'a') as f:
                f.write(variables[value])



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


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else: is_true = False


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        if arg1_.startswith('"') and arg1_.endswith('"'):
            arg1_ = arg1_.replace('\"', '')
        elif arg1_.isdigit():
            arg1_ = find_type(arg1_)
        else:
            arg1_ = variables[arg1_]

        
        if arg3_.startswith('"') and arg3_.endswith('"'):
            arg3_ = arg3_.replace('\"', '')
        elif arg3_.isdigit():
            arg3_ = find_type(arg3_)
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
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



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
    
    line_nu = 0
    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            lines[line_nu] = code

    line_num = 0



    
    line_nu = 0
    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            find_goto(lines[line_nu])

    line_num = 0



    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_num += 1
            if not code.startswith('    '):
                current_line = code
                try:
                    main(code)
                except:
                    up_value = '\u21E7' * len(lines[line_num])
                    print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                    print(f'           \033[96m{up_value}\033[0m')




```

## Challenges
making the if statment logic  










# Day 9 / 2026/01/22

I updated `main.py`  

I made my run.bat file to make the code to an app  

I made a system variable in my programming language called @all_vars which is a list of all the variables including @all_vars  

## my code:

`run.bat`:

```
@echo off
set "file_name=v3.py"
pyarmor gen "v3.py"
pyinstaller --name kood "dist\v3.py" --onefile --noconfirm --workpath build_temp
rmdir /S /Q "build_temp"
rmdir /S /Q "dist\pyarmor_runtime_000000"
del "kood.spec"
del "dist\v3.py"

"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "iss\inno-setup.iss" /O"dist"
```

`main.py`:

```

import random
from sys import argv, exit as exit_
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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_ in variables:
        return variables[value_]
    elif value_.startswith('\"'):
        return str(value_)

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        exit_()


    elif code_("run_function:"):
        # command :
        # run_function:my_function:my_args="hello"
        code = code.removeprefix("run_function:")
        
        try:
            f_name, args = code.split(':')
            var_a = marks_code[f_name].split('::::')
            args = args.split(',')
            arg_len = len(args)
            f_variables = {}
            for _ in range(arg_len):
                var_ = None
                value_ = None
                var_, value_ = args[_+1].split('=')

                value_ = find_type(value_)

                f_variables[var_[_+1]] = value_[_+1]

            variables.update(f_variables)
            for _ in var_a:
                if _ != "":
                    main(_)
            variables_ = {}
            for name_, value__ in variables.items():
                if name_ not in f_variables:
                    variables_[name_] = value__
            variables = variables_
        except:
            var_a = marks_code[code].split('::::')
            for _ in var_a:
                if _ != "":
                    main(_)


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
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        item_1, operator, item_2 = var_value.split(' ', 2)

        if item_1.replace('.', '').isdigit():
            item_1 = find_type(item_1)
        elif item_1.startswith('\"'):
            item_1 = item_1.strip('\"')
        else:
            item_1 = variables[item_1]


        if item_2.replace('.', '').isdigit():
            item_2 = find_type(item_2)
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
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        

        if value.startswith("\""):
            code = code.strip('\" ')
            with open(file_name, 'a') as f:
                f.write(value)
        else:
            code = code.strip('\" ')
            with open(file_name, 'a') as f:
                f.write(variables[value])



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


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else: is_true = False


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        if arg1_.startswith('"') and arg1_.endswith('"'):
            arg1_ = arg1_.replace('\"', '')
        elif arg1_.isdigit():
            arg1_ = find_type(arg1_)
        else:
            arg1_ = variables[arg1_]

        
        if arg3_.startswith('"') and arg3_.endswith('"'):
            arg3_ = arg3_.replace('\"', '')
        elif arg3_.isdigit():
            arg3_ = find_type(arg3_)
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
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



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
    
    line_nu = 0
    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            lines[line_nu] = code

    line_num = 0



    
    line_nu = 0
    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            find_goto(lines[line_nu])

    line_num = 0



    with open(argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_num += 1
            if not code.startswith('    '):
                current_line = code
                try:
                    main(code)
                except:
                    up_value = '\u21E7' * len(lines[line_num])
                    print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                    print(f'           \033[96m{up_value}\033[0m')




```

## Challenges
No Challenges  










# Day 10 / 2026/01/23

I started making a quick-start manual for Kood  

## my code:

`quick-start.md`:

```
# How To Install

## Requirements
**Computer** : Windows 11, Windows 10  
**Applications** : Kood app, Visual Studio Code  

## Kood Programming
Go to kood-programming.netlify.app/install and click install, and kood-installer should get installed.

Once you have installed kood-installer, go to your downloads and double-click it. Read the license and click "I accept the agreement" and click next. If "Create a desktop shortcut" isn't checked then check it and click next. Click install and wait for Kood programming to be installed. Lastly, click Finish.

To verify if kood programming is installed click ⊞ + R, type `cmd`, and click enter. Copy and paste this command into the black screen `kood -v` and it should print the version of Kood.

## Visual Studio Code
Go to code.visualstudio.com and click "Download for Windows", and VSCodeUserSetup-xxx-x.xxx.x should get installed.

Once you have the VSCode installer, go to your downloads and double-click it. Read the license and click "I accept the agreement" and click next, then click next again. Click next. Then check all the boxes and click next. Click install and wait for Visual Studio Code to be installed. Lastly, click Finish.  
  
  
  
# How To Uninstall

## Kood Programming
Go to your settings app and search "Installed apps", select "Installed apps" and search for "Kood version x.x.x" and click the 3 dots beside it. Click "Uninstall" and confirm your uninstallation

## Visual Studio Code
Go to your settings app and search "Installed apps", select "Installed apps" and search for "Microsoft Visual Studio Code (User)" and click the 3 dots beside it. Click "Uninstall" and confirm your uninstallation
  
  
  
# Hello World

## Description
how to make a hello world program. A hello world program is a program were it shows the text "Hello World!" on the screen. this is the simplest program you could make in a programming language. Many tutorials normally start with a hello world program because of it being very generic and simple. So lets make our first program in the Kood programming language.


## Start A Project
On your desktop make a folder called "My first Kood Project", then in Visual Studio Code, click on "Open Folder..." and select the folder you just created on your desktop. A panel will open on the left of your Visual Studio Code window, right-click the panel in the center and click "New File..." and enter your filename as "main.kd" and add the following code:
`addline:"Hello World!"`

In Visual Studio code click `Ctrl` + `` ` `` and a black screen will pop out from the bottom of the Visual Studio Code window. Click once on the back popup and type the following `kood main.kd`
```

## Challenges
No Challenges  










# Day 11, 12 / 2026/01/24-25

I edited my `quick-start.md` file
I started making the website

## my code:

`quick-start.md`:

```
# How To Install

## Requirements
**Computer** : Windows 11, Windows 10  
**Applications** : Kood app, Visual Studio Code  

## Kood Programming
Go to kood-programming.netlify.app and click "install kood", and kood-installer should get installed.

Once you have installed kood-installer, go to your downloads and double-click it. Read the license and click "I accept the agreement" and click next. If "Create a desktop shortcut" isn't checked then check it and click next. Click install and wait for Kood programming to be installed. Lastly, click Finish.

To verify if kood programming is installed click ⊞ + R, type `cmd`, and click enter. Copy and paste this command into the black screen `kood -v` and it should print the version of Kood.

## Visual Studio Code
Go to code.visualstudio.com and click "Download for Windows", and VSCodeUserSetup-xxx-x.xxx.x should get installed.

Once you have the VSCode installer, go to your downloads and double-click it. Read the license and click "I accept the agreement" and click for the next 3 times. Click next. Then check all the boxes and click next. Click install and wait for Visual Studio Code to be installed. Lastly, click Finish.  
  
  
  
# How To Uninstall

## Kood Programming
Go to your settings app and search "Installed apps", select "Installed apps" and search for "Kood version x.x.x" and click the 3 dots beside it. Click "Uninstall" and confirm your uninstallation

## Visual Studio Code
Go to your settings app and search "Installed apps", select "Installed apps" and search for "Microsoft Visual Studio Code (User)" and click the 3 dots beside it. Click "Uninstall" and confirm your uninstallation
  
  
  
# Hello World

## Description
how to make a hello world program. A hello world program is a program were it shows the text "Hello World!" on the screen. this is the simplest program you could make in a programming language. Many tutorials normally start with a hello world program because of it being very generic and simple. So lets make our first program in the Kood programming language.


## Start A Project
On your desktop make a folder called "My first Kood Project", then in Visual Studio Code, click on "Open Folder..." and select the folder you just created on your desktop. A panel will open on the left of your Visual Studio Code window, right-click the panel in the center and click "New File..." and enter your filename as "main.kd" and add the following code:
```
addline:"Hello World!"
```

The reason main.kd ends in `.kd` and not `.txt` or `.docx` is because a Kood code file ends with `.kd`. In Visual Studio code click `Ctrl` + `` ` `` and a black screen will pop out from the bottom of the Visual Studio Code window. Click once on the black popup and type the following `kood main.kd`
```

`index.html`:

```
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Kood programming</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>
<body style="background-color: bisque;">
    <div style="border-radius: 50px; display: flex; align-items: center; background-color: rgba(119, 23, 119, 0.785);">
        <h1 style="margin-left: 60px;">Kood programming</h1>
        <img style="margin-left: 30px;" width="50px" height="50px" src="logo.png">
    </div>

    <h1 style="text-align: center;">Download</h1>

    
    <div style="display: flex; justify-content: center;">
        <a href="kood-installer.exe" download="kood-installer.exe"><button style="border-radius: 30px; background-color: cadetblue;"><h1 style="text-align: center;">-Install Kood-</h1></button></a>
    </div>
    <br>
    <br>
    <br>

    <hr style="height: 20px; background-color: #000000;">

    <br>
    <br>
    <br>

    <h1 style="text-align: center;">Quick start</h1>

    <h2>How To Install</h2>

    <h3> Requirements </h3>
    <p><b>Computer</b> : Windows 11, Windows 10</p>
    <p><b>Applications</b> : <a href="#kood-installer">Kood Programming</a>, <a href="#VScode-installer">Visual Studio Code</a></p>

    <br>

    <h3 id="kood-installer"> Kood Programming</h3>
    
    <p>Visit kood-programming.netlify.app and click "Install Kood". Once you have installed kood-installer, go to your downloads and double-click it. Read the license and click "I accept the agreement" and click next. If "Create a desktop shortcut" isn't checked then check it and click next. Click install and wait for Kood programming to be installed. Lastly, click Finish. To verify if kood programming is installed click ⊞ + R, type `cmd`, and click enter. Copy and paste this command into the black screen `kood -v` and it should print the version of Kood.</p>

    <br>

    <h3 id="VScode-installer"> Visual Studio Code</h3>

    <p>Go to code.visualstudio.com and click "Download for Windows", and VSCodeUserSetup-xxx-x.xxx.x should get installed. Once you have the VSCode installer, go to your downloads and double-click it. Read the license and click "I accept the agreement" and click next for the next 2 times. Then check all the boxes and click next. Click install and wait for Visual Studio Code to be installed. Lastly, click Finish.  </p>
    
    
    
    <h2> How To Uninstall </h2>

    <h3> Kood Programming</h3>

    <p>Go to your settings app and search "Installed apps", select "Installed apps" and search for "Kood version x.x.x" and click the 3 dots beside it. Click "Uninstall" and confirm your uninstallation</p>

    <h3> Visual Studio Code</h3>
    <p>Go to your settings app and search "Installed apps", select "Installed apps" and search for "Microsoft Visual Studio Code (User)" and click the 3 dots beside it. Click "Uninstall" and confirm your uninstallation</p>
    
    
    
    <h2> Hello World</h2>

    <h3> Description</h3>

    <p>How to make a hello world program. A hello world program is an app were it shows the text "Hello World!" on the screen. This is the simplest program you could make in a programming language. Many tutorials normally start with a hello world program because of it being very generic and simple. So lets make our first program in the Kood programming language.</p>


    <h3> Start A Project</h3>

    <p>On your desktop make a folder called "My first Kood Project", then in Visual Studio Code, click on "Open Folder..." and select the folder you just created on your desktop. A panel will open on the left side of your Visual Studio Code window, right-click the panel in the center and click "New File..." and enter your filename as "main.kd" and add the following code:</p>
    <pre><code>
    addline:"Hello World!"
    </pre></code>

    <p>The reason main.kd ends in <code>.kd</code> and not <code>.txt</code> or <code>.docx</code> is because a Kood code file ends with <code>.kd</code>. In Visual Studio code click Ctrl + ` and a black screen will pop out from the bottom of the Visual Studio Code window. Click once on the black popup and type the following and click enter : <pre><code>    kood main.kd</code></pre> This will run the kood file</p>

    
</body>
</html>
```

## Challenges
checking for problems in the writing of `quick-start.md`  










# Day 13, 14 / 2026/01/26-27

Started making example scripts  

## my code:

`main.py`:

```

import random
import sys
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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_ in variables:
        return variables[value_]
    elif value_.startswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("run_function:"):
        # command :
        # run_function:my_function:my_args="hello"
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for _ in var_a:
            if _ != "":
                main(_)


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
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:my_text.txt
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



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


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



if len(sys.argv) == 1:
    print("usage: kood -v | kood -h | kood <code.kd>")
elif sys.argv[1] == '-v':
    print("kood v0.1.0 by KMK virtual ©")
elif sys.argv[1] == '-h':
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
    
    line_nu = 0
    with open(sys.argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            lines[line_nu] = code

    line_num = 0



    
    line_nu = 0
    with open(sys.argv[1], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            find_goto(lines[line_nu])

    line_num = 0


    try:
        with open(sys.argv[1], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_num += 1
                if not code.startswith('    '):
                    current_line = code
                    try:
                        main(code)

                    except SystemExit:
                        raise
                    
                    except:
                        if current_line != ':':
                            error = "No \":\" was added"
                        
                        if error == "":
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                        else:
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')


    except FileNotFoundError:
        error = "Code file not found"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')





```


`math.kd`:

```
* Get all user inputs
getline:num1="what is your first number :  "
getline:operator="what is your operator (+,-,/,*) :  "
getline:num2="what is your second number :  "


* Make the anwswer variable's default value to 0 and translate the users first and second number from word form to number form
item:answer=0
conv:str-num:num1
conv:str-num:num2

* Clear the screen from text
clear

* Check which math operation did the user pick
if operator = "+"::
    m_item:answer=num1 + num2
if operator = "-"::
    m_item:answer=num1 - num2
if operator = "/"::
    m_item:answer=num1 / num2
if operator = "*"::
    m_item:answer=num1 * num2

* Add the answer to the screen
addline:answer

* make a random number from 1 to 100
random:num3=0,100
* Use the 'conv' function to convert the random number into text
conv:num-str:num3
* Merge the text "The random number from 0 to 100 is :  " and the 'num3' variable (This is why you need to convert the number to text) and add that text to the screen
m_item:num4="The random number from 0 to 100 is :  " + num3
addline:num4

* Get the length of the text of the variable 'num4' and store it in the variable 'num5'. Then merge the text "The lenth of the current text is :  " and the 'num5' variable, and add that value to the variable 'num6'. Add it to the screen
len:num5=num4
conv:num-str:num5
m_item:num6="The lenth of the current text is :  " + num5
addline:num6
```


`functions.kd`:

```
function greet
    * The variable 'name' is a variable made later for the greet function and add text to the screen
    m_item:text="hi, I'm " + name
    addline:text

* This is where the 'name' variable is assigned to the value "Robert" and the greet function is being called
item:name="Robert"
run_function:greet

* Makes a variable called 'your_name' witht the value of ""
item:your_name=""

* Make a loop of asking "what is your name :  " until the user puts something
while your_name = ""::
    getline:your_name="what is your name :  "

* Use the m_item function (math item) to merge the text "Hi, " and the variable 'your_name' and add that value to the 'text' variable
m_item:text="Hi, " + your_name

* Add the variable 'text' to the screen
addline:text

* Using the 'timer' command, you could wait a certain amount of seconds without doing anything, in this case it's only waiting 1 second
timer:1
* When you use the 'exit' command, you exit the code and don't run anything more
exit
addline:"ABC"
```


`file-management.kd`:
```
getline:file_content_input="What is your text to put in your file :  "
make_file:"my_text.txt"=file_content_input

read_file:"my_text.txt"

m_item:my_file_contents="the file contents for my_text.txt is :  " + my_text.txt

addline:my_file_contents

getline:new_contents="What is your text to put in your file :  "

add_file:"my_text.txt"=new_contents

read_file:"my_text.txt"

m_item:my_file_contents="the file contents for my_text.txt is :  " + my_text.txt

addline:my_file_contents

```

## Challenges
making the example files for Kood  










# Day 15 / 2026/01/28

I edited my main python code, and edited my examples  

## my code:

`math.kd`:

```
* Get all user inputs for the first nummber, the math operator, and the second number.
getline:num1="what is your first number :  "
getline:operator="what is your operator (+,-,/,*) :  "
getline:num2="what is your second number :  "


* Make the 'answer' variable's default value to 0 and translate the users first and second number from word form to number form.
item:answer=0
conv:str-num:num1
conv:str-num:num2

* Clear the screen from text.
clear

* Check which math operation did the user pick, +, -, /, or *.
if operator = "+"::
    m_item:answer=num1 + num2
if operator = "-"::
    m_item:answer=num1 - num2
if operator = "/"::
    m_item:answer=num1 / num2
if operator = "*"::
    m_item:answer=num1 * num2

* Add the answer to the screen.
addline:answer

* Make a random number from 0 to 100.
random:num3=0,100
* Use the 'conv' function to convert the random number into text.
conv:num-str:num3
* Merge the text "The random number from 0 to 100 is :  " and the 'num3' variable (This is why you need to convert the number to text because you can't merge text with numbers, only numbers with numbers and text with text) and add that text to the screen.
m_item:num4="The random number from 0 to 100 is :  " + num3
addline:num4

* Get the length of the text of the variable 'num4'. Then store it in the variable 'num5'. Then merge the text "The lenth of the current text is :  " and the 'num5' variable. Lastly, add that value to the variable 'num6', and add it to the screen.
len:num5=num4
conv:num-str:num5
m_item:num6="The lenth of the current text is :  " + num5
addline:num6
```

`functions.kd`:

```
* Make a function called 'greet'.
function greet
    * The variable 'name' is a variable made later for the greet function and add text to the screen.
    m_item:text="hi, I'm " + name
    addline:text

* This is where the 'name' variable is assigned to the value "Robert" and the greet function is being called.
item:name="Robert"
run_function:greet

* Makes a variable called 'your_name' witht the value of "".
item:your_name=""

* Make a loop of asking "what is your name :  " until the user puts something so the user doesn't just click enter.
while your_name = ""::
    getline:your_name="what is your name :  "

* Use the m_item function (math item) to merge the text "Hi, " and the variable 'your_name' and add that value to the 'text' variable.
m_item:text="Hi, " + your_name

* Add the variable 'text' to the screen.
addline:text

* Use the '@all_vars' system variable to list all the variables.
addline:@all_vars

* Using the 'timer' command, you could wait a certain amount of seconds without doing anything, in this case it's only waiting 1 second.
timer:1
* When you use the 'exit' command, you exit the code and don't run anything more.
exit
addline:"ABC"
```

`file-management.kd`:

```
* Using the 'getline' function to get user input and use the 'make_file' function to make the file "my_text.txt" and add the contents of the user.
getline:file_content_input="What is your text to put in your file :  "
make_file:"my_text.txt"=file_content_input

* Read the file "my_text.txt" and put the contents in the variable named 'my_text.txt' because thats the file name.
read_file:"my_text.txt"

* Merge the text "the file contents for my_text.txt is :  " and the variable 'my_text.txt' because the variable 'my_text.txt' is where the file contents were stored and add the merged text to the screen.
m_item:my_file_contents="the file contents for my_text.txt is :  " + my_text.txt
addline:my_file_contents

* Get user input on "What is your text to put in your file :  " and append that value to the existing "my_text.txt" file. Then read it, merge "the file contents for my_text.txt is :  " and the variable 'my_text.txt' and add that text to the screen.
getline:new_contents="What is your text to put in your file :  "
add_file:"my_text.txt"=new_contents
read_file:"my_text.txt"
m_item:my_file_contents="the file contents for my_text.txt is :  " + my_text.txt
addline:my_file_contents


* Do what was done in the last code, but instead of using the 'add_file' function, use the 'write_file' function to overwrite instead of extend the file.
getline:file_content_input="What is your text to put in your file after erasing contents :  "
write_file:"my_text.txt"=file_content_input
read_file:"my_text.txt"
m_item:my_file_contents="the file contents for my_text.txt is :  " + my_text.txt
addline:my_file_contents
```

## Challenges
No Challenges  










# Day 16, 17, 18, 19, 20, 21, 22, 23 / 2026/01/29, 30, 31, 2026/02/1, 2, 3, 4, 5

I created a compiler script that reads itself instead of a kd file so Its all one app instead of the kood app and the script.In this way it allows the user to run the code using kood, or make a "baked" bundle of the kood apps binary, and a new version of the script which is binary.  

I also created an easter egg function called Pythonic_code to run python code.  

## my code:

`main.py`:

```
import random
import sys
from os import system as cmd
from time import sleep as wait
from os.path import abspath as dir_of

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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_ in variables:
        return variables[value_]
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function:my_args="hello"
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for _ in var_a:
            if _ != "":
                main(_)


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        text = find_type(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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

        variables[var_name] = input(user_input).replace("*n*", "\n")


    elif code_("timer:"):
        # command :
        # timer:2
        code = code.removeprefix("timer:")
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:my_text.txt
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')

        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



if len(sys.argv) == 1:
    print("usage: kood -v | kood -h | kood <code.kd>")
elif sys.argv[1] == '-v':
    print("kood v0.1.0 by KMK virtual ©")
elif sys.argv[1] == '-h':
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
    
elif sys.argv[1] == '-run':
    
    line_nu = 0
    with open(sys.argv[2], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            lines[line_nu] = code

    line_num = 0



    
    line_nu = 0
    with open(sys.argv[2], "r", encoding="utf-8") as code_file:
        test_code = code_file.read()
        for code in test_code.splitlines():
            line_nu += 1
            find_goto(lines[line_nu])

    line_num = 0


    try:
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_num += 1
                if not code.startswith('    '):
                    current_line = code
                    try:
                        main(code)

                    except SystemExit:
                        raise
                    
                    except:
                        if current_line != ':':
                            error = "No \":\" was added"
                        
                        if error == "":
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                        else:
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')


    except FileNotFoundError:
        error = "Code file not found"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')


elif sys.argv[1] == '-compile':
    file_dir = dir_of(__file__).replace('\\v2.py', '')
    with open(f'{file_dir}\\compiler.exe', 'rb') as cmpl:
        with open(sys.argv[2], 'rb') as code:
            with open(f'{sys.argv[2].replace('.kd', '.exe')}', 'wb') as exe:
                exe.write(cmpl.read())
                exe.write(b'compiled_code_starts')
                exe.write(code.read())
```

`compiler.py`:

```
import random
import sys
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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_ in variables:
        return variables[value_]
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function:my_args="hello"
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for _ in var_a:
            if _ != "":
                main(_)


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        text = find_type(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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

        variables[var_name] = input(user_input).replace("*n*", "\n")


    elif code_("timer:"):
        # command :
        # timer:2
        code = code.removeprefix("timer:")
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:my_text.txt
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')

        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        




with open(sys.executable, "rb") as f:
    file = f.read()
    FILE_NAME_INT = file.find(b'compiled_code_start' + b's') + len(b'compiled_code_start' + b's')



line_nu = 0
with open(sys.executable, "rb") as code_file:
    code_file.seek(FILE_NAME_INT)
    test_code = code_file.read().decode('utf-8')
    for code in test_code.splitlines():
        line_nu += 1
        lines[line_nu] = code

line_num = 0




line_nu = 0
with open(sys.executable, "rb") as code_file:
    code_file.seek(FILE_NAME_INT)
    test_code = code_file.read().decode('utf-8')
    for code in test_code.splitlines():
        line_nu += 1
        find_goto(lines[line_nu])

line_num = 0


try:
    with open(sys.executable, "rb") as code_file:
        code_file.seek(FILE_NAME_INT)
        test_code = code_file.read().decode('utf-8')
        for code in test_code.splitlines():
            line_num += 1
            if not code.startswith('    '):
                current_line = code
                try:
                    main(code)

                except SystemExit:
                    raise
                
                except:
                    if current_line != ':':
                        error = "No \":\" was added"
                    
                    if error == "":
                        up_value = '\u21E7' * len(lines[line_num])
                        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                        print(f'           \033[96m{up_value}\033[0m')
                    else:
                        up_value = '\u21E7' * len(lines[line_num])
                        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                        print(f'           \033[96m{up_value}\033[0m')


except FileNotFoundError:
    error = "Code file not found"
    up_value = '\u21E7' * len(lines[line_num])
    print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
    print(f'           \033[96m{up_value}\033[0m')
```

## Challenges
Making a compiler and the system to read itself starting from the code.    










# Day 24, 25, 26 / 2026/02/06, 07, 08

updated compiler.py, and main.py  

## my code:

`main.py`:

```
import random
import sys
from os import system as cmd
from time import sleep as wait
from os.path import abspath as dir_of

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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    elif value_ in variables:
        return variables[value_]
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for code_to_run_ in var_a:
            if code_to_run_ != "":
                main(code_to_run_)


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        text = find_type(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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

        variables[var_name] = find_type(input(user_input))


    elif code_("timer:"):
        # command :
        # timer:2
        code = code.removeprefix("timer:")
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:"my_text.txt"
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



if len(sys.argv) == 1:
    print("usage: kood -v | Get version info\nkood -h | Help\nkood <code.kd> | Run Kood file")
elif sys.argv[1] == '-v':
    print("kood v0.1.0 by KMK virtual ©")
elif sys.argv[1] == '-h':
    print("""


`*` : a comment    

example: `* this is a comment`




`clear` : to clear all text on screen  

example: `clear`  




`run_function:<function_name>` : to run a function  

example: `run_function:my_hello_function`  




`addline:<my_text>` : to print text to the screen  

example: `addline:hello world`  




`item:<my_var>="my text"` : to make a variable  

example: `item:my_var="hello world"`  




`m_item:<my_var>=<my_hello_world> + <number or text>` : a math version of `item:` to do simple math like adding 1 to a variable intager of 10 resulting in 11 or adding text like "Tom" to a variable that has text like "hi," resulting in "hi,Tom"  

example: `m_item:my_var=my_old + 1`  




`getline:<my var>="my question to user ning"` : to ask the user a question and store the answer inn a variable  

example: `getline:my_var="enter your name :  "`  




`timer:<time to wait in seconds>` : to set a timer to wait and do nothing  

example: `timer:2`  




`len:<var>=<var_to_get_length_of>` : to get length of a variable, text, or number  

example: `len:my_var=my_other_var`  




`conv:<str-num|num-str>:<my var>` : to convert text to float/integer, and to convert float/integer to text like "9" (text) to 9 (number)  

example: `conv:str-num:my_var`  




`random:<my_var>=<1st number>, <2nd number>` : to get a random number in the range of the first number and the second number  

example: `random:my_var=1,10`  




`make_file:<my_file_name>="<file contents>"` : to make a file in the current folder the script is in and add file contants  

example `make_file:my_text.txt="helloworld"`  




`read_file:"<my_file_name>"` : to read a file in the current folder the script is in  

example: `read_file:my_text.txt`  




`add_file` : to add on to a file  

example: `add_file:my_text.txt="helloworld"`  




`write_file:<my_file_name>="<file contents>"` : "make_file" but instead of creating, you would write  

example: `write_file:my_text.txt="helloworld"`  




```
while <1st condition> <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do until conditions are not true>
    <another funtion to do until conditions are not true>
``` : to do something until conditions aren't true

example: ```
while my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  




```
if <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do if conditions are true>
    <another funtion to do if conditions are true>
``` : to do a command if a condition is true  

example:
```
if my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  
          


To run code : kood my_code.kd
""")
    
elif sys.argv[1] == '-run':


    try:    
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                lines[line_nu] = code

        line_num = 0



        
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                find_goto(lines[line_nu])

        line_num = 0


        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_num += 1
                if not code.startswith('    '):
                    current_line = code
                    try:
                        main(code)

                    except SystemExit:
                        raise
                    
                    except:
                        if current_line != ':':
                            error = "No \":\" was added"
                        
                        if error == "":
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                        else:
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')


    except FileNotFoundError or KeyError:
        error = "Code file not found"
        print(f'\033[35mERROR: \033[0m\n    \033[31m{error}\033[0m')


elif sys.argv[1] == '-compile':
    try:
        is_exe = sys.frozen
    except AttributeError:
        is_exe = False
    if is_exe:
        file_folder_dir=sys.executable.split('\\')
        file_folder_dir.pop()
        file_folder_dir = '\\'.join(file_folder_dir)
    else:
        file_folder_dir=__file__.split('\\')
        file_folder_dir.pop()
        file_folder_dir = '\\'.join(file_folder_dir)

    with open(f'{file_folder_dir}\\compiler.exe', 'rb') as cmpl:
        with open(sys.argv[2], 'rb') as code:
            with open(f'{sys.argv[2].replace('.kd', '.exe')}', 'wb') as exe:
                exe.write(cmpl.read())
                exe.write(b'compiled_code_starts')
                exe.write(code.read())
```

`compiler.py`:

```
import random
import sys
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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    elif value_ in variables:
        return variables[value_]
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for code_to_run_ in var_a:
            if code_to_run_ != "":
                main(code_to_run_)


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        text = find_type(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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

        variables[var_name] = find_type(input(user_input))


    elif code_("timer:"):
        # command :
        # timer:2
        code = code.removeprefix("timer:")
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:"my_text.txt"
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        




with open(sys.executable, "rb") as f:
    file = f.read()
    FILE_NAME_INT = file.find(b'compiled_code_start' + b's') + len(b'compiled_code_start' + b's')



line_nu = 0
with open(sys.executable, "rb") as code_file:
    code_file.seek(FILE_NAME_INT)
    test_code = code_file.read().decode('utf-8')
    for code in test_code.splitlines():
        line_nu += 1
        lines[line_nu] = code

line_num = 0




line_nu = 0
with open(sys.executable, "rb") as code_file:
    code_file.seek(FILE_NAME_INT)
    test_code = code_file.read().decode('utf-8')
    for code in test_code.splitlines():
        line_nu += 1
        find_goto(lines[line_nu])

line_num = 0


try:
    with open(sys.executable, "rb") as code_file:
        code_file.seek(FILE_NAME_INT)
        test_code = code_file.read().decode('utf-8')
        for code in test_code.splitlines():
            line_num += 1
            if not code.startswith('    '):
                current_line = code
                try:
                    main(code)

                except SystemExit:
                    raise
                
                except:
                    if current_line != ':':
                        error = "No \":\" was added"
                    
                    if error == "":
                        up_value = '\u21E7' * len(lines[line_num])
                        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                        print(f'           \033[96m{up_value}\033[0m')
                    else:
                        up_value = '\u21E7' * len(lines[line_num])
                        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                        print(f'           \033[96m{up_value}\033[0m')


except FileNotFoundError:
    error = "Code file not found"
    up_value = '\u21E7' * len(lines[line_num])
    print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
    print(f'           \033[96m{up_value}\033[0m')
```

## Challenges
No Challenges  










# Day 26, 27, 28, 29 / 2026/02/08, 09, 10, 11

I made a editor for my language with graphics  

## my code:

`main.py`:

```
import random
import sys
from os import system as cmd
from time import sleep as wait
from os.path import abspath as dir_of

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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    elif value_ in variables:
        return variables[value_]
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for code_to_run_ in var_a:
            if code_to_run_ != "":
                main(code_to_run_)


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        text = find_type(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:"my_text.txt"
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



if len(sys.argv) == 1:
    print("usage: kood -v | Get version info\nkood -h | Help\nkood -run <code.kd> | Run Kood file\nkood -compile <code.kd> | Compile Kood file")
elif sys.argv[1] == '-v':
    print("kood v0.1.0 by KMK virtual ©")
elif sys.argv[1] == '-h':
    print("""


`*` : a comment    

example: `* this is a comment`




`clear` : to clear all text on screen  

example: `clear`  




`run_function:<function_name>` : to run a function  

example: `run_function:my_hello_function`  




`addline:<my_text>` : to print text to the screen  

example: `addline:hello world`  




`item:<my_var>="my text"` : to make a variable  

example: `item:my_var="hello world"`  




`m_item:<my_var>=<my_hello_world> + <number or text>` : a math version of `item:` to do simple math like adding 1 to a variable intager of 10 resulting in 11 or adding text like "Tom" to a variable that has text like "hi," resulting in "hi,Tom"  

example: `m_item:my_var=my_old + 1`  




`getline:<my var>="my question to user ning"` : to ask the user a question and store the answer inn a variable  

example: `getline:my_var="enter your name :  "`  




`timer:<time to wait in seconds>` : to set a timer to wait and do nothing  

example: `timer:2`  




`len:<var>=<var_to_get_length_of>` : to get length of a variable, text, or number  

example: `len:my_var=my_other_var`  




`conv:<str-num|num-str>:<my var>` : to convert text to float/integer, and to convert float/integer to text like "9" (text) to 9 (number)  

example: `conv:str-num:my_var`  




`random:<my_var>=<1st number>, <2nd number>` : to get a random number in the range of the first number and the second number  

example: `random:my_var=1,10`  




`make_file:<my_file_name>="<file contents>"` : to make a file in the current folder the script is in and add file contants  

example `make_file:my_text.txt="helloworld"`  




`read_file:"<my_file_name>"` : to read a file in the current folder the script is in  

example: `read_file:my_text.txt`  




`add_file` : to add on to a file  

example: `add_file:my_text.txt="helloworld"`  




`write_file:<my_file_name>="<file contents>"` : "make_file" but instead of creating, you would write  

example: `write_file:my_text.txt="helloworld"`  




```
while <1st condition> <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do until conditions are not true>
    <another funtion to do until conditions are not true>
``` : to do something until conditions aren't true

example: ```
while my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  




```
if <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do if conditions are true>
    <another funtion to do if conditions are true>
``` : to do a command if a condition is true  

example:
```
if my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  
          


To run code : kood my_code.kd
""")
    
elif sys.argv[1] == '-run':


    try:    
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                lines[line_nu] = code

        line_num = 0



        
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                find_goto(lines[line_nu])

        line_num = 0


        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_num += 1
                if not code.startswith('    '):
                    current_line = code
                    try:
                        main(code)

                    except SystemExit:
                        raise
                    
                    except:
                        if current_line != ':':
                            error = "No \":\" was added"
                        
                        if error == "":
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                        else:
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')


    except FileNotFoundError or KeyError:
        error = "Code file not found"
        print(f'\033[35mERROR: \033[0m\n    \033[31m{error}\033[0m')


elif sys.argv[1] == '-compile':
    try:
        is_exe = sys.frozen
    except AttributeError:
        is_exe = False
    if is_exe:
        file_folder_dir=sys.executable.split('\\')
        file_folder_dir.pop()
        file_folder_dir = '\\'.join(file_folder_dir)
    else:
        file_folder_dir=__file__.split('\\')
        file_folder_dir.pop()
        file_folder_dir = '\\'.join(file_folder_dir)

    with open(f'{file_folder_dir}\\compiler.exe', 'rb') as cmpl:
        with open(sys.argv[2], 'rb') as code:
            with open(f'{sys.argv[2].replace('.kd', '.exe')}', 'wb') as exe:
                exe.write(cmpl.read())
                exe.write(b'compiled_code_starts')
                exe.write(code.read())
```

`copmiler.py`:

```
import random
import sys
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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    elif value_ in variables:
        return variables[value_]
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for code_to_run_ in var_a:
            if code_to_run_ != "":
                main(code_to_run_)


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        text = find_type(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:"my_text.txt"
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        




with open(sys.executable, "rb") as f:
    file = f.read()
    FILE_NAME_INT = file.find(b'compiled_code_start' + b's') + len(b'compiled_code_start' + b's')



line_nu = 0
with open(sys.executable, "rb") as code_file:
    code_file.seek(FILE_NAME_INT)
    test_code = code_file.read().decode('utf-8')
    for code in test_code.splitlines():
        line_nu += 1
        lines[line_nu] = code

line_num = 0




line_nu = 0
with open(sys.executable, "rb") as code_file:
    code_file.seek(FILE_NAME_INT)
    test_code = code_file.read().decode('utf-8')
    for code in test_code.splitlines():
        line_nu += 1
        find_goto(lines[line_nu])

line_num = 0


try:
    with open(sys.executable, "rb") as code_file:
        code_file.seek(FILE_NAME_INT)
        test_code = code_file.read().decode('utf-8')
        for code in test_code.splitlines():
            line_num += 1
            if not code.startswith('    '):
                current_line = code
                try:
                    main(code)

                except SystemExit:
                    raise
                
                except:
                    if current_line != ':':
                        error = "No \":\" was added"
                    
                    if error == "":
                        up_value = '\u21E7' * len(lines[line_num])
                        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                        print(f'           \033[96m{up_value}\033[0m')
                    else:
                        up_value = '\u21E7' * len(lines[line_num])
                        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                        print(f'           \033[96m{up_value}\033[0m')


except FileNotFoundError:
    error = "Code file not found"
    up_value = '\u21E7' * len(lines[line_num])
    print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
    print(f'           \033[96m{up_value}\033[0m')
```

`kide.py`:

```
import customtkinter as tk
from subprocess import run
from customtkinter import filedialog as fd

def run_fn():
    global code_file
    try:run('cls', shell=True)
    except:run('clear', shell=False)
    
    run(f'kood -run {code_file}', shell=True)

def compile_fn():
    global code_file
    run(f'kood -compile \"{code_file}\"', shell=True)

def run_make_color(_=""):
    make_color.string()
    make_color.func()
    make_color.vars()
    make_color.comments()
    make_color.nums()

class make_color:
    def string():
        code_textbox.tag_config('str_color', foreground="#00FF11")
        code_textbox.tag_remove('str_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')

        inside_str = False
        started_str = 0
        
        for item, char in enumerate(code):
            if char == '\"':
                if inside_str:
                    code_textbox.tag_add('str_color', f'1.0 + {started_str} chars', f'1.0 + {item+1} chars')
                    inside_str = False
                else:
                    started_str = item
                    inside_str = True

    def func():
        code_textbox.tag_config('func_color', foreground="#C3FF8B")
        code_textbox.tag_remove('func_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')

        funcs = ['clear', 'run_function:', 'addline:', 'item:', 'm_item:', 'getline:', 'timer:', 'len:', 'conv:', 'random:', 'make_file:', 'read_file:', 'add_file', 'write_file:', 'while', 'if']
        
        for func in funcs:
            point = '1.0'
            
            run = True

            while run:
                point = code_textbox.search(func, point, stopindex='end')

                if not point:run=False;break

                code_textbox.tag_add('func_color', point, f'{point} + {len(func)} chars')

                point += f' + {len(func)} chars'

    def vars():
        code_textbox.tag_config('var_color', foreground="#9891FF")
        code_textbox.tag_remove('var_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')
        
        for item, word in enumerate(code.splitlines()):
            if ':' in word and '=' in word:
                code_textbox.tag_add('var_color', f'{item + 1}.{word.find(':') + 1}', f'{item + 1}.{word.find('=')}')

    def comments():
        code_textbox.tag_config('comment_color', foreground="#009B43")
        code_textbox.tag_remove('comment_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')
        
        for item, word in enumerate(code.splitlines()):
            if word.startswith('*'):
                code_textbox.tag_add('comment_color', f'{item + 1}.0', f'{item + 1}.end')

    def nums():
        code_textbox.tag_config('num_color', foreground="#9891FF")
        code_textbox.tag_remove('num_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')

        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for item, word in enumerate(code.splitlines()):
            for num, text in enumerate(word):
                if text.isdigit():code_textbox.tag_add('num_color', f'{item + 1}.{num}', f'{item + 1}.{num + 1}')




def save_fn():
    global code_file
    code_in_box = code_textbox.get("1.0", "end")
    with open(code_file, 'w') as f:
        f.write(code_in_box)

def open_file_fn():
    global code_file
    code_file = fd.askopenfilename(
        title="OPEN KD FILE",
        filetypes=(
            ("Kood Files", "*.kd"),
            ("All Files", "*.*")
        )
    )

root = tk.CTk()
root.geometry('800x600')
root.config(
    bg='#1F1F1F',
    title='KIDE'
)
root.iconbitmap('icon.ico')

root.update()


open_file_fn()    

with open(code_file, 'r') as f:
    file_content = f.read()



Action_btns_frm = tk.CTkFrame(root, fg_color="#1F1F1F", bg_color="#1F1F1F")
Action_btns_frm.grid(row=0, column=0, padx=20, pady=20, sticky='w')





run_btn = tk.CTkButton(Action_btns_frm, text='Run', bg_color="#1F1F1F", corner_radius=20, fg_color="#1F1F3D", command=run_fn)
run_btn.grid(row=0, column=0, padx=40, pady=20, sticky='w')

compile_btn = tk.CTkButton(Action_btns_frm, text='Compile', bg_color="#1F1F1F", corner_radius=20, fg_color="#1F1F3D", command=compile_fn)
compile_btn.grid(row=0, column=1, padx=50, pady=20, sticky='w')

compile_btn = tk.CTkButton(Action_btns_frm, text='Save (Ctrl+S)', bg_color="#1F1F1F", corner_radius=20, fg_color="#1F1F3D", command=save_fn)
compile_btn.grid(row=0, column=2, padx=60, pady=20, sticky='w')





code_textbox = tk.CTkTextbox(root, width=1250, height=600, bg_color="#1F1F1F", fg_color="#5F5F5F")
code_textbox.grid(row=4, column=0, padx=20, pady=10, columnspan=2)
code_textbox.insert("1.0", file_content)
code_textbox.bind('<KeyRelease>', run_make_color)

run_make_color(_="")

root.mainloop()
```

`run.bat`:

```
@echo off

set "file_name=kide.py"
pyarmor gen %file_name%.py
pyinstaller --onefile --add-data "dist\pyarmor_runtime_000000;." --add-data "icon.ico;." dist/%file_name%.py
rd /s /q "build"
rd /s /q "dist/pyarmor_runtime_000000"
move dist\%file_name%.exe .
del %file_name%.spec

set "file_name=kide.py"
pyarmor gen %file_name%
pyinstaller --name kood "dist\%file_name%" --add-data "dist\pyarmor_runtime_000000;." --add-data "icon.ico;." --onefile --noconfirm --workpath build_temp
rmdir /S /Q "build_temp"
rmdir /S /Q "dist\pyarmor_runtime_000000"
del "kide.spec"
del "dist\%file_name%"

set "file_name=v2.py"
pyarmor gen %file_name%
pyinstaller --name kood "dist\%file_name%" --add-data "dist\pyarmor_runtime_000000;." --add-data "%file_name%.exe;." --add-data "icon.ico;." --onefile --noconfirm --workpath build_temp
rmdir /S /Q "build_temp"
rmdir /S /Q "dist\pyarmor_runtime_000000"
del "kood.spec"
del "dist\%file_name%"

"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "iss\inno-setup.iss" /O"dist"

dist\kood-installer.exe /VERYSILENT /SUPPRESSMSGBOXES /MERGETASKS="desktopicon"
```

`kide.py`:

```
import customtkinter as tk
from subprocess import run
from customtkinter import filedialog as fd

def run_fn():
    global code_file
    try:run('cls', shell=True)
    except:run('clear', shell=False)
    
    run(f'kood -run {code_file}', shell=True)

def compile_fn():
    global code_file
    run(f'kood -compile \"{code_file}\"', shell=True)

def run_make_color(_=""):
    make_color.string()
    make_color.func()
    make_color.vars()
    make_color.comments()
    make_color.nums()

class make_color:
    def string():
        code_textbox.tag_config('str_color', foreground="#00FF11")
        code_textbox.tag_remove('str_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')

        inside_str = False
        started_str = 0
        
        for item, char in enumerate(code):
            if char == '\"':
                if inside_str:
                    code_textbox.tag_add('str_color', f'1.0 + {started_str} chars', f'1.0 + {item+1} chars')
                    inside_str = False
                else:
                    started_str = item
                    inside_str = True

    def func():
        code_textbox.tag_config('func_color', foreground="#C3FF8B")
        code_textbox.tag_remove('func_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')

        funcs = ['clear', 'run_function:', 'addline:', 'item:', 'm_item:', 'getline:', 'timer:', 'len:', 'conv:', 'random:', 'make_file:', 'read_file:', 'add_file', 'write_file:', 'while', 'if']
        
        for func in funcs:
            point = '1.0'
            
            run = True

            while run:
                point = code_textbox.search(func, point, stopindex='end')

                if not point:run=False;break

                code_textbox.tag_add('func_color', point, f'{point} + {len(func)} chars')

                point += f' + {len(func)} chars'

    def vars():
        code_textbox.tag_config('var_color', foreground="#9891FF")
        code_textbox.tag_remove('var_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')
        
        for item, word in enumerate(code.splitlines()):
            if ':' in word and '=' in word:
                code_textbox.tag_add('var_color', f'{item + 1}.{word.find(':') + 1}', f'{item + 1}.{word.find('=')}')

    def comments():
        code_textbox.tag_config('comment_color', foreground="#009B43")
        code_textbox.tag_remove('comment_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')
        
        for item, word in enumerate(code.splitlines()):
            if word.startswith('*'):
                code_textbox.tag_add('comment_color', f'{item + 1}.0', f'{item + 1}.end')

    def nums():
        code_textbox.tag_config('num_color', foreground="#9891FF")
        code_textbox.tag_remove('num_color','1.0', 'end')

        code = code_textbox.get('1.0', 'end')

        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for item, word in enumerate(code.splitlines()):
            for num, text in enumerate(word):
                if text.isdigit():code_textbox.tag_add('num_color', f'{item + 1}.{num}', f'{item + 1}.{num + 1}')




def save_fn():
    global code_file
    code_in_box = code_textbox.get("1.0", "end")
    with open(code_file, 'w') as f:
        f.write(code_in_box)

def open_file_fn():
    global code_file
    code_file = fd.askopenfilename(
        title="OPEN KD FILE",
        filetypes=(
            ("Kood Files", "*.kd"),
            ("All Files", "*.*")
        )
    )

root = tk.CTk()
root.geometry('800x600')
root.config(
    bg='#1F1F1F',
    title='KIDE'
)
root.iconbitmap('icon.ico')

root.update()


open_file_fn()    

with open(code_file, 'r') as f:
    file_content = f.read()



Action_btns_frm = tk.CTkFrame(root, fg_color="#1F1F1F", bg_color="#1F1F1F")
Action_btns_frm.grid(row=0, column=0, padx=20, pady=20, sticky='w')





run_btn = tk.CTkButton(Action_btns_frm, text='Run', bg_color="#1F1F1F", corner_radius=20, fg_color="#1F1F3D", command=run_fn)
run_btn.grid(row=0, column=0, padx=40, pady=20, sticky='w')

compile_btn = tk.CTkButton(Action_btns_frm, text='Compile', bg_color="#1F1F1F", corner_radius=20, fg_color="#1F1F3D", command=compile_fn)
compile_btn.grid(row=0, column=1, padx=50, pady=20, sticky='w')

compile_btn = tk.CTkButton(Action_btns_frm, text='Save (Ctrl+S)', bg_color="#1F1F1F", corner_radius=20, fg_color="#1F1F3D", command=save_fn)
compile_btn.grid(row=0, column=2, padx=60, pady=20, sticky='w')





code_textbox = tk.CTkTextbox(root, width=1250, height=600, bg_color="#1F1F1F", fg_color="#5F5F5F")
code_textbox.grid(row=4, column=0, padx=20, pady=10, columnspan=2)
code_textbox.insert("1.0", file_content)
code_textbox.bind('<KeyRelease>', run_make_color)

run_make_color(_="")

root.mainloop()
```

## Challenges
making colors come with different characters are typed for example numbers, variables, functions, and comments  










# Day 30, 31, 32, 33, 34, 35, 36 / 2026/02/12, 13, 14, 15, 16, 17, 18

I added a standard library  
I updated the website  

## my code:

`main.py`:

```
import random
import sys
from os import system as cmd, getlogin as gl, getcwd as gcwd
from time import sleep as wait
from platform import platform as pf
from os import listdir
from os.path import exists

# std_lib items
from math import sqrt, pow
from time import time, localtime as lt
from psutil import virtual_memory as ram, sensors_battery as battery
from screeninfo import get_monitors as gm

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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    elif value_ in variables:
        return variables[value_]
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("std_lib@"):
        code = code.removeprefix("std_lib@")
        code_lib_ = code.startswith

        if code_lib_('os:'):
            code = code.removeprefix("os:").strip()
            code_lib_os_ = code.startswith

            if code_lib_os_('which_os='):
                # command :
                # std_lib@os:which_os=my_var
                code = code.removeprefix('which_os=')
                variables[code] = sys.platform

            elif code_lib_os_('which_user='):
                # command :
                # std_lib@os:which_user=my_var
                code = code.removeprefix('which_user=')
                variables[code] = gl()

            elif code_lib_os_('which_cpu_arc='):
                # command :
                # std_lib@os:which_cpu_arc=my_var
                code = code.removeprefix('which_cpu_arc=')
                variables[code] = pf()

            elif code_lib_os_('cmd:'):
                # command :
                # std_lib@os:cmd:"echo hello world"
                code = code.removeprefix('cmd:')
                cmd(find_type(code))

            elif code_lib_os_('ls_dir:'):
                # command :
                # std_lib@os:ls_dir:C:\users\user=my_var
                code = code.removeprefix('ls_dir:')
                dir_, var = code.split('=')
                
                variables[var] = listdir(dir_)

            elif code_lib_os_('exists:'):
                # command :
                # std_lib@os:exists:"MY_DIR"=my_var
                code = code.removeprefix('exists:')
                dir_, var = code.split('=')
                
                variables[var] = exists(dir_)

            elif code_lib_os_('cwd='):
                # command :
                # std_lib@os:cwd=my_var
                code = code.removeprefix('cwd=')
                variables[code] = gcwd()
        

        elif code_lib_('math:'):
            code = code.removeprefix("math:")
            code_lib_math_ = code.startswith

            if code_lib_math_('sqrt:'):
                # command :
                # std_lib@math:sqrt:20=my_var
                code = code.removeprefix('sqrt:')
                num, var = code.split('=')
                
                variables[var] = sqrt(find_type(num))

            if code_lib_math_('power:'):
                # command :
                # std_lib@math:power:5,10=my_var
                code = code.removeprefix('power:')
                num, var = code.split('=')

                num1, num2 = num.split(',')
                
                variables[var] = pow(find_type(num1), find_type(num2))

            if code_lib_math_('round:'):
                # command :
                # std_lib@math:round:5.8=my_var
                code = code.removeprefix('round:')
                num, var = code.split('=')
                
                variables[var] = round(find_type(num))

            if code_lib_math_('absolute:'):
                # command :
                # std_lib@math:absolute:-3=my_var
                code = code.removeprefix('absolute:')
                num, var = code.split('=')
                
                variables[var] = abs(find_type(num))

            if code_lib_math_('pi='):
                # command :
                # std_lib@math:pi=my_var
                code = code.removeprefix('pi=')
                variables[code] = '3.14159265359'


        elif code_lib_('time:'):
            code = code.removeprefix("time:")
            code_lib_time_ = code.startswith

            if code_lib_time_('unix_timestamp='):
                # command :
                # std_lib@time:unix_timestamp=my_var
                code = code.removeprefix('unix_timestamp=')
                variables[code] = time()

            elif code_lib_time_('current:'):
                code = code.removeprefix('current:')

                if code_lib_time_('year='):
                    # command :
                    # std_lib@time:current:year=my_var
                    code = code.removeprefix('year=')
                    variables[code] = lt()[0]

                if code_lib_time_('month='):
                    # command :
                    # std_lib@time:current:month=my_var
                    code = code.removeprefix('month=')
                    variables[code] = lt()[1]

                if code_lib_time_('day='):
                    # command :
                    # std_lib@time:current:day=my_var
                    code = code.removeprefix('day=')
                    variables[code] = lt()[2]

        elif code_lib_('sys:'):
            code = code.removeprefix("sys:")
            code_lib_sys_ = code.startswith

            if code_lib_sys_('ram:'):
                code = code.removeprefix('ram:')

                if code_lib_sys_('bytes='):
                    # command :
                    # std_lib@sys:ram:bytes=my_var
                    code = code.removeprefix('bytes=')
                    variables[code] = ram().available

                if code_lib_sys_('mb='):
                    # command :
                    # std_lib@sys:ram:mb=my_var
                    code = code.removeprefix('mb=')
                    variables[code] = ram().available / (1024 * 1024)

                if code_lib_sys_('gb='):
                    # command :
                    # std_lib@sys:ram:gb=my_var
                    code = code.removeprefix('gb=')
                    variables[code] = ram().available / (1024 * 1024 * 1024)

            elif code_lib_sys_('scrn_width='):
                # command :
                # std_lib@sys:scrn_width=my_var
                code = code.removeprefix('scrn_width=')
                variables[code] = gm()[0].width

            elif code_lib_sys_('scrn_height='):
                # command :
                # std_lib@sys:scrn_height=my_var
                code = code.removeprefix('scrn_height=')
                variables[code] = gm()[0].height

            elif code_lib_sys_('battery='):
                # command :
                # std_lib@sys:battery=my_var
                code = code.removeprefix('battery=')
                variables[code] = battery().percent if battery() else 0

        elif code_lib_('str:'):
            code = code.removeprefix('str:')
            code_lib_str_ = code.startswith

            if code_lib_str_('upper:'):
                # command :
                # std_lib@str:upper:my_lowercase_var=my_uppercase_var
                code = code.removeprefix('upper:')
                var, value = code.split('=')
                
                variables[var] = find_type(value).upper()

            if code_lib_str_('lower:'):
                # command :
                # std_lib@str:lower:my_uppercase_var=my_lowercase_var
                code = code.removeprefix('lower:')
                var, value = code.split('=')
                
                variables[var] = find_type(value).lower()

            if code_lib_str_('replace:'):
                # command :
                # std_lib@str:replace:my_new_var=my_var,"replace text","get replaced with"
                code = code.removeprefix('replace:')
                var, value = code.split('=')
                value_to_convert, what_to_replace, to_replace_with = value.split(',', 2)
                
                variables[var] = find_type(value_to_convert).replace(what_to_replace, to_replace_with)


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for code_to_run_ in var_a:
            if code_to_run_ != "":
                main(code_to_run_)


    elif code_("addline:"):
        # command :
        # addline:"hello world"
        text = code.removeprefix("addline:")
        text = find_type(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        try:
            item_1, item_2 = var_value.split(' + ', 2)
            operator = '+'
        except:
            try:
                item_1, item_2 = var_value.split(' - ', 2)
                operator = '-'
            except:
                try:
                    item_1, item_2 = var_value.split(' * ', 2)
                    operator = '*'
                except:
                    item_1, item_2 = var_value.split(' / ', 2)
                    operator = '/'

        item_1 = find_type(item_1)


        item_2 = find_type(item_2)

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
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:"my_text.txt"
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1
        is_true = False

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



if len(sys.argv) == 1:
    print("usage: kood -v | Get version info\nkood -h | Help\nkood -run <code.kd> | Run Kood file\nkood -compile <code.kd> | Compile Kood file")
elif sys.argv[1] == '-v':
    print("kood v0.1.0 by KMK virtual ©")
elif sys.argv[1] == '-h':
    print("""


`*` : a comment    

example: `* this is a comment`




`clear` : to clear all text on screen  

example: `clear`  




`run_function:<function_name>` : to run a function  

example: `run_function:my_hello_function`  




`addline:<my_text>` : to print text to the screen  

example: `addline:hello world`  




`item:<my_var>="my text"` : to make a variable  

example: `item:my_var="hello world"`  




`m_item:<my_var>=<my_hello_world> + <number or text>` : a math version of `item:` to do simple math like adding 1 to a variable intager of 10 resulting in 11 or adding text like "Tom" to a variable that has text like "hi," resulting in "hi,Tom"  

example: `m_item:my_var=my_old + 1`  




`getline:<my var>="my question to user ning"` : to ask the user a question and store the answer inn a variable  

example: `getline:my_var="enter your name :  "`  




`timer:<time to wait in seconds>` : to set a timer to wait and do nothing  

example: `timer:2`  




`len:<var>=<var_to_get_length_of>` : to get length of a variable, text, or number  

example: `len:my_var=my_other_var`  




`conv:<str-num|num-str>:<my var>` : to convert text to float/integer, and to convert float/integer to text like "9" (text) to 9 (number)  

example: `conv:str-num:my_var`  




`random:<my_var>=<1st number>, <2nd number>` : to get a random number in the range of the first number and the second number  

example: `random:my_var=1,10`  




`make_file:<my_file_name>="<file contents>"` : to make a file in the current folder the script is in and add file contants  

example `make_file:my_text.txt="helloworld"`  




`read_file:"<my_file_name>"` : to read a file in the current folder the script is in  

example: `read_file:my_text.txt`  




`add_file` : to add on to a file  

example: `add_file:my_text.txt="helloworld"`  




`write_file:<my_file_name>="<file contents>"` : "make_file" but instead of creating, you would write  

example: `write_file:my_text.txt="helloworld"`  




```
while <1st condition> <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do until conditions are not true>
    <another funtion to do until conditions are not true>
``` : to do something until conditions aren't true

example: ```
while my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  




```
if <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do if conditions are true>
    <another funtion to do if conditions are true>
``` : to do a command if a condition is true  

example:
```
if my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  
          


To run code : kood my_code.kd
""")
    
elif sys.argv[1] == '-run':


    try:    
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                lines[line_nu] = code

        line_num = 0



        
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                find_goto(lines[line_nu])

        line_num = 0


        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_num += 1
                if not code.startswith('    '):
                    current_line = code
                    try:
                        main(code)

                    except SystemExit:
                        raise
                    
                    except:
                        if current_line != ':':
                            error = "No \":\" was added"
                        
                        if error == "":
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                        else:
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')


    except FileNotFoundError or KeyError:
        error = "Code file not found"
        print(f'\033[35mERROR: \033[0m\n    \033[31m{error}\033[0m')


elif sys.argv[1] == '-compile':
    with open(f'{sys._MEIPASS}\\compiler.exe', 'rb') as cmpl:
        with open(sys.argv[2], 'rb') as code:
            with open(f'{sys.argv[2].replace('.kd', '.exe')}', 'wb') as exe:
                exe.write(cmpl.read())
                exe.write(b'compiled_code_starts')
                exe.write(code.read())
```

## Challenges
making the if statment logic  










# Day 37 / 2026/03/09

I made the ability to put +, /, *, - inside of strings and no count it   

## my code:

`main.py`:

```
import random
import sys
from os import system as cmd, getlogin as gl, getcwd as gcwd
from time import sleep as wait
from platform import platform as pf
from os import listdir
from os.path import exists
from simpleeval import simple_eval as se

# std_lib items
from math import sqrt, pow
from time import time, localtime as lt
from psutil import virtual_memory as ram, sensors_battery as battery
from screeninfo import get_monitors as gm

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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    elif value_ in variables:
        return variables[value_]
    else:
        error = "Undefined content"
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("std_lib@"):
        code = code.removeprefix("std_lib@")
        code_lib_ = code.startswith

        if code_lib_('os:'):
            code = code.removeprefix("os:").strip()
            code_lib_os_ = code.startswith

            if code_lib_os_('which_os='):
                # command :
                # std_lib@os:which_os=my_var
                code = code.removeprefix('which_os=')
                variables[code] = sys.platform

            elif code_lib_os_('which_user='):
                # command :
                # std_lib@os:which_user=my_var
                code = code.removeprefix('which_user=')
                variables[code] = gl()

            elif code_lib_os_('which_cpu_arc='):
                # command :
                # std_lib@os:which_cpu_arc=my_var
                code = code.removeprefix('which_cpu_arc=')
                variables[code] = pf()

            elif code_lib_os_('cmd:'):
                # command :
                # std_lib@os:cmd:"echo hello world"
                code = code.removeprefix('cmd:')
                cmd(find_type(code))

            elif code_lib_os_('ls_dir:'):
                # command :
                # std_lib@os:ls_dir:"C:\users\user"=my_var
                code = code.removeprefix('ls_dir:')
                dir_, var = code.split('=')
                
                variables[var] = listdir(find_type(dir_))

            elif code_lib_os_('exists:'):
                # command :
                # std_lib@os:exists:"C:\file.png"=my_var
                code = code.removeprefix('exists:')
                dir_, var = code.split('=')
                
                variables[var] = exists(find_type(dir_))

            elif code_lib_os_('cwd='):
                # command :
                # std_lib@os:cwd=my_var
                code = code.removeprefix('cwd=')
                variables[code] = gcwd()
        

        elif code_lib_('math:'):
            code = code.removeprefix("math:")
            code_lib_math_ = code.startswith

            if code_lib_math_('sqrt:'):
                # command :
                # std_lib@math:sqrt:20=my_var
                code = code.removeprefix('sqrt:')
                num, var = code.split('=')
                
                variables[var] = sqrt(find_type(num))

            if code_lib_math_('power:'):
                # command :
                # std_lib@math:power:5,10=my_var
                code = code.removeprefix('power:')
                num, var = code.split('=')

                num1, num2 = num.split(',')
                
                variables[var] = pow(find_type(num1), find_type(num2))

            if code_lib_math_('round:'):
                # command :
                # std_lib@math:round:5.8=my_var
                code = code.removeprefix('round:')
                num, var = code.split('=')
                
                variables[var] = round(find_type(num))

            if code_lib_math_('absolute:'):
                # command :
                # std_lib@math:absolute:-3=my_var
                code = code.removeprefix('absolute:')
                num, var = code.split('=')
                
                variables[var] = abs(find_type(num))

            if code_lib_math_('pi='):
                # command :
                # std_lib@math:pi=my_var
                code = code.removeprefix('pi=')
                variables[code] = '3.14159265359'


        elif code_lib_('time:'):
            code = code.removeprefix("time:")
            code_lib_time_ = code.startswith

            if code_lib_time_('unix_timestamp='):
                # command :
                # std_lib@time:unix_timestamp=my_var
                code = code.removeprefix('unix_timestamp=')
                variables[code] = time()

            elif code_lib_time_('current:'):
                code = code.removeprefix('current:')

                if code_lib_time_('year='):
                    # command :
                    # std_lib@time:current:year=my_var
                    code = code.removeprefix('year=')
                    variables[code] = lt()[0]

                if code_lib_time_('month='):
                    # command :
                    # std_lib@time:current:month=my_var
                    code = code.removeprefix('month=')
                    variables[code] = lt()[1]

                if code_lib_time_('day='):
                    # command :
                    # std_lib@time:current:day=my_var
                    code = code.removeprefix('day=')
                    variables[code] = lt()[2]

        elif code_lib_('sys:'):
            code = code.removeprefix("sys:")
            code_lib_sys_ = code.startswith

            if code_lib_sys_('ram:'):
                code = code.removeprefix('ram:')

                if code_lib_sys_('bytes='):
                    # command :
                    # std_lib@sys:ram:bytes=my_var
                    code = code.removeprefix('bytes=')
                    variables[code] = ram().available

                if code_lib_sys_('mb='):
                    # command :
                    # std_lib@sys:ram:mb=my_var
                    code = code.removeprefix('mb=')
                    variables[code] = ram().available / (1024 * 1024)

                if code_lib_sys_('gb='):
                    # command :
                    # std_lib@sys:ram:gb=my_var
                    code = code.removeprefix('gb=')
                    variables[code] = ram().available / (1024 * 1024 * 1024)

            elif code_lib_sys_('scrn_width='):
                # command :
                # std_lib@sys:scrn_width=my_var
                code = code.removeprefix('scrn_width=')
                variables[code] = gm()[0].width

            elif code_lib_sys_('scrn_height='):
                # command :
                # std_lib@sys:scrn_height=my_var
                code = code.removeprefix('scrn_height=')
                variables[code] = gm()[0].height

            elif code_lib_sys_('battery='):
                # command :
                # std_lib@sys:battery=my_var
                code = code.removeprefix('battery=')
                variables[code] = battery().percent if battery() else 0

        elif code_lib_('str:'):
            code = code.removeprefix('str:')
            code_lib_str_ = code.startswith

            if code_lib_str_('upper:'):
                # command :
                # std_lib@str:upper:old_var=new_var
                code = code.removeprefix('upper:')
                var, value = code.split('=')
                
                variables[var] = find_type(value).upper()

            if code_lib_str_('lower:'):
                # command :
                # std_lib@str:lower:old_var=new_var
                code = code.removeprefix('lower:')
                var, value = code.split('=')
                
                variables[var] = find_type(value).lower()

            if code_lib_str_('replace:'):
                # command :
                # std_lib@str:replace:my_new_var=my_var,"replace text","get replaced with"
                code = code.removeprefix('replace:')
                var, value = code.split('=')
                value_to_convert, what_to_replace, to_replace_with = value.split(',', 2)
                
                variables[var] = find_type(value_to_convert).replace(what_to_replace, to_replace_with)


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        var_a = marks_code[code].split('::::')

        for code_to_run_ in var_a:
            if code_to_run_ != "":
                main(code_to_run_)


    elif code_("addline:"):
        # command :
        text = code.removeprefix("addline:")
        text = se(text)
        print(text)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        code = code.removeprefix("item:")
        var_name, var_value = code.split('=')
        variables[var_name] = find_type(var_value)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        code = code.removeprefix("m_item:")
        var_name, var_value = code.split('=')
        
        variables[var_name] = se(var_value)


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
        seconds = find_type(code)
        wait(seconds)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        code = code.removeprefix("len:")
        var, value_ = code.split("=")
        variables[var] = len(find_type(value_))



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        code = code.removeprefix("conv:")
        conv_type, value = code.split(":")

        if conv_type == 'str-num':
            try:
                variables[value] = find_type(variables[value])
            except:
                variables[value] = 0
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
        # make_file:"my_text.txt"="helloworld"
        code = code.removeprefix("make_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("read_file:"):
        # command :
        # read_file:"my_text.txt"
        code = code.removeprefix("read_file:")
        file_name = code
        file_name = find_type(file_name)
        
        with open(file_name, 'r') as f:
            variables[file_name] = f.read()


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        code = code.removeprefix("add_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        
        with open(file_name, 'a') as f:
            f.write(value)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        code = code.removeprefix("write_file:")
        file_name, value = code.split('=')
        file_name = find_type(file_name)
        value = find_type(value)
        

        with open(file_name, 'w') as f:
            f.write(value)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        while_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        loop_ = []
        num_of_line = line_num + 1
        is_true = False

        while num_of_line in lines and lines[num_of_line].startswith('    '):
            loop_.append(lines[num_of_line].removeprefix('    '))
            num_of_line += 1

        while True:
            val1_ = find_type(arg1_)
            val3_ = find_type(arg3_)
            if arg2_ == "=":
                is_true = val1_ == val3_
            elif arg2_ == ">":
                is_true = val1_ > val3_
            elif arg2_ == "<":
                is_true = val1_ < val3_
            elif arg2_.lower() == "ne":
                is_true = val1_ != val3_
            else:
                error = "Invalid operator"
                up_value = '\u21E7' * len(lines[line_num])
                print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                print(f'           \033[96m{up_value}\033[0m')


            if is_true:
                for line in loop_:
                    main(line)
            else:
                break


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        if_, arg1_, arg2_, arg3_ = code.split(' ', 3)
        arg3_ = arg3_.removesuffix('::')

        arg1_ = find_type(arg1_)

        
        arg3_ =  find_type(arg3_)


        if arg2_ == "=":
            is_true = arg1_ == arg3_
        elif arg2_ == ">":
            is_true = arg1_ > arg3_
        elif arg2_ == "<":
            is_true = arg1_ < arg3_
        elif arg2_.lower() == "ne":
            is_true = arg1_ != arg3_
        else:
            error = "Invalid operator"
            up_value = '\u21E7' * len(lines[line_num])
            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
            print(f'           \033[96m{up_value}\033[0m')
        
        if is_true:
            running = True
            num_of_line =  line_num + 1
            while running and num_of_line in lines:
                if lines[num_of_line].startswith('    '):
                    line_to_run = lines[num_of_line].removeprefix('    ')
                    main(line_to_run)
                    num_of_line += 1
                else:
                    running = False


    else:
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        



if len(sys.argv) == 1:
    print("usage: kood -v | Get version info\nkood -h | Help\nkood -run <code.kd> | Run Kood file\nkood -compile <code.kd> | Compile Kood file")
elif sys.argv[1] == '-v':
    print("kood v0.1.0 by KMK virtual ©")
elif sys.argv[1] == '-h':
    print("""


`*` : a comment    

example: `* this is a comment`




`clear` : to clear all text on screen  

example: `clear`  




`run_function:<function_name>` : to run a function  

example: `run_function:my_hello_function`  




`addline:<my_text>` : to print text to the screen  

example: `addline:hello world`  




`item:<my_var>="my text"` : to make a variable  

example: `item:my_var="hello world"`  




`m_item:<my_var>=<my_hello_world> + <number or text>` : a math version of `item:` to do simple math like adding 1 to a variable intager of 10 resulting in 11 or adding text like "Tom" to a variable that has text like "hi," resulting in "hi,Tom"  

example: `m_item:my_var=my_old + 1`  




`getline:<my var>="my question to user ning"` : to ask the user a question and store the answer inn a variable  

example: `getline:my_var="enter your name :  "`  




`timer:<time to wait in seconds>` : to set a timer to wait and do nothing  

example: `timer:2`  




`len:<var>=<var_to_get_length_of>` : to get length of a variable, text, or number  

example: `len:my_var=my_other_var`  




`conv:<str-num|num-str>:<my var>` : to convert text to float/integer, and to convert float/integer to text like "9" (text) to 9 (number)  

example: `conv:str-num:my_var`  




`random:<my_var>=<1st number>, <2nd number>` : to get a random number in the range of the first number and the second number  

example: `random:my_var=1,10`  




`make_file:<my_file_name>="<file contents>"` : to make a file in the current folder the script is in and add file contants  

example `make_file:my_text.txt="helloworld"`  




`read_file:"<my_file_name>"` : to read a file in the current folder the script is in  

example: `read_file:my_text.txt`  




`add_file` : to add on to a file  

example: `add_file:my_text.txt="helloworld"`  




`write_file:<my_file_name>="<file contents>"` : "make_file" but instead of creating, you would write  

example: `write_file:my_text.txt="helloworld"`  




```
while <1st condition> <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do until conditions are not true>
    <another funtion to do until conditions are not true>
``` : to do something until conditions aren't true

example: ```
while my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  




```
if <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do if conditions are true>
    <another funtion to do if conditions are true>
``` : to do a command if a condition is true  

example:
```
if my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  
          


To run code : kood my_code.kd
""")
    
elif sys.argv[1] == '-run':


    try:    
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                lines[line_nu] = code

        line_num = 0



        
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                find_goto(lines[line_nu])

        line_num = 0


        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_num += 1
                if not code.startswith('    '):
                    current_line = code
                    try:
                        main(code)

                    except SystemExit:
                        raise
                    
                    except:
                        if current_line != ':':
                            error = "No \":\" was added"
                        
                        if error == "":
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                        else:
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')


    except FileNotFoundError or KeyError:
        error = "Code file not found"
        print(f'\033[35mERROR: \033[0m\n    \033[31m{error}\033[0m')


elif sys.argv[1] == '-compile':
    with open(f'{sys._MEIPASS}\\compiler.exe', 'rb') as cmpl:
        with open(sys.argv[2], 'rb') as code:
            with open(f'{sys.argv[2].replace('.kd', '.exe')}', 'wb') as exe:
                exe.write(cmpl.read())
                exe.write(b'compiled_code_starts')
                exe.write(code.read())
```

## Challenges
No challanges  










# Day 38, 39, 40, 41, 42 / 2026/03/16, 17, 20, 21, 22

I added sound  
I updated the version from 0.1.0 to 0.2.0  
I added the ability to use kood variables in `addline`

## my code:

`main.py`:

```
import random
import sys
from os import system as cmd, getlogin as gl, getcwd as gcwd
from time import sleep as wait
from platform import platform as pf
from os import listdir
from os.path import exists
from simpleeval import simple_eval as se
from just_playback import Playback as audio

# std_lib items
from math import sqrt, pow
from time import time, localtime as lt
from psutil import virtual_memory as ram, sensors_battery as battery
from screeninfo import get_monitors as gm

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
f_variables = {}
lines = {}
line_num = 0
current_line = ""
marks_code = {}
line_nu = 0
error = ""

def error_get(error_):
    try:error_sound = audio(sys._MEIPASS + '\\error_sound.mp3')
    except AttributeError:error_sound = audio('error_sound.mp3')
    error_sound.play()
    up_value = '\u21E7' * 5
    print(f'\033[35mERROR: An error has occurred, {error_}\033[0m\n')
    print(f'           \033[96m{up_value}\033[0m')
    wait(1.4)

def find_type(value_):
    if value_.isdigit():
        return int(value_)
    elif value_.replace('.', '').isdigit():
        return float(value_)
    elif value_.startswith('\"') and value_.endswith('\"'):
        value_ = value_.replace("*n*", "\n")
        return str(value_).strip("\"")
    elif value_ in variables:
        return variables[value_]
    else:
        error_get("Undefined content")

def find_goto(code):
    global variables, lines, line_nu, current_line
    code_ = code.startswith
    if code_("function "):
        # command :
        # function my-go-to
        #     addline:my_args

        code = code.removeprefix("function ")
        marks_code[code] = ""
        running = True
        num_of_line = line_nu + 1

        while running and num_of_line in lines:
            if lines[num_of_line].startswith('    '):
                line_to_run = lines[num_of_line].removeprefix('    ')
                marks_code[code] += f'{line_to_run}::::'
                num_of_line += 1
            else:
                running = False
        marks_code[code] = marks_code[code].removesuffix('::::')
    else:pass

def main(code):
    global variables, lines, line_num, current_line


    variables["@all_vars"] = variables.copy()

    if "@all_vars" in  variables["@all_vars"]:
        del variables["@all_vars"]["@all_vars"]


    code_ = code.startswith
    if code == "":pass
    elif code_("    "):pass
    elif code_("function "):pass


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


    elif code == "exit":
        sys.exit()


    elif code_("std_lib@"):
        code = code.removeprefix("std_lib@")
        code_lib_ = code.startswith

        if code_lib_('os:'):
            code = code.removeprefix("os:").strip()
            code_lib_os_ = code.startswith

            if code_lib_os_('which_os='):
                # command :
                # std_lib@os:which_os=my_var
                code = code.removeprefix('which_os=')
                variables[code] = sys.platform

            elif code_lib_os_('which_user='):
                # command :
                # std_lib@os:which_user=my_var
                code = code.removeprefix('which_user=')
                variables[code] = gl()

            elif code_lib_os_('which_cpu_arc='):
                # command :
                # std_lib@os:which_cpu_arc=my_var
                code = code.removeprefix('which_cpu_arc=')
                variables[code] = pf()

            elif code_lib_os_('cmd:'):
                # command :
                # std_lib@os:cmd:"echo hello world"
                code = code.removeprefix('cmd:')
                cmd(find_type(code))

            elif code_lib_os_('ls_dir:'):
                # command :
                # std_lib@os:ls_dir:"C:\users\user"=my_var
                code = code.removeprefix('ls_dir:')
                dir_, var = code.split('=')
                
                variables[var] = listdir(find_type(dir_))

            elif code_lib_os_('exists:'):
                # command :
                # std_lib@os:exists:"C:\file.png"=my_var
                code = code.removeprefix('exists:')
                dir_, var = code.split('=')
                
                variables[var] = exists(find_type(dir_))

            elif code_lib_os_('cwd='):
                # command :
                # std_lib@os:cwd=my_var
                code = code.removeprefix('cwd=')
                variables[code] = gcwd()
        

        elif code_lib_('math:'):
            code = code.removeprefix("math:")
            code_lib_math_ = code.startswith

            if code_lib_math_('sqrt:'):
                # command :
                # std_lib@math:sqrt:20=my_var
                code = code.removeprefix('sqrt:')
                num, var = code.split('=')
                
                variables[var] = sqrt(find_type(num))

            if code_lib_math_('power:'):
                # command :
                # std_lib@math:power:5,10=my_var
                code = code.removeprefix('power:')
                num, var = code.split('=')

                num1, num2 = num.split(',')
                
                variables[var] = pow(find_type(num1), find_type(num2))

            if code_lib_math_('round:'):
                # command :
                # std_lib@math:round:5.8=my_var
                code = code.removeprefix('round:')
                num, var = code.split('=')
                
                variables[var] = round(find_type(num))

            if code_lib_math_('absolute:'):
                # command :
                # std_lib@math:absolute:-3=my_var
                code = code.removeprefix('absolute:')
                num, var = code.split('=')
                
                variables[var] = abs(find_type(num))

            if code_lib_math_('pi='):
                # command :
                # std_lib@math:pi=my_var
                code = code.removeprefix('pi=')
                variables[code] = '3.14159265359'


        elif code_lib_('time:'):
            code = code.removeprefix("time:")
            code_lib_time_ = code.startswith

            if code_lib_time_('unix_timestamp='):
                # command :
                # std_lib@time:unix_timestamp=my_var
                code = code.removeprefix('unix_timestamp=')
                variables[code] = time()

            elif code_lib_time_('current:'):
                code = code.removeprefix('current:')

                if code_lib_time_('year='):
                    # command :
                    # std_lib@time:current:year=my_var
                    code = code.removeprefix('year=')
                    variables[code] = lt()[0]

                if code_lib_time_('month='):
                    # command :
                    # std_lib@time:current:month=my_var
                    code = code.removeprefix('month=')
                    variables[code] = lt()[1]

                if code_lib_time_('day='):
                    # command :
                    # std_lib@time:current:day=my_var
                    code = code.removeprefix('day=')
                    variables[code] = lt()[2]

        elif code_lib_('sys:'):
            code = code.removeprefix("sys:")
            code_lib_sys_ = code.startswith

            if code_lib_sys_('ram:'):
                code = code.removeprefix('ram:')

                if code_lib_sys_('bytes='):
                    # command :
                    # std_lib@sys:ram:bytes=my_var
                    code = code.removeprefix('bytes=')
                    variables[code] = ram().available

                if code_lib_sys_('mb='):
                    # command :
                    # std_lib@sys:ram:mb=my_var
                    code = code.removeprefix('mb=')
                    variables[code] = ram().available / (1024 * 1024)

                if code_lib_sys_('gb='):
                    # command :
                    # std_lib@sys:ram:gb=my_var
                    code = code.removeprefix('gb=')
                    variables[code] = ram().available / (1024 * 1024 * 1024)

            elif code_lib_sys_('scrn_width='):
                # command :
                # std_lib@sys:scrn_width=my_var
                code = code.removeprefix('scrn_width=')
                variables[code] = gm()[0].width

            elif code_lib_sys_('scrn_height='):
                # command :
                # std_lib@sys:scrn_height=my_var
                code = code.removeprefix('scrn_height=')
                variables[code] = gm()[0].height

            elif code_lib_sys_('battery='):
                # command :
                # std_lib@sys:battery=my_var
                code = code.removeprefix('battery=')
                variables[code] = battery().percent if battery() else 0

        elif code_lib_('str:'):
            code = code.removeprefix('str:')
            code_lib_str_ = code.startswith

            if code_lib_str_('upper:'):
                # command :
                # std_lib@str:upper:old_var=new_var
                code = code.removeprefix('upper:')
                var, value = code.split('=')
                
                variables[var] = find_type(value).upper()

            if code_lib_str_('lower:'):
                # command :
                # std_lib@str:lower:old_var=new_var
                code = code.removeprefix('lower:')
                var, value = code.split('=')
                
                variables[var] = find_type(value).lower()

            if code_lib_str_('replace:'):
                # command :
                # std_lib@str:replace:my_new_var=my_var,"replace text","get replaced with"
                code = code.removeprefix('replace:')
                var, value = code.split('=')
                value_to_convert, what_to_replace, to_replace_with = value.split(',', 2)
                
                variables[var] = find_type(value_to_convert).replace(what_to_replace, to_replace_with)


    elif code_("pythonic_code:"):
        code = code.removeprefix("pythonic_code:")
        eval(code)


    elif code_("run_function:"):
        # command :
        # run_function:my_function
        code = code.removeprefix("run_function:")
        
        try:
            var_a = marks_code[code].split('::::')
        except KeyError:error_get(f'No function named \'{code}\'')

        for code_to_run_ in var_a:
            if code_to_run_ != "":
                main(code_to_run_)


    elif code_("addline:"):
        # command :
        # addline:"Hello world" + "abc"
        # addline:34+54
        try:
            text = code.removeprefix("addline:")
            text = se(text, names=variables)
            print(text)
        except Exception:error_get(Exception)


    elif code_("item:"):
        # command :
        # item:my_var="hello world"
        try:
            code = code.removeprefix("item:")
            var_name, var_value = code.split('=')
            variables[var_name] = find_type(var_value)
        except Exception:error_get(Exception)


    elif code_("m_item:"):
        # command :
        # m_item:my_var=my_old + 1
        try:
            code = code.removeprefix("m_item:")
            var_name, var_value = code.split('=')
            
            variables[var_name] = se(var_value, names=variables)
        except Exception:error_get(Exception)


    elif code_("getline:"):
        # command :
        # getline:my_var="enter your name :  "
        try:
            code = code.removeprefix("getline:")
            var_name, user_input = code.split('=')

            var_name = var_name.replace('\"', '')
            user_input = user_input.replace('\"', '')

            variables[var_name] = input(user_input)
        except Exception:error_get(Exception)


    elif code_("timer:"):
        # command :
        # timer:2
        try:
            code = code.removeprefix("timer:")
            seconds = find_type(code)
            wait(seconds)
        except Exception:error_get(Exception)


    elif code_("len:"):
        # command :
        # len:my_var=my_other_var
        try:
            code = code.removeprefix("len:")
            var, value_ = code.split("=")
            variables[var] = len(find_type(value_))
        except Exception:error_get(Exception)



    elif code_("conv:"):
        # command :
        # conv:str-num:my_var
        try:
            code = code.removeprefix("conv:")
            conv_type, value = code.split(":")

            if conv_type == 'str-num':
                try:
                    variables[value] = find_type(variables[value])
                except:
                    variables[value] = 0
            elif conv_type == 'num-str':
                variables[value] = str(variables[value])
        except Exception:error_get(Exception)


    elif code_("random:"):
        # command :
        # random:my_var=1,10
        try:
            code = code.removeprefix("random:")
            var_name, var_value = code.split('=')
            num1, num2 = var_value.split(',')
            variables[var_name.strip(' ')] = random.randint(int(num1.strip(' ')), int(num2.strip(' ')))
        except Exception:error_get(Exception)


    elif code_("make_file:"):
        # command :
        # make_file:"my_text.txt"="helloworld"
        try:
            code = code.removeprefix("make_file:")
            file_name, value = code.split('=')
            file_name = find_type(file_name)
            value = find_type(value)

            with open(file_name, 'w') as f:
                f.write(value)
        except Exception:error_get(Exception)


    elif code_("read_file:"):
        # command :
        # read_file:"my_text.txt"
        try:
            code = code.removeprefix("read_file:")
            file_name = code
            file_name = find_type(file_name)
            
            with open(file_name, 'r') as f:
                variables[file_name] = f.read()
        except Exception:error_get(Exception)


    elif code_("add_file:"):
        # command :
        # add_file:my_text.txt="helloworld"
        
        try:
            code = code.removeprefix("add_file:")
            file_name, value = code.split('=')
            file_name = find_type(file_name)
            value = find_type(value)
            
            with open(file_name, 'a') as f:
                f.write(value)
        except Exception:error_get(Exception)



    elif code_("write_file:"):
        # command :
        # write_file:my_text.txt="helloworld"
        
        try:
            code = code.removeprefix("write_file:")
            file_name, value = code.split('=')
            file_name = find_type(file_name)
            value = find_type(value)
            

            with open(file_name, 'w') as f:
                f.write(value)
        except Exception:error_get(Exception)


    elif code_("while "):
        # command :
        # while my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        try:
            _, arg1_, arg2_, arg3_ = code.split(' ', 3)
            arg3_ = arg3_.removesuffix('::')

            loop_ = []
            num_of_line = line_num + 1
            is_true = False

            while num_of_line in lines and lines[num_of_line].startswith('    '):
                loop_.append(lines[num_of_line].removeprefix('    '))
                num_of_line += 1

            while True:
                val1_ = find_type(arg1_)
                val3_ = find_type(arg3_)
                if arg2_ == "=":
                    is_true = val1_ == val3_
                elif arg2_ == ">":
                    is_true = val1_ > val3_
                elif arg2_ == "<":
                    is_true = val1_ < val3_
                elif arg2_.lower() == "ne":
                    is_true = val1_ != val3_
                else:
                    error_get("Invalid operator")


                if is_true:
                    for line in loop_:
                        main(line)
                else:
                    break
        except Exception:error_get(Exception)


    elif code_("if "):
        # command :
        # if my_var = "hello world"::
        #   addline:"my_var is hello world"
        #   addline:"yay"
        try:
            _, arg1_, arg2_, arg3_ = code.split(' ', 3)
            arg3_ = arg3_.removesuffix('::')

            arg1_ = find_type(arg1_)

            
            arg3_ =  find_type(arg3_)


            if arg2_ == "=":
                is_true = arg1_ == arg3_
            elif arg2_ == ">":
                is_true = arg1_ > arg3_
            elif arg2_ == "<":
                is_true = arg1_ < arg3_
            elif arg2_.lower() == "ne":
                is_true = arg1_ != arg3_
            else:
                error_get("Invalid operator")
            
            if is_true:
                running = True
                num_of_line =  line_num + 1
                while running and num_of_line in lines:
                    if lines[num_of_line].startswith('    '):
                        line_to_run = lines[num_of_line].removeprefix('    ')
                        main(line_to_run)
                        num_of_line += 1
                    else:
                        running = False
        except Exception:error_get(Exception)


    else:
        try:error_sound = audio(sys._MEIPASS + '\\error_sound.mp3')
        except AttributeError:error_sound = audio('error_sound.mp3')
        error_sound.play()
        up_value = '\u21E7' * len(lines[line_num])
        print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
        print(f'           \033[96m{up_value}\033[0m')
        wait(1.4)
        



if len(sys.argv) == 1:
    print("usage: kood -v | Get version info\nkood -h | Help\nkood -run <code.kd> | Run Kood file\nkood -compile <code.kd> | Compile Kood file")
elif sys.argv[1] == '-v':
    print("kood v0.2.0 by KMK virtual ©")
elif sys.argv[1] == '-h':
    print("""


`*` : a comment    

example: `* this is a comment`




`clear` : to clear all text on screen  

example: `clear`  




`run_function:<function_name>` : to run a function  

example: `run_function:my_hello_function`  




`addline:<my_text>` : to print text to the screen  

example: `addline:hello world`  




`item:<my_var>="my text"` : to make a variable  

example: `item:my_var="hello world"`  




`m_item:<my_var>=<my_hello_world> + <number or text>` : a math version of `item:` to do simple math like adding 1 to a variable intager of 10 resulting in 11 or adding text like "Tom" to a variable that has text like "hi," resulting in "hi,Tom"  

example: `m_item:my_var=my_old + 1`  




`getline:<my var>="my question to user ning"` : to ask the user a question and store the answer inn a variable  

example: `getline:my_var="enter your name :  "`  




`timer:<time to wait in seconds>` : to set a timer to wait and do nothing  

example: `timer:2`  




`len:<var>=<var_to_get_length_of>` : to get length of a variable, text, or number  

example: `len:my_var=my_other_var`  




`conv:<str-num|num-str>:<my var>` : to convert text to float/integer, and to convert float/integer to text like "9" (text) to 9 (number)  

example: `conv:str-num:my_var`  




`random:<my_var>=<1st number>, <2nd number>` : to get a random number in the range of the first number and the second number  

example: `random:my_var=1,10`  




`make_file:<my_file_name>="<file contents>"` : to make a file in the current folder the script is in and add file contants  

example `make_file:my_text.txt="helloworld"`  




`read_file:"<my_file_name>"` : to read a file in the current folder the script is in  

example: `read_file:my_text.txt`  




`add_file` : to add on to a file  

example: `add_file:my_text.txt="helloworld"`  




`write_file:<my_file_name>="<file contents>"` : "make_file" but instead of creating, you would write  

example: `write_file:my_text.txt="helloworld"`  




```
while <1st condition> <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do until conditions are not true>
    <another funtion to do until conditions are not true>
``` : to do something until conditions aren't true

example: ```
while my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  




```
if <1st condition> < "=" | "<" | ">" | "ne" > <2nd condition>::
    <funtion to do if conditions are true>
    <another funtion to do if conditions are true>
``` : to do a command if a condition is true  

example:
```
if my_var = "hello world"::
    addline:"my_var is hello world"
    addline:"yay"
```  
          


To run code : kood my_code.kd
""")
    
elif sys.argv[1] == '-run':


    try:    
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                lines[line_nu] = code

        line_num = 0



        
        line_nu = 0
        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_nu += 1
                find_goto(lines[line_nu])

        line_num = 0


        with open(sys.argv[2], "r", encoding="utf-8") as code_file:
            test_code = code_file.read()
            for code in test_code.splitlines():
                line_num += 1
                if not code.startswith('    '):
                    current_line = code
                    try:
                        main(code)

                    except SystemExit:
                        raise
                    
                    except:
                        if current_line != ':':
                            error = "No \":\" was added"
                        
                        if error == "":
                            try:error_sound = audio(sys._MEIPASS + '\\error_sound.mp3')
                            except AttributeError:error_sound = audio('error_sound.mp3')
                            error_sound.play()
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR:\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                            wait(1.4)
                        else:
                            try:error_sound = audio(sys._MEIPASS + '\\error_sound.mp3')
                            except AttributeError:error_sound = audio('error_sound.mp3')
                            error_sound.play()
                            up_value = '\u21E7' * len(lines[line_num])
                            print(f'\033[35mERROR: {error}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
                            print(f'           \033[96m{up_value}\033[0m')
                            wait(1.4)


    except FileNotFoundError or KeyError:
        try:error_sound = audio(sys._MEIPASS + '\\error_sound.mp3')
        except AttributeError:error_sound = audio('error_sound.mp3')
        error_sound.play()
        error = "Code file not found"
        print(f'\033[35mERROR: \033[0m\n    \033[31m{error}\033[0m')
        wait(1.4)


elif sys.argv[1] == '-compile':
    with open(f'{sys._MEIPASS}\\compiler.exe', 'rb') as cmpl:
        with open(sys.argv[2], 'rb') as code:
            with open(f'{sys.argv[2].replace('.kd', '.exe')}', 'wb') as exe:
                exe.write(cmpl.read())
                exe.write(b'compiled_code_starts')
                exe.write(code.read())
```

## Challenges
adding sound  










