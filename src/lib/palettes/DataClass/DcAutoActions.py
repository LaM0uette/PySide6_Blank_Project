"""
DcAutoActions.%class(
    auto_repeat: bool = % \n
    auto_exclusive: bool = % \n
    auto_repeat_delay: int = % \n
    auto_repeat_interval: int = %)
"""

from dataclasses import dataclass


@dataclass
class Base:

    auto_repeat: bool = False
    auto_exclusive: bool = False
    auto_repeat_delay: int = 300
    auto_repeat_interval: int = 100
