import libvirt
from typing import Callable

def qemuMonitorEventDeregister(conn: libvirt.virConnect, callbackID: int) -> None: ...
def qemuMonitorEventRegister(conn: libvirt.virConnect, dom: libvirt.virDomain, event: str, cb: Callable[[libvirt.virConnect, libvirt.virDomain, str, int, int, str, libvirt._T], None], opaque: libvirt._T, flags: int=...) -> int: ...
def qemuAgentCommand(domain: libvirt.virDomain, cmd: str, timeout: int, flags: int) -> str: ...
def qemuAttach(conn: libvirt.virConnect, pid_value: int, flags: int) -> libvirt.virDomain: ...
def qemuMonitorCommand(domain: libvirt.virDomain, cmd: str, flags: int) -> str: ...

VIR_CONNECT_DOMAIN_QEMU_MONITOR_EVENT_REGISTER_REGEX: int
VIR_CONNECT_DOMAIN_QEMU_MONITOR_EVENT_REGISTER_NOCASE: int
VIR_DOMAIN_QEMU_AGENT_COMMAND_BLOCK: int
VIR_DOMAIN_QEMU_AGENT_COMMAND_MIN: int
VIR_DOMAIN_QEMU_AGENT_COMMAND_DEFAULT: int
VIR_DOMAIN_QEMU_AGENT_COMMAND_NOWAIT: int
VIR_DOMAIN_QEMU_AGENT_COMMAND_SHUTDOWN: int
VIR_DOMAIN_QEMU_MONITOR_COMMAND_DEFAULT: int
VIR_DOMAIN_QEMU_MONITOR_COMMAND_HMP: int
