import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
from haversine import haversine

def random_dmatrix(input, method = 'euclidean', depo_init = False, depo_x = 0, depo_y = 0, x_lb = 0, y_lb = 0, x_ub = 100, y_ub = 100, api_key):
    if (method == 'haversine') & (depo_init == True):
        return input, None
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
            input = pd.concat([pd.DataFrame({'x_cord': [depo_x],'y_cord':[depo_y]}), input], ignore_index=True)
            d_matrix = pd.DataFrame(distance_matrix(input.values, input.values), columns=input.index)
        if (depo_init == False) & (method == 'euclidean'):
            d_matrix = pd.DataFrame(distance_matrix(input.values, input.values), columns=input.index)
        if (depo_init == False) & (method == 'haversine'):
            d_matrix = pd.DataFrame(index=list(range(input.shape[0])), columns=list(range(input.shape[0])))
            for i in range(d_matrix.shape[0]):
                for j in range(d_matrix.shape[0]): 
                    d_matrix.iloc[i,j] = haversine((input.loc[i,'x_cord'], input.loc[i,'y_cord']), (input.loc[j,'x_cord'], input.loc[i,'y_cord',]))
         if (depo_init == False) & (method == 'roadDistance'):
            d_matrix = pd.DataFrame(index=list(range(input.shape[0])), columns=list(range(input.shape[0])))
            input['lat_long'] = input['y_cord'].astype(str) + ',' + input['x_cord'].astype(str)
            
           for j in range(input.shape[0]):
               for k in range(input.shape[0]):
            if (j==k):
                d_matrix.iloc[j,k]=0
            if (j !=k):
                source = input.loc[j,'lat_long']
                dest = input.loc[k,'lat_long']
                url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
                r = requests.request('GET',url + 'origins=' + source +'&destinations=' + dest + '&key=' + api_key)
                d_matrix.iloc[j,k] = r.json()['rows'][0]['elements'][0]['distance']['value']/1000
        return (input,d_matrix)
