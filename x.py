import h5py

f = h5py.File('V20_ESSIntegration_2018-12-10_1009.nxs','r',  libver='latest', swmr=True)
print(h5py.version.hdf5_version_tuple)
print(list(f.keys()))
print(list(f.items()))
print(list(f["/entry/ESS_users"].items()))
names=f["/entry/ESS_users/name"]
for name in names:
    print(name)
f.close()
