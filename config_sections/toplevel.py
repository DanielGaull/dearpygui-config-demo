def add_top_level(dpg, init_values):
    ### Section for configuring operation mode ###
    with dpg.collapsing_header(label="Operation Mode"):
        dpg.add_radio_button(["Fully Intrisinc", "Simulate Hardware",
                          "Fully Simulated"], default_value="Fully Intrinsic")