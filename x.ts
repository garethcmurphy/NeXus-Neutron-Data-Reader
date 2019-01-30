const hdf5 = require("hdf5").hdf5;
const h5lt = require("hdf5").h5lt;

const Access = require("hdf5/lib/globals").Access;

class GetH5Info {
  filename: string;
  constructor() {
    this.filename = "V20_ESSIntegration_2018-12-10_1009.nxs";
  }
  getInfo() {
    const file = new hdf5.File(this.filename, Access.ACC_RDONLY);
    let group = file.openGroup("/entry/");
    let members = group.getMemberNames();
    console.log(members);
    group = file.openGroup("/entry/ESS_users/");
    members = group.getMemberNames();
    console.log(members);
    const array = h5lt.readDataset(group.id, "name");
    console.log(array);
  }
}

const h5 = new GetH5Info();
h5.getInfo();
