from pathlib import Path
import dicom
import pathconfig

def filename_gen():
    for path1 in pathconfig.data_root.glob("DOI/*"):
        for path2 in Path(path1).glob("./*"):
            for path3 in Path(path2).glob("./*"):
                for filename in Path(path3).glob("./*"):
                    yield str(filename)


def dicom_gen(img_type):
    """
    generator of dicom data whose SeriesDescription is img_type.
    
    retruns
        dicom.dataset.FileDataset

    img_type : str or list of str
        img_types should be subset of ['cropped images', 'ROI mask images', 'full mammogram images'].
        (I did not check all over the datasets.)
        Ex. img_type = "full mammogram images"
    """
    if not isinstance(img_type, list):
        img_type = [img_type]

    filenames = filename_gen()
    for filename in filenames:
        ds = dicom.read_file(filename)
        try:
            if ds.SeriesDescription in img_type:
                yield ds
            else:
                pass
        except AttributeError:
            pass
