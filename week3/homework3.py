import numpy as np
def arr_replace(x):
    x=np.array(x)
    x[x%2!=0]=0
    return x

import numpy as np
def arr_replace_where(x):
    x = np.array(x)
    return np.where(x%2==0,0,x)

import numpy as np
def arr_repeat(x):
    x = np.array(x)
    return np.repeat(x,3,0)

import numpy as np
def arr_join(x):
    x = np.array(x)
    return np.tile(x,3)
