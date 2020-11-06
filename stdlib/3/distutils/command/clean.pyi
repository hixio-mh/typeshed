from distutils.cmd import Command
from typing import ClassVar, List, Optional, Tuple

class clean(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]

    build_base: Optional[str]
    build_lib: Optional[str]
    build_temp: Optional[str]
    build_scripts: Optional[str]
    bdist_base: Optional[str]
    all: Optional[bool]
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
