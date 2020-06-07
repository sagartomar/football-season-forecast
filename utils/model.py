import pymc3 as pm

def save_parameters(trace, idata, model_name):
    save_path = f'out/{model_name}'
    pm.save_trace(trace, save_path + '/trace')
    idata.to_netcdf(save_path + '/idata.nc')
