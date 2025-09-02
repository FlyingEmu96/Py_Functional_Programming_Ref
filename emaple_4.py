def process_line(line):
    stripped = line.strip()              # remove spaces/tabs/newlines from start and end
    capitalized = stripped.upper()       # make every letter uppercase
    rm_punc = capitalized.replace(".", "")  # remove all periods from the text
    suffixed = f"{rm_punc}..."           # add three dots (...) at the end
    return suffixed                      # give back the final string
