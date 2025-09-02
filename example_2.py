def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents = documents + (new_doc,)
    return documents

# This function demonstrates how new data can be constructed in a functional style: 
# `add_prefix` takes a `document` string and a collection of existing `documents` 
# (represented as a tuple), creates a prefix based on the current length of `documents`, 
# and produces a new version of the collection that includes the prefixed document. 
# It avoids mutating the original tuple—instead, it returns a new one with the added element—
# showing immutability and transformation by function application.
#
# Teaching points:
# 1. Data transformation – inputs are used to build a new output rather than changing state.  
# 2. Purity – same inputs always give the same output, with no side effects.  
# 3. Immutability – tuples cannot be modified in place, so concatenation creates a new one.  
# 4. Functional thinking – logic is expressed as transformation of values, not commands.  
