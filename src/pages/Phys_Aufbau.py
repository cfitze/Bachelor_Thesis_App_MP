import dash
from dash import dcc, html, Output, Input, State, callback, Dash
import plotly.graph_objs as go
import dash_leaflet as dl
# import json
import dash_bootstrap_components as dbc
import pathlib

# Register the subpage Physikalischer Aufbau
dash.register_page(__name__, path='/aufbau', name='Physikalischer Aufbau', order=3)  # is a subpage of the home page

# to use the path of the current module
PATH = pathlib.Path(__file__).parent.parent

# to use the path of the data folder
DATA_PATH_LATEX_PICTURES = PATH.joinpath("assets/Bachelor_Thesis_Latex/Latex_Pictures").resolve()

# Define the layout for this page
layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Physikalischer Aufbau der Liegenschafen", className="pages-header"),
                html.P(
                    "Auf dieser Seite werden der Standort, der physikalische Aufbau, wie auch die benötigten Komponenten der Solaranlage erwähnt, welche benötigt werden um das Ganze in Betrieb zu nehmen.", className='subheader', style={'text-align': 'left'}
                ),
                # html.P("Interaktiver 3D Link einbaue nmit Callback von Liegenschaft Alle-->https://vizview.solextron.com/?projectId=Njg5ODIyM2MtZGZjNy0xMWVkLWExMTEtMjc1OGZiYTcwY2YxXzIwMjMwOTIy&lang=de     5-->https://vizview.solextron.com/?projectId=NTE3ZDVhMWEtZGZjMC0xMWVkLWFiY2EtYjlkNWJiYjY5MzM3XzIwMjMwOTI2&lang=en   7/9/11-->https://vizview.solextron.com/?projectId=ZDE0NmUyZDQtY2ZlNC0xMWVkLWFiYjQtZjdjNzk4Y2MyNTJiXzIwMjMwOTI2&lang=en     13--> https://vizview.solextron.com/?projectId=NzU1YWEwM2EtY2ZlMS0xMWVkLWFkNjktMmJmYzUzMTU5YTM4XzIwMjMwOTI2&lang=en", className='normal-text', style={'text-align': 'left'}),
            ],
            style={"margin": "auto", "width": "100%", "text-align": "center"},
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                        dbc.Row(
                            [
                            dbc.Col(
                                html.Div(
                                    [
                                    # html.P("Wählen sie eine Liegenschaft aus.", className='picture-title', style={"text-align": "left"}),
                                    dcc.Dropdown(
                                        id="dropdown-phys",
                                        options=[
                                            {"label": "Riedgrabenstrasse 5", "value": "5"},
                                            {"label": "Riedgrabenstrasse 7/9/11", "value": "7_9_11"},
                                            {"label": "Riedgrabenstrasse 13", "value": "13"},
                                            {"label": "Riedgrabenstrasse 5/7/9/11/13", "value": "5_7_9_11_13"},
                                        ],
                                        value="5",
                                        clearable=False,
                                        style={
                                            "color": "black",
                                            "font-weight": "bold",
                                            "font-size": "16px",
                                            "width": "270px",
                                            "margin-right": "20px",
                                            "margin-top": "15px",
                                            "margin-bottom": "15px",
                                            "background-color": "transparent",
                                        },
                                    ),
                                    ],
                                ),
                                width=6,
                            ),

                            dbc.Col(
                                    html.Div( 
                                        html.A(
                                            id="external-3d-link",
                                            href="",
                                            target="_blank",
                                            children=[
                                                html.Span("Externer 3D Link von Solextron", style={"margin-left": "10px", "font-size": "17px", "color": "white"}),
                                            ],
                                            style={"text-align": "center", "margin-top": "15px", "display": "block"},
                                        ),
                                        style={"text-align": "center", "margin-top": "15px", 'margin-bottom': '15px'},
                                    ),
                                    width=5,
                            ),
                            ],
                        ),
                            html.Div(
                                id="image-slider-container",
                                children=[
                                    html.Img(id="image-standort", style={"max-width": "100%"}),
                                    html.Img(id="image-aufbau", style={"max-width": "100%"}),
                                    html.Div(
                                        [
                                        html.Button(
                                            id="previous-button",
                                            title="Zeige den Standort im Bild",
                                            className="arrow-left",
                                            children=[
                                                html.Span(),
                                            ]
                                        ),

                                            html.Span(
                                                "Standort",
                                                style={
                                                    "margin-left": "20px",
                                                    "margin-right": "20px",
                                                    "font-size": "17px",
                                                    "font-weight": "bold",
                                                    "color": "white",
                                                },
                                            ),
                                            html.Span(
                                                "Aufbau",
                                                style={
                                                    "margin-left": "20px",
                                                    "margin-right": "20px",
                                                    "font-size": "17px",
                                                    "color": "white",
                                                    "font-weight": "bold",
                                                },
                                            ),
                                        html.Button(
                                            id="next-button",
                                            title="Zeige den Aufbau im Bild",
                                            className="arrow-right",
                                            style={"boarder": 'none'},
                                            children=[
                                                html.Span(),
                                            ]
                                        ),

                                        ],
                                        style={"text-align": "center", "margin-top": "15px"},
                                    ),
                                    
                                ],
                                style={"margin-top": "10px"},
                            ),
                        ]
                    ),
                    width=5,
                ),
                dbc.Col(
                    html.Div(
                        id='table-container-phys',
                        children=[
                            html.Table(
                                id='table-components',
                                style={
                                    'border': '1px solid black',
                                    'border-collapse': 'collapse',
                                    'width': '100%',
                                    'margin': 'auto',
                                    'margin-top': '20%'
                                },
                                children=[
                                    html.Tr([
                                        html.Th('Column 1', style={'border': '1px solid black', 'padding': '8px'}),
                                        html.Th('Column 2', style={'border': '1px solid black', 'padding': '8px'}),
                                        html.Th('Column 3', style={'border': '1px solid black', 'padding': '8px'})
                                    ]),
                                ]
                            ),
                        ],
                        style={'overflow': 'auto'}
                    ),
                    width=3,
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P("Standort der Solaranlage in Rümlang",className= 'picture-title', style={"text-align": "center"}),
                                ],
                                style={"margin": "auto", "width": "80%", "margin-top":"15px"},  # Centered text
                            ),
                            html.Div(
                                [
                                    dl.Map(
                                        id="map",
                                        center=[47.4617372, 8.5202995],
                                        zoom=15,
                                        style={"width": "90%", "height": "400px", "margin-top": "15px", "margin-right": "5px"},
                                        children=[
                                            dl.TileLayer(url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"),
                                            dl.Marker(
                                                position=[47.46135, 8.51967],
                                                children=[
                                                    dl.Tooltip(
                                                        children=[
                                                            html.Div(
                                                                "Riedgrabenstrasse 5/7/9/11/13, 8153 Rümlang",
                                                                className="custom-tooltip",
                                                                style={"font-size": "12px", "font-weight": "bold"},
                                                            )
                                                        ],
                                                        permanent=True,
                                                    )
                                                ],
                                            ),
                                        ],
                                    )
                                ]
                            ),
                        ],

                    ), width=4,
                ),
            ]
        ),
    ]
)

@callback(
    Output('table-components', 'children'),
    Input('dropdown-phys', 'value')
)
def update_table1(option):
    options_data1 = {
        '5': [
            ['Solarmodule', 'Longi Solar 440 Wp','1'],
            ['Inverter', '31.5','1'],
            ['Batterie', '9.1','1'],
            ['Energieertrag [MWh/Jahr]', '24.8','1'],
            ['Installierte PV-Leistung [kWp]', '23.9','1'],
            ['Spez. Ertrag [kWh/kWp]', '23.9','1']
        ],
        '7_9_11': [
            ['Solarmodule', 'Longi Solar 440 Wp','1'],
            ['Inverter', 'X','1'],
            ['Batterie', '!','1'],
            ['MWh/Jahr', 'A','1'],
            ['kWp', '1','1'],
            ['Spez. Ertrag [kWh/kWp]', '23.9','1']
        ],
        '13': [
            ['Solarmodule', 'Longi Solar 440 Wp','1'],
            ['Inverter', '!','1'],
            ['Batterie', '1','1'],
            ['MWh/Jahr', 'X','1'],
            ['kWp', '5','1'],
            ['Spez. Ertrag [kWh/kWp]', '23.9','1']
        ],
        '5_7_9_11_13': [
            ['Solarmodule', 'Longi Solar 440 Wp','1'],
            ['Inverter', '5','1'],
            ['Batterie', 'A','1'],
            ['MWh/Jahr', '1','1'],
            ['kWp', 'X','1'],
            ['Spez. Ertrag [kWh/kWp]', '23.9','1']
        ]
    }
    
    data1 = options_data1.get(option, [])
    
    table_rows1 = [
        html.Tr([
            html.Th('Art der Komponenten', style={'border': '2px solid black', 'padding': '8px'}),
            html.Th('Komponenten', style={'border': '2px solid black', 'padding': '8px'}),
            html.Th('Anzahl', style={'border': '2px solid black', 'padding': '8px'})
        ]),
        *[html.Tr([
            html.Td(
                cell,
                style={
                    'border': '1px solid black',
                    'padding': '8px',
                    'font-weight': 'bold' if col_idx > 0 else 'normal'
                }
            ) for col_idx, cell in enumerate(row)]
        ) for row in data1]
    ]
    return table_rows1


@callback(
    Output('image-standort', 'src'),
    Output('image-aufbau', 'src'),
    Output('previous-button', 'style'),
    Output('next-button', 'style'),
    Input('dropdown-phys', 'value'),
    Input('previous-button', 'n_clicks'),
    Input('next-button', 'n_clicks')
)
def update_images(value, prev_clicks, next_clicks):
    assets_path_standort ='assets/Bachelor_Thesis_Latex/Latex_Pictures/Standort_RS_'
    assets_path_aufbau = 'assets/Bachelor_Thesis_Latex/Latex_Pictures/Aufbau_RS_'
    images = [f'{assets_path_standort}{value}.png', f'{assets_path_aufbau}{value}.png']
    # images = [f'{DATA_PATH_LATEX_PICTURES}\\{assets_path_standort}{value}.png', f'{DATA_PATH_LATEX_PICTURES}\\{assets_path_aufbau}{value}.png']
    num_images = len(images)
    prev_clicks = prev_clicks or 0
    next_clicks = next_clicks or 0
    current_image_index = (prev_clicks - next_clicks) % num_images

    prev_button_style = {'display': 'inline-block', 'background-color': 'transparent', 'color': 'white'}
    next_button_style = {'display': 'inline-block', 'background-color': 'transparent', 'color': 'white'}

    if current_image_index == 0:
        prev_button_style['display'] = 'none'
    elif current_image_index == num_images - 1:
        next_button_style['display'] = 'none'

    if current_image_index == 0:
        return images[current_image_index], None, prev_button_style, next_button_style
    else:
        return None, images[current_image_index], prev_button_style, next_button_style

@callback(
    Output("external-3d-link", "href"),
    Input("dropdown-phys", "value"),
)
def update_external_3d_link(selected_value):
    if selected_value == "5":
        return "https://vizview.solextron.com/?projectId=Njg5ODIyM2MtZGZjNy0xMWVkLWExMTEtMjc1OGZiYTcwY2YxXzIwMjMwOTIy&lang=de"
    elif selected_value == "7_9_11":
        return "https://vizview.solextron.com/?projectId=NTE3ZDVhMWEtZGZjMC0xMWVkLWFiY2EtYjlkNWJiYjY5MzM3XzIwMjMwOTI2&lang=en"
    elif selected_value == "13":
        return "https://vizview.solextron.com/?projectId=NzU1YWEwM2EtY2ZlMS0xMWVkLWFkNjktMmJmYzUzMTU5YTM4XzIwMjMwOTI2&lang=en"
    elif selected_value == "5_7_9_11_13":
        return "https://vizview.solextron.com/?projectId=Njg5ODIyM2MtZGZjNy0xMWVkLWExMTEtMjc1OGZiYTcwY2YxXzIwMjMwOTIy&lang=de"  # Replace with the appropriate link
    else:
        return ""


# Font Awesome Icons:

#     'fas fa-chevron-left': Solid chevron-left icon
#     'fas fa-chevron-right': Solid chevron-right icon
#     'fas fa-arrow-left': Solid arrow-left icon
#     'fas fa-arrow-right': Solid arrow-right icon
#     'fas fa-angle-left': Solid angle-left icon
#     'fas fa-angle-right': Solid angle-right icon
#     'fas fa-caret-left': Solid caret-left icon
#     'fas fa-caret-right': Solid caret-right icon
#     'fas fa-long-arrow-alt-left': Solid long-arrow-alt-left icon
#     'fas fa-long-arrow-alt-right': Solid long-arrow-alt-right icon

# Bootstrap Icons:

#     'bi bi-chevron-left': Chevron-left icon from Bootstrap Icons
#     'bi bi-chevron-right': Chevron-right icon from Bootstrap Icons
#     'bi bi-arrow-left': Arrow-left icon from Bootstrap Icons
#     'bi bi-arrow-right': Arrow-right icon from Bootstrap Icons
#     'bi bi-caret-left': Caret-left icon from Bootstrap Icons
#     'bi bi-caret-right': Caret-right icon from Bootstrap Icons
#     'bi bi-box-arrow-left': Box-arrow-left icon from Bootstrap Icons
#     'bi bi-box-arrow-right': Box-arrow-right icon from Bootstrap Icons

# Feather Icons:

#     'feather icon-chevron-left': Chevron-left icon from Feather Icons
#     'feather icon-chevron-right': Chevron-right icon from Feather Icons
#     'feather icon-arrow-left': Arrow-left icon from Feather Icons
#     'feather icon-arrow-right': Arrow-right icon from Feather Icons
#     'feather icon-caret-left': Caret-left icon from Feather Icons
#     'feather icon-caret-right': Caret-right icon from Feather Icons
#     'feather icon-corner-left-down': Corner-left-down icon from Feather Icons
#     'feather icon-corner-right-down': Corner-right-down icon from Feather Icons




# # Option 3: Using custom JavaScript
# @callback(
#     Output('map-custom-js', 'children'),
#     Input('dropdown-phys', 'value')
# )
# def update_custom_js(value):
#     if value == 'option2':
#         custom_map = """
#         <div id='custom-map' style='width: 100%; height: 400px;'></div>
#         <script>
#             // Create the map instance
#             var map = L.map('custom-map').setView([51.5074, -0.1278], 10);
#             // Add a tile layer
#             L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
#                 attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a> contributors'
#             }).addTo(map);
#             // Add markers or other map interactions as needed
#         </script>
#         """
#         return html.Div([html.Script(custom_map)])
#     else:
#         return None

