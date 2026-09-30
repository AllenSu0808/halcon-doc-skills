# write_polygon_xld_dxf (Operator)

## Name

`write_polygon_xld_dxf` — Write XLD polygons to a file in DXF format.

## Signature

`def write_polygon_xld_dxf(polygons: HObject, file_name: str) -> None`

## Description

`write_polygon_xld_dxf` writes the XLD polygons
*`polygons`* to the file *`file_name`* in DXF format.
If no absolute path is given in
*`file_name`* the output file is created in the current
directory of the HALCON process.

`write_polygon_xld_dxf` writes the file according to the
DXF version AC1009 (AutoCAD Release 12). Each polygon is stored
as a POLYLINE.

The operator [`read_polygon_xld_dxf`](read_polygon_xld_dxf.md) can be used to read the
XLD polygon.

## Attention

The XLD contours that are possibly referenced by *`polygons`*
are not stored in the DXF file. Therefore, when the polygons are
read again using [`read_polygon_xld_dxf`](read_polygon_xld_dxf.md), this information
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

Name of the DXF file.

File extension:
.`dxf`

## Result

If the parameters are correct and the file could be written the
operator `write_polygon_xld_dxf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.

## Possible Predecessors

`gen_polygons_xld`

## See also

`read_polygon_xld_dxf`,
`write_contour_xld_dxf`

## Module

Foundation
