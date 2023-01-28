"""
1678. Goal Parser Interpretation

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""

def interpret(command: str) -> str:
        while "()" in command or "(al)" in command:
            command = command.replace("()", "o").replace("(al)", "al")
        return command

if __name__ == "__main__":
    # test cases
    assert interpret("G()(al)") == "Goal"
    assert interpret("G()()()()(al)") == "Gooooal"
    assert interpret("(al)G(al)()()G") == "alGalooG"