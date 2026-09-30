# GenMeasureRectangle2 (Operator)

## Name

`GenMeasureRectangle2` — Prepare the extraction of straight edges perpendicular to a rectangle.

## Signature

`static void HOperatorSet.GenMeasureRectangle2(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, HTuple width, HTuple height, HTuple interpolation, out HTuple measureHandle)`

`public HMeasure(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, int width, int height, string interpolation)`

`public HMeasure(double row, double column, double phi, double length1, double length2, int width, int height, string interpolation)`

`void HMeasure.GenMeasureRectangle2(HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, int width, int height, string interpolation)`

`void HMeasure.GenMeasureRectangle2(double row, double column, double phi, double length1, double length2, int width, int height, string interpolation)`

## Description

`GenMeasureRectangle2` prepares the extraction of
*straight* edges which lie *perpendicular* to the major
axis of a rectangle. The center of the rectangle is passed in the
parameters *`row`* and *`column`*, the direction of the
major axis of the rectangle in *`phi`*, and the length of the
two axes, i.e., half the diameter of the rectangle, in
*`length1`* and *`length2`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The edge extraction algorithm is described in the documentation of
the operator [`MeasurePos`](measure_pos.md). As discussed there, different
types of interpolation can be used for the calculation of the
one-dimensional gray value profile. For *`interpolation`* =
*"nearest_neighbor"*, the gray values in the measurement are
obtained from the gray values of the closest pixel, i.e., by
constant interpolation. For *`interpolation`* =
*"bilinear"*, bilinear interpolation is used, while for
*`interpolation`* = *"bicubic"*, bicubic interpolation
is used.

To perform the actual measurement at optimal speed, all computations that can
be used for multiple measurements are already performed in the operator
`GenMeasureRectangle2`. For this, an optimized data structure, a
so-called measure object, is constructed and returned in
*`measureHandle`*. The size of the images in which measurements will be
performed must be specified in the parameters *`width`* and
*`height`*.

The system parameter *"int_zooming"* (see [`SetSystem`](set_system.md))
affects the accuracy and speed of the calculations used to construct
the measure object. If *"int_zooming"* is set to
*"true"*, the internal calculations are performed using fixed
point arithmetic, leading to much shorter execution times. However,
the geometric accuracy is slightly lower in this mode. If
*"int_zooming"* is set to *"false"*, the internal
calculations are performed using floating point arithmetic, leading
to the maximum geometric accuracy, but also to significantly
increased execution times.

## Attention

Note that when using bilinear or bicubic interpolation, not only the
measurement rectangle but additionally the margin around the
rectangle must fit into the image. The width of the margin (in all
four directions) must be at least one pixel for bilinear
interpolation and two pixels for bicubic interpolation. For
projection lines that do not fulfill this condition, no gray value
is computed. Thus, no edge can be extracted at these positions.

Please also note that the center coordinates of the rectangle are rounded
internally, so that the center lies on the pixel grid.
This is done to ensure consistency.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`row`** (input_control)  rectangle2.center.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the rectangle.

Default:
300.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
row
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`column`** (input_control)  rectangle2.center.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the rectangle.

Default:
200.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
column
≤
511.0` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`phi`** (input_control)  rectangle2.angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Angle of longitudinal axis of the rectangle to
horizontal (radians).

Default:
0.0

Suggested values:
-1.178097, -0.785398, -0.392699, 0.0, 0.392699, 0.785398, 1.178097

Value range:
`phi` (lin)

Minimum increment:
0.001

Recommended increment:
0.1

**`length1`** (input_control)  rectangle2.hwidth `→` [HTuple](HTuple.md) (*double* / int / long)

Half width of the rectangle.

Default:
100.0

Suggested values:
3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0, 300.0, 500.0

Value range:
`1.0
≤
length1` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`length2`** (input_control)  rectangle2.hheight `→` [HTuple](HTuple.md) (*double* / int / long)

Half height of the rectangle.

Default:
20.0

Suggested values:
1.0, 2.0, 3.0, 5.0, 10.0, 15.0, 20.0, 50.0, 100.0, 200.0

Value range:
`0.0
≤
length2` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the image to be processed subsequently.

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768

Value range:
`0
≤
width` (lin)

Minimum increment:
1

Recommended increment:
16

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the image to be processed subsequently.

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576

Value range:
`0
≤
height` (lin)

Minimum increment:
1

Recommended increment:
16

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of interpolation to be used.

Default:
"nearest_neighbor"

List of values:
"bicubic", "bilinear", "nearest_neighbor"

**`measureHandle`** (output_control)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

## Result

If the parameter values are correct the operator
`GenMeasureRectangle2` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`DrawRectangle2`

## Possible Successors

`MeasurePos`,
`MeasurePairs`,
`FuzzyMeasurePos`,
`FuzzyMeasurePairs`,
`FuzzyMeasurePairing`,
`MeasureThresh`

## Alternatives

`EdgesSubPix`

## See also

`GenMeasureArc`

## Module

1D Metrology
