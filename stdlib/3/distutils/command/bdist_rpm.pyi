from distutils.cmd import Command
from typing import ClassVar, List, Optional, Set, Tuple

class bdist_rpm(Command):
    description: ClassVar[str]
    user_options: ClassVar[List[Tuple[str, Optional[str], str]]]
    boolean_options: ClassVar[List[str]]
    negative_opt: ClassVar[Set[str]]

    bdist_base: Optional[str]
    rpm_base: Optional[str]
    dist_dir: Optional[str]
    python: Optional[str]
    fix_python: Optional[str]
    spec_only: Optional[str]
    binary_only: Optional[str]
    source_only: Optional[str]
    use_bzip2: Optional[str]
    distribution_name: Optional[str]
    group: Optional[str]
    release: Optional[str]
    serial: Optional[str]
    vendor: Optional[str]
    packager: Optional[str]
    doc_files: Optional[str]
    changelog: Optional[str]
    icon: Optional[str]
    prep_script: Optional[str]
    build_script: Optional[str]
    install_script: Optional[str]
    clean_script: Optional[str]
    verify_script: Optional[str]
    pre_install: Optional[str]
    post_install: Optional[str]
    pre_uninstall: Optional[str]
    post_uninstall: Optional[str]
    prep: Optional[str]
    provides: Optional[str]
    requires: Optional[str]
    conflicts: Optional[str]
    build_requires: Optional[str]
    obsoletes: Optional[str]

    keep_temp: int
    use_rpm_opt_flags: int
    rpm3_mode: int
    no_autoreq: int
    force_arch: Optional[str]
    quiet: int = ...
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def finalize_package_data(self) -> None: ...
    def run(self) -> None: ...
