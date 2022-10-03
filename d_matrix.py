import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix

def random_dmatrix(input, depo_init = False, depo_x = 0, depo_y = 0, x_lb = 0, y_lb = 0, x_ub = 100, y_ub = 100):
    if (type(input)) == int:
        df = pd.DataFrame({'x_cord': np.random.randint(x_lb,x_ub,input),
                    'y_cord':np.random.randint(y_lb,y_ub,input)})
        if depo_init == True:
            df.iloc[0]['x_cord'] = depo_x
            df.iloc[0]['y_cord'] = depo_y
        d_matrix = pd.DataFrame(distance_matrix(df.values, df.values), columns=df.index)
        d_matrix = np.rint(d_matrix)
        return (df,d_matrix)
    else:
        if depo_init == True:
            input = pd.concat([pd.DataFrame({'x_cord': [depo_x],
                                          'y_cord':[depo_y]}), input], ignore_index=True)
        d_matrix = pd.DataFrame(distance_matrix(input.values, input.values), columns=input.index)
        d_matrix = np.rint(d_matrix)
        return (input,d_matrix)

if (__name__ == '__main__'):
    data = pd.DataFrame({'x_cord': [10,15,20,25],
                    'y_cord':[10,25,30,24]})
    df, d_matrix = random_dmatrix(input = pd.DataFrame({'x_cord': [10,15,20,25],'y_cord':[10,25,30,24]}), depo_init=True, depo_x=10, depo_y=15)
    print(df)
    print(d_matrix)
