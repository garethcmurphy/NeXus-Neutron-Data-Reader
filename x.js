const hdf5 = require("hdf5").hdf5;
const h5lt = require("hdf5").h5lt;
const Access = require("hdf5/lib/globals").Access;
try
{
    var file = new hdf5.File('./roothaan.h5', Access.ACC_TRUNC);
    var group=file.createGroup('entry/sample');
    var quotes=new Array(1);
    quotes[0]="Never put off till tomorrow what may be done day after tomorrow just as well.\0";
    h5lt.makeDataset(group.id, "description", quotes);
    var scalar="Never put off till tomorrow what may be done day after tomorrow just as well.\0";
    h5lt.makeDataset(group.id, "scalar", scalar);
    group.close();
    file.close();
    file = new hdf5.File('./v20.h5', Access.ACC_RDWR);
    group=file.openGroup('entry/sample');
    var array=h5lt.readDataset(group.id, 'description');
    console.dir(array.length);
    if(array.constructor.name==='Array'){
        for(var mIndex=0;mIndex<array.length;mIndex++){
            console.dir(array[mIndex]);
        }
    }
    console.log(h5lt.readDataset(group.id, 'scalar'));
    group.close();
    file.close();
}
catch(err) {
    console.dir(err.message);
}
