from utilities import justify_str_group

class GaSection:
    def __init__(self, dpg):
        self.__dpg = dpg

        def enable_state_on_toggle(_, enabled, item):
            if enabled:
                dpg.show_item(item)
            else:
                dpg.hide_item(item)

        ### Section for configuring genetic algorithm parameters ###
        with dpg.collapsing_header(label="Genetic Algorithm"):
            ga_justified_strs = justify_str_group("Population Size: ",
                                                "Mutation Probability: ",
                                                "Crossover Probability: ",
                                                "Elitism Fraction: ")

            with dpg.group(horizontal=True):
                dpg.add_text(ga_justified_strs["Population Size: "])
                dpg.add_input_int(tag='population_size', min_value=2, min_clamped=True, default_value=50)

            dpg.add_separator()

            with dpg.group(horizontal=True):
                dpg.add_text(ga_justified_strs["Mutation Probability: "])
                dpg.add_slider_float(tag='mutation_probability', min_value=0, max_value=1.0, clamped=True)

            with dpg.group(horizontal=True):
                dpg.add_text(ga_justified_strs["Crossover Probability: "])
                dpg.add_slider_float(tag='crossover_probability', min_value=0, max_value=1.0, clamped=True)

            with dpg.group(horizontal=True):
                dpg.add_text(ga_justified_strs["Elitism Fraction: "])
                dpg.add_slider_float(tag='elitism_fraction', min_value=0, max_value=1.0, clamped=True)

            dpg.add_separator()

            with dpg.table(header_row=False):
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    with dpg.table_cell():
                        dpg.add_text("Selection Type:")
                        dpg.add_radio_button(tag='selection', items=["Single Elite", "Fractional Elite",
                                                "Classic Tournament",
                                                "Fitness Proportional", "Rank Proportional", "MAP Elites"],
                                                default_value="Fitness Proportional")

                    with dpg.table_cell():
                        dpg.add_text("Diversity Measure:")
                        dpg.add_radio_button(tag='diversity_measure', items=["None", "Unique Individuals", "Hamming Distance"],
                                                default_value="Hamming Distance")

            dpg.add_separator()

            stp_justified_strs = justify_str_group("Stop after generation: ",
                                                "Stop after reaching fitness value: ")

            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='has_gen_max', label=stp_justified_strs["Stop after generation: "],
                                    callback=enable_state_on_toggle,
                                    user_data="gen_max", default_value=True)
                dpg.add_input_int(tag='gen_max', min_value=2, min_clamped=True, default_value=500)

            with dpg.group(horizontal=True):
                dpg.add_checkbox(tag='has_fit_max', label=stp_justified_strs["Stop after reaching fitness value: "],
                                    callback=enable_state_on_toggle,
                                    user_data="fitness_target")
                dpg.add_input_int(tag='fit_max', min_value=2, min_clamped=True, default_value=1000,
                                    enabled=False)
                dpg.hide_item("fit_max")
    
    def get_values(self):
        return {
            'population_size': self.__dpg.get_value('population_size'),
            'mutation_probability': self.__dpg.get_value('mutation_probability'),
            'crossover_probability': self.__dpg.get_value('crossover_probability'),
            'elitism_fraction': self.__dpg.get_value('elitism_fraction'),
            'selection': self.__dpg.get_value('selection'),
            'diversity_measure': self.__dpg.get_value('diversity_measure'),
            'diversity_measure': self.__dpg.get_value('diversity_measure'),
            'generations': self.__dpg.get_value('gen_max') if self.__dpg.get_value('has_gen_max') else 'IGNORE',
            'target_fitness': self.__dpg.get_value('fit_max') if self.__dpg.get_value('has_fit_max') else 'IGNORE',
        }