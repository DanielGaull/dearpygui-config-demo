
class TopLevelSection:
    def __init__(self, dpg):
        self.__dpg = dpg
        ### Section for configuring operation mode ###
        with dpg.collapsing_header(label="Operation Mode"):
            dpg.add_radio_button(tag='simulation_mode', items=["Fully Intrisinc", "Simulate Hardware", "Fully Simulated"], 
                default_value="Fully Intrinsic")

    def get_values(self):
        return {
            'simulation_mode': self.__dpg.get_value('simulation_mode')
        }