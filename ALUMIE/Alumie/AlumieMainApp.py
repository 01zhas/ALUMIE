from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDialog, QTableWidgetItem
import sys

from PyQt6 import QtCore

from Alumie.AlumieMain import Ui_AlumiaWindow
from Setting.SettingApp import SettingApp


# from qt_material import apply_stylesheet


class Alumie(QMainWindow, Ui_AlumiaWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.tables = [self.tableBoxite, self.tableLimestone, self.tableSoda, self.tableWhiteMud]

        self.setting_filename = "../saves/setting.cfg"
        self.default_setting_filename = "../saves/default_setting.cfg"
        self.setting_dialog = QDialog()
        self.setting_ui = SettingApp()
        self.setting_ui.setupUi(self.setting_dialog)
        self.setting_ui.load_cfg(self.setting_filename)
        self.setting_dialog.accepted.connect(self.setting_accept)
        self.setting_dialog.rejected.connect(self.setting_reject)

        self.action_save.triggered.connect(self.save_file)
        self.action_setting.triggered.connect(self.set_settings)
        self.action_default.triggered.connect(self.set_default_settings)
        self.action_exit.triggered.connect(self.close)
        self.action_run.triggered.connect(self.run)

    def run(self):
        # TODO: Закончить все таблицы
        # TODO: Сделать проверку на правильность в ввода
        # TODO: Возможно добавить больше конфигурации спросить у Кирова: Потери Na2O, Al2O3 с алюминатном растворе, влажность в 10 пункте

        self.tabWidget.setEnabled(True)
        self.setting_values()
        self.set_tables_values()
        self.tables13()
        self.tables14()
        self.tables15()
        self.tables16()
        self.tables17()
        self.tables18()
        self.tables19()
        self.tables20()
        self.tables21()
        self.tables22()
        self.tables23()
        self.tables24()
        self.tables25()
        self.tables26()

    @staticmethod
    def ttf(tab):
        return float(tab.text().replace(",", "."))

    def set_settings(self):
        self.setting_dialog.show()

    def set_default_settings(self):
        self.setting_ui.load_cfg(self.default_setting_filename)

    def setting_reject(self):
        self.setting_ui.load_cfg(self.setting_filename)

    def setting_accept(self):
        settings_values = [self.setting_ui.Crushing.text(), self.setting_ui.Grind.text(), self.setting_ui.Baking.text(),
                           self.setting_ui.Calcination_2.text(), self.setting_ui.ChemicalLosses.text(),
                           self.setting_ui.Underwashing.text(), self.setting_ui.Desilting.text(),
                           self.setting_ui.Carbonation.text(), self.setting_ui.Evaporation.text(),
                           self.setting_ui.Calcination.text(), self.setting_ui.DumpMud.text(),
                           self.setting_ui.WhiteMud.text(), self.setting_ui.CarbonMud.text(),
                           self.setting_ui.AluminumHydroxide.text(), self.setting_ui.Na2O.text(),
                           self.setting_ui.CaO.text(), self.setting_ui.ChargeHumidity.text(),
                           self.setting_ui.HumidityWhiteMud.text(), self.setting_ui.HumidityAluminumHydroxide.text(),
                           self.setting_ui.HumidityDumpMud.text(), self.setting_ui.Release.text(),
                           self.setting_ui.Extract.text(), self.setting_ui.Mass.text(),
                           self.setting_ui.SiliconModule.text()]

        f = open(self.setting_filename, 'w+')
        with f:
            f.write(str(settings_values))

        self.setting_values()

    def setting_values(self):

        self.Crushing = self.ttf(self.setting_ui.Crushing)
        self.Grind = self.ttf(self.setting_ui.Grind)
        self.Baking = self.ttf(self.setting_ui.Baking)
        self.Calcination_2 = self.ttf(self.setting_ui.Calcination_2)
        self.ChemicalLosses = self.ttf(self.setting_ui.ChemicalLosses)
        self.Underwashing = self.ttf(self.setting_ui.Underwashing)
        self.Desilting = self.ttf(self.setting_ui.Desilting)
        self.Carbonation = self.ttf(self.setting_ui.Carbonation)
        self.Evaporation = self.ttf(self.setting_ui.Evaporation)
        self.Calcination = self.ttf(self.setting_ui.Calcination)
        self.SumLosses = self.Crushing + self.Grind + self.Baking + self.Calcination_2 + self.ChemicalLosses + self.Underwashing + self.Desilting + self.Carbonation + self.Evaporation + self.Calcination

        self.DumpMud = self.ttf(self.setting_ui.DumpMud)
        self.WhiteMud = self.ttf(self.setting_ui.WhiteMud)
        self.CarbonMud = self.ttf(self.setting_ui.CarbonMud)
        self.AluminumHydroxide = self.ttf(self.setting_ui.AluminumHydroxide)
        self.Na2O = self.ttf(self.setting_ui.Na2O)
        self.CaO = self.ttf(self.setting_ui.CaO)
        self.ChargeHumidity = self.ttf(self.setting_ui.ChargeHumidity)
        self.HumidityWhiteMud = self.ttf(self.setting_ui.HumidityWhiteMud)
        self.HumidityAluminumHydroxide = self.ttf(self.setting_ui.HumidityAluminumHydroxide)
        self.HumidityDumpMud = self.ttf(self.setting_ui.HumidityDumpMud)
        self.Release = self.ttf(self.setting_ui.Release)
        self.Extract = self.ttf(self.setting_ui.Extract)
        self.Mass = self.ttf(self.setting_ui.Mass)
        self.SiliconModule = self.ttf(self.setting_ui.SiliconModule)

    def set_tables_values(self):
        self.tableBoxite_Al2O3 = self.ttf(self.tableBoxite.item(0, 0))
        self.tableBoxite_Fe2O3 = self.ttf(self.tableBoxite.item(1, 0))
        self.tableBoxite_SiO2 = self.ttf(self.tableBoxite.item(2, 0))
        self.tableBoxite_TiO2 = self.ttf(self.tableBoxite.item(3, 0))
        self.tableBoxite_CaO = self.ttf(self.tableBoxite.item(4, 0))
        self.tableBoxite_CO2 = self.ttf(self.tableBoxite.item(5, 0))
        self.tableBoxite_Other = self.ttf(self.tableBoxite.item(6, 0))
        self.tableBoxite_PPP = self.ttf(self.tableBoxite.item(7, 0))
        self.tableBoxite_H2O = self.ttf(self.tableBoxite.item(8, 0))

        self.tableLimestone_CaO = self.ttf(self.tableLimestone.item(0, 0))
        self.tableLimestone_CO2 = self.ttf(self.tableLimestone.item(1, 0))
        self.tableLimestone_SiO2 = self.ttf(self.tableLimestone.item(2, 0))
        self.tableLimestone_Other = self.ttf(self.tableLimestone.item(3, 0))
        self.tableLimestone_H2O = self.ttf(self.tableLimestone.item(4, 0))

        self.tableSoda_Mass = self.ttf(self.tableSoda.item(0, 0))
        self.tableSoda_Na2CO3 = self.ttf(self.tableSoda.item(1, 0))
        self.tableSoda_Other = self.ttf(self.tableSoda.item(2, 0))
        self.tableSoda_H2O = self.ttf(self.tableSoda.item(3, 0))

        self.tableWhiteMud_Mass = self.ttf(self.tableWhiteMud.item(0, 0))
        self.tableWhiteMud_Al2O3 = self.ttf(self.tableWhiteMud.item(1, 0))
        self.tableWhiteMud_Na2O = self.ttf(self.tableWhiteMud.item(2, 0))
        self.tableWhiteMud_Fe2O3 = self.ttf(self.tableWhiteMud.item(3, 0))
        self.tableWhiteMud_SiO2 = self.ttf(self.tableWhiteMud.item(4, 0))
        self.tableWhiteMud_CaO = self.ttf(self.tableWhiteMud.item(5, 0))
        self.tableWhiteMud_CO2 = self.ttf(self.tableWhiteMud.item(6, 0))
        self.tableWhiteMud_PPP = self.ttf(self.tableWhiteMud.item(7, 0))

        box = (self.Mass * 0.99 * 100) / (self.tableBoxite_Al2O3/100 * self.Release)  # 2437.82
        loss = box * self.tableBoxite_Al2O3 / 100  # 1170.5
        loss_Al2O3 = loss - self.Mass * 0.99  # 180.15
        loss_Na2O = (self.tableSoda_Mass / 106 * 62)
        loss_Al2O3_crushing = loss_Al2O3 / self.SumLosses * self.Calcination  # 7.02
        loss_Al2O3_crushing_boxite = loss_Al2O3_crushing / self.tableBoxite_Al2O3 * 100  # 14.63
        self.DryBoxiteMass = box - loss_Al2O3_crushing_boxite  # 2423.19
        self.WetBoxiteMass = self.DryBoxiteMass / ((100 - self.tableBoxite_H2O) / 100) # 2605.58

        self.Crushing_Al2O3 = loss_Al2O3 / self.SumLosses * self.Crushing
        self.Grind_Al2O3 = loss_Al2O3 / self.SumLosses * self.Grind
        self.Baking_Al2O3 = loss_Al2O3 / self.SumLosses * self.Baking
        self.Calcination_2_Al2O3 = loss_Al2O3 / self.SumLosses * self.Calcination_2
        self.ChemicalLosses_Al2O3 = loss_Al2O3 / self.SumLosses * self.ChemicalLosses
        self.Desilting_Al2O3 = loss_Al2O3 / self.SumLosses * self.Desilting
        self.Carbonation_Al2O3 = loss_Al2O3 / self.SumLosses * self.Carbonation
        self.Evaporation_Al2O3 = loss_Al2O3 / self.SumLosses * self.Evaporation
        self.Calcination_Al2O3 = loss_Al2O3 / self.SumLosses * self.Calcination
        self.Underwashing_Al2O3 = loss_Al2O3 / self.SumLosses * self.Underwashing

        self.Grind_Na2O = 0.5
        self.Baking_Na2O = 2.0
        self.Calcination_2_Na2O = 1.0
        self.Desilting_Na2O = 1.0
        self.Carbonation_Na2O = 0.5
        self.Evaporation_Na2O = 0.5
        self.Calcination_Na2O = 1.0
        self.Underwashing_Na2O = 4.0
        self.ChemicalLosses_Na2O = loss_Na2O - self.Grind_Na2O - self.Baking_Na2O - self.Calcination_2_Na2O - self.Desilting_Na2O - self.Carbonation_Na2O - self.Evaporation_Na2O - self.Calcination_Na2O - self.Underwashing_Na2O

    def save_file(self):
        files_types = "Binary compressed file (*.bin);;Text file (*.txt)"
        filename = QFileDialog.getSaveFileName(self, "Save File", "saves", files_types)

        if filename[0]:
            filetype = filename[0].split(".")[1]

            text = ""
            for tab in self.tables:
                t = self.__get_save_text(table=tab)
                text = text + t + "\n"

            if filetype == "bin":
                text = text.encode("ascii")
                f = open(filename[0], 'wb')
            else:
                f = open(filename[0], 'w')

            with f:

                f.write(text)

                QMessageBox.about(self, "Сохранение", "Файл был успешно сохранен", )

    @staticmethod
    def __get_save_text(table):
        rows = table.rowCount()
        text = ""
        for r in range(rows):
            t = table.item(r, 0).text()
            text = text + t + " "
        return text

    def setItem(self, table, row, column, value):
        item = QTableWidgetItem(str(round(value, 2)))
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        table.setItem(row, column, item)

    def tables13(self):

        DryBoxiteAl2O3 = self.DryBoxiteMass * self.tableBoxite_Al2O3 / 100
        DryBoxiteFe2O3 = self.DryBoxiteMass * self.tableBoxite_Fe2O3 / 100
        DryBoxiteSiO2 = self.DryBoxiteMass * self.tableBoxite_SiO2 / 100
        DryBoxiteTiO2 = self.DryBoxiteMass * self.tableBoxite_TiO2 / 100
        DryBoxiteCaO = self.DryBoxiteMass * self.tableBoxite_CaO / 100
        DryBoxiteCO2 = self.DryBoxiteMass * self.tableBoxite_CO2 / 100
        DryBoxiteOther = self.DryBoxiteMass * self.tableBoxite_Other / 100
        DryBoxitePPP = self.DryBoxiteMass * self.tableBoxite_PPP / 100
        DryBoxiteH2O = self.WetBoxiteMass - self.DryBoxiteMass

        WhiteMudAl2O3 = self.tableWhiteMud_Mass * self.tableWhiteMud_Al2O3 / 100
        WhiteMudNa2O = self.tableWhiteMud_Mass * self.tableWhiteMud_Na2O / 100
        WhiteMudFe2O3 = self.tableWhiteMud_Mass * self.tableWhiteMud_Fe2O3 / 100
        WhiteMudSiO2 = self.tableWhiteMud_Mass * self.tableWhiteMud_SiO2 / 100
        WhiteMudCaO = self.tableWhiteMud_Mass * self.tableWhiteMud_CaO / 100
        WhiteMudCO2 = self.tableWhiteMud_Mass * self.tableWhiteMud_CO2 / 100
        WhiteMudPPP = self.tableWhiteMud_Mass * self.tableWhiteMud_PPP / 100
        WhiteMudH2O = self.tableWhiteMud_Mass * self.HumidityWhiteMud / (100 - self.HumidityWhiteMud)

        AlumSolutionAl2O3 = DryBoxiteAl2O3 + WhiteMudAl2O3 + 0.30 + 20 - self.Baking_Al2O3 - self.Calcination_2_Al2O3 - self.ChemicalLosses_Al2O3 - self.Underwashing_Al2O3  # 1058.39
        AlumSolutionSiO2 = AlumSolutionAl2O3 / 30  # 35.28
        AlumSolutionStageOneAl2O3 = AlumSolutionAl2O3 - WhiteMudAl2O3  # 1020.83
        AlumSolutionStageOneSiO2 = AlumSolutionStageOneAl2O3 / 400  # 2.55

        CarbonMudCaO = AlumSolutionStageOneSiO2 / 60 / 0.18 * 3 * 56 # 39.67
        HydrogranateAl2O3 = AlumSolutionStageOneSiO2 / 60 / 0.18 * 102  # 24.08
        HydrogranateH2O = AlumSolutionStageOneSiO2 / 60 / 0.18 * 5.6 * 18  # 23.80
        HydrogranateMass = AlumSolutionStageOneSiO2 + CarbonMudCaO + HydrogranateAl2O3 + HydrogranateH2O  # 90.10

        CarbonMudCO2 = CarbonMudCaO / 56 * 44  # 31.17

        CarbonMudH2O = (CarbonMudCO2 + CarbonMudCaO) * 30 / 70
        CarbonMudMass = CarbonMudH2O + CarbonMudCO2 + CarbonMudCaO

        LimestoneCaOact = self.tableLimestone_CaO - (self.tableLimestone_SiO2 * 2 * 56) / 60

        neededCaO = 2 * (((DryBoxiteSiO2 + WhiteMudSiO2) / 60) + DryBoxiteTiO2 / 80)
        neededCaOMass = neededCaO * 56
        LimestoneAl2O3Massneed = neededCaOMass - (DryBoxiteCaO + WhiteMudCaO + CarbonMudCaO / 2)
        DryLimestoneMass = LimestoneAl2O3Massneed * 100 / LimestoneCaOact
        WetLimestoneMass = DryLimestoneMass / (100 - self.tableLimestone_H2O) * 100
        LimestoneMass_CaO = DryLimestoneMass * self.tableLimestone_CaO / 100
        LimestoneMass_CO2 = DryLimestoneMass * self.tableLimestone_CO2 / 100
        LimestoneMass_SiO2 = DryLimestoneMass * self.tableLimestone_SiO2 / 100
        LimestoneMass_Other = DryLimestoneMass * self.tableLimestone_Other / 100
        LimestoneMass_H2O = WetLimestoneMass - DryLimestoneMass

        Na2Oneeded = (20 + DryBoxiteAl2O3 + WhiteMudAl2O3 + 0.30) / 102 + (DryBoxiteFe2O3 + WhiteMudFe2O3) / 160
        RecycledSolutionNa2O = Na2Oneeded * 62
        RecycledSolutionNa2O = RecycledSolutionNa2O - WhiteMudNa2O - 0.32 - self.tableSoda_Mass / 106 * 62
        Na2OneededMass2 = RecycledSolutionNa2O - 32.83
        RecycledSolutionCO2 = Na2OneededMass2 * 44 / 62
        RecycledSolutionMass = Na2OneededMass2 / 310.1 * 1440
        RecycledSolutionH2O = RecycledSolutionMass - (20 + RecycledSolutionCO2 + RecycledSolutionNa2O)

        self.setItem(self.tableBoxite13, 0, 0, DryBoxiteAl2O3)
        self.setItem(self.tableBoxite13, 0, 1, DryBoxiteFe2O3)
        self.setItem(self.tableBoxite13, 0, 2, DryBoxiteSiO2)
        self.setItem(self.tableBoxite13, 0, 3, DryBoxiteTiO2)
        self.setItem(self.tableBoxite13, 0, 4, DryBoxiteCaO)
        self.setItem(self.tableBoxite13, 0, 5, DryBoxiteCO2)
        self.setItem(self.tableBoxite13, 0, 6, DryBoxiteOther)
        self.setItem(self.tableBoxite13, 0, 7, DryBoxitePPP)
        self.setItem(self.tableBoxite13, 0, 8, DryBoxiteH2O)
        self.setItem(self.tableBoxite13, 0, 9, self.WetBoxiteMass)

        self.setItem(self.tableLimestone13, 0, 0, LimestoneMass_SiO2)
        self.setItem(self.tableLimestone13, 0, 1, LimestoneMass_CaO)
        self.setItem(self.tableLimestone13, 0, 2, LimestoneMass_CO2)
        self.setItem(self.tableLimestone13, 0, 3, LimestoneMass_Other)
        self.setItem(self.tableLimestone13, 0, 4, LimestoneMass_H2O)
        self.setItem(self.tableLimestone13, 0, 5, WetLimestoneMass)

        self.setItem(self.tableWhiteMud13, 0, 0, WhiteMudAl2O3)
        self.setItem(self.tableWhiteMud13, 0, 1, WhiteMudFe2O3)
        self.setItem(self.tableWhiteMud13, 0, 2, WhiteMudSiO2)
        self.setItem(self.tableWhiteMud13, 0, 3, WhiteMudCaO)
        self.setItem(self.tableWhiteMud13, 0, 4, WhiteMudCO2)
        self.setItem(self.tableWhiteMud13, 0, 5, WhiteMudNa2O)
        self.setItem(self.tableWhiteMud13, 0, 6, WhiteMudPPP)
        self.setItem(self.tableWhiteMud13, 0, 7, WhiteMudH2O)
        WhiteMudSum = WhiteMudAl2O3 + WhiteMudFe2O3 + WhiteMudSiO2 + WhiteMudCaO + WhiteMudCO2 + WhiteMudNa2O + WhiteMudPPP + WhiteMudH2O
        self.setItem(self.tableWhiteMud13, 0, 8, WhiteMudSum)

        CarbonMudCaO = CarbonMudCaO / 2
        CarbonMudCO2 = CarbonMudCO2 / 2
        CarbonMudH2O = CarbonMudH2O / 2
        CarbonMudMass = CarbonMudMass / 2

        self.setItem(self.tableCarbonMud13, 0, 0, CarbonMudCaO)
        self.setItem(self.tableCarbonMud13, 0, 1, CarbonMudCO2)
        self.setItem(self.tableCarbonMud13, 0, 2, CarbonMudH2O)
        self.setItem(self.tableCarbonMud13, 0, 3, CarbonMudMass)

        Na2CO3Mass = self.tableSoda_Mass
        SodaCO2 = (Na2CO3Mass / 106 * 44)
        SodaNa2O = (Na2CO3Mass / 106 * 62)
        SodaOther = ((self.tableSoda_Mass/self.tableSoda_Na2CO3 * 100) * (self.tableSoda_Other / 100))
        SodaH2O = (self.tableSoda_Mass/self.tableSoda_Na2CO3 * 100) * (self.tableSoda_H2O / 100)
        SodaMass = SodaCO2 + SodaNa2O + SodaOther + SodaH2O
        self.setItem(self.tableSoda13, 0, 0, SodaCO2)
        self.setItem(self.tableSoda13, 0, 1, SodaNa2O)
        self.setItem(self.tableSoda13, 0, 2, SodaOther)
        self.setItem(self.tableSoda13, 0, 3, SodaH2O)
        self.setItem(self.tableSoda13, 0, 4, SodaMass)

        self.setItem(self.tableRecycledSolution13, 0, 0, 20.00)
        self.setItem(self.tableRecycledSolution13, 0, 1, RecycledSolutionCO2)
        self.setItem(self.tableRecycledSolution13, 0, 2, RecycledSolutionNa2O)
        self.setItem(self.tableRecycledSolution13, 0, 3, RecycledSolutionH2O)
        self.setItem(self.tableRecycledSolution13, 0, 4, RecycledSolutionMass)

        PulpAl2O3 = DryBoxiteAl2O3 + WhiteMudAl2O3 + 20
        PulpFe2O3 = DryBoxiteFe2O3 + WhiteMudFe2O3
        PulpSiO2 = DryBoxiteSiO2 + LimestoneMass_SiO2 + WhiteMudSiO2
        PulpTiO2 = DryBoxiteTiO2
        PulpCaO = DryBoxiteCaO + LimestoneMass_CaO + WhiteMudCaO + CarbonMudCaO
        PulpCO2 = DryBoxiteCO2 + LimestoneMass_CO2 + WhiteMudCO2 + CarbonMudCO2 + SodaCO2 + RecycledSolutionCO2
        PulpNa2O = WhiteMudNa2O + SodaNa2O + RecycledSolutionNa2O - self.Grind_Na2O
        PulpOther = DryBoxiteOther + LimestoneMass_Other + SodaOther
        PulpPPP = DryBoxitePPP + WhiteMudPPP
        PulpH2O = DryBoxiteH2O + LimestoneMass_H2O + WhiteMudH2O + CarbonMudH2O + SodaH2O + RecycledSolutionH2O
        PulpMass = PulpAl2O3 + PulpFe2O3 + PulpSiO2 + PulpTiO2 + PulpCaO + PulpCO2 + PulpNa2O + PulpOther + PulpPPP + PulpH2O

        self.setItem(self.tablePulp13, 0, 0, PulpAl2O3)
        self.setItem(self.tablePulp13, 0, 1, PulpFe2O3)
        self.setItem(self.tablePulp13, 0, 2, PulpSiO2)
        self.setItem(self.tablePulp13, 0, 3, PulpTiO2)
        self.setItem(self.tablePulp13, 0, 4, PulpCaO)
        self.setItem(self.tablePulp13, 0, 5, PulpCO2)
        self.setItem(self.tablePulp13, 0, 6, PulpNa2O)
        self.setItem(self.tablePulp13, 0, 7, PulpOther)
        self.setItem(self.tablePulp13, 0, 8, PulpPPP)
        self.setItem(self.tablePulp13, 0, 9, PulpH2O)
        self.setItem(self.tablePulp13, 0, 10, PulpMass - self.Grind_Na2O)

        self.setItem(self.tableWidget_192, 0, 0, self.Grind_Na2O)

        SumMass = RecycledSolutionMass + SodaMass + CarbonMudMass + WetLimestoneMass + self.WetBoxiteMass + WhiteMudSum
        self.label.setText(f"Всего: {round(SumMass, 2)} кг")
        self.label_2.setText(f"Всего: {round(SumMass, 2)} кг")

    def tables14(self):
        pass

    def tables15(self):
        pass

    def tables16(self):
        pass

    def tables17(self):
        pass

    def tables18(self):
        pass

    def tables19(self):
        pass

    def tables20(self):
        pass

    def tables21(self):
        pass

    def tables22(self):
        pass

    def tables23(self):
        pass

    def tables24(self):
        pass

    def tables25(self):
        pass

    def tables26(self):
        pass


app = QApplication(sys.argv)
AlumieApp = Alumie()
extra = {

    # Density Scale
    'density_scale': '-3',
}
# apply_stylesheet(app, theme='dark_blue.xml', invert_secondary=False, extra=extra)
sys.exit(app.exec())
