import operator
import sys


class XorOp:
    __data = []
    __change = 1
    __n = ['=', '<', '>']

    def __init__(self, values):
        for line in values:
            if '^' in line:
                self.__data.append(line)

    @staticmethod
    def check_facts(char, facts):
        for line in facts:
            for c in line:
                if c == char:
                    return True
        return False

    def operation(self, var_list, neg, facts):
        num_t = 0
        equals = 0
        for char, value in sorted(neg.items(), key=operator.itemgetter(1)):
            if neg[char] == 2:
                equals = 1
            if neg[char] == 0 or neg[char] == 3 and char.isalpha():
                if var_list[char] is True:
                    num_t += 1
            elif neg[char] == 1 or neg[char] == 4 and char.isalpha():
                if var_list[char] is False:
                    num_t += 1
            if equals == 1 and char.isalpha():
                if num_t == 1 and neg[char] == 3:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is False:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = True
                elif num_t == 1 and neg[char] == 4:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is True:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = False
        return var_list

    def xor_op(self, var_list, facts):
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
            var_list = self.operation(var_list, neg, facts)
        return var_list
