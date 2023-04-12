import pandas as pd
import numpy as np


chat_id = 432056961 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    # конверсии в контроле и тесте соотв
    conv_x = x_success / x_cnt 
    conv_y = y_success / y_cnt
    # uplift. считаем, что тест показал себя лучше. Если показывает себя лучше контроль, то ( conv_x / conv_y - 1 )
    uplift = conv_y / conv_x - 1
    
    return ... # Ваш ответ, True или False
