import os

def save_idata(idata, model_name):
    path = f'out/{model_name}'
    if not os.path.exists(path):
        os.makedirs(path)
    idata.to_netcdf(os.path.join(path, 'idata.nc'))
