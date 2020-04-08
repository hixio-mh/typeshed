from typing import Any

from ldap.controls import RequestControl as RequestControl
from pyasn1.type import univ

SESSION_TRACKING_CONTROL_OID: str
SESSION_TRACKING_FORMAT_OID_RADIUS_ACCT_SESSION_ID: Any
SESSION_TRACKING_FORMAT_OID_RADIUS_ACCT_MULTI_SESSION_ID: Any
SESSION_TRACKING_FORMAT_OID_USERNAME: Any

class SessionTrackingControl(RequestControl):
    class SessionIdentifierControlValue(univ.Sequence):
        componentType: Any = ...
    controlType: Any = ...
    criticality: bool = ...
    def __init__(self, sessionSourceIp: Any, sessionSourceName: Any, formatOID: Any, sessionTrackingIdentifier: Any) -> None: ...
    def encodeControlValue(self): ...
