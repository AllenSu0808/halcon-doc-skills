# write_polygon_xld_arc_info (Operator)

## Name

`write_polygon_xld_arc_info` — Write XLD polygons to a file in ARC/INFO generate format.

## Signature

`def write_polygon_xld_arc_info(polygons: HObject, file_name: str) -> None`

## Description

`write_polygon_xld_arc_info` writes the XLD polygons
*`polygons`* to an ARC/INFO generate format file with name
*`file_name`*. If no absolute path is given in
*`file_name`*, the output file is created in the current
directory of the HALCON process. The polygons must have been
transformed to the world coordinate system with
[`affine_trans_polygon_xld`](affine_trans_polygon_xld.md) beforehand. The necessary
transformation can be read from an ARC/INFO world file with
[`read_world_file`](read_world_file.md).

## Attention

The XLD contours that are possibly referenced by *`polygons`*
are not stored in the ARC/INFO file, since this is not possible with
the ARC/INFO generate file format. Therefore, when the polygons are
read again using [`read_polygon_xld_arc_info`](read_polygon_xld_arc_info.md), this information
is lost, and no references to contours are generated for the
polygons. Hence, operators that access the contours associated with
a polygon, e.g., [`split_contours_xld`](split_contours_xld.md) will not work
correctly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygons`** (input_object)  xld_poly(-array) `→` HObject

XLD polygons to be written.

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
affine_trans_polygon_xld (Polygons, PolygonsWorld, WorldTransformation)
write_polygon_xld_arc_info (PolygonsWorld, 'result.gen')
```

## Result

If the parameters are correct and the file could be written, the
operator `write_polygon_xld_arc_info` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`affine_trans_polygon_xld`

## See also

`read_world_file`,
`read_polygon_xld_arc_info`,
`write_contour_xld_arc_info`

## Module

Foundation
