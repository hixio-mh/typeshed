import threading
from typing import Any, Dict, Optional, Text, Tuple

from _ldap import *
from ldap.dn import dn2str as dn2str, explode_dn as explode_dn, explode_rdn as explode_rdn, str2dn as str2dn
from ldap.functions import (
    escape_str as escape_str,
    get_option as get_option,
    initialize as initialize,
    set_option as set_option,
    strf_secs as strf_secs,
    strp_secs as strp_secs,
)
from ldap.ldapobject import NO_UNIQUE_ENTRY as NO_UNIQUE_ENTRY, LDAPBytesWarning as LDAPBytesWarning
from typing_extension import Protocol, TypedDicts

class _ApiInfo(TypedDicts):
    info_version: int
    extensions: Tuple[Text, ...]
    vendor_version: int
    protocol_version: int
    vendor_name: str
    api_version: int

LIBLDAP_API_INFO: _ApiInfo
OPT_NAMES_DICT: Dict[int, str]

class DummyLock(Protocol):
    def __init__(self) -> None: ...
    def acquire(self) -> None: ...
    def release(self) -> None: ...

LDAPLockBaseClass = DummyLock

class LDAPLock:
    def __init__(self, lock_class: Optional[Any] = ..., desc: str = ...) -> None: ...
    def acquire(self): ...
    def release(self): ...

OPT_DIAGNOSTIC_MESSAGE = OPT_ERROR_STRING
