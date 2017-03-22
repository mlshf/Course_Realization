from pycparser import parse_file,c_parser, c_generator, c_ast
import io
from contextlib import redirect_stdout
import sys
from anytree import RenderTree, Node
import astmscp

# with open("C:/Users/fu3uk/Desktop/a/main.c", 'r') as fin:
    # print(fin.read())

# with open("C:/Users/fu3uk/Desktop/a/main_pp.c", 'r') as fin:
    # print(fin.read())

ast1 = parse_file("C:/Users/fu3uk/Desktop/a/main_I.c")
#ast2 = parse_file("C:/Users/fu3uk/Desktop/a/main.c")
#ast1.show()
for i in ast1.ext:
    if not ("Typedef" in str(i)):
        i.show()
#print("")
#ast2.show()
print("")

lines = [8, 2]

ast_root = Node(";")

for i in range(0, len(ast1.ext)):
    if (not "Typedef" in str(ast1.ext[i])) and (not "Pragma" in str(ast1.ext[i])):
        compound = ast1.ext[i].body.block_items
        if not "None" in str(compound):
            astmscp.ast_compound(compound, ast_root, ast_root)

for pre, fill, node in RenderTree(ast_root):
    print("%s%s" % (pre, node.name))
print("")


r = Node("?")
r1 = Node(";")
r1n1 = Node("=", parent = r1)
r1n11 = Node("x", parent = r1n1)
r1n12 = Node("+", parent=r1n1)
r1n121 = Node("a", parent = r1n12)
r1n122 = Node("/", parent = r1n12)
r1n1221 = Node("1", parent=r1n122)
r1n1222 = Node("27", parent=r1n122)
r1n2 = Node("return", parent = r1)

r2 = Node(";")
r2n1 = Node("=", parent = r2)
r2n11 = Node("X2", parent = r2n1)
r2n12 = Node("+", parent=r2n1)
r2n121 = Node("B", parent = r2n12)
r2n122 = Node("*", parent = r2n12)
r2n1221 = Node("3", parent=r2n122)
r2n1222 = Node("-", parent=r2n122)
r2n12221 = Node("y", parent=r2n1222)
r2n12222 = Node("ZZZ", parent=r2n1222)
r2n2 = Node("exit", parent = r2)

num = 1
rules1 = []
rules2 = []
astmscp.createAUT(ast_root, r2, r, num, rules1, rules2)

for pre, fill, node in RenderTree(r1):
    print("%s%s" % (pre, node.name))
print("")

for pre, fill, node in RenderTree(r2):
    print("%s%s" % (pre, node.name))
print("")

for pre, fill, node in RenderTree(r):
    print("%s%s" % (pre, node.name))
print("")

print("Distance between trees is: " + str(astmscp.distanceAUT(rules1, rules2)))

#print(aString) #This prints "None" instead of printing the parse tree
