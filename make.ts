var hdf5 = require('hdf5').hdf5;
var h5lt = require('hdf5').h5lt;

var Access = require('hdf5/lib/globals').Access;

var H5Type = require('hdf5/lib/globals.js').H5Type;

var file = new hdf5.File('./ess_file1.h5', Access.ACC_TRUNC);
var group=file.createGroup('entry');
var buffer=Buffer.alloc(8*10*8, "\0", "binary");
for (j = 0; j < 10; j++) {
  for (i = 0; i < 8; i++){
    if (j< (10/2)) {
      buffer.writeDoubleLE(1.0, 8*(i*10+j));
    }
    else {
      buffer.writeDoubleLE(2.0, 8*(i*10+j));
    }
  }
}

h5lt.makeDataset(group.id, 'ESS_Users', buffer, {type: H5Type.H5T_NATIVE_DOUBLE, rank: 2, rows: 8, columns: 10});
