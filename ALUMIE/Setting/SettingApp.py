from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDialog
import sys

from Setting.Settings import Ui_Settings
from qt_material import apply_stylesheet


class SettingApp(Ui_Settings):
    def __init__(self):
        super().__init__()
        
    def load_cfg(self, setting_filename):
        settings_values = [self.Crushing, self.Grind, self.Baking,
                           self.Calcination_2, self.ChemicalLosses,
                           self.Underwashing, self.Desilting,
                           self.Carbonation, self.Evaporation,
                           self.Calcination, self.DumpMud,
                           self.WhiteMud, self.CarbonMud,
                           self.AluminumHydroxide, self.Na2O,
                           self.CaO, self.ChargeHumidity,
                           self.HumidityWhiteMud, self.HumidityAluminumHydroxide,
                           self.HumidityDumpMud, self.Release,
                           self.Extract, self.Mass,
                           self.SiliconModule]
        
        if setting_filename:
            try:
                f = open(setting_filename, 'r')
                with f:
                    values = eval(f.read())

                    for i in range(len(values)):
                        settings_values[i].setValue(float(values[i].replace(",", ".")))
            except:
                print("Файла нет")