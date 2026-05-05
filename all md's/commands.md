

`*` : a comment    

example: `* this is a comment`




`clear` : to clear all text on screen  

example: `clear`  




`exit` : to exit/end the code  

example: `exit`  




`std_lib@os:which_os=<var>` : to get the OS  

example: `std_lib@os:which_os=my_var`  




`std_lib@os:which_user=<var>` : to get the user running the kood code  

example: `std_lib@os:which_user=my_var`  




`std_lib@os:which_cpu_arc=<var>` : to get the CPU architecture  

example: `std_lib@os:which_cpu_arc=my_var`  




`std_lib@os:cmd:<command>` : to run a command in the OS's terminal  

example: `std_lib@os:cmd:"echo hello world"`  




`std_lib@os:ls_dir:<path>=<var>` : to get all items in a folder  

example: `std_lib@os:ls_dir:"C:\users\user"=my_var`  




`std_lib@os:exists:<file_path>=<var>` : to check if a file/folder exists  

example: `std_lib@os:exists:"C:\file.png"=my_var`  




`std_lib@os:cwd=<var>` : to get the current folder the program is running in  

example: `std_lib@os:cwd=my_var`  




`std_lib@math:sqrt:<num>=<var>` : to get square root  

example: `std_lib@math:sqrt:20=my_var`  




`std_lib@math:power:<num_1>,<num_2>=<var>` : to get power of a number  

example: `std_lib@math:power:5,10=my_var`  




`std_lib@math:round:<num>=<var>` : to get a rounded number  

example: `std_lib@math:round:5.8=my_var`  




`std_lib@math:absolute:<num>=<var>` : to get the absolute value of a number  

example: `std_lib@math:absolute:-3=my_var`  




`std_lib@math:pi=<var>` : to get the value of pi  

example: `std_lib@math:pi=my_var`  




`std_lib@time:unix_timestamp=<var>` : to get the unix timestamp, which is the amount of seconds since Jan 1, 1970  

example: `std_lib@time:unix_timestamp=my_var`  





`std_lib@time:current:<year | month | day>=<var>` : to get the current date  

example: `std_lib@time:current:year=my_var`  




`std_lib@sys:ram:<bytes | mb | gb>=<var>` : to get the RAM of the computer  

example: `std_lib@sys:ram:bytes=my_var`  




`std_lib@sys:<scrn_width | scrn_height>=my_var` : to get the dimensions of the user's screen  

example: `std_lib@sys:scrn_width=my_var`  




`std_lib@sys:battery=<var>` : to get the battery percentage of the user's computer  

example: `std_lib@sys:battery=my_var`  




`std_lib@str:<upper | lower>:old_var=new_var` : to make text fully uppercase or lowwercase  

example: `std_lib@str:upper:old_var=new_var`  




`std_lib@str:replace:my_new_var=my_var,<replace_text>,<get_replaced_with>` : to get new text but, replacing some words with new words  

example: `std_lib@str:replace:my_new_var=my_var,"replace text","get replaced with"`  




`run_function:<function_name>` : to run a function  

example: `run_function:my_hello_function`  




`addline:<my_text>` : to print text to the screen  

example: `addline:hello world`  




`item:<my_var>="my text"` : to make a variable  

example: `item:my_var="hello world"`  




`m_item:<my_var>=<my_hello_world> + <number or text>` : a math version of `item:` to do simple math like adding 1 to a variable intager of 10 resulting in 11 or adding text like "Tom" to a variable that has text like "hi," resulting in "hi,Tom"  

example: `m_item:my_var=my_old + 1`  




`getline:<my var>="my question to user"` : to ask the user a question and store the answer inn a variable  

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




`add_file:<my_file_name>="<file contents>"` : to add on to a file  

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