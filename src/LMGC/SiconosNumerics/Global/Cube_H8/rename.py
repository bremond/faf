import os
import shutil as shutil
from glob import glob 
base = 'Cubes_H8'
counter =0
for filename in glob('*.hdf5'):
    print( filename)
    #statinfo = os.stat(os.path.join(dirname, filename))
    #print statinfo.st_size,  statinfo_previous.st_size
    new_filename = filename.replace('GFC3D',base)
    if counter%1==0 :
        print "copy", filename, "in ", os.path.join("./rename/", new_filename) 
        shutil.copy(filename, os.path.join("./rename/", new_filename))
    counter =counter +1
