# write_region (Operator)

## Name

`write_region` — Write regions to a file.

## Signature

`def write_region(region: HObject, file_name: str) -> None`

## Description

The operator `write_region` writes the regions in *`region`*
into a binary file. The regions can be written in the HALCON Iconic Object
format (HOBJ), as TIFF files or as HALCON region files. The
format is selected via the file name extension of *`file_name`*. If
no extension is specified or if the file extension is `'.hobj'`,
the regions are stored in the HOBJ format. If no extension is specified
in *`file_name`*, the extension `'.hobj'` will be appended.
See [`write_object`](write_object.md) for more information about the
HOBJ format. If the extension `'.tif'` or `'.tiff'` is
specified, the regions are stored as TIFF files. If the extension
`'.reg'` is specified, the regions are stored as a HALCON region file.
The HALCON region file format is now legacy and the file format HOBJ should
be used instead unless the files must be readable with HALCON versions older
than 12.0. Iconic object tuples with an arbitrary number of regions
can be written. The output data can be read via the operator
[`read_region`](read_region.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Region of the images which are returned.

**`file_name`** (input_control)  filename.write `→` str

Name of region file.

Default:
"region.hobj"

File extension:
.`hobj`, .`reg`, .`tif`, .`tiff`

## Result

If the parameter values are correct the operator
`write_region` returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception
handling is raised.

## Possible Predecessors

`read_image`,
`read_region`,
`read_object`,
`threshold`,
`regiongrowing`

## See also

`read_region`

## Module

Foundation
