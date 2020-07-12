import dash_core_components as dcc
import dash_html_components as html


def generate_country_dropdown(id, value, countries):
    options_country = [
        {
            "label": row[1]['full_name'],
            "value": row[1]['code']
        } for row in countries.iterrows()
    ]

    return dcc.Dropdown(
        id=id,
        options=options_country,
        value=value
    )


def generate_measures_checklist(id, measures):
    opts_measures = [
        {"label": m.replace("_", " "), "value": m} for m in measures
    ]

    return dcc.Checklist(
        id=id,
        options=opts_measures,
        value=measures,  # select all
        labelStyle={'display': 'inline-block'}  # horizontal placement
    )


def generate_metrics_dropdown(id):
    return dcc.Dropdown(
        id=id,
        options=[
            {"label": 'R0 (TODO)', "value": "r0"},
            {"label": "Excess Mortality (TODO)", "value": "excess_mortality"},
            {"label": "New Cases", "value": "new_cases"},
            {"label": "New Covid Deaths", "value": "new_deaths"},
            {"label": "Hospitalized", "value": "hosp"},
            {"label": "Ventilator", "value": "vent"},
            {"label": "ICU", "value": "icu"},
            {"label": "Cumul. Cases", "value": "confirmed"},
            {"label": "Cumul. Covid Deaths", "value": "deaths"},
        ],
        value=["new_cases"],
        multi=True
    )


def generate_button(label, id):
    return html.Button(label, id=id)

def generate_input_number(id):
    return dcc.Input(id=id, type='number', placeholder=5)




