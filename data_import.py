import pydicom
import multitasking

def import_dcm(fname):
# load the DICOM file
    print('loading ' + fname)
    dcmfile = pydicom.dcmread(fname)

# create 3D array
    img_shape = list(dcmfile.pixel_array.shape)
    print(img_shape)

# fill 3D array with the images from the files
    channels = multitasking.process_3Dimage_single(dcmfile.pixel_array, img_shape)
    for key in channels.keys():
        with open(str(key) + '.xyz', 'w', encoding='utf8') as f:
            f.write(str(len(channels[key])) + "\n")
            for i in channels[key]:
                f.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")
            f.close()
    return channels
