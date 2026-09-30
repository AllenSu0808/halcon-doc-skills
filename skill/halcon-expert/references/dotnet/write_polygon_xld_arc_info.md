# WritePolygonXldArcInfo (Operator)

## Name

`WritePolygonXldArcInfo` — Write XLD polygons to a file in ARC/INFO generate format.

## Signature

`static void HOperatorSet.WritePolygonXldArcInfo(HObject polygons, HTuple fileName)`

`void HXLDPoly.WritePolygonXldArcInfo(string fileName)`

## Description

`WritePolygonXldArcInfo` writes the XLD polygons
*`polygons`* to an ARC/INFO generate format file with name
*`fileName`*. If no absolute path is given in
*`fileName`*, the output file is created in the current
directory of the HALCON process. The polygons must have been
transformed to the world coordinate system with
[`AffineTransPolygonXld`](affine_trans_polygon_xld.md) beforehand. The necessary
transformation can be read from an ARC/INFO world file with
[`ReadWorldFile`](read_world_file.md).

## Attention

The XLD contours that are possibly referenced by *`polygons`*
are not stored in the ARC/INFO file, since this is not possible with
the ARC/INFO generate file format. Therefore, when the polygons are
read again using [`ReadPolygonXldArcInfo`](read_polygon_xld_arc_info.md), this information
is lost, and no references to contours are generated for the
polygons. Hence, operators that access the contours associated with
a polygon, e.g., [`SplitContoursXld`](split_contours_xld.md) will not work
correctly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`polygons`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

XLD polygons to be written.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

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
operator `WritePolygonXldArcInfo` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`AffineTransPolygonXld`

## See also

`ReadWorldFile`,
`ReadPolygonXldArcInfo`,
`WriteContourXldArcInfo`

## Module

Foundation
