# dash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import plotly.graph_objects as go



import dash_layout.dashboard_html as divs
import dash_layout.dashboard_controls as controls
import dash_plots.charts as charts

from etl.extract_and_clean import CovidDatahub

external_stylesheets = ['css/layout.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# datasets for dashboard
covid_datahub = CovidDatahub()
# covid_datahub.get_raw()
covid_datahub.get_cleaned(from_disk=True)

df_datahub = covid_datahub.get_cleaned_df()
COUNTRIES = covid_datahub.get_countries()
MEASURES = covid_datahub.get_measures()

print(MEASURES)

# html layout defined in dash_layout.dashboard_html as divs
# add controls to html

# generate all country options for selector
select_country1 = controls.generate_country_dropdown("country_dropdown1", "NLD", COUNTRIES)
select_country2 = controls.generate_country_dropdown("country_dropdown2", "BEL", COUNTRIES)

divs.div_row2_left.children.append(select_country1)
divs.div_row2_left.children.append(select_country2)

# select measures
select_measure = controls.generate_measures_checklist("measures_checklist", MEASURES)
divs.div_row2_center.children.append(select_measure)

# select secondary metric to plot
select_secondary_plot = controls.generate_metrics_dropdown("select_secondary_plot")
divs.div_row2_right_top.children.append(select_secondary_plot)

# align functionality for metrics plots
divs.div_row2_right_bottom.children.append(
    controls.generate_button("Time Shift!", "shift_button")
)
divs.div_row2_right_bottom.children.append(
    controls.generate_input_number("shift_days")
)

# add (empty) plots
divs.div_row1_left.children.append(
    dcc.Graph(id='left_plot')
)

divs.div_row1_right.children.append(
    dcc.Graph(id='right_plot')
)

app.layout = html.Div([
    divs.div_full
])

# add interactions
output_chart_left = Output(component_id='left_plot', component_property='figure')
output_chart_right = Output(component_id='right_plot', component_property='figure')
outputs = [output_chart_left, output_chart_right]

country_dropdown_left = Input(component_id='country_dropdown1', component_property='value')
country_dropdown_right = Input(component_id='country_dropdown2', component_property='value')
measures_check = Input(component_id='measures_checklist', component_property='value')
select_secondary_y = Input(component_id='select_secondary_plot', component_property='value')
inputs = [country_dropdown_left, country_dropdown_right, measures_check, select_secondary_y]


@app.callback(outputs, inputs)
def output_left(country_left, country_right, measures, secondary_y):
    data_left = charts.generate_traces_areaplot(df_datahub, country_left, measures) + \
                charts.generate_traces_lineplot(df_datahub, country_left, secondary_y)

    data_right = charts.generate_traces_areaplot(df_datahub, country_right, measures) + \
                 charts.generate_traces_lineplot(df_datahub, country_right, secondary_y)

    layout_left = charts.generate_traces_layout(country_left)
    layout_right = charts.generate_traces_layout(country_right)

    return go.Figure(data=data_left, layout=layout_left), \
           go.Figure(data=data_right, layout=layout_right)


if __name__ == '__main__':
    app.run_server(debug=True)
