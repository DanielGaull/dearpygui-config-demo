from utilities import justify_str_group

class FitnessSection:
  def __init__(self, dpg):
    with dpg.collapsing_header(label="Fitness"):
      fit_justified_strs = justify_str_group("Variance Weight: ",
                                              "Pulse Weight: ",
                                              "Combination Type: ",
                                              "Oscillator Frequency: ")

      # A callback function called everytime the value chosen for the fitness
      # function changes. Since each fitness function has different parameters
      # (or at least different names for the parameters), this function ensures
      # that the config application shows only the parameter for the currently
      # selected fitness function
      def cb_update_fit_fn(sender, fitness_function):
        dpg.delete_item("fit_fn_param")
        
        if fitness_function == "Combined":
          with dpg.group(tag="fit_fn_param",
                          before="fit_fn_param_anchor"):
            with (dpg.group(horizontal=True)):
              dpg.add_text(fit_justified_strs["Combination Type: "])
              dpg.add_radio_button('combined_mode', ["Add", "Mult"], horizontal=True)
            
            with (dpg.group(horizontal=True)):
              dpg.add_text(fit_justified_strs["Variance Weight: "])
              dpg.add_slider_float('var_weight', min_value=0, max_value=5.0, clamped=True)

            with (dpg.group(horizontal=True)):
              dpg.add_text(fit_justified_strs["Pulse Weight: "])
              dpg.add_slider_float('pulse_weight', min_value=0, max_value=5.0, clamped=True)
        elif fitness_function == "Pulse":
          with dpg.group(tag="fit_fn_param",
                          before="fit_fn_param_anchor"):
            dpg.add_text(fit_justified_strs["Oscillator Frequency: "])
            dpg.add_input_int('desired_freq', min_value=1, min_clamped=True, max_value=1000000,
                              max_clamped=True, default_value=1000)

      dpg.add_text("Fitness Function:")
      dpg.add_radio_button('fitness_func', ["Variance", "Pulse", "Combined"],
                            default_value="Variance", callback=cb_update_fit_fn,
                            horizontal=True)

      dpg.add_separator(tag="fit_fn_param_anchor")

  def get_values(self):
    return {
      'combined_mode': self.__dpg.get_value('combined_mode'),
      'var_weight': self.__dpg.get_value('var_weight'),
      'pulse_weight': self.__dpg.get_value('pulse_weight'),
      'desired_freq': self.__dpg.get_value('desired_freq'),
      'fitness_func': self.__dpg.get_value('fitness_func'),
    }