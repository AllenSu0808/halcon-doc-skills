# read_image (Operator)

## Name

`read_image` — Read an image with different file formats.

## Signature

`def read_image(file_name: MaybeSequence[str]) -> HObject`

## Description

The operator `read_image` reads the indicated image files from
the background storage and generates the image. One or more file
names can be passed in *`file_name`*. If more than one file
name is passed, an image object tuple with the corresponding number
of image objects is returned.

### HALCON formats (HOBJ and IMA)

For images in the HALCON Iconic Object format (HOBJ), multiple images
saved in one file are returned as a tuple of images. If regions or XLDs
are contained within the file, an exception is raised. See
[`write_object`](write_object.md) for more information about the HOBJ format.

All images files written by the operator [`write_image`](write_image.md) (format
'ima') have the extension `'.ima'`. A description file can
be available for every image in IMA format (same file name with
extension `'.exp'`). The type of the pixel data
(`byte`, `int4`, `real`) can also be taken from
the description file. If the description file is not available, the
type `byte` is used by default as well as a default data
size (`'height'` x `'width'`) that can
be queried via [`get_system`](get_system.md). If the data size of the
`'.ima'` file and the default data size are not equal, an
exception is raised.

### Other formats

Besides the HALCON formats, TIFF, GIF, BMP, JPEG, JPEG-2000, JPEG-XR, PNG,
PCX, SUN-Raster, PGM, PPM, PBM, and XWD files can also be read. The
gray values of PBM images are set at the values 0 and 255. The file
formats are either recognized by the extension (if indicated) or
because of the internal structure of the files. If the extension is
indicated the image can be found faster. If no extension is
indicated, files with an extension are preferred to files without
extension. In case of PGM, PPM, and PBM the corresponding extension
(e.g., `'pgm'`) or the general value `'pnm'` can be
used. In case of TIFF `'tiff'` and `'tif'` are
accepted. In case of JPEG-XR `'jxr'`, `'wdp'`, `'wmp'`,
and `'hdp'` are accepted.
In case of JPEG-2000 only `'jp2'` is accepted. In case
of colored images an image with three color channels is
created, the red channel being stored in the first, the green channel
in the second and the blue channel in the third component (channel
number).

For the image formats TIFF, PNG, JPEG-XR, and JPEG-2000, binary alpha
channels are interpreted as domains. For TIFF files, additionally
binary SubIFDs with PhotometricInterpretation = TransparencyMask
are interpreted as domains. Otherwise, the domain of the generated
image object (= all pixels of the matrix) is chosen maximal.

For TIFF images, multipage TIFF files are returned as image object
tuples. SubIFDs in a TIFF file are only read if their dimensions
are equal to the dimensions of the main image.

Images of type 'int8' can be read on 64 bit systems only. Furthermore,
only the IMA and the TIFF format support this image type.

Image files are searched in the current directory and in the image
directory of HALCON (determined by the environment variable). The
image directory of HALCON is preset at `'.'` and
`'/usr/local/halcon/images'` in a Unix-like environment and can be
set via the operator [`set_system`](set_system.md). More than one image
directory can be indicated. This is done by separating the
individual directories by a colon.

Furthermore, the search path can be set via the environment variable
HALCONIMAGES (same structure as `'image_dir'`). Example:

```
   setenv HALCONIMAGES "/usr/images:/usr/local/halcon/images"
```

HALCON also searches images in the subdirectory
`'images'` (Images for the program examples). The
environment variable HALCONROOT is used for the HALCON directory.

## Attention

If CMYK or YCCK JPEG/JPEG-XR files are read, HALCON assumes that these
files follow the Adobe Photoshop convention that the CMYK channels
are stored inverted, i.e., 0 represents 100% ink coverage, rather
than 0% ink as one would expect. The images are converted to RGB
images using this convention. If the JPEG file does not follow this
convention, but stores the CMYK channels in the usual fashion,
[`invert_image`](invert_image.md) must be called after reading the image.

If PNG images that contain an alpha channel are read, the alpha
channel is returned as the second or fourth channel of the output
image, unless the alpha channel contains exactly two different gray
values, in which case a one or three channel image with a reduced
domain is returned, in which the points in the domain correspond to
the points with the higher gray value in the alpha channel.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image(-array) `→` HObject (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Read image.

**`file_name`** (input_control)  filename.read(-array) `→` MaybeSequence[str]

Name of the image to be read.

Default:
"printer_chip/printer_chip_01"

Suggested values:
"fabrik", "fuse", "mreut", "multiple_dies_01", "particle", "patras", "printer_chip/printer_chip_01", "rings_and_nuts", "tooth_rim"

File extension:
.`hobj`, .`ima`, .`tif`, .`tiff`, .`gif`, .`bmp`, .`jpg`, .`jpeg`, .`jp2`, .`jxr`, .`png`, .`pcx`, .`ras`, .`xwd`, .`pbm`, .`pnm`, .`pgm`, .`ppm`

## Result

If the parameters are correct the operator `read_image`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Successors

`disp_image`,
`threshold`,
`regiongrowing`,
`count_channels`,
`decompose3`,
`class_ndim_norm`,
`gauss_filter`,
`fill_interlace`,
`zoom_image_size`,
`zoom_image_factor`,
`crop_part`,
`write_image`,
`rgb1_to_gray`

## Alternatives

`read_sequence`

## See also

`set_system`,
`write_image`

## Module

Foundation
