#!/usr/bin/env python3

import dearpygui.dearpygui as dpg
from sections.fitness import add_fitness
from sections.ga import add_ga
from sections.hardware import add_hardware
from sections.init import add_init
from sections.logging import add_logging
from sections.system import add_system
from sections.toplevel import add_top_level

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
                no_collapse=True, no_title_bar=True):
  add_top_level(dpg)
  add_fitness(dpg)
  add_ga(dpg)
  add_init(dpg)
  add_logging(dpg)
  add_system(dpg)
  add_hardware(dpg)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
