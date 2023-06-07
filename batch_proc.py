import sys
import re

assert len(sys.argv) > 1

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

patterns = {
    "comment": re.compile(r"#.*"),
    "special": re.compile(r"__version__.*"),
    "wildcard": re.compile(r"from \.\w+ import \*"),
    "singleline": re.compile(r"from \.(\w+(\.\w+)*)? import \w+ as \w+(, \w+ as \w+)*"),
    "multiline_start": re.compile(r"from \.+(\w+(\.\w+)*)? import \("),
    "multiline": re.compile(r"    \w+ as \w+,"),
    "multiline_end": re.compile(r"\)"),
    "bad_singleline": re.compile(r"from (?P<from>\.(\w+(\.\w+)*)?) import (?P<import>\w+(, \w+)*)"),
    "bad_multiline": re.compile(r"    (\w+),"),
}

for i in range(len(lines)):
    line = lines[i][:-1]
    if not line:
        pass
    elif patterns["comment"].fullmatch(line):
        pass
    elif patterns["special"].fullmatch(line):
        pass
    elif patterns["wildcard"].fullmatch(line):
        pass
    elif patterns["singleline"].fullmatch(line):
        pass
    elif patterns["multiline_start"].fullmatch(line):
        pass
    elif patterns["multiline"].fullmatch(line):
        pass
    elif patterns["multiline_end"].fullmatch(line):
        pass
    elif match := patterns["bad_singleline"].fullmatch(line):
        line = f"from {match.group('from')} import {', '.join(f'{name} as {name}' for name in match.group('import').split(', '))}"
    elif match := patterns["bad_multiline"].fullmatch(line):
        line = match.expand(r"    \1 as \1,")
    else:
        raise Exception(f"{sys.argv[1]}:{i}: " + line)
    lines[i] = line + "\n"

with open(sys.argv[1], "w") as f:
    f.writelines(lines)
