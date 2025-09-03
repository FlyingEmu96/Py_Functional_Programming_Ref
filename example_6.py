def file_type_getter(file_extension_tuples):
    mapping = {}  # empty dictionary
    
    for file_type, extensions in file_extension_tuples:
        for ext in extensions:
            mapping[ext] = file_type  # map each extension to its type

    # return a lookup function
    return lambda ext: mapping.get(ext, "Unknown")

#lambda mapping
