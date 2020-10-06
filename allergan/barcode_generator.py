import pandas as pd
from sqlalchemy import create_engine
import os
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

postgres_hr = "postgresql://anmol_gorakshakar:Iwbo2D1iM@localhost:5432/historeceptomics"
cnx_hr = create_engine(postgres_hr)


class pl:
    def __init__(self):
        return

        # REVIEW: change function and add keyword arguments

    def query_generator(self, gene):
        query = f"""
                SELECT * FROM biogps_gmean
                WHERE symbol in ('gene')
                """
        return query

    def biogps_plotter(self, gene, connection=cnx_hr):
        query = self.query_generator(gene)
        df = pd.read_sql_query(query, connection).drop(["index", "symbol"], axis=1)

        # initialize the image
        # REVIEW: Add functionality to pass axes objects
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.plot(df.transpose())
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype="image/png")
