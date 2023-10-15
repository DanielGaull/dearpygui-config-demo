from utilities import justify_str_group

class HardwareSection:
    def __init__(self, dpg):
        self.__dpg = dpg
        ## Section for configuring hardware parameters
        with dpg.collapsing_header(label="Hardware"):
            hw_justified_strs = justify_str_group("Baud rate: ", "MCU read timeout: ",
                                                "FPGA routing: ")
            with dpg.group(horizontal=True):
                dpg.add_text(hw_justified_strs["Baud rate: "])
                dpg.add_combo('serial_baud', [9600, 14400, 19200, 38400, 57600, 115200],
                                default_value=115200)
                with dpg.group(horizontal=True):
                    dpg.add_text(hw_justified_strs["MCU read timeout: "])
                    dpg.add_input_float('mcu_read_timeout', min_value=1.0, min_clamped=True, default_value=1.1,
                                        step=0.1)

            dpg.add_separator()

            with dpg.group(horizontal=True):
                dpg.add_text(hw_justified_strs["FPGA routing: "])
                dpg.add_radio_button('routing', ["MOORE", "NEWSE"], default_value="MOORE",
                                        horizontal=True)
            
            dpg.add_text("Accessed columns: ")

            with dpg.table(header_row=False):
                for i in range (9):
                    dpg.add_table_column()

                idx = 0 
                for i in range(6):
                    with dpg.table_row():
                        for j in range(9):
                            dpg.add_selectable(label=idx)  
                            idx += 1
    
    def get_values(self):
        return {
            'routing': self.__dpg.get_value('routing'),
            'serial_baud': self.__dpg.get_value('serial_baud'),
            # TODO: Accessed columns
        }