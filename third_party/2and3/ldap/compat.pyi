from collections import UserDict
from shutil import which as which
from typing import Any
from urllib.parse import quote as quote, quote_plus as quote_plus, unquote as unquote, urlparse as urlparse
from urllib.request import urlopen as urlopen

IterableUserDict = UserDict

def reraise(exc_type: Any, exc_value: Any, exc_traceback: Any) -> None: ...
