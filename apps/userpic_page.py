import dash_html_components as html
import dash_core_components as dcc

userpic_layout = [
    html.Div(id = 'preview',children = [
        # html.Div(id = 'w-title-container',children = [
        #     html.H3('贵州大学数据可视化分析系统'),
        # ],style = {'text-align':'center','font-weight':'bold'}),
        # html.Div(id = 'w-team-name', children = [
        #     html.H5('开发者：余俊晖'),
        # ],style = {'text-align':'center','font-weight':'bold'}),

       
        html.Div(id = 'preview-text',children = [
            
            html.Div(
                children = [
                    # html.Hr(),
                    # html.P(children = [
                    #     '本作品基于python的',
                    #     html.A(id = 'dash-url',children = ['plot.ly'],href = 'https://plot.ly/',target = '_blank'),
                    #     '的dash框架实现。图表中自带了很多基础的控件，可以对图表进行拖拽选择',
                    #     '指定区域的大小缩放，鼠标悬停显示所处位置的数据点或数据块的具体信息，具体的特色功能详见一起提交的作品说明。',
                    #     ],className = 'sj-p'
                    # ),
                    html.Div(id = 'student-id',children = [
                        html.H6(
                            id = 'student-id-indicator',
                            children = '请输入所要展示画像的学生学号: ',
                            style = {'display': 'inline-block','margin-right':'10px','font-weight':'bold'}),
                        dcc.Input(id='input-student-id',
                            type='text',
                            value='14012',
                            style = {'display': 'inline-block','margin-left':'10px','margin-right':'10px'}),
                        html.Button(
                            children = '提交',
                            id='student-id-submmit',
                            className= 'button-raised button-primary button-pill',
                            n_clicks = 0,),
                        # html.Hr(style = {'width':'90%'}),
                        # html.Div(id = 'student-info',style = {'padding-bottom':'10px'}),
                    ]),

                    html.Img(src='../static/studentPic/14012.jpg'),
                    html.Img(src='../static/studentPic/13968.jpg'),

                    html.P("""
                        。。。前端待开发中
                    """,className = 'sj-p')
                        ],style = {'margin-left':'5%','margin-right':'5%','padding-bottom':'10%'},


            )
        ])
    ],className = 'text-container'), 
]

