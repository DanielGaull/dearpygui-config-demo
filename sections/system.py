from functools import partial
from callback_utilities import cb_handle_select_one_file

def add_system(dpg):
    select_one_file = partial(cb_handle_select_one_file, dpg)

    ## Section for configuring system parameters
    with dpg.collapsing_header(label="System"):
        with dpg.group(horizontal=True):
            dpg.add_text("MCU USB device: ")
            dpg.add_input_text(readonly=True, tag="device_file_display",
                                user_data="device_file_selector")
            dpg.bind_item_handler_registry("device_file_display", "show_item_on_click")

            # NOTE: If modal=False, then if the user clicks outside the file dialog,
            # the parent window will become active and the dialog will be hidden
            # behind it. If we disable movement of the parent window, the file dialog
            # will effectively be lost for good, so in that case we should set
            # modal=True
            with dpg.file_dialog(show=False, directory_selector=False, modal=True,
                                    width=500, height=300, tag="device_file_selector",
                                    callback=select_one_file,
                                    user_data="device_file_display"):
                dpg.add_file_extension(".*")