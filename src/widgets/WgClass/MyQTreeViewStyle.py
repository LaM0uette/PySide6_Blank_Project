from .MyQTreeView import MyQTreeView
from src.lib.globals import v_wg
from src.lib.palettes import *


class Style(MyQTreeView):
    def __init__(
            self,
            widget,
            size_policy=DcSizePolicy.Expanding,
            dim=v_wg.DIM,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            frame=v_wg.FRAME,

            scroll_policy=v_wg.SCROLL_POLICY,

            abstract_item_view=DcAbstractItemView.Base,
            drag_drop=DcDragDrop.Base,
            selection_mode=PaSelectionMode.SINGLE,
            selection_behavior=PaSelectionBehavior.ROW,

            uniform_row_height=False,
            items_expandable=True,
            sorting=False,
            animate=False,
            header_hidden=False,

            background=v_wg.BACKGROUND,
            background_header=v_wg.BACKGROUND,
            background_item=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            foreground_header=v_wg.FOREGROUND,
            foreground_item=v_wg.FOREGROUND,
            border=v_wg.BORDER,
            border_header=v_wg.BORDER,
            border_item=v_wg.BORDER,
            scroll=v_wg.SCROLL,
    ):
        super().__init__(widget, size_policy, dim, font, cursor, focus_policy, layout_direction, frame, scroll_policy, abstract_item_view, drag_drop, selection_mode, selection_behavior, uniform_row_height,items_expandable,sorting,animate,header_hidden)

        style = f"""
                /* TREEWIDGET */
                QHeaderView::section {{
                background-color: rgba{background_header.base};
                color: rgba{foreground_header.base};
                border-top: {border_header.base[0]}px {border_header.base_style} rgba{border_header.base_rgb};
                border-bottom: {border_header.base[1]}px {border_header.base_style} rgba{border_header.base_rgb};
                border-right: {border_header.base[2]}px {border_header.base_style} rgba{border_header.base_rgb};
                border-left: {border_header.base[3]}px {border_header.base_style} rgba{border_header.base_rgb};
                }}

                QTreeView {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                }}

                QTreeView::item {{
                background-color: rgba{background_item.base};
                color: rgba{foreground_item.base};
                border-top: {border_item.base[0]}px {border_item.base_style} rgba{border_item.base_rgb};
                border-bottom: {border_item.base[1]}px {border_item.base_style} rgba{border_item.base_rgb};
                border-right: {border_item.base[2]}px {border_item.base_style} rgba{border_item.base_rgb};
                border-left: {border_item.base[3]}px {border_item.base_style} rgba{border_item.base_rgb};
                border-top-right-radius: {border_item.radius[0]}px;
                border-top-left-radius: {border_item.radius[1]}px;
                border-bottom-right-radius: {border_item.radius[2]}px;
                border-bottom-left-radius: {border_item.radius[3]}px;
                }}

                QTreeView::item:hover {{
                background-color: rgba{background_item.hover};
                color: rgba{foreground_item.hover};
                border-top: {border_item.hover[0]}px {border_item.hover_style} rgba{border_item.hover_rgb};
                border-bottom: {border_item.hover[1]}px {border_item.hover_style} rgba{border_item.hover_rgb};
                border-right: {border_item.hover[2]}px {border_item.hover_style} rgba{border_item.hover_rgb};
                border-left: {border_item.hover[3]}px {border_item.hover_style} rgba{border_item.hover_rgb};
                }}

                QTreeView::item:selected {{
                background-color: rgba{background_item.checked};
                color: rgba{foreground_item.checked};
                border-top: {border_item.checked[0]}px {border_item.checked_style} rgba{border_item.checked_rgb};
                border-bottom: {border_item.checked[1]}px {border_item.checked_style} rgba{border_item.checked_rgb};
                border-right: {border_item.checked[2]}px {border_item.checked_style} rgba{border_item.checked_rgb};
                border-left: {border_item.checked[3]}px {border_item.checked_style} rgba{border_item.checked_rgb};
                }}

                QTreeView::item:selected:hover {{
                background-color: rgba{background_item.checked_hover};
                color: rgba{foreground_item.checked_hover};
                border-top: {border_item.checked_hover[0]}px {border_item.checked_hover_style} rgba{border_item.checked_hover_rgb};
                border-bottom: {border_item.checked_hover[1]}px {border_item.checked_hover_style} rgba{border_item.checked_hover_rgb};
                border-right: {border_item.checked_hover[2]}px {border_item.checked_hover_style} rgba{border_item.checked_hover_rgb};
                border-left: {border_item.checked_hover[3]}px {border_item.checked_hover_style} rgba{border_item.checked_hover_rgb};
                }}

                /* BORDURES */
                .QTreeView {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QTreeView:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb};
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}

                /* RAYONS */
                .QTreeView {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}

                /* SCROLL */
                QScrollBar {{
                background-color: rgba{scroll.bg};
                width: {scroll.width}px;
                height: {scroll.height}px;
                }}
                QScrollBar::handle:horizontal {{
                min-width: {scroll.min_width_handle}px;
                }}
                QScrollBar::handle:vertical {{
                min-height: {scroll.min_height_min_handle}px;
                }}
                QScrollBar::handle {{
                background-color: rgba{scroll.handle_fg};
                }}
                QScrollBar::handle:hover {{
                background-color: rgba{scroll.handle_fg_hover};
                }}

                QScrollBar::add-page, QScrollBar::sub-page {{
                background-color: rgba{scroll.handle_bg};
                border: none;
                }}
                QScrollBar::add-page:hover, QScrollBar::sub-page:hover {{
                background-color: rgba{scroll.handle_bg_hover};
                border: none;
                }}"""
        widget.setStyleSheet(style)