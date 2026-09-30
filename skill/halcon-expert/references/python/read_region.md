# read_region (Operator)

## Name

`read_region` — Read binary images or HALCON regions.

## Signature

`def read_region(file_name: str) -> HObject`

## Description

The operator `read_region` reads regions from a binary file.

The following formats are currently supported:

- **HALCON Iconic Object (HOBJ):** —

  File format for iconic HALCON objects. The HOBJ file must contain
  *only* regions to be readable by `read_region`. If other
  objects (e.g., images or XLDs) are stored in the file,
  an exception is raised. In this case [`read_object`](read_object.md) can
  be used to read the corresponding HOBJ file.
  The HOBJ format is the default file format for regions.
  Therefore, the extension `'.hobj'` does not have to
  be specified when reading or writing the file. See
  [`write_object`](write_object.md) for more information about the HOBJ format.
- **HALCON regions:** —

  File format for HALCON regions.
  This file format supports multiple regions in a single file.
  The file extension is `'.reg'`. This format is now legacy and the
  HOBJ format should be used instead.
- **Tiff:** —

  Binary Tiff images with extension `'.tiff'` or
  `'.tif'`. A tiff image can contain any number of regions.
  The color white is used as foreground.
- **PNG:** —

  Binary PNG images with extension `'.png'`. The result is
  always *one* region. The color white is used as foreground.
- **BMP:** —

  Binary Windows bitmap images with extension `'.bmp'`.
  The result is always *one* region. The color white is used as
  foreground.

A search path (`'image_dir'`) can be defined analogous
to the operator [`read_image`](read_image.md).

## Attention

The clipping based on the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.
Consequently, if no image of sufficient size has been created before
the call to `read_region`,
`set_system('clip_region','false')` should be called before
calling `read_region` to ensure that the region is not being
clipped.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region(-array) `→` HObject

Read region.

**`file_name`** (input_control)  filename.read `→` str

Name of the region to be read.

File extension:
.`hobj`, .`reg`, .`tif`, .`tiff`, .`png`, .`bmp`

## Result

If the parameter values are correct the operator `read_region`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`reduce_domain`,
`disp_region`

## See also

`write_region`,
`read_image`,
`write_object`

## Module

Foundation
