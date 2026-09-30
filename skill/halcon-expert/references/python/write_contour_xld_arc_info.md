# write_contour_xld_arc_info (Operator)

## Name

`write_contour_xld_arc_info` — Write XLD contours to a file in ARC/INFO generate format.

## Signature

`def write_contour_xld_arc_info(contours: HObject, file_name: str) -> None`

## Description

`write_contour_xld_arc_info` writes the XLD contours
*`contours`* to an ARC/INFO generate format file with name
*`file_name`*. If no absolute path is given in
*`file_name`*, the output file is created in the current
directory of the HALCON process. The contours must have been
transformed to the world coordinate system with
[`affine_trans_contour_xld`](affine_trans_contour_xld.md) beforehand. The necessary
transformation can be read from an ARC/INFO world file with
[`read_world_file`](read_world_file.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

XLD contours to be written.

**`file_name`** (input_control)  filename.write `→` str

Name of the ARC/INFO file.

## Example (HDevelop)

```
* Read transformation and image
read_world_file ('image.tfw', WorldTransformation)
read_image (Image, 'image.tif')
* Segment image
* ...
* Write result
affine_trans_contour_xld (Contours, ContoursWorld, WorldTransformation)
write_contour_xld_arc_info (ContoursWorld, 'result.gen')
```

## Result

If the parameters are correct and the file could be written, the
operator `write_contour_xld_arc_info` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`affine_trans_contour_xld`

## See also

`read_world_file`,
`read_contour_xld_arc_info`,
`write_polygon_xld_arc_info`

## Module

Foundation
