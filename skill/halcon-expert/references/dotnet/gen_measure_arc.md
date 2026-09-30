# GenMeasureArc (Operator)

## Name

`GenMeasureArc` — Prepare the extraction of straight edges perpendicular to an annular arc.

## Signature

`static void HOperatorSet.GenMeasureArc(HTuple centerRow, HTuple centerCol, HTuple radius, HTuple angleStart, HTuple angleExtent, HTuple annulusRadius, HTuple width, HTuple height, HTuple interpolation, out HTuple measureHandle)`

`public HMeasure(HTuple centerRow, HTuple centerCol, HTuple radius, HTuple angleStart, HTuple angleExtent, HTuple annulusRadius, int width, int height, string interpolation)`

`public HMeasure(double centerRow, double centerCol, double radius, double angleStart, double angleExtent, double annulusRadius, int width, int height, string interpolation)`

`void HMeasure.GenMeasureArc(HTuple centerRow, HTuple centerCol, HTuple radius, HTuple angleStart, HTuple angleExtent, HTuple annulusRadius, int width, int height, string interpolation)`

`void HMeasure.GenMeasureArc(double centerRow, double centerCol, double radius, double angleStart, double angleExtent, double annulusRadius, int width, int height, string interpolation)`

## Description

`GenMeasureArc` prepares the extraction of *straight*
edges which lie *perpendicular* to an annular arc. Here,
annular arc denotes a circular arc with an associated width. The
center of the arc is passed in the parameters *`centerRow`* and
*`centerCol`*, its radius in *`radius`*, the starting
angle in *`angleStart`*, and its angular extent relative to the
starting angle in *`angleExtent`*. If *`angleExtent`* >
0, an arc with counterclockwise orientation is generated, otherwise
an arc with clockwise orientation. The radius of the annular arc,
i.e., half its width, is determined by *`annulusRadius`*.

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
`GenMeasureArc`. For this, an optimized data structure, a so-called
measure object, is constructed and returned in *`measureHandle`*. The
size of the images in which measurements will be performed must be specified
in the parameters *`width`* and *`height`*.

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

Please also note that the center coordinates of the arc are rounded
internally, so that the center lies on the pixel grid.
This is done to ensure consistency.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`centerRow`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the arc.

Default:
100.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
centerRow` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`centerCol`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the arc.

Default:
100.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
centerCol` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`radius`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the arc.

Default:
50.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`radius` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`AnnulusRadius <= Radius`

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Start angle of the arc in radians.

Default:
0.0

Suggested values:
-3.14159, -2.35619, -1.57080, -0.78540, 0.0, 0.78540, 1.57080, 2.35619, 3.14159

Value range:
`-3.14159
≤
angleStart
≤
3.14159` (lin)

Minimum increment:
0.03142

Recommended increment:
0.31416

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Angular extent of the arc in radians.

Default:
6.28318

Suggested values:
-6.28318, -5.49779, -4.71239, -3.92699, -3.14159, -2.35619, -1.57080, -0.78540, 0.78540, 1.57080, 2.35619, 3.14159, 3.92699, 4.71239, 5.49779, 6.28318

Value range:
`-6.28318
≤
angleExtent
≤
6.28318` (lin)

Minimum increment:
0.03142

Recommended increment:
0.31416

**`annulusRadius`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Radius (half width) of the annulus.

Default:
10.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`annulusRadius` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`AnnulusRadius > 0`

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

If the parameter values are correct, the operator
`GenMeasureArc` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`DrawCircle`

## Possible Successors

`MeasurePos`,
`MeasurePairs`,
`FuzzyMeasurePos`,
`FuzzyMeasurePairs`,
`FuzzyMeasurePairing`

## Alternatives

`EdgesSubPix`

## See also

`GenMeasureRectangle2`

## Module

1D Metrology
