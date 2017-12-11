import operator
import sys


class AndOp:
    __data = []
    __n = ['=', '<', '>']

    def __init__(self, values):
        for line in values:
            if '+' in line:
                self.__data.append(line)

    @staticmethod
    def check_facts(char, facts):
        for line in facts:
            for c in line:
                if c == char:
                    return True
        return False

    def before_equals(self, var_list, neg, facts):
        num_t = 0
        num_char = 0
        equal = 0
        for char, value in sorted(neg.items(), key=operator.itemgetter(1)):
            if neg[char] == 2:
                equal = 1
            if neg[char] == 0 and var_list[char] is True:
                num_t += 1
            elif neg[char] == 1 and var_list[char] is False:
                num_t += 1
            if char.isalpha() and neg[char] < 2:
                num_char += 1
            if num_char == num_t and equal == 1 and char.isalpha():
                if neg[char] == 4:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is True:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = False
                if neg[char] == 3:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is False:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = True
        return var_list

    def after_equals(self, var_list, neg, facts):
        equals = 0
        first_t = 0
        for char, value in sorted(neg.items(), key=operator.itemgetter(1)):
            if neg[char] == 2:
                equals = 1
            if char.isalpha() and equals == 0:
                if var_list[char] is False and neg[char] == 1:
                    first_t = 1
                if var_list[char] is True and neg[char] == 0:
                    first_t = 1
            if equals == 1 and char.isalpha():
                if neg[char] == 4 and first_t == 1:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is True:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = False
                if neg[char] == 3 and first_t == 1:
                    if self.check_facts(char, facts) is True:
                        if var_list[char] is False:
                            print "Error : Contradiction"
                            sys.exit(1)
                    var_list[char] = True
        return var_list

    def operation(self, var_list, neg, facts):
        i = 0
        j = 0
        for char in neg:
            if neg[char] < 2 and char.isalpha():
                i += 1
            elif char.isalpha():
                j += 1
        if i > j:
            var_list = self.before_equals(var_list, neg, facts)
        elif i < j:
            var_list = self.after_equals(var_list, neg, facts)
        return var_list

    def and_op(self, var_list, facts):      # 0-1 for before equals 3-4 for after equals 2 for operation
        for line in self.__data:            # 1-4 numbers are negative 0-3 are positive
            equals = 0
            not_i = 0
            neg = {}
            for char in line:
                if char in self.__n and equals == 0:
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
            self.operation(var_list, neg, facts)
        return var_list
