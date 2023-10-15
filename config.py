#!/usr/bin/env python3

import dearpygui.dearpygui as dpg
from config_sections.FitnessSection import FitnessSection
from config_sections.GaSection import GaSection
from config_sections.HardwareSection import HardwareSection
from config_sections.InitSection import InitSection
from config_sections.LoggingSection import LoggingSection
from config_sections.SystemSection import SystemSection
from config_sections.TopLevelSection import TopLevelSection
from top_bar import add_top_bar

# Creat context before we do any with DearPyGui. Depending on the the action,
# we may segfault if the context doesn't exist.
dpg.create_context()

with dpg.item_handler_registry(tag="show_item_on_click") as handler:
  def cb_show_item_on_click(_, click_event_data):
    # I couldn't find this in the documentation, but was able to determine
    # through testing that the second item of the 'click_event_data' tuple is
    # the id of the element that was clicked. This is why we document things
    # people!
    clicked_item = click_event_data[1]
    target = dpg.get_item_user_data(clicked_item) 
    dpg.show_item(target)

  dpg.add_item_clicked_handler(callback=cb_show_item_on_click)

### Start creating GUI ###

dpg.create_viewport(title="Config Editor", width=1000, height=700)#,
                    #max_width=700, min_width=700, max_height=700,
                    #min_height=700)

with dpg.window(label="", width=1000, height=700, no_resize=True, no_move=True,
                no_collapse=True, no_title_bar=False): # The title bar makes this ugly, but only way to get the menu to show for now

  add_top_bar(dpg)

  with dpg.child_window():
    top_level_section = TopLevelSection(dpg)
    fitness_section = FitnessSection(dpg)
    ga_section = GaSection(dpg)
    init_section = InitSection(dpg)
    logging_section = LoggingSection(dpg)
    system_section = SystemSection(dpg)
    hardware_section = HardwareSection(dpg)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
