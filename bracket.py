import re
from string import strip

import sys

str_to_token = {'True': True,
                'False': False,
                '+': lambda left, right: left and right,
                '|': lambda left, right: left or right,
                '^': lambda left, right: left ^ right,
                '(': '(',
                ')': ')'}


def create_token_list(s, str_to_token=str_to_token):
    s = s.replace('(', ' ( ')
    s = s.replace(')', ' ) ')
    return [str_to_token[char] for char in s.split()]


def find(lst, what, start):
    return [i for i, it in enumerate(lst) if it == what and i >= start]


def eval(token_lst):
    return token_lst[1](token_lst[0], token_lst[2])


def bool_eval(token_list, res=True):
    if not token_list:
        return res
    if len(token_list) == 1:
        return token_list[0]
    left = find(token_list, '(', 0)
    if not left:
        return eval(token_list)
    l_paren = left[-1]
    r_paren = find(token_list, ')', l_paren + 4)[0]
    token_list[l_paren:r_paren + 1] = [eval(token_list[l_paren + 1:r_paren])]
    return bool_eval(token_list, eval)


def brackets(string):
    return bool_eval(create_token_list(string))


def check_facts(char, facts):
    for line in facts:
        for c in line:
            if c == char:
                return True
    return False


class Bracket:
    __data = []

    def __init__(self, kb):
        for line in kb:
            if '(' in line or '(' in line:
                self.__data.append(line)

    def check_facts(char, facts):
        for line in facts:
            for c in line:
                if c == char:
                    print 'Error: Contradiction'
                    sys.exit(1)
        return False

    def bracket_op(self, varlist, facts):
        for line in self.__data:
            end = line.split('=>', 1)[1]
            line = strip(line.split('=', 1)[0])
            line = line.replace('|', ' | ')
            line = line.replace('+', ' + ')
            line = line.replace('^', ' ^ ')
            i = 0
            while i < len(line):
                char = line[i]
                if char.isalpha() or line[i - 1] == '!':
                    if line[i - 1] == '!':
                        line = line.replace('!', '', 1)
                        if varlist[char] is False:
                            line = line.replace(char, 'True')
                            i += 4
                        else:
                            line = line.replace(char, 'False')
                            i += 5
                    else:
                        if varlist[char] is True:
                            line = line.replace(char, 'True')
                            i += 4
                        else:
                            line = line.replace(char, 'False')
                            i += 5
                else:
                    i += 1
            check_facts(end, facts)
            varlist[end] = brackets(line)
        return varlist
