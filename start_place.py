import ipywidgets as widgets
def start_place():
    ''' define the buttton table using widgets.ToggleButtons
    Desc:
        basic table blocks was composed by widgets.ToggleButtons 
        using widgets.HBox(horizontal) and widgets.VBox(vertical)
        merging into a tab by using function widgets.Tab
    '''
    good_bad = widgets.ToggleButtons(
        options=['良好GOOD','复杂BAD'],
        description='良好或复杂:',
    )

    left_right = widgets.ToggleButtons(
        options=['左侧L', '右侧R'],
        value = '左侧L',
        description='左侧或右侧:',
    )

    color = widgets.ToggleButtons(
        options=['白0', '黄1'],
        value = '白0',
        description='白色或黄色:',
    )

    road = widgets.ToggleButtons(
        options=['单d', '双s'],
        value = '单d',
        description='单行或双行:',
    )

    width = widgets.ToggleButtons(
        options=['宽K', '窄Z'],
        value = '宽K',
        description='单行或双行:',
    )

    line_ = widgets.ToggleButtons(
        options=['虚0', '实1', '虚实2'],
        value = '虚0',
        description='虚线或实线:',
    )
    start_place_ = widgets.VBox([left_right, color, line_,  road, width])
    left_right1 = widgets.ToggleButtons(
       options=['', '左侧L', '右侧R'],
        value = '',
        description='左侧或右侧:',
    )

    color1 = widgets.ToggleButtons(
        options=['', '白0', '黄1'],
        value = '',
        description='白色或黄色:',
    )

    road1 = widgets.ToggleButtons(
        options=['', '单d', '双s'],
        value = '',
        description='单行或双行:',
    )

    width1 = widgets.ToggleButtons(
        options=['', '宽K', '窄Z'],
        value = '',
        description='单行或双行:',
    )

    line_1 = widgets.ToggleButtons(
        options=['', '虚0', '实1', '虚实2'],
        value = '',
        description='虚线或实线:',
    )
    
    start_place_1 = widgets.VBox([left_right1, color1, line_1,  road1, width1])
    tab = widgets.Tab(children=[start_place_, start_place_1])
    tab.set_title(0, '单车道情况')
    tab.set_title(1, '双车道时第二车道')
    
    timing_ = widgets.ToggleButtons(
        options=['白天DAY', '夜晚NIG', '黄昏DUSK', '黎明DAWN'],
        description='所处时间段:'
    )

    weather_ = widgets.ToggleButtons(
        options=['晴天SUN', '雨天RAIN', '小雪SNOW', '雾天FOG', '阴天CLO'],
        description='天气情况:'
    )

    shifted_ = widgets.ToggleButtons(
        options=['没偏移MPY', '有左偏ZP', '有右偏YP'],
        description='偏移情况:'
    )

    lis = ['',
           '白天前车001',
           '斑马线002',
           '侧车阴影003',
           '车道线模糊004',
           '导流线005',
           '反光006',
           '减速线007',
           '箭头008',
           '逆光009',
           '晚上前车尾灯010',
           '污迹011',
           '阴影012',
           '雨刮013',
           '长排路灯014',
           '长字体015',
           '修补路面016',
           '路面水渍0017']

    others_ = widgets.ToggleButtons(
        options=lis,
        description='其他情况:'
    )

    road_line = widgets.ToggleButtons(
        options=['直道ZD', '弯道WD', '急弯道JWD'],
        description='其他情况:'
    )

    shifting_speed = widgets.ToggleButtons(
        options=['没偏移MPY', '有快偏KP', '有慢偏MP'],
        description='其他情况:'
    )
    return widgets.VBox(children=[good_bad, tab, timing_, weather_, shifted_, others_, road_line, shifting_speed])




