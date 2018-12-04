# Prueba de regresión lineal múltiple python
# Usando como referencia https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9

import pandas as pd
import numpy as np
import statsmodels.formula.api as sm
# import scipy.stats as st #import all scipy stats
from scipy.stats import t

edad = np.array([42, 64, 47, 56, 54, 48, 57, 52, 67, 46, 58, 62, 49, 56, 63, 64, 67, 49, 53, 59, 65, 67, 49, 53, 57, 47, 58, 48, 51, 49, 68, 58, 54, 59, 45])
colesterol = np.array([282, 235, 200, 200, 300, 215, 216, 254, 310, 237, 220, 233, 240, 295, 310, 268, 243, 239, 198, 218, 215, 254, 218, 221, 237, 244, 223, 198, 234, 175, 230, 248, 218, 285, 253])
imc = np.array([31.64, 30.80, 25.61, 26.17, 31.96, 23.18, 21.19, 26.95, 24.26, 21.87, 25.61, 27.92, 27.73, 22.49, 28.50, 30.04, 23.88, 21.99, 26.93, 27.00, 24.04, 28.65, 25.71, 25.33, 25.42, 23.99, 25.23, 25.81, 26.93, 27.77, 30.85, 21.61, 26.3, 31.44, 25])
presion = np.array([97, 90, 80, 75, 100, 67, 80, 70, 105, 70, 70, 75, 90, 95, 95, 90, 85, 75, 75, 85, 70, 105, 85, 80, 90, 85, 70, 85, 80, 80, 70, 75, 95, 100, 75])

pacientes = pd.DataFrame({
    'edad': edad,
    'colesterol': colesterol,
    'imc': imc,
    'presion': presion
})

ml_pacientes = sm.ols(formula='presion ~ colesterol + imc + edad', data=pacientes).fit()

#predictions = ml_pacientes.predict(X)

# Print out the statistics
print(ml_pacientes.summary())

n = len(pacientes.index)
# t.ppf is equivalent to qt in R
print(t.ppf([(.025, .975)], n-4))
