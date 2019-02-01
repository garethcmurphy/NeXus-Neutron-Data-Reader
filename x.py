#!/usr/bin/env python3
import h5py

class GetH5Info:
    def __init__(self):
        filename= "v20.h5"
        #filename = "V20_ESSIntegration_2018-12-10_1009.nxs"
        f = h5py.File(filename,'r',  libver='latest', swmr=True)
        print(h5py.version.hdf5_version_tuple)
        print(list(f.keys()))
        print(list(f.items()))
        if ("/entry/ESS_users" in f):
            print(list(f["/entry/ESS_users"].items()))
            names=f["/entry/ESS_users/name"]
            for name in names:
                print(name)
        title = self.get_property(f,"/entry/title")
        sample_description = self.get_ellipsis(f, "/entry/sample/description")
        print(title)
        print(sample_description)
        f.close()

    def get_property(self, f, path):
        title = ""
        if (path in f):
            title = f[path]
        return title

    def get_ellipsis(self,f,path):
        title = ""
        if (path in f):
            dset = f[path]
        return dset[...]
        

GetH5Info()
