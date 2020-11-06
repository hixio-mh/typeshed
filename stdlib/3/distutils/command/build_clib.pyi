from distutils.cmd import Command
from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union
from typing_extensions import TypedDict

class _BuildInfo(TypedDict, total=False):
    sources: Sequence[str]
    macros: Sequence[str]
    include_dirs: Sequence[str]

_LIBS = List[Tuple[str, Dict[str, _BuildInfo]]]

def show_compilers() -> None: ...

class build_clib(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]
    help_options: ClassVar[List[Tuple[str, Optional[str], str, Callable[..., Any]]]]

    build_clib: Optional[str]
    build_temp: Optional[str]
    libraries: Optional[_LIBS]
    include_dirs: Union[None, List[str], str]
    define: Optional[List[Tuple[str, str]]]
    undef: Optional[List[str]]
    debug: Optional[int]
    force: int
    compiler: Optional[str]
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def check_library_list(self, libraries: _LIBS) -> None: ...
    def get_library_names(self) -> List[str]: ...
    def get_source_files(self) -> List[str]: ...
    def build_libraries(self, libraries: _LIBS) -> None: ...
