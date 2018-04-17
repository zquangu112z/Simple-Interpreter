from simple_interpreter.imp_lexer import *

if __name__ == '__main__':
    file = open("src/simple_interpreter/factorical.imp")
    characters = file.read()
    file.close()
    tokens = imp_lex(characters)
    for token in tokens:
        print(token)
