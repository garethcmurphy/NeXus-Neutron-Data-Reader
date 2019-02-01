#!/usr/bin/env python3
import h5py
import inspect
import copy
import json
import socket


class GetH5Info:
    nexusInfo = {}
    filename = "v20.h5"
    metadata = {}

    sourceFolderArray = {
        "0001": "v20/2018_01_24",
        "0002": "v20/2018_12_13/v20-2018-12-14T11:22:26+0100",
        "0003": "v20/2018_12_13/v20-2018-12-14T11:23:38+0100",
        "0004": "v20/2018_12_13/v20-2018-12-14T15:12:53+0100",
        "0005": "v20/2018_12_13/v20-2018-12-14T16:12:01+0100",
        "0006": "v20/2018_12_13/v20-2018-12-14T16:12:26+0100",
        "0007": "v20/2018_12_13/v20-2018-12-15T16:56:22+0100",
        "0008": "v20/2018_12_13/v20-2018-12-15T18:10:22+0100",
        "0009": "v20/2018_12_13/v20-2018-12-17T07:13:37+0100",
        "0010": "v20/2018_12_13/v20-2018-12-17T19:31:02+0100",
        "0011": "v20/2018_12_13/v20-2018-12-18T09:18:46+0100",
        "0012": "v20/2018_12_13/v20-2018-12-18T10:42:33+0100",
        "0013": "v20/2018_12_13/v20-2018-12-18T11:01:28+0100",
        "0014": "v20/2018_12_13/v20-2018-12-19T08:17:32+0100",
        "0015": "v20/2018_12_13/v20-2018-12-19T08:56:00+0100",
        "0016": "v20/2018_12_13/V20_ESSIntegration_20181210",
        "0017": "v20/2018_12_13/V20_ESSIntegration_2018-12-10_1009",
        "0018": "v20/2018_12_13/V20_ESSIntegration_2018-12-10_1805",
        "0019": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0915",
        "0020": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0943",
        "0021": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0951",
        "0022": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_0952",
        "0023": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1018",
        "0024": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1713",
        "0025": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1743",
        "0026": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1847",
        "0027": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1914",
        "0028": "v20/2018_12_13/V20_ESSIntegration_2018-12-11_1923",
        "0029": "v20/2018_12_13/V20_ESSIntegration_2018-12-12_1209",
        "0030": "v20/2018_12_13/V20_ESSIntegration_2018-12-13_0942",
        "0031": "v20/2018_12_13/V20_ESSIntegration_2018-12-13_1028",
        "0032": "v20/2018_12_13/V20_ESSIntegration_2018-12-13T15:53:48",
        "0033": "v20/2018_12_13/V20_ESSIntegration_2018-12-13T16:20:00",
        "0034": "v20/2018_12_13/V20_ESSIntegration_2018-12-14T09:25:00"
    }

    inv_map = {v: k for k, v in sourceFolderArray.items()}

    def __init__(self):
        self.filename = "v20.h5"

    def get_h5_info(self, filename):

        self.nexusInfo = {}
        f = h5py.File(filename, 'r',  libver='latest', swmr=True)

        self.nexusInfo["creator"] = self.get_attribute(f.attrs, "creator")
        self.nexusInfo["file_name"] = self.get_attribute(f.attrs, "file_name")
        self.nexusInfo["file_time"] = self.get_attribute(f.attrs, "file_time")
        my_list = list()
        self.get_names(my_list, f, "/entry/ESS_users")
        self.get_names(my_list, f, "/entry/HZB_users")
        self.get_names(my_list, f, "/entry/STFC_users")
        self.nexusInfo["names"] = my_list
        title = self.get_property(f, "/entry/title")
        self.nexusInfo["title"] = title
        source_name = self.get_property(f, "/entry/instrument/source/name")
        sample_description = self.get_ellipsis(f, "/entry/sample/description")
        self.nexusInfo["sample_description"] = sample_description[()]
        self.nexusInfo["source_name"] = source_name
        f.close()
        # print(self.nexusInfo)
        tag = filename.replace("/users/detector/experiments/", "")
        sep = "/"
        tag2 = sep.join(tag.split(sep)[:-1])
        tag3 = "v20/2018_12_13/"+self.nexusInfo["file_name"]
        tag4 = self.inv_map[tag3]
        self.metadata[tag4] = self.nexusInfo

    def get_names(self, my_list, f, tag):
        if tag in f:
            names = f[tag+"/name"]
            my_list.extend(names)

    def get_attribute(self, attrs, attr):
        value = ""
        if (attr in attrs.keys()):
            value = attrs[attr]
        return value

    def get_property(self, f, path):
        title2 = ""
        if (path in f):
            title = f[path][...]
            title2 = title[()]
        # print(path, title2)
        return title2

    def get_ellipsis(self, f, path):
        if (path in f):
            dset = f[path]
        return dset[...]

    def loop(self):
        hostname = socket.gethostname()
        filenames = [
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-18T09:18:46+0100/v20-2018-12-18T09:18:46+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-14T16:12:01+0100/v20-2018-12-14T16:12:01+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_1743/V20_ESSIntegration_2018-12-11_1743.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-14T11:22:26+0100/v20-2018-12-14T11:22:26+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_0952/V20_ESSIntegration_2018-12-11_0952.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-10_1009/V20_ESSIntegration_2018-12-10_1009.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-14T09:25:00/V20_ESSIntegration_2018-12-14T09:25:00.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-19T08:17:32+0100/v20-2018-12-19T08:17:32+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-18T10:42:33+0100/v20-2018-12-18T10:42:33+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-19T08:56:00+0100/v20-2018-12-19T08:56:00+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-18T11:01:28+0100/v20-2018-12-18T11:01:28+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_1914/V20_ESSIntegration_2018-12-11_1914.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_0951/V20_ESSIntegration_2018-12-11_0951.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-17T07:13:37+0100/v20-2018-12-17T07:13:37+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-12_1209/V20_ESSIntegration_2018-12-12_1209.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-13_1028/V20_ESSIntegration_2018-12-13_1028.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_1847/V20_ESSIntegration_2018-12-11_1847.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-14T11:23:38+0100/v20-2018-12-14T11:23:38+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_1923/V20_ESSIntegration_2018-12-11_1923.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-13_0942/V20_ESSIntegration_2018-12-13_0942.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-15T18:10:22+0100/v20-2018-12-15T18:10:22+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_1713/V20_ESSIntegration_2018-12-11_1713.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-13T16:20:00/V20_ESSIntegration_2018-12-13T16:20:00.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_1018/V20_ESSIntegration_2018-12-11_1018.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-17T19:31:02+0100/v20-2018-12-17T19:31:02+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-13T15:53:48/V20_ESSIntegration_2018-12-13T15:53:48.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_0915/V20_ESSIntegration_2018-12-11_0915.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-14T15:12:53+0100/v20-2018-12-14T15:12:53+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_20181210/V20_ESSIntegration_20181210.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-11_0943/V20_ESSIntegration_2018-12-11_0943.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-15T16:56:22+0100/v20-2018-12-15T16:56:22+0100.nxs",
            "/users/detector/experiments/v20/2018_12_13/V20_ESSIntegration_2018-12-10_1805/V20_ESSIntegration_2018-12-10_1805.nxs",
            "/users/detector/experiments/v20/2018_12_13/v20-2018-12-14T16:12:26+0100/v20-2018-12-14T16:12:26+0100.nxs",
        ]
        if hostname == 'CI0020036':
            filenames = [
                "/Users/garethmurphy/Downloads/nexusnode/V20_ESSIntegration_2018-12-10_1009.nxs"]
        for filename in filenames:
            self.get_h5_info(filename)


if __name__ == "__main__":
    h5 = GetH5Info()
    h5.loop()

    print(json.dumps(h5.metadata, indent=2, sort_keys=True))

    filename = "metadata.json"
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(h5.metadata, f, indent=2, sort_keys=True )
