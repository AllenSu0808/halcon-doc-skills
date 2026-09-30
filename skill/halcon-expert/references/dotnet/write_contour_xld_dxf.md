# WriteContourXldDxf (Operator)

## Name

`WriteContourXldDxf` — Write XLD contours to a file in DXF format.

## Signature

`static void HOperatorSet.WriteContourXldDxf(HObject contours, HTuple fileName)`

`void HXLDCont.WriteContourXldDxf(string fileName)`

## Description

`WriteContourXldDxf` writes the XLD contours
*`contours`* to the file *`fileName`* in DXF format.
If no absolute path is given in
*`fileName`* the output file is created in the current
directory of the HALCON process.

Besides the geometry of the *`contours`*,
all attributes and global attributes that are defined for the
*`contours`* are written to the file.

`WriteContourXldDxf` writes the file according to the
DXF version AC1009 (AutoCAD Release 12). Each contour is stored
as a POLYLINE. The attribute values are stored as extended data of
each VERTEX of the POLYLINE. The global attribute values are stored
as extended data of the POLYLINE. All attribute names
are also stored as extended data of the POLYLINE.

The operator [`ReadContourXldDxf`](read_contour_xld_dxf.md) can be used to read the
XLD contours together with their attributes.

Other applications that are able to read DXF files
only import the contour geometry, but they ignore the
attribute information.

**Description of the format of the extended data**

Each block of extended data starts with the following DXF group:

1001
HALCON

The attributes are written in the following format as
extended data of each VERTEX:

| DXF | Explanation |
| --- | --- |
| 1000 | Meaning |
| contour attributes |  |
| 1002 | Beginning of the value list |
| { |  |
| 1070 | Number of attributes (here: 3) |
| 3 |  |
| 1040 | Value of the first attribute |
| 5.00434303 |  |
| 1040 | Value of the second attribute |
| 126.8638916 |  |
| 1040 | Value of the third attribute |
| 4.99164152 |  |
| 1002 | End of the value list |
| } |  |

The global attributes are written in the following format as
extended data of each POLYLINE:

| DXF | Explanation |
| --- | --- |
| 1000 | Meaning |
| global contour attributes |  |
| 1002 | Beginning of the value list |
| { |  |
| 1070 | Number of global attributes (here: 5) |
| 5 |  |
| 1040 | Value of the first global attribute |
| 0.77951831 |  |
| 1040 | Value of the second global attribute |
| 0.62637949 |  |
| 1040 | Value of the third global attribute |
| 103.94314575 |  |
| 1040 | Value of the fourth global attribute |
| 0.21434096 |  |
| 1040 | Value of the fifth global attribute |
| 0.21921949 |  |
| 1002 | End of the value list |
| } |  |

The names of the attributes are written in the following format as
extended data of each POLYLINE:

| DXF | Explanation |
| --- | --- |
| 1000 | Meaning |
| names of contour attributes |  |
| 1002 | Beginning of the value list |
| { |  |
| 1070 | Number of attribute names (here: 3) |
| 3 |  |
| 1000 | Name of the first attribute |
| angle |  |
| 1000 | Name of the second attribute |
| response |  |
| 1000 | Name of the third attribute |
| edge_direction |  |
| 1002 | End of the value list |
| } |  |

The names of the global attributes are written in the following format as
extended data of each POLYLINE:

| DXF | Explanation |
| --- | --- |
| 1000 | Meaning |
| names of global contour attributes |  |
| 1002 | Beginning of the value list |
| { |  |
| 1070 | Number of global attribute names (here: 5) |
| 5 |  |
| 1000 | Name of the first global attribute |
| regr_norm_row |  |
| 1000 | Name of the second global attribute |
| regr_norm_col |  |
| 1000 | Name of the third global attribute |
| regr_dist |  |
| 1000 | Name of the fourth global attribute |
| regr_mean_dist |  |
| 1000 | Name of the fifth global attribute |
| regr_dev_dist |  |
| 1002 | End of the value list |
| } |  |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

XLD contours to be written.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the DXF file.

File extension:
.`dxf`

## Result

If the parameters are correct and the file could be written the
operator `WriteContourXldDxf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.

## Possible Predecessors

`EdgesSubPix`

## See also

`ReadContourXldDxf`,
`WritePolygonXldDxf`,
`QueryContourAttribsXld`,
`QueryContourGlobalAttribsXld`,
`GetContourAttribXld`,
`GetContourGlobalAttribXld`

## Module

Foundation
