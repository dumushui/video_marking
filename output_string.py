
import re
import ipywidgets

def return_value(box_tab):
    ''' return values of boxs and tab
    Desc:
        the ipywidgets.HBox, ipywidgets.VBox and ipywidgets.tab was consist of 
        ipywidgets.widgets.widget_selection.ToggleButtons
        using recursion to return all the values from the defined table
    Args:
        box_tab: ipywidgets.HBox or ipywidgets.Tab 
    Returns:
        list that contain all the children values

    Example:
        return_value(start_place())

        ['良好GOOD',
        [['左侧L', '白0', '虚0', '单d', '宽K'], ['', '', '', '', '']],
        '白天DAY',
        '晴天SUN',
        '没偏移MPY',
        '',
        '直道ZD',
        '没偏移MPY']
    '''

    # list_ = []
    # for i in box_tab.children:
    #     if isinstance(i, ipywidgets.widgets.widget_selection.ToggleButtons):
    #         list_.append(i.value)
    #     else:
    #         list_.append(return_value(i))
    # return list_

    return [i.value if isinstance(i, ipywidgets.widgets.widget_selection.ToggleButtons) else return_value(i)  for i in box_tab.children]


def collect_character(list_:list):
    ''' collect letter from the reslut from return_value
    Desc:
        Since the value collect function using recursion and the data structure required
        using recursion to collect letter that we need 
        raise error when the data format was not correct
    Args:
        list_: result values from widgets.children
    Returns:
        return all the letter in the original shape

    Example：
        list_ = return_value(start_place()).remove('')
        collect_character(list_)

        ['GOOD',
        [['L', '0', '0', 'd', 'K'], ['', '', '', '', '']],
        'DAY',
        'SUN',
        'MPY',
        'ZD',
        'MPY']
    '''
    output = []
    if '' in list_ :
        if len(list(filter(lambda x: x == '',list_))) != 5:
            raise ValueError('如果要第二车道，那么需要全部填写')
    for i in list_:
        if isinstance(i, str):
            output.append(''.join(re.findall(r'[A-Z]|[a-z]|\d+',i)))
        else:
            output.append(collect_character(i))
    return output    



def formulate_string(list_:list):
    ''' to combine letter into the string in specific format
    Desc: 
        connect labels with '_' 
    Args: 
        list_ : list consists of letters
    Retrun:
        labels in string
    Example:
        list_ = return_value(start_place()).remove('')
        collect_character(list_)
    
        "GOOD_L00dK__DAY_SUN_MPY_ZD_MPY"
    '''
    for index,value in enumerate(list_):
        if isinstance(value, list):
            list_[index] = formulate_string(value)
        else:
            pass
    if len(list_) == 5: #
        return ''.join(list_)
    else:
        return '_'.join(list_)
        

def return_string(sp:ipywidgets.widgets.widget_box.VBox):
    ''' return labels string
    Desc:
        using functions behind to return labels string 
    Args: 
        sp:ipywidgets.widgets.widget_box.VBox
    Return:
        labels in string
    '''
    list_ = return_value(sp)
    # There's default '' in "other" case need to remove
    if '' in list_:
        list_.remove('')
    list_ = collect_character(list_)
    str_ = formulate_string(list_)
    return '_'+str_