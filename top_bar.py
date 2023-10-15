
def add_top_bar(dpg):
    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Open")
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Save As")