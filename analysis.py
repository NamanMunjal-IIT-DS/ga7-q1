import marimo

__generated_with = "unknown"
app = marimo.App(width="medium")


@app.cell
def _():
    # 24f2001419@ds.study.iitm.ac.in

    import marimo as mo
    import pandas as pd
    import numpy as np

    return mo, np, pd


@app.cell
def _(np, pd):
    def data():
        # Let's use a simple, generated dataset for demonstration purposes.
        data = {
            "x_variable": np.linspace(0, 100, 100),
            "y_variable": np.sin(np.linspace(0, 10, 100)) * 50 + 50,
            "category": np.random.choice(['A', 'B', 'C'], 100)
        }
        df = pd.DataFrame(data)
        return df

    # Create an interactive slider widget.
    # The slider's value will influence the dynamic markdown and plot.
    return (data,)


@app.cell
def _(mo):
    def slider():
        # This slider will control the threshold for filtering the data.
        slider = mo.ui.slider(
            start=0, stop=100, step=1, value=50, label="Select a Threshold for Y"
        )
        return slider

    return (slider,)


@app.cell
def _(slider):
    def filtered_data(df):
        # This cell filters the DataFrame `df` based on the current value of the `slider`.
        s=slider()
        filtered_df = df[df["y_variable"] > s.value]
        return filtered_df

    # Generate a plot based on the filtered data.
    # This cell depends on the `filtered_data` cell.
    return (filtered_data,)


@app.cell
def _(mo):
    def plot(filtered_df):
        # The plot visualizes the relationship between x and y for the filtered data.
        # This demonstrates a variable dependency on `filtered_data`.
        fig = filtered_df.plot(
            x="x_variable",
            y="y_variable",
            kind="scatter",
            title="Relationship between X and Y (Filtered)"
        ).get_figure()
        return mo.mpl.figure(fig)

    # Generate dynamic markdown output.
    # This cell has a variable dependency on the `slider` and `filtered_data` cells.
    return (plot,)


@app.cell
def _(mo):
    def markdown_output(slider, filtered_df):
        # This markdown output dynamically updates to show how many rows are selected.
        # The output changes whenever the slider's value is changed.
        num_rows = len(filtered_df)
        return mo.md(
            f"The current threshold for the Y variable is **{slider.value}**."
            f" Based on this, **{num_rows}** data points are selected."
        )
    return (markdown_output,)


@app.cell
def _(mo):
    def final_output(markdown_output, plot):
        # This cell combines the dynamic markdown and the plot for the final presentation.
        return mo.vstack([markdown_output, plot])
    return (final_output,)


@app.cell
def _(data, filtered_data, final_output, markdown_output, plot):
    filtered_data(data())
    plot()
    markdown_output()
    final_output()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
