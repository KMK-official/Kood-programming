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
    up_value = '\u21E7' * len(lines[line_num])
    print(f'\033[35mERROR: An error has occurred, {error_}\033[0m\n    \033[31mLINE : {line_num}\n    CODE : {lines[line_num]}\033[0m')
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
        except (Exception, BaseException):error_get(Exception)


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