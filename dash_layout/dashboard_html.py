import dash_html_components as html

div_row1_left = html.Div(id="row1_left", children=[],
                         style=dict(border="0px solid red", height="100%", width="49%", overflow="hidden", float="left")
                         )

div_row1_right = html.Div(id="row1_right", children=[],
                          style=dict(border="0px solid blue", height="100%", width="49%", overflow="hidden",
                                     float="left")
                          )

div_row1 = html.Div(id="row1", children=[div_row1_left, div_row1_right],
                    style=dict(border="0px solid black", height="60%", width="99%", overflow="visible")
                    )

div_row2_left = html.Div(id="row2_left", children=[],
                         style={
                             "border": "0px solid red",
                             "height": "100%", "width": "24%",
                             "overflow": "hidden",
                             "float": "left",
                             "padding-right": "5px"
                         }
                         )

div_row2_center = html.Div(id="row2_center", children=[],
                           style=dict(border="0px solid green", height="100%", width="49%", overflow="visible",
                                      float="left")
                           )

div_row2_right = html.Div(id="row2_right", children=[],
                          style=dict(border="0px solid black", height="100%", width="24%", overflow="visible",
                                     float="left")
                          )

div_row2 = html.Div(id="row_2", children=[div_row2_left, div_row2_center, div_row2_right],
                    style={
                        "border": "0px solid black",
                        "height": "20%", "width": "99%",
                        "overflow": "visible",
                    }
                    )

div_row2_right_top = html.Div(id="row2_right_top", children=[],
                              style={
                                  "border": "0px solid black",
                                  "height": "49%", "width": "99%",
                              }
                              )

div_row2_right_bottom = html.Div(id="row2_right_bottom", children=[],
                                 style={
                                     "border": "0px solid black",
                                     "height": "49%", "width": "99%",
                                 }
                                 )

div_row2_right.children.append(div_row2_right_top)
div_row2_right.children.append(div_row2_right_bottom)

div_full = html.Div(id='full_viz', children=[div_row1, div_row2], style={
    "border": "0px solid green",
    "height": "800px", "width": "1000px",
    "overflow": "visible"

})
