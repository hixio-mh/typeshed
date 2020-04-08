from typing import Any, Optional

from ldap.dn import explode_dn as explode_dn, explode_rdn as explode_rdn

def initialize(
    uri: Any,
    trace_level: int = ...,
    trace_file: Any = ...,
    trace_stack_limit: Optional[Any] = ...,
    bytes_mode: Optional[Any] = ...,
): ...
def get_option(option: Any): ...
def set_option(option: Any, invalue: Any): ...
def escape_str(escape_func: Any, s: Any, *args: Any): ...
def strf_secs(secs: Any): ...
def strp_secs(dt_str: Any): ...

# Names in __all__ with no definition:
#   init
#   open
