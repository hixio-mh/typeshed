from distutils.cmd import Command
from typing import ClassVar, List, Optional, Tuple, Union

class install_data(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]

    install_dir: Optional[str]
    outfiles: List[str]
    root: Optional[str]
    force: int
    data_files: List[Union[str, Tuple[str, List[str]]]]
    warn_dir: int
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_inputs(self) -> List[Union[str, Tuple[str, List[str]]]]: ...
    def get_outputs(self) -> List[str]: ...
