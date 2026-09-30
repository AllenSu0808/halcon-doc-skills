# WritePolygonXldDxf (Operator)

## Name

`WritePolygonXldDxf` — Write XLD polygons to a file in DXF format.

## Signature

`static void HOperatorSet.WritePolygonXldDxf(HObject polygons, HTuple fileName)`

`void HXLDPoly.WritePolygonXldDxf(string fileName)`

## Description

`WritePolygonXldDxf` writes the XLD polygons
*`polygons`* to the file *`fileName`* in DXF format.
If no absolute path is given in
*`fileName`* the output file is created in the current
directory of the HALCON process.

`WritePolygonXldDxf` writes the file according to the
DXF version AC1009 (AutoCAD Release 12). Each polygon is stored
as a POLYLINE.

The operator [`ReadPolygonXldDxf`](read_polygon_xld_dxf.md) can be used to read the
XLD polygon.

## Attention

The XLD contours that are possibly referenced by *`polygons`*
are not stored in the DXF file. Therefore, when the polygons are
read again using [`ReadPolygonXldDxf`](read_polygon_xld_dxf.md), this information
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

Name of the DXF file.

File extension:
.`dxf`

## Result

If the parameters are correct and the file could be written the
operator `WritePolygonXldDxf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.

## Possible Predecessors

`GenPolygonsXld`

## See also

`ReadPolygonXldDxf`,
`WriteContourXldDxf`

## Module

Foundation
