#Basic modules
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
#Color cycle to plot all curves
from cycler import cycler
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from time import sleep
from kin_parser import KinParser

plt.rc("figure", figsize=(8, 8))


class Interface():
    def __init__(self, linear_names, log_names, ax_1_log, ax_2_log, path, path_kin, path_models):
        self.linnames = linear_names
        self.lognames = log_names
        self.log1 = ax_1_log
        self.log2 = ax_2_log
        self.color_cycle= cycler("linestyle", ["-","--"]) * plt.rcParams["axes.prop_cycle"]
        self.path = path
        self.path_kin = path_kin
        self.path_models = path_models
        self.parser = KinParser(self.path_kin, self.path_models)
    def full_way(self, p, parts, subs, T, t, save=False):
        self.parser.create_new_kin_spec(p, parts, subs,T, t)
        self.process_the_file()
        if save:
            self.plot_graph(save=(p, parts, subs, T))
        else:
            self.plot_graph()

    def plot_graph(self, save=None):
        data = pd.read_csv(self.path_models + "spec.csv", index_col=0)
        ax = plt.gca()
        ax2 = ax.twinx()
        if self.log1:
            ax2.set_yscale("log")
        if self.log2:
            ax.set_yscale("log")
        iterator = iter(self.color_cycle)
        for column in data.columns:
            if column in self.linnames:
                ax2.plot(data.index, data[column], label=column, **next(iterator))
            elif column in self.lognames:
                ax.plot(data.index, data[column], label=column, **next(iterator))
        ax.grid()
        locs = ax.xaxis.get_major_locator()()
        ax.xaxis.set_minor_locator(MultipleLocator((locs[1]-locs[0])/8))
        ax.tick_params(axis='x', which='minor', bottom=True, length=5)
        if not save is None:
            p, parts, subs, T = save
            ax.text(0.5, 1.05, "p: {0:2.2e} атм, T: {1:4.0f} К, relation: [{5} {2} : {6} {3} : {7} {4}]".format(p, T, *parts, *subs),
                    transform=ax.transAxes,
                    verticalalignment='center',
                   horizontalalignment='center',
                   bbox=dict(facecolor='blue', alpha=0.2),
                   fontdict=dict(fontsize=16))
        temp1, temp2 = ax.get_legend_handles_labels()
        temp3, temp4 = ax2.get_legend_handles_labels()
        ax2.legend(temp1+temp3, temp2+temp4)
        plt.tight_layout()
        if not save is None:
            plt.savefig("./graphs/{1:3.2f}_{0:2.2f}_{2}_{3}_{4}.png".format(np.log10(p), T, *parts), dpi=200)

    def process_the_file(self):
        if os.path.exists(self.path_models+"spec.csv"):
            os.remove(self.path_models+"spec.csv")
        os.chdir(self.path)
        app = Application(backend="win32").start("wkinet.exe")
        app.window().menu().get_menu_path("Файл")[0].sub_menu().get_menu_path("Открыть")[0].click()
        dlg = app.top_window()
        dlg.Edit.set_edit_text("spec.kin")
        dlg["Открыть"].click_input()
        app.top_window().set_focus()
        sleep(0.5)
        send_keys("{F5}")
        sleep(4)
        app.top_window().menu_select("Окна->Решение 1")
        sleep(0.5)
        app.top_window().menu_select("Файл->Экспорт")
        app.top_window().set_focus()
        dlg = app.top_window()
        dlg.Edit.set_edit_text("spec.csv")
        dlg["Сохранить"].click_input()
        sleep(2)
        app.kill()