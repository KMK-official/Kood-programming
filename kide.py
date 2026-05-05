import customtkinter as tk
from subprocess import run
from customtkinter import filedialog as fd
import sys

variables = []

def run_fn(event=None):
    global code_file
    try:run('cls', shell=True)
    except:run('clear', shell=False)
    
    run(f'kood -run {code_file}', shell=True)

def compile_fn(event=None):
    global code_file
    try:run('cls', shell=True)
    except:run('clear', shell=False)

    
    exe_file_list = code_file.rsplit('.', 1)

    exe_file = str(exe_file_list[0]) + '.exe'
    

    run(f'kood -compile \"{code_file}\"', shell=True)
    print('success\n\ncompiled')
    run(f'\"{exe_file}\"')

def run_make_color(event=None):
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
        
        for item, word in enumerate(code.splitlines()):
            for num, text in enumerate(word):
                if text.isdigit():code_textbox.tag_add('num_color', f'{item + 1}.{num}', f'{item + 1}.{num + 1}')




def save_fn(event=None):
    global code_file
    code_in_box = code_textbox.get("1.0", "end-1c")
    with open(code_file, 'w') as f:
        f.write(code_in_box)
    return "break"

def open_file_fn(event=None):
    global code_file
    code_file = fd.askopenfilename(
        title="OPEN KD FILE",
        filetypes=(
            ("v2.py Files", "*.kd"),
            ("All Files", "*.*")
        )
    )

root = tk.CTk()
root.geometry('800x600')
root.config(
    bg='#1F1F1F',
)
root.title('KIDE')
try:root.iconbitmap(sys._MEIPASS + '/icon.ico')
except:root.iconbitmap('iss/icon.ico')
root.bind('<Control-s>', save_fn)
root.bind('<Control-r>', run_fn)
root.bind('<Control-k>', compile_fn)

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

run_make_color(event="")

root.mainloop()