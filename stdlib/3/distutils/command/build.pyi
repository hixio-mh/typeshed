from distutils.cmd import Command
from typing import Any, Callable, ClassVar, List, Optional, Tuple

def show_compilers() -> None: ...

class build(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]
    help_options: ClassVar[List[Tuple[str, Optional[str], str, Callable[..., Any]]]]
    sub_commands: ClassVar[List[Tuple[str, Optional[Callable[[Command], bool]]]]]

    build_base: str
    build_purelib: Optional[str]
    build_platlib: Optional[str]
    build_lib: Optional[str]
    build_temp: Optional[str]
    build_scripts: Optional[str]
    compiler: Optional[str]
    plat_name: Optional[str]
    debug: Optional[bool]
    force: int
    executable: Optional[str]
    parallel: Optional[int]
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def has_pure_modules(self) -> bool: ...
    def has_c_libraries(self) -> bool: ...
    def has_ext_modules(self) -> bool: ...
    def has_scripts(self) -> bool: ...
