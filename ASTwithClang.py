# Working with Clang's AST via python

#import the required libraries
from clang import cindex

# Index provides an interface to the Clang Cindex Library.
# Basically, Index provides an interface for reading and parsing translation units
index = cindex.Index.create()

# Runs Clangs, and generates AST from given source code
translation_unit = index.parse("sample_hello.cpp")

# Printing some stuff from AST
for child in translation_unit.cursor.get_children():
   print (child.spelling)
