
def add_init(dpg):
    def select_one_file(dpg, _, file_selection_data, write_loc):
        selected_files = list(file_selection_data["selections"].values())
        if len(selected_files) == 0:
            return
        dpg.set_value(write_loc, selected_files[0])

    ### Section for configuring initialization mode ###
    with dpg.collapsing_header(label="Initialization"):
        # A callback function called everytime the initialization mode changes. It's
        # responsible for showing/hiding the randomization parameters everytime the
        # "Randomize" option is selected/deselected.
        def cb_handle_init_mode_change(sender, init_mode):
            dpg.delete_item("randomize_params")

            if init_mode == "Randomize":
                with dpg.group(horizontal=True, tag="randomize_params",
                                before="randomize_params_anchor"):
                    dpg.add_text("Randomize: ")
                    dpg.add_combo(["until pulse threshold", "until variance threshold",
                                    "once"], default_value="once")
            elif init_mode == "Use existing population":
                with dpg.group(horizontal=True, tag="existing_pop_params",
                                before="randomize_params_anchor"):
                    item = "Populations Source: "
                    dpg.add_text(item)
                    dpg.add_input_text(readonly=True, tag=f"{item} display",
                                    user_data=f"{item} selector")
                dpg.bind_item_handler_registry(f"{item} display", "show_item_on_click")
                with dpg.file_dialog(show=False, directory_selector=True, modal=True,
                                        width=500, height=300, tag=f"{item} selector",
                                        user_data=f"{item} display",
                                        callback=select_one_file):
                    dpg.add_file_extension(".*")

        with dpg.group():
            dpg.add_text("Initialization Mode:")
            dpg.add_radio_button(["Clone from seed", "Clone from seed and mutate",
                                    "Randomize", "Use existing population"],
                                    callback=cb_handle_init_mode_change,
                                    default_value="Randomize")

        with dpg.group(horizontal=True, tag="randomize_params"):
            dpg.add_text("Randomize: ")
            dpg.add_combo(["until pulse threshold", "until variance threshold",
                            "once"], default_value="once")
            dpg.add_spacer(tag="randomize_params_anchor")