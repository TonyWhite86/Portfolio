"""Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
- Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
- Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
- Expresión balanceada: { [ a ( c + d ) ] - 5 }
- Expresión no balanceada: { a ( c + d ) ] - 5 }"""


def isBalanced(expression: str) -> bool:
    stack = list()
    for char in expression:
        # This first if it's the begining of the bucle to select the opener
        if char == "[" or char == "{" or char == "(":
            stack.append(char)
            continue

        if char == "]":
            if len(stack) != 0:
                pop = stack.pop()
                if pop != "[":
                    return False
            else:
                return False

        elif char == "}":
            if len(stack) != 0:
                pop = stack.pop()
                if pop != "{":
                    return False
            else:
                return False

        elif char == ")":
            if len(stack) != 0:
                pop = stack.pop()
                if pop != "(":
                    return False
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

print(isBalanced("{a + b [c] (2x2)}}}}"))
print(isBalanced("{ [ a ( c + d ) ] - 5 }"))
print(isBalanced("{ a ( c + d ) ] - 5 }"))
print(isBalanced("{a^4 + (((ax4)}"))
print(isBalanced("{ ] a ( c + d ) + ( 2 - 3 )[ - 5 }"))
print(isBalanced("{{{{{{(}}}}}}"))
print(isBalanced("(a"))




