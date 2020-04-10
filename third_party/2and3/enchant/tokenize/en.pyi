from typing import Container

import enchant.tokenize

class tokenize(enchant.tokenize.tokenize):
    def __init__(self, text: str, valid_chars: Container[str] = ...) -> None: ...
    def next(self) -> enchant.tokenize.Token: ...
