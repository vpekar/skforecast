# Fixtures model_selection multi-series
# ==============================================================================
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error

# Fixtures
# series_1 = np.random.rand(50)
# series_2 = np.random.rand(50)
# exog_1   = series_1 + np.random.normal(0, 0.1, 50)
# exog_2   = np.random.rand(50)
# exog_3   = np.random.rand(50)
# exog_4   = series_2 + np.random.normal(0, 0.1, 50)

series = pd.DataFrame({
     'l1': pd.Series(np.array(
               [0.69646919, 0.28613933, 0.22685145, 0.55131477, 0.71946897,
               0.42310646, 0.9807642 , 0.68482974, 0.4809319 , 0.39211752,
               0.34317802, 0.72904971, 0.43857224, 0.0596779 , 0.39804426,
               0.73799541, 0.18249173, 0.17545176, 0.53155137, 0.53182759,
               0.63440096, 0.84943179, 0.72445532, 0.61102351, 0.72244338,
               0.32295891, 0.36178866, 0.22826323, 0.29371405, 0.63097612,
               0.09210494, 0.43370117, 0.43086276, 0.4936851 , 0.42583029,
               0.31226122, 0.42635131, 0.89338916, 0.94416002, 0.50183668,
               0.62395295, 0.1156184 , 0.31728548, 0.41482621, 0.86630916,
               0.25045537, 0.48303426, 0.98555979, 0.51948512, 0.61289453]
                    )
          ), 
     'l2': pd.Series(np.array(
               [0.12062867, 0.8263408 , 0.60306013, 0.54506801, 0.34276383,
               0.30412079, 0.41702221, 0.68130077, 0.87545684, 0.51042234,
               0.66931378, 0.58593655, 0.6249035 , 0.67468905, 0.84234244,
               0.08319499, 0.76368284, 0.24366637, 0.19422296, 0.57245696,
               0.09571252, 0.88532683, 0.62724897, 0.72341636, 0.01612921,
               0.59443188, 0.55678519, 0.15895964, 0.15307052, 0.69552953,
               0.31876643, 0.6919703 , 0.55438325, 0.38895057, 0.92513249,
               0.84167   , 0.35739757, 0.04359146, 0.30476807, 0.39818568,
               0.70495883, 0.99535848, 0.35591487, 0.76254781, 0.59317692,
               0.6917018 , 0.15112745, 0.39887629, 0.2408559 , 0.34345601]
                    )
          )
})

exog = pd.DataFrame({
     'exog1': pd.Series(np.array(
               [0.81362466, 0.18065237, 0.23475578, 0.65981251, 0.77626016,
               0.41868245, 0.96643556, 0.67516195, 0.4466783 , 0.44168289,
               0.35158485, 0.75925757, 0.40625296, 0.19853505, 0.34611829,
               0.61579746, 0.07568532, 0.06880357, 0.59517447, 0.57993728,
               0.79023383, 0.66388325, 0.67390093, 0.68257639, 0.47676493,
               0.3977578 , 0.56785123, 0.34779524, 0.26016756, 0.70679266,
               0.04774995, 0.39197318, 0.46367839, 0.4370433 , 0.41450122,
               0.37961077, 0.47225148, 0.79649699, 1.0426137 , 0.48792391,
               0.50458267, 0.20520444, 0.23720236, 0.39452153, 0.85171668,
               0.15336444, 0.4738726 , 1.17622403, 0.53176631, 0.55083837])
               ),
     'exog2': pd.Series(np.array(
          [0.22529048, 0.97937984, 0.17235964, 0.24529647, 0.7127206 ,
          0.62075889, 0.11435243, 0.91700825, 0.5831643 , 0.04030412,
          0.65716865, 0.30658072, 0.46395434, 0.48452434, 0.46278193,
          0.18426942, 0.26344748, 0.23883066, 0.72779828, 0.07488211,
          0.94899474, 0.44163677, 0.25777764, 0.90987212, 0.38569441,
          0.77341595, 0.70397664, 0.61953314, 0.66083099, 0.24472837,
          0.37629717, 0.09605039, 0.9278549 , 0.3234861 , 0.272853  ,
          0.73149366, 0.84567995, 0.03531591, 0.25809087, 0.53148211,
          0.83952041, 0.26563705, 0.60606193, 0.0181884 , 0.60906828,
          0.19357335, 0.16319844, 0.58427611, 0.81820829, 0.08336001])
     ),
     'exog3': pd.Series(np.array(
          [0.14173692, 0.19838271, 0.48780824, 0.08424373, 0.08567588,
          0.70887437, 0.04705875, 0.22284741, 0.92726105, 0.99537986,
          0.83901923, 0.29050851, 0.05909171, 0.27456474, 0.25750109,
          0.43010083, 0.29702035, 0.56146054, 0.1388417 , 0.84215781,
          0.83955923, 0.96457563, 0.66089525, 0.15896887, 0.61108399,
          0.27603516, 0.92614876, 0.48826627, 0.32792168, 0.87529287,
          0.6452307 , 0.50767682, 0.26563346, 0.54585537, 0.80222916,
          0.88929714, 0.86435062, 0.71305703, 0.18654522, 0.41497294,
          0.66556244, 0.71263307, 0.98795819, 0.6306933 , 0.14902407,
          0.16021244, 0.66550264, 0.77537995, 0.07558725, 0.21460743])
     ),
     'exog4': pd.Series(np.array(
          [-0.06574814,  0.90956685,  0.62142653,  0.82637769,  0.56159495,
          0.34376551,  0.45848779,  0.38489167,  0.89467872,  0.54904309,
          0.8185359 ,  0.48700256,  0.68844761,  0.69774397,  0.76506425,
          0.00440831,  0.79692897,  0.12322595,  0.12812382,  0.62445613,
          0.2433968 ,  0.84983804,  0.6108338 ,  0.68502064,  0.01186788,
          0.54597677,  0.44377848,  0.29329784, -0.02316005,  0.45542694,
          0.221795  ,  0.7963138 ,  0.57343061,  0.33216654,  0.91545132,
          0.93857233,  0.39897906,  0.16776203,  0.31379519,  0.3557038 ,
          0.83869898,  0.99444057,  0.32071535,  0.80514198,  0.52945861,
          0.76451127,  0.37253453,  0.37938831,  0.12500821,  0.30680189])
     ),
})


def custom_metric(y_true, y_pred):  # pragma: no cover
    """
    """
    metric = mean_absolute_error(y_true, y_pred)
    
    return metric