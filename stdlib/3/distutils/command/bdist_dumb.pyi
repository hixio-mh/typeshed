from distutils.cmd import Command
from typing import Any, ClassVar, List, Optional, Tuple

class bdist_dumb(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]
    default_format: Any
    bdist_dir: Optional[str]
    plat_name: Optional[str]
    format: Optional[str]
    keep_temp: int
    dist_dir: Optional[str]
    skip_build: Optional[int]
    relative: int
    owner: Optional[str]
    group: Optional[str]
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
