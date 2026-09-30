# ReadContourXldDxf (Operator)

## Name

`ReadContourXldDxf` — Read XLD contours from a DXF file.

## Signature

`static void HOperatorSet.ReadContourXldDxf(out HObject contours, HTuple fileName, HTuple genParamName, HTuple genParamValue, out HTuple dxfStatus)`

`HTuple HXLDCont.ReadContourXldDxf(string fileName, HTuple genParamName, HTuple genParamValue)`

`string HXLDCont.ReadContourXldDxf(string fileName, string genParamName, double genParamValue)`

## Description

`ReadContourXldDxf` reads the contents of the DXF file
*`fileName`* (DXF version AC1009, AutoCAD Release 12) and
converts them to the XLD contours *`contours`*.
If no absolute path is given in
*`fileName`* the DXF file is searched in the current
directory of the HALCON process.

The output parameter *`dxfStatus`* contains information about
the number of contours that were read and, if necessary,
warnings that parts of the DXF file could not be interpreted.

The operator `ReadContourXldDxf` supports the following
DXF entities:

- POLYLINE

  - 2D curves made up of line segments
  - Closed 2D curves made up of line segments
- LWPOLYLINE
- LINE
- POINT
- CIRCLE
- ARC
- ELLIPSE
- SPLINE
- BLOCK
- INSERT

The x and y coordinates of the DXF entities are stored in the column
and row coordinates, respectively, of the XLD contours
*`contours`*. The z coordinates of the DXF entities are
ignored.

If the file has been created with the operator
[`WriteContourXldDxf`](write_contour_xld_dxf.md), all attributes and global attributes
that were originally defined for the XLD contours are read.
This means that `ReadContourXldDxf` supports all the extended
data written by the operator [`WriteContourXldDxf`](write_contour_xld_dxf.md).
The reading of these attributes can be switched off by setting
the generic parameter *"read_attributes"* to
*"false"*. Generic parameters are set by specifying the
parameter name(s) in *`genParamName`* and the corresponding
value(s) in *`genParamValue`*.

DXF entities of the type CIRCLE, ARC, ELLIPSE, and SPLINE
are approximated by XLD contours. The accuracy of this
approximation can be controlled with the two generic parameters
*"min_num_points"* and *"max_approx_error"*.
The parameter *"min_num_points"* defines the minimum
number of sampling points that are used for the approximation.
Note that the parameter *"min_num_points"* always refers to
the full circle or ellipse, respectively, even for ARCs or elliptical
arcs, i.e., if *"min_num_points"* is set to *50*
and a DXF entity of the type ARC is read that represents a semi-circle,
this semi-circle is approximated by at least 25 sampling points.
The parameter *"max_approx_error"* defines the maximum
deviation of the XLD contour from the ideal
circle or ellipse, respectively (unit: pixel).
For the determination of the accuracy of the approximation
both criteria are evaluated. Then, the criterion that leads
to the more accurate approximation is used.

Internally, the following default values are used for the generic
parameters:

- *"read_attributes"* = *"true"*
- *"min_num_points"* = *20*
- *"max_approx_error"* = *0.25*

To achieve a more accurate approximation, either the value for
*"min_num_points"* must be increased or the value for
*"max_approx_error"* must be decreased.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Read XLD contours.

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the DXF file.

File extension:
.`dxf`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be
adjusted for the DXF input.

Default:
[]

List of values:
"max_approx_error", "min_num_points", "read_attributes"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of the generic parameters that can be
adjusted for the DXF input.

Default:
[]

Suggested values:
"true", "false", 0.1, 0.25, 0.5, 1, 2, 5, 10, 20

**`dxfStatus`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Status information.

## Result

If the parameters are correct and the file could be read the
operator `ReadContourXldDxf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.

## Possible Predecessors

`WriteContourXldDxf`

## See also

`WriteContourXldDxf`,
`ReadPolygonXldDxf`,
`QueryContourAttribsXld`,
`QueryContourGlobalAttribsXld`,
`GetContourAttribXld`,
`GetContourGlobalAttribXld`

## Module

Foundation
