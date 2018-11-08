import ldap.sasl
import ldap.ldapobject
from typing import Any, Dict, List, Literal, Optional, Text, Tuple, Union

ATTR = Text
ATTRS = List[ATTR]
VALUE = Text  # if bytes_mode=False else bytes
VALUES = List[VALUE]
RESULT = Dict[ATTR, VALUES]
RESULTS = List[Tuple[ATTR, RESULT]]
ADDLIST = List[Tuple[ATTR, VALUES]]
MODLIST = List[Tuple[int, ATTR, VALUES]]
UADDLIST = List[Union[Tuple[Text, Any], Tuple[Text, Any, Any]]]
UMODLIST = List[Tuple[Text, Any, Any]]
CTLS = Optional[List[ldap.controls.LDAPControl]]
SCOPES = Literal["base", "base+one", "one", "sub", "domain"]
POLICIES = Dict[Text, Dict[Text, Dict[Text, Any]]]

def parentDn(dn: ATTR, base: ATTR=...) -> Optional[ATTR]: ...
def explodeDn(dn: ATTR, notypes: int=...) -> List[ATTR]: ...
def getRootDnConnection(start_tls: int=..., decode_ignorelist: ATTRS=..., reconnect: bool=...) -> access: ...
def getAdminConnection(start_tls: int=..., decode_ignorelist: ATTRS=..., reconnect: bool=...) -> access: ...
def getBackupConnection(start_tls: int=..., decode_ignorelist: ATTRS=..., reconnect: bool=...) -> access: ...
def getMachineConnection(start_tls: int=..., decode_ignorelist: ATTRS=..., ldap_master: bool=..., secret_file: str=..., reconnect: bool=..., random_server: bool=...) -> access: ...

class access:
    host: str = ...
    base: ATTR = ...
    binddn: Optional[ATTR] = ...
    bindpw: str = ...
    start_tls: int = ...
    ca_certfile: Optional[str] = ...
    reconnect: bool = ...
    port: int = ...
    protocol: str = ...
    uri: str = ...
    decode_ignorelist: ATTRS = ...
    follow_referral: bool = ...
    client_connection_attempt: Any = ...
    def __init__(self, host: str=..., port: int=..., base: ATTR=..., binddn: Optional[ATTR]=..., bindpw: str=..., start_tls: int=..., ca_certfile: str=..., decode_ignorelist: ATTRS=..., use_ldaps: bool=..., uri: str=..., follow_referral: bool=..., reconnect: bool=...) -> None: ...
    def bind(self, binddn: ATTR, bindpw: str) -> None: ...
    def bind_saml(self, bindpw: str) -> None: ...
    def unbind(self) -> None: ...
    def whoami(self) -> ATTR: ...
    def get(self, dn: ATTR, attr: ATTRS=..., required: bool=...) -> RESULT: ...
    def getAttr(self, dn: ATTR, attr: ATTR, required: bool=...) -> VALUES: ...
    def search(self, filter: ATTR=..., base: ATTR=..., scope: SCOPES=..., attr: List[str]=..., unique: bool=..., required: bool=..., timeout: int=..., sizelimit: int=..., serverctrls: CTLS=..., response: Optional[Dict]=...) -> RESULTS: ...
    def searchDn(self, filter: ATTR=..., base: ATTR=..., scope: SCOPES=..., unique: bool=..., required: bool=..., timeout: int=..., sizelimit: int=..., serverctrls: CTLS=..., response: Optional[Dict]=...) -> ATTRS: ...
    def getPolicies(self, dn: ATTR, policies: Optional[ATTRS]=..., attrs: Optional[RESULT]=..., result: None=..., fixedattrs: None=...) -> POLICIES: ...
    def get_schema(self) -> ldap.schema.subentry.SubSchema: ...
    def add(self, dn: ATTR, al: UADDLIST, serverctrls: CTLS=..., response: Optional[dict]=...) -> None: ...
    def modify(self, dn: ATTR, changes: UMODLIST, serverctrls: CTLS=..., response: Optional[dict]=...) -> ATTR: ...
    def modify_s(self, dn: ATTR, ml: MODLIST) -> None: ...
    def modify_ext_s(self, dn: ATTR, ml: MODLIST, serverctrls: CTLS=..., response: Optional[dict]=...) -> None: ...
    def rename(self, dn: ATTR, newdn: ATTR, serverctrls: CTLS=..., response: Optional[dict]=...) -> None: ...
    def rename_ext_s(self, dn: ATTR, newrdn: ATTR, newsuperior: Optional[ATTR]=..., serverctrls: CTLS=..., response: Optional[dict]=...) -> None: ...
    def delete(self, dn: ATTR) -> None: ...
    def parentDn(self, dn: ATTR) -> Optional[ATTR]: ...
    def explodeDn(self, dn: ATTR, notypes: Union[bool, int]=...) -> List[ATTR]: ...
    @classmethod
    def compare_dn(cls: Any, a: ATTR, b: ATTR) -> bool: ...
