from distutils.cmd import Command
from typing import ClassVar, List, Optional, Pattern, Tuple

first_line_re: Pattern[bytes]

class build_scripts(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]

    build_dir: Optional[str]
    scripts: Optional[List[str]]
    force: Optional[int]
    executable: Optional[str]
    outfiles: None
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def get_source_files(self) -> List[str]: ...
    def run(self) -> None: ...
    def copy_scripts(self) -> Tuple[List[str], List[str]]: ...

class build_scripts_2to3(build_scripts):
    def copy_scripts(self) -> Tuple[List[str], List[str]]: ...
