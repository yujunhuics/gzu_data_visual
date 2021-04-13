import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from app import app

from apps.student_page import student_layout
from apps.subject_page import subject_layout
from apps.mass_page import mass_layout
from apps.dorm_page import dorm_layout
from apps.welcome_page import welcome_layout
from apps.userpic_page import userpic_layout
from apps.medical_page import medical_layout

total_layout = html.Div(id='total-content', children=[html.Div([
    html.Div(
        className='app-title',
        children=[
            html.Img(id='total_img', src='./static/background.jpg', style={'width': '100%', 'height': 'auto'}, ),
        ],
    ),

    dcc.Tabs(id='main-func-selector', value='welcome', className='custom-tabs-container', children=[
        dcc.Tab(label='Home', value='welcome', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='学生画像', value='userpic', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='学生基本情况数据分析', value='student_analysis', className='custom-tab',
                selected_className='custom-tab--selected'),
        dcc.Tab(label='课程数据分析', value='subject_analysis', className='custom-tab',
                selected_className='custom-tab--selected'),
        dcc.Tab(label='全校各年级数据分析', value='mass_analysis', className='custom-tab',
                selected_className='custom-tab--selected'),
        dcc.Tab(label='校园住宿数据分析', value='dorm_analysis', className='custom-tab',
                selected_className='custom-tab--selected'),
        dcc.Tab(label='医疗数据分析', value='medical_analysis', className='custom-tab',
                selected_className='custom-tab--selected'),
    ]),
    html.Div(id='sub-div')
])],
                        )


@app.callback(
    Output('sub-div', 'children'),
    [Input('main-func-selector', 'value')]
)
def main_func_selector(value):
    if value == 'welcome':
        return welcome_layout
    elif value == 'userpic':
        return userpic_layout
    elif value == 'student_analysis':
        return student_layout
    elif value == 'subject_analysis':
        return subject_layout
    elif value == 'mass_analysis':
        return mass_layout
    elif value == 'dorm_analysis':
        return dorm_layout
    elif value == 'medical_analysis':
        return medical_layout
