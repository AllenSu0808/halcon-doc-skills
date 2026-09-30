# ReadRegion (Operator)

## Name

`ReadRegion` — Read binary images or HALCON regions.

## Signature

`static void HOperatorSet.ReadRegion(out HObject region, HTuple fileName)`

`void HRegion.ReadRegion(string fileName)`

## Description

The operator `ReadRegion` reads regions from a binary file.

The following formats are currently supported:

- **HALCON Iconic Object (HOBJ):** —

  File format for iconic HALCON objects. The HOBJ file must contain
  *only* regions to be readable by `ReadRegion`. If other
  objects (e.g., images or XLDs) are stored in the file,
  an exception is raised. In this case [`ReadObject`](read_object.md) can
  be used to read the corresponding HOBJ file.
  The HOBJ format is the default file format for regions.
  Therefore, the extension `'.hobj'` does not have to
  be specified when reading or writing the file. See
  [`WriteObject`](write_object.md) for more information about the HOBJ format.
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
to the operator [`ReadImage`](read_image.md).

## Attention

The clipping based on the current image format is set via the
operator `set_system('clip_region',<'true'/'false'>)`.
Consequently, if no image of sufficient size has been created before
the call to `ReadRegion`,
`set_system('clip_region','false')` should be called before
calling `ReadRegion` to ensure that the region is not being
clipped.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Read region.

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the region to be read.

File extension:
.`hobj`, .`reg`, .`tif`, .`tiff`, .`png`, .`bmp`

## Example (HDevelop)

```
* Reading of regions and giving them gray values.
  read_image(Img,'ima_test')
  read_region(Regs,'reg_test')
  reduce_domain(Img,Regs,Res)
```

## Result

If the parameter values are correct the operator `ReadRegion`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`ReadImage`

## Possible Successors

`ReduceDomain`,
`DispRegion`

## See also

`WriteRegion`,
`ReadImage`,
`WriteObject`

## Module

Foundation
