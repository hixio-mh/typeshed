from typing import Any, Optional

def addModlist(entry: Any, ignore_attr_types: Optional[Any] = ...): ...
def modifyModlist(
    old_entry: Any,
    new_entry: Any,
    ignore_attr_types: Optional[Any] = ...,
    ignore_oldexistent: int = ...,
    case_ignore_attr_types: Optional[Any] = ...,
): ...
