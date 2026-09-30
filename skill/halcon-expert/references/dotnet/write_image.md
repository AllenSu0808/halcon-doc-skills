# WriteImage (Operator)

## Name

`WriteImage` — Write images in graphic formats.

## Signature

`static void HOperatorSet.WriteImage(HObject image, HTuple format, HTuple fillColor, HTuple fileName)`

`void HImage.WriteImage(string format, HTuple fillColor, HTuple fileName)`

`void HImage.WriteImage(string format, int fillColor, string fileName)`

## Description

The operator `WriteImage` saves the input image *`image`* in the
file *`fileName`* in the format *`format`*. If the domain (region)
cannot be saved in the specified *`format`* (this is the case for 'bmp',
'jpeg', and 'ima'), all pixels outside the region receive the color defined
by *`fillColor`*. For gray value images a value between 0 (black) and
255 (white) must be passed. For RGB color images the RGB values can be passed
directly as a hexadecimal value: e.g., 0xffff00 for a yellow background
(red=255, green=255, blue=0).

The following formats are currently supported:

### 'tiff', 'bigtiff': TIFF format, file extension *.tif

All HALCON pixel types are supported. Image object tuples with up to 65535
image objects and up to 65535 channels can be written.
Image objects with channels of mixed pixel types can be written.

Compression is possible with

|  |  |
| --- | --- |
| *"deflate [num]"*: | Adobe deflate compression (lossless) |
| *"jpeg [num]"*: | JPEG (lossy) |
| *"lzw"* | LZW (lossless) |
| *"packbits"* | PackBits (lossless) |

Here, *"[num]"* denotes an optional specification of a compression
parameter. For *"deflate"*, a number between *0* (no
compression) and *9* (maximum compression) can be specified. For
*"jpeg"*, a number between *0* and *100* can be
specified. The semantics are identical to the semantics of 'jpeg' described
below. *"jpeg"* can only be used for images of type byte and int1
with up to four channels.

The domain (region) of each image object can be saved in compressed form via
*"mask"* (default setting) or as an additional alpha channel via
*"alpha"*. The domain is only stored if it does not comprise the full
image. *"jpeg"* and *"alpha"* cannot be used together because
owing to the lossy compression of JPEG the domain of the image cannot be
reconstructed correctly. The different options can be accumulated by
appending them separated by a space character.

Examples:

|  |  |
| --- | --- |
| *"tiff deflate 9"*: | Adobe deflate compression, |
|  | the domain is stored as a mask image if necessary |
| *"tiff jpeg 90"*: | JPEG compression with high quality, |
|  | the domain is stored as a mask image if necessary |
| *"tiff lzw alpha"*: | LZW compression, |
|  | the domain is stored as an alpha channel if necessary |
| *"tiff"* or *"tiff none"*: | no compression, |
|  | the domain is stored as a mask image if necessary |

*Attention:* Note that *"bigtiff"* denotes TIFF files that
can be larger than 4 GB, while *"tiff"* denotes TIFF files that are
limited to 4 GB. The file size depends on the image size and the selected
compression. Therefore, *"bigtiff"* should be selected if there is
a possibility that the compressed file will grow to more than 4 GB.

### 'bmp': Windows-BMP format, file extension *.bmp

*Restriction:*

- This format can only store images with one channel (gray value image)
  or three channels (RGB image).
- Only images with the pixel type byte are supported
  for this file format.

### 'jpeg': JPEG format (lossy compression), file extension *.jpg

Together with the format string the quality value determining the compression
rate can be provided, e.g., 'jpeg 30'.

*Restriction:*

- This format can only store images with one channel (gray value image)
  or three channels (RGB image).
- Only images with the pixel type byte are supported
  for this file format.

*Attention:* Images stored for being processed later should not be
stored in this format due to the loss of information during compression.

### 'jp2': JPEG-2000 format (lossless and lossy compression), file extension *.jp2

The format string can contain additional parameters in the form
*"jp2 [rate] [mode] [w,h] r[num]"*. All parameters except
*"jp2"* are optional.

- *"[rate]"* is the desired compression rate, corresponding to the
  ratio of the size of the compressed image to the uncompressed image in
  percent. Valid values are in the range [0..100]. Since lossless JPEG-2000
  compression already reduces the file size significantly, only smaller values
  (typically smaller than 50) influence the file size. If no value, *0*
  or *100* is given for the compression rate, the image is written using
  lossless compression.
- *"[mode]"* selects the type of discrete wavelet transform to use
  to compress the image. Possible values are *"int"*, which selects a
  reversible 5/3 transform, and *"real"*, which selects an irreversible
  9/7 transform. If the mode is not provided, *"int"* will be used if
  the compression is lossless or the image has a reduced domain, and
  *"real"* otherwise.
- *"[w,h]"* sets the tile width and tile height to use when writing
  the image. If no tile size is provided, the image is stored as a single tile.
  Note that tiling the image into multiple tiles reduces the amount of memory
  required by `WriteImage` and [`ReadImage`](read_image.md).
- *"r[num]"* sets the number of resolutions to save the image in.
  The number must be in the range [1..33]. A value of *1* saves the
  image at full resolution only. If no value is given for the number of
  resolutions to save, *6* is used by default. `WriteImage` will
  only save as many resolutions as are supported by the selected tile size.

Example:

|  |  |
| --- | --- |
| *"jp2 40 real 512,512 r6"*: | Compression rate 40%, 9/7 DWT, tile size 512x512, six resolutions |

The image can contain an arbitrary number of channels. Possible types are
byte, cyclic, direction, int1, uint2, int2, and int4. In the case of int4 it
is only possible to store images with less or equal to 24 bits precision
(otherwise an exception is raised). If the image contains a direction channel,
the image will be written with lossless compression regardless of the supplied
compression parameters. If an image with a reduced domain is written, the
region is stored as 1-bit alpha channel.

*Restriction:* The maximal supported image size (width x height)
for JPEG-2000 is $2^{31}-1$ also in HALCON-XL.

*Attention:* Note that the JPEG-2000 encoding of an image requires
a lot of memory. For large images, it is therefore recommended to either save
the image in multiple tiles or to use a different format (e.g.,
*"tiff"*).

*Attention:* Compression parameters apply globally to all channels of
the image, including the 1-bit alpha channel that is stored if the image has
a reduced domain. If you do not want compression artifacts in the alpha
channel, you must save the domain separately from the image data.

### 'jpegxr': JPEG-XR format (lossless and lossy compression), file extension *.jxr

Together with the format string the quality value determining the compression
rate can be provided, e.g., *"jpegxr 30"* (use *"jpegxr 100"*
or *"jpegxr"* for lossless encoding).
Image object tuples with an arbitrary number of image
objects can be written. In the case of int4 and real images, the numeric
range is compressed to 24 bit accuracy. Note that this may induce loss
regardless of the quality setting. If an image with a reduced domain is written,
the region is stored without loss as 1-bit alpha channel. Complex images,
vector fields and regular images with two gray value channels are padded with
an empty third channel to be compliant with the standard.

*Restriction:*

- This format cannot be written in parallel.
- Images can have up to 8 channels.
- All HALCON pixel types except int8 are supported.

*Attention:* Note that you need to have write permission in your
current working directory in order to save an image in JPEG-XR format,
regardless of the target directory.

### 'png': PNG format (lossless compression), file extension *.png

Together with the format string, a compression level between 0 and 9 can be
specified, where 0 corresponds to no compression and 9 to the best possible
compression. Alternatively, the compression can be selected with the
following strings: *"best"*, *"fastest"*, and *"none"*.
Hence, examples for correct parameters are *"png"*, *"png 7"*,
and *"png none"*.

Images of type byte and uint2 can be stored in PNG files. If an image with a
reduced domain is written, the region is stored as the alpha channel, where
the points within the domain are stored as the maximum gray value of the
image type and the points outside the domain are stored as the gray value 0.
If an image with a full domain is written, no alpha channel is stored.

*Restriction:*

- This format can only store images with one channel
  (gray value image) or three channels (RGB image).
- The maximal supported image size (width x height)
  for PNG is $2^{31}-1$ also in HALCON-XL.

### 'hobj': HALCON Iconic Object (HOBJ), file extension *.hobj

All types of HALCON images are supported. See [`WriteObject`](write_object.md) for more
information about the HOBJ format.

### 'ima': HALCON format, file extension *.ima and *.exp

This file format is now legacy and the HOBJ format should be used instead.
The data is written in binary form line by line (without header or carriage
return). The size of the image and the pixel type are stored in the
description file ”*`fileName`*.exp”. All HALCON pixel types except
*"complex"* and *"vector_field"* can be written.

*Restriction:* This format can only store images with one
channel (gray value image).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Input images.

**`format`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Graphic format.

Default:
"tiff"

Suggested values:
"tiff", "tiff mask", "tiff alpha", "tiff deflate 9", "tiff deflate 9 alpha", "tiff jpeg 90", "tiff lzw", "tiff lzw alpha ", "tiff packbits", "bigtiff", "bigtiff mask", "bigtiff alpha", "bigtiff deflate 9", "bigtiff deflate 9 alpha", "bigtiff jpeg 90", "bigtiff lzw", "bigtiff lzw alpha ", "bigtiff packbits", "bmp", "jpeg", "jpeg 100", "jpeg 80", "jpeg 60", "jpeg 40", "jpeg 20", "jp2", "jp2 50", "jp2 40", "jp2 30", "jp2 20", "jpegxr", "jpegxr 50", "jpegxr 40", "jpegxr 30", "jpegxr 20", "png", "png best", "png fastest", "png none", "ima", "hobj"

**`fillColor`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Fill gray value for pixels not belonging
to the image domain (region).

Default:
0

Suggested values:
-1, 0, 255, 65280, 16711680

**`fileName`** (input_control)  filename.write(-array) `→` [HTuple](HTuple.md) (*string*)

Name of image file.

File extension:
.`hobj`, .`ima`, .`tif`, .`tiff`, .`bmp`, .`jpg`, .`jpeg`, .`jp2`, .`jxr`, .`png`

## Result

If the parameter values are correct the operator `WriteImage`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`ReadImage`

## Module

Foundation
