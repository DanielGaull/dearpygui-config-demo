# Currently unused, callbacks are individually defined in each file that they're needed

# A callback function called that enables/disables the given item when the
# toggle state of the sender changes. Usually used for checkboxes.
def cb_handle_enable_state_on_toggle(dpg, _, enabled, item):
  if enabled:
    #dpg.enable_item(item)
    dpg.show_item(item)
  else:
    #dpg.disable_item(item)
    dpg.hide_item(item)

def cb_handle_select_one_file(dpg, _, file_selection_data, write_loc):
  # We iterate through all the selected files. Since we didn't specify
  # multi-select, there should be exactly either 0 or 1 files i the list.
  # If there are 0, assume the user is effective cancelling (not choosing) and
  # do nothing.
  selected_files = list(file_selection_data["selections"].values())
  if len(selected_files) == 0:
    return
  dpg.set_value(write_loc, selected_files[0])