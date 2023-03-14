# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 08:08:02 2021

@author: User
"""
import xarray as xr
import numpy as np
import pandas as pd

data = xr.open_dataset(r'C:\Users\User\Documents\LCQAr\pesquisa\dados_IEMA\correlacao_mensal_correta\MERRA\varios_pontos\MERRA2_400.tavgM_2d_chm_Nx.201901.nc4 (2).nc4')
CO = np.array(data.variables['COSC'][:,:,0])
CO_2D = CO.flatten()
CO_2D = pd.DataFrame(CO.flatten())

