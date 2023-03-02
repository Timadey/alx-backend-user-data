#!/usr/bin/env python3

"""
a function called filter_datum that returns the log message obfuscated
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obsfuscate a message that contains some fields
    """
    fields = [f'(?<={x}=)' for x in fields]
    re_fields = '|'.join(fields)
    pat = r'(?:' + re_fields + r')(\w|\/)+'
    return re.sub(pat, 'xxx', message)
