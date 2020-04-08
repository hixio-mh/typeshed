from typing import Any

CB_USER: int
CB_AUTHNAME: int
CB_LANGUAGE: int
CB_PASS: int
CB_ECHOPROMPT: int
CB_NOECHOPROMPT: int
CB_GETREALM: int

class sasl:
    cb_value_dict: Any = ...
    mech: Any = ...
    def __init__(self, cb_value_dict: Any, mech: Any) -> None: ...
    def callback(self, cb_id: Any, challenge: Any, prompt: Any, defresult: Any): ...

class cram_md5(sasl):
    def __init__(self, authc_id: Any, password: Any, authz_id: str = ...) -> None: ...

class digest_md5(sasl):
    def __init__(self, authc_id: Any, password: Any, authz_id: str = ...) -> None: ...

class gssapi(sasl):
    def __init__(self, authz_id: str = ...) -> None: ...

class external(sasl):
    def __init__(self, authz_id: str = ...) -> None: ...
