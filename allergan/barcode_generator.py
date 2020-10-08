import pandas as pd
from sqlalchemy import create_engine
import os
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

postgres_al = "postgresql://anmol_gorakshakar:Iwbo2D1iM@localhost:5432/allergan"
cnx_al = create_engine(postgres_al)


class pl:
    def __init__(self):
        return

        # REVIEW: change function and add keyword arguments

    def query_generator(self, gene):
        query = f"""select * from barcode
                            where gene in ('{gene.capitalize()}')"""
        return query

    def biogps_plotter(self, gene, connection=cnx_al):
        query = self.query_generator(gene)
        fig, ax = plt.subplots()
        # Annotate
        an1 = ax.annotate(
            "Single cell",
            xy=(1.0, 1.0),
            xycoords="data",
            va="center",
            ha="left",
            bbox=dict(boxstyle="round", fc="w"),
        )
        an2 = ax.annotate(
            "Bulk tissue",
            xy=(2.0, 0.5),
            xycoords=an1,  # (1, 0.5) of the an1's bbox
            xytext=(30, 0),
            textcoords="offset points",
            va="center",
            ha="left",
            bbox=dict(boxstyle="round", fc="w"),
            # arrowprops=dict(arrowstyle="->")
        )
        ax.axvline(linewidth=3, color="r", x=3.5)
        dat = (
            pd.read_sql_query(query, cnx_al)
            .drop("index", axis=1)
            .set_index("gene")
            .transpose()
        )
        new_header = dat.iloc[0]  # grab the first row for the header
        dat.columns = new_header  # set the header row as the df header
        dat.plot(kind="bar", figsize=(12, 8), ax=ax)
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        ax.xaxis.labelpad = 20
        plt.close()
        return Response(output.getvalue(), mimetype="image/png")
