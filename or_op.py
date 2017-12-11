import operator
import sys


class OrOp:
    __data = []
    __n = ['=', '<', '>']
    __change = 1

    def __init__(self, var_list):
        for line in var_list:
            if '|' in line or ('^' not in line and '+' not in line):
                self.__data.append(line)

    @staticmethod
    def check_facts(char, facts):
        for line in facts:
            for c in line:
                if c == char:
                    return True
        return False

    def operations(self, var_list, neg, facts):
        equals = 0
        num_t = 0
        for char, value in sorted(neg.items(), key=operator.itemgetter(1)):
            if neg[char] == 2:
                equals = 1
            if neg[char] == 0 or neg[char] == 3:
                if var_list[char] is True:
                    num_t += 1
            if neg[char] == 1 or neg[char] == 4:
                if var_list[char] is False:
                    num_t += 1
            if equals == 1 and num_t > 0:
                if neg[char] == 3:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is False:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = True
                elif neg[char] == 4:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is True:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = False
        return var_list

    def or_op(self, var_list, facts):
        while self.__change == 1:
            c = 0
            for line in self.__data:
                neg = {}
                equals = 0
                not_i = 0
                for char in line:
                    if char == '=':
                        equals = 1
                        neg[char] = 2
                    if char == '!':
                        not_i = 1
                    if char.isalpha() and equals == 0:
                        if not_i == 0:
                            neg[char] = 0
                        elif not_i == 1:
                            neg[char] = 1
                            not_i = 0
                    if char.isalpha() and equals == 1:
                        if not_i == 0:
                            neg[char] = 3
                        elif not_i == 1:
                            neg[char] = 4
                            not_i = 0
                var_list = self.operations(var_list, neg, facts)
            if c == 0:
                self.__change = 0
        return var_list
