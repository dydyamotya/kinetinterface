import numpy as np

def format_temperatures(temperature: float) -> list:
    return ["{:.2f}, 0, 0\n".format(temperature)]
def format_time(potolok:float) -> list:
    return ["0 ({:1.0e}) {:1.2e}\n".format(potolok*5e-5, potolok)]
def format_subs(conc:float, substance: str) -> list:
    return ["[{}] = {:1.2e}\n".format(substance, conc)]


class KinParser():
    def __init__(self, path_kin, path_models):
        self.path = path_kin
        self.path_m = path_models
        self._parse()
    def _parse(self):
        fd = open(self.path, 'r')
        lines = fd.readlines()
        fd.close()
        temp_idx = None
        conc_idx = None
        time_grid_idx = None
        for idx, line in enumerate(lines):
            if line == "<Initial concentrations>\n":
                conc_idx = idx
            if line == "<Temperature>\n":
                temp_idx = idx
            if line == "<Time grid>\n":
                time_grid_idx = idx
        self.first_lines = lines[:conc_idx+2]
        self.middle_lines = lines[temp_idx-1:temp_idx+2]
        self.last_lines = lines[time_grid_idx-1:time_grid_idx+2]
        self.archilast_lines = lines[time_grid_idx+3:]
    def create_new_kin_spec(self, p, parts, subs, temperature, potolok):
        sum_ = np.sum(parts)
        itog_lines = []
        itog_lines += self.first_lines
        for sub, part in zip(subs, parts):
            c = 101325*p/1000/8.314/temperature*part/sum_
            itog_lines += format_subs(c, sub)
        itog_lines += self.middle_lines + format_temperatures(temperature) + self.last_lines + format_time(potolok) + self.archilast_lines
        print(itog_lines)
        with open(self.path_m +"spec.kin", 'w') as fd:
            for line in itog_lines:
                fd.write(line)
        