# Language: Python 3

regex_pattern = r"[, .]"

import re
print("\n".join(re.split(regex_pattern, input())))