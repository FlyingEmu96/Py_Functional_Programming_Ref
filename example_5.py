def file_to_prompt(file, to_string):
    stringified = to_string(file)
    return f"```\n{stringified}\n```"

# function that takes file dic then turns it into strings in a format
