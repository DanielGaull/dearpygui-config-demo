from utilities import justify_str_group

def add_logging(dpg):
    def select_one_file(dpg, _, file_selection_data, write_loc):
        selected_files = list(file_selection_data["selections"].values())
        if len(selected_files) == 0:
            return
        dpg.set_value(write_loc, selected_files[0])
    def enable_state_on_toggle(dpg, _, enabled, item):
        if enabled:
            dpg.show_item(item)
        else:
            dpg.hide_item(item)

    ### Section for configuring logging and output ###
    with dpg.collapsing_header(label="Logging and Output"):
        outp_justified_strs = justify_str_group("Log level: ", "Log to file: ",
                                            "Save plots to: ",
                                            "Save Output to: ",
                                            "Save .asc files to: ",
                                            "Save .bin files to: ",
                                            "Save MCU data to: ",
                                            "Analysis directory: ")

        with dpg.group(horizontal=True):
            dpg.add_text(outp_justified_strs["Log level: "])
            dpg.add_slider_int(min_value=0, max_value=4, default_value=0)

        dpg.add_separator()

        with dpg.group(horizontal=True):
            dpg.add_checkbox(label=outp_justified_strs["Log to file: "],
                                default_value=True)
            dpg.add_input_text(readonly=True, tag="log_file_display",
                                user_data="log_file_selector")
            dpg.bind_item_handler_registry("log_file_display", "show_item_on_click")

        # NOTE: If modal=False, then if the user clicks outside the file dialog,
        # the parent window will become active and the dialog will be hidden
        # behind it. If we disable movement of the parent window, the file dialog
        # will effectively be lost for good, so in that case we should set
        # modal=True
        with dpg.file_dialog(show=False, directory_selector=False, modal=True,
                                width=500, height=300, tag="log_file_selector",
                                callback=select_one_file,
                                user_data="log_file_display"):
            dpg.add_file_extension(".*")

        with dpg.group(horizontal=True):
            dpg.add_checkbox(label=outp_justified_strs["Save plots to: "], 
                                callback=enable_state_on_toggle,
                                user_data="plot_file_display", default_value=True)
            dpg.add_input_text(readonly=True, tag="plot_file_display",
                                user_data="plot_file_selector")
            dpg.bind_item_handler_registry("plot_file_display", "show_item_on_click")

        with dpg.file_dialog(show=False, directory_selector=True, modal=True,
                                width=500, height=300, tag="plot_file_selector",
                                callback=select_one_file,
                                user_data="plot_file_display"):
            dpg.add_file_extension(".*")

        dpg.add_separator()

        # Non-optional output directories
        items = ["Save Output to: ", "Save .asc files to: ",
                "Save .bin files to: ", "Save MCU data to: ",
                "Analysis directory: "]
        for item in items:
            with dpg.group(horizontal=True):
                dpg.add_text(outp_justified_strs[item])
                dpg.add_input_text(readonly=True, tag=f"{item} display",
                                    user_data=f"{item} selector")
                dpg.bind_item_handler_registry(f"{item} display", "show_item_on_click")
                with dpg.file_dialog(show=False, directory_selector=True, modal=True,
                                    width=500, height=300, tag=f"{item} selector",
                                    user_data=f"{item} display",
                                    callback=select_one_file):
                    dpg.add_file_extension(".*")