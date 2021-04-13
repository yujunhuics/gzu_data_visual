import dash_html_components as html

welcome_layout = [
    html.Div(id='preview', children=[
        html.Div(id='w-title-container', children=[
            html.H3('贵州大学数据可视化分析系统'),
        ], style={'text-align': 'center', 'font-weight': 'bold'}),
        html.Div(id='w-team-name', children=[
            html.H5('开发者：余俊晖'),
        ], style={'text-align': 'center', 'font-weight': 'bold'}),

        html.Div(id='preview-text', children=[

            html.Div(
                children=[
                    html.Hr(),
                    html.P(children=[
                        '主要框架：',
                        # html.Hr(),
                        # html.Br(),
                        html.A(id='dash-url', children=['1.plot.ly'], href='https://plot.ly/', target='_blank'),

                        html.A(id='echarts', children=['  2.echarts'], href='https://echarts.apache.org/zh/index.html',
                               target='_blank'),
                        html.A(id='word_cloud', children=['  3.word_cloud'],
                               href='http://amueller.github.io/word_cloud/', target='_blank'),
                        # '的dash框架实现。图表中自带了很多基础的控件，可以对图表进行拖拽选择',
                        # '指定区域的大小缩放，鼠标悬停显示所处位置的数据点或数据块的具体信息，具体的特色功能详见一起提交的作品说明。',
                    ], className='sj-p',

                    ),

                    html.P(children=["""
                        功能介绍:
                        1、学生画像
                        2、学生基本情况数据分析。
                        3、课程数据分析
                        4、全校各年级数据分析
                        5、校园住宿数据分析
                        6、医疗数据分析
                    """], className='sj-p'),

                    html.P(children=[
                        '外部链接：',
                        html.A(id='pre-url', children=['早期工作'], href='http://amueller.github.io/word_cloud/',
                               target='_blank'),
                        # '的dash框架实现。图表中自带了很多基础的控件，可以对图表进行拖拽选择',
                        # '指定区域的大小缩放，鼠标悬停显示所处位置的数据点或数据块的具体信息，具体的特色功能详见一起提交的作品说明。',
                    ], className='sj-p',

                    ),
                    html.Br(),
                    html.Div(
                        id='preview-text', children=[
                            html.Img(src='../static/chitu_qrcode.png')], style={'margin-left': '50%', 'margin-right': '50%', 'padding-bottom': '10%'}),

                ], style={'margin-left': '5%', 'margin-right': '5%', 'padding-bottom': '10%'}
            )
        ])
    ], className='text-container'),
]
