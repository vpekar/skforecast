# Unit test __init__ ForecasterAutoreg
# ==============================================================================
import re
import pytest
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from skforecast.preprocessing import RollingFeatures
from skforecast.ForecasterAutoreg import ForecasterAutoreg


def test_init_ValueError_when_no_lags_or_window_features():
    """
    Test ValueError is raised when no lags or window_features are passed.
    """
    err_msg = re.escape(
        ("At least one of the arguments `lags` or `window_features` "
         "must be different from None. This is required to create the "
         "predictors used in training the forecaster.")
    )
    with pytest.raises(ValueError, match = err_msg):
        ForecasterAutoreg(
            regressor       = LinearRegression(),
            lags            = None,
            window_features = None
        )


@pytest.mark.parametrize("lags, window_features, expected", 
                         [(5, None, 5), 
                          (None, True, 6), 
                          (5, True, 6)], 
                         ids = lambda dt: f'lags, window_features, expected: {dt}')
def test_init_window_size_correctly_stored(lags, window_features, expected):
    """
    Test window_size is correctly stored when lags or window_features are passed.
    """
    if window_features:
        window_features = RollingFeatures(
            stats=['ratio_min_max', 'median'], window_sizes=[5, 6]
        )

    forecaster = ForecasterAutoreg(
                     regressor       = LinearRegression(),
                     lags            = lags,
                     window_features = window_features
                 )
    
    assert forecaster.window_size == expected
    if window_features:
        assert forecaster.window_features_class_names == ['RollingFeatures']
    else:
        assert forecaster.window_features_class_names is None


@pytest.mark.parametrize("dif", 
                         [0, 0.5, 1.5, 'not_int'], 
                         ids = lambda dif: f'differentiation: {dif}')
def test_init_ValueError_when_differentiation_argument_is_not_int_or_greater_than_0(dif):
    """
    Test ValueError is raised when differentiation is not an int or greater than 0.
    """
    err_msg = re.escape(
        (f"Argument `differentiation` must be an integer equal to or "
         f"greater than 1. Got {dif}.")
    )
    with pytest.raises(ValueError, match = err_msg):
        ForecasterAutoreg(
            regressor       = LinearRegression(),
            lags            = 5,
            differentiation = dif
        )


@pytest.mark.parametrize("dif", 
                         [1, 2], 
                         ids = lambda dif: f'differentiation: {dif}')
def test_init_window_size_is_increased_when_differentiation(dif):
    """
    Test window_size is increased when including differentiation.
    """
    forecaster = ForecasterAutoreg(
                     regressor       = LinearRegression(),
                     lags            = 5,
                     differentiation = dif
                 )
    
    assert forecaster.window_size == len(forecaster.lags) + dif


def test_init_binner_is_created_when_binner_kwargs_is_None():
    """
    Test binner is initialized with the default kwargs
    """
    forecaster = ForecasterAutoreg(
                     regressor = object(),
                     lags      = 5,
                 )
    
    expected = {
        'n_bins': 10, 'encode': 'ordinal', 'strategy': 'quantile',
        'subsample': 200000, 'random_state': 789654, 'dtype': np.float64
    }

    assert forecaster.binner.get_params() == expected


def test_init_binner_is_created_when_binner_kwargs_is_not_None():
    """
    Test binner is initialized with kwargs
    """
    binner_kwargs = {
        'n_bins': 10, 'encode': 'onehot', 'strategy': 'quantile',
        'subsample': 100, 'random_state': 1234, 'dtype': np.float64
    }
    forecaster = ForecasterAutoreg(
                     regressor     = object(),
                     lags          = 5,
                     binner_kwargs = binner_kwargs
                 )
    
    expected = {
        'n_bins': 10, 'encode': 'ordinal', 'strategy': 'quantile',
        'subsample': 100, 'random_state': 1234, 'dtype': np.float64
    }

    assert forecaster.binner.get_params() == expected
