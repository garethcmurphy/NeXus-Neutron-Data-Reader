#!/usr/bin/env python3
import h5py
import inspect
import copy


class GetH5Info:
    nexusInfo = {}
    filename = "v20.h5"

    def __init__(self):
        self.filename = "v20.h5"

    def get_h5_info(self, filename):

        f = h5py.File(filename, 'r',  libver='latest', swmr=True)

        self.nexusInfo["creator"] = self.get_attribute(f.attrs, "creator")
        self.nexusInfo["file_name"] = self.get_attribute(f.attrs, "file_name")
        self.nexusInfo["file_time"] = self.get_attribute(f.attrs, "file_time")
        if ("/entry/ESS_users" in f):
            my_list = list()
            names = f["/entry/ESS_users/name"]
            for name in names:
                my_list.append(name)
            self.nexusInfo["names"] = my_list
        title = self.get_property(f, "/entry/title")
        source_name = self.get_property(f, "/entry/instrument/source/name")
        sample_description = self.get_ellipsis(f, "/entry/sample/description")
        self.nexusInfo["sample_description"] = sample_description[()]
        self.nexusInfo["source_name"] = source_name
        f.close()
        print(self.nexusInfo)

    def get_attribute(self, attrs, attr):
        value = ""
        if (attr in attrs.keys()):
            value = attrs[attr]
        return value

    def get_property(self, f, path):
        title2= ""
        if (path in f):
            title = f[path][...]
            title2= title[()]
        print(path, title2)
        return title2

    def get_ellipsis(self, f, path):
        if (path in f):
            dset = f[path]
        return dset[...]

    def loop(self):
        filenames=["v20.h5"]
        for filename in filenames:
            self.get_h5_info(filename)


if __name__ == "__main__":
    h5=GetH5Info()
    h5.loop()
