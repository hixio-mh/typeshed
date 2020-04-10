from typing import IO, Any, Callable, Iterable, List, Optional, Text, Tuple

from enchant.errors import *

def raw_unicode(raw: bytes) -> Text: ...
def raw_bytes(raw: Any) -> bytes: ...

class EnchantStr(str):
    def __new__(cls, value: Any): ...
    def encode(self) -> bytes: ...  # type: ignore
    def decode(self, value: Any) -> Text: ...  # type: ignore

class UTF16EnchantStr(EnchantStr):
    REPLACEMENT_CHAR: str = ...
    def encode(self) -> bytes: ...  # type: ignore

def printf(values: Iterable[Any], sep: str = ..., end: str = ..., file: IO[str] = ...) -> None: ...
def levenshtein(s1: str, s2: str) -> int: ...
def trim_suggestions(word: str, suggs: Iterable[str], maxlen: int, calcdist: Callable[[str, str], int] = ...) -> List[str]: ...
def get_default_language(default: str = ...) -> str: ...
def get_resource_filename(resname: str) -> str: ...
def win32_data_files() -> List[Tuple[str, List[str]]]: ...
