import pydicom
import multitasking

def import_dcm(fname: str) -> dict:
# load the DICOM file
    print('loading ' + fname)
    dcmfile = pydicom.dcmread(fname)
    ps = dcmfile.PixelSpacing
    print("Pixel spacing" + str(ps))
    print(dcmfile)

# create 3D array
    img_shape = list(dcmfile.pixel_array.shape)
    print(img_shape)

# fill 3D array with the images from the files
    return multitasking.process_3Dimage_single(dcmfile.pixel_array, img_shape, ps)
