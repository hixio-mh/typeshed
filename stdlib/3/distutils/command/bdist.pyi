from distutils.cmd import Command
from typing import Any, Callable, ClassVar, Dict, List, Optional, Tuple

def show_formats() -> None: ...

class bdist(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]
    help_options: ClassVar[List[Tuple[str, Optional[str], str, Callable[..., Any]]]]
    no_format_option: ClassVar[Tuple[str, ...]]
    default_format: ClassVar[Dict[str, str]]
    format_commands: ClassVar[List[str]]
    format_command: ClassVar[Dict[str, Tuple[str, str]]]

    bdist_base: Optional[str]
    plat_name: Optional[str]
    formats: Optional[str]
    dist_dir: Optional[str]
    skip_build: int
    group: Optional[str]
    owner: Optional[str]
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
