def stylize_title(document):
    return add_border(center_title(document))

def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)

# This code shows function composition in action: `stylize_title` applies two pure functions 
# in sequence—first centering the document’s title (`center_title`), then adding a border 
# beneath it (`add_border`). Each helper function extracts the first line of the document, 
# transforms it (centering within 40 characters or appending a row of asterisks), and returns 
# a new string without mutating the input. This illustrates functional programming principles 
# where problems are broken into small, deterministic transformations that can be composed 
# into larger behaviors.
#
# Teaching points:
# 1. Function composition – combining small transformations (`add_border(center_title(x))`).
# 2. Purity and determinism – outputs depend only on inputs, with no side effects.
# 3. Decomposition – splitting logic into reusable, testable functions.
# 4. Immutability – original inputs remain unchanged, new strings are produced.

