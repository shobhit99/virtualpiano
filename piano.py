import ply.lex as lex
import pyautogui
import time
import sys

tokens = [
    'NOTE',
    'COMBINATION',
    'TIME',
    'NEWLINE'

]

t_NOTE = r'[A-Za-z0-9!@$%^*(]'

def t_TIME(t):
    r'`\d\.\d{1,3}`'
    t.value = float(t.value[1:-1])
    return t

def t_COMBINATION(t):
    r'\[[A-Za-z0-9!@$%^*(]+\]'
    t.value = list(t.value[1:-1])
    return t

t_NEWLINE = r'\n'
t_ignore = r' '

def t_error(t):
    print('Illegal charas')
    t.lexer.skip(1)

lexer = lex.lex()
music = open("lightofseven.txt", "r").read()
lexer.input(music)

time.sleep(2)

while True:
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'NOTE' or tok.type == 'COMBINATION':
        pyautogui.press(tok.value)
    elif tok.type == 'TIME':
        time.sleep(tok.value)
    time.sleep(0.2)