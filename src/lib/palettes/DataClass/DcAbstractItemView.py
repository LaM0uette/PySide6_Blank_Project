"""
DcAbstractItemView.%class(
    auto_scroll: bool = %
    auto_scroll_margin: int = %
    tab_navigation: bool = %
    alternative_row_colors: bool = %)
"""

from dataclasses import dataclass


@dataclass
class Base:

    auto_scroll: bool = True
    auto_scroll_margin: int = 16
    tab_navigation: bool = True
    alternative_row_colors: bool = False
