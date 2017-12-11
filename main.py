from validate import *
from or_op import *
from and_op import *
from xor_op import *
from query import *
from bracket import *


def update_facts(f, v_list):
    no_i = 0
    for line in f:
        for char in line:
            if char == "!":
                no_i = 1
            if char.isalpha() and no_i == 0:
                v_list[char] = True
            if char.isalpha() and no_i == 1:
                v_list[char] = False
    return v_list


if len(sys.argv) != 2:
    print ('Usage: python main.py [filename]')
    sys.exit(1)
val = Validate(sys.argv[1])
kb = Validate.get_kb(val)
facts = val.get_facts()
q = Validate.get_quarries(val)
val_list = Validate.get_dictionary(val)
val_list = update_facts(facts, val_list)
bracket = Bracket(kb)
val_list = bracket.bracket_op(val_list, facts)
or_op = OrOp(kb)
val_list = or_op.or_op(val_list, facts)
and_op = AndOp(kb)
val_list = and_op.and_op(val_list, facts)
xor_op = XorOp(kb)
val_list = xor_op.xor_op(val_list, facts)
query = Query(val_list)
query.facts(q)
