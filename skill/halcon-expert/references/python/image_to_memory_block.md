# image_to_memory_block (Operator)

## Name

`image_to_memory_block` — Write an image to a memory block in various graphic formats.

## Signature

`def image_to_memory_block(image: HObject, format: str, fill_color: Union[int, float]) -> HHandle`

## Description

The operator `image_to_memory_block` saves the input image
*`image`* to the memory block *`memory_block_handle`* in the format
*`format`*. If the domain (region) cannot be saved in the specified
*`format`* (this is the case for 'jpeg'), all pixels outside the region
receive the color defined by *`fill_color`*. For gray value images a value
between *0* (black) and *255* (white) must be passed. For RGB
color images the RGB values can be passed directly as a hexadecimal value:
e.g., *0xffff00* for a yellow background (red=255, green=255, blue=0).

The following formats can be set in *`format`*:

- **'jpeg': JPEG format (lossy compression), file extension *.jpg** —

  This format can only store images with one channel (gray value image) or three
  channels (RGB image).

  Only images with the pixel type byte are supported for this file format.

  Together with the format string the quality value determining the compression
  rate can be provided. Large values (maximum 100) create a large memory block
  with high image quality. Small values significantly decrease the image quality
  and the size of the memory block.

  *Possible values:* *"jpeg"*, *"jpeg 30"*,
  *"jpeg 60"*.

  *Attention:* Images stored for being processed later should not be
  stored in this format due to the loss of information during compression.
- **'png': PNG format (lossless compression), file extension *.png** —

  This format can only store images with one channel (gray value image) or three
  channels (RGB image). The maximal supported image size (width x height) for
  PNG is $2^{31}-1$, also in HALCON XL.

  Images of type byte and uint2 can be stored in PNG format.

  Together with the format string, a compression level between 0 and 9 can be
  specified, where 0 corresponds to no compression and 9 to the best possible
  compression. Alternatively, the compression can be selected by using string
  constants.

  *Possible values:* *"png"*, *"png 7"*,
  *"png none"*, *"png best"*, *"png fastest"*.

  If an image with a reduced domain is written, the region is stored as the
  alpha channel, where the points within the domain are stored as the maximum
  gray value of the image type and the points outside the domain are stored as
  the gray value 0. If an image with a full domain is written, no alpha channel
  is stored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Input image.

**`format`** (input_control)  string `→` str

Graphic format.

Default:
"jpeg"

Suggested values:
"jpeg", "png"

**`fill_color`** (input_control)  number `→` Union[int, float]

Gray value for pixels not belonging to the image domain
(region).

Default:
0

Suggested values:
-1, 0, 255, 65280, 16711680

**`memory_block_handle`** (output_control)  memory_block `→` HHandle

Memory block handle.

## Result

If the parameter values are correct the operator `image_to_memory_block`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`get_memory_block_ptr`,
`write_memory_block`,
`serialize_tuple`

## See also

`memory_block_to_image`

## Module

Foundation
