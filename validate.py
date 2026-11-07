# validate.py - three-layer prompt injection defence

# Layer 1: maximum input length

# Layer 2: regex injection blocklist

# Layer 3: output scanner (in output_scanner.py, imported here)

import re

from output_scanner import check_output

MAX_LENGTH = 500

blocklist = [

    r"ignore (all )?previous instructions",

    r"you are now",

    r"pretend you are",

    r"act as if you have no",

    r"[A-Za-z0-9+/]{40,}={0,2}",

    r"ignore this",

    r"system note",

    r"decode (this )?base64",

    r"system prompt",

    r"all passwords",
]

def check_input(text):


    if len(text) > MAX_LENGTH:

        return False, "Input too long (max 500 characters)"


    for pattern in blocklist:

        if re.search(pattern, text, re.IGNORECASE):

            return False, "Blocked: prompt injection pattern detected"

    return True, ""



