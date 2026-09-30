# gen_measure_arc (Operator)

## Name

`gen_measure_arc` — Prepare the extraction of straight edges perpendicular to an annular arc.

## Signature

`gen_measure_arc( : : CenterRow, CenterCol, Radius, AngleStart, AngleExtent, AnnulusRadius, Width, Height, Interpolation : MeasureHandle)`

## Description

`gen_measure_arc` prepares the extraction of *straight*
edges which lie *perpendicular* to an annular arc. Here,
annular arc denotes a circular arc with an associated width. The
center of the arc is passed in the parameters *`CenterRow`* and
*`CenterCol`*, its radius in *`Radius`*, the starting
angle in *`AngleStart`*, and its angular extent relative to the
starting angle in *`AngleExtent`*. If *`AngleExtent`* >
0, an arc with counterclockwise orientation is generated, otherwise
an arc with clockwise orientation. The radius of the annular arc,
i.e., half its width, is determined by *`AnnulusRadius`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The edge extraction algorithm is described in the documentation of
the operator [`measure_pos`](measure_pos.md). As discussed there, different
types of interpolation can be used for the calculation of the
one-dimensional gray value profile. For *`Interpolation`* =
*'nearest_neighbor'*, the gray values in the measurement are
obtained from the gray values of the closest pixel, i.e., by
constant interpolation. For *`Interpolation`* =
*'bilinear'*, bilinear interpolation is used, while for
*`Interpolation`* = *'bicubic'*, bicubic interpolation
is used.

To perform the actual measurement at optimal speed, all computations that can
be used for multiple measurements are already performed in the operator
`gen_measure_arc`. For this, an optimized data structure, a so-called
measure object, is constructed and returned in *`MeasureHandle`*. The
size of the images in which measurements will be performed must be specified
in the parameters *`Width`* and *`Height`*.

The system parameter *'int_zooming'* (see [`set_system`](set_system.md))
affects the accuracy and speed of the calculations used to construct
the measure object. If *'int_zooming'* is set to
*'true'*, the internal calculations are performed using fixed
point arithmetic, leading to much shorter execution times. However,
the geometric accuracy is slightly lower in this mode. If
*'int_zooming'* is set to *'false'*, the internal
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

**`CenterRow`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the center of the arc.

Default:
100.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
CenterRow` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`CenterCol`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the center of the arc.

Default:
100.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`0.0
≤
CenterCol` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Radius`** (input_control)  number `→`  (real / integer)

Radius of the arc.

Default:
50.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`Radius` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`AnnulusRadius <= Radius`

**`AngleStart`** (input_control)  angle.rad `→`  (real / integer)

Start angle of the arc in radians.

Default:
0.0

Suggested values:
-3.14159, -2.35619, -1.57080, -0.78540, 0.0, 0.78540, 1.57080, 2.35619, 3.14159

Value range:
`-3.14159
≤
AngleStart
≤
3.14159` (lin)

Minimum increment:
0.03142

Recommended increment:
0.31416

**`AngleExtent`** (input_control)  angle.rad `→`  (real / integer)

Angular extent of the arc in radians.

Default:
6.28318

Suggested values:
-6.28318, -5.49779, -4.71239, -3.92699, -3.14159, -2.35619, -1.57080, -0.78540, 0.78540, 1.57080, 2.35619, 3.14159, 3.92699, 4.71239, 5.49779, 6.28318

Value range:
`-6.28318
≤
AngleExtent
≤
6.28318` (lin)

Minimum increment:
0.03142

Recommended increment:
0.31416

**`AnnulusRadius`** (input_control)  number `→`  (real / integer)

Radius (half width) of the annulus.

Default:
10.0

Suggested values:
10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 400.0, 500.0

Value range:
`AnnulusRadius` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

Restriction:
`AnnulusRadius > 0`

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the image to be processed subsequently.

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768

Value range:
`0
≤
Width` (lin)

Minimum increment:
1

Recommended increment:
16

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the image to be processed subsequently.

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576

Value range:
`0
≤
Height` (lin)

Minimum increment:
1

Recommended increment:
16

**`Interpolation`** (input_control)  string `→`  (string)

Type of interpolation to be used.

Default:
'nearest_neighbor'

List of values:
'bicubic', 'bilinear', 'nearest_neighbor'

**`MeasureHandle`** (output_control)  measure `→`  (handle)

Measure object handle.

## Result

If the parameter values are correct, the operator
`gen_measure_arc` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`draw_circle`

## Possible Successors

`measure_pos`,
`measure_pairs`,
`fuzzy_measure_pos`,
`fuzzy_measure_pairs`,
`fuzzy_measure_pairing`

## Alternatives

`edges_sub_pix`

## See also

`gen_measure_rectangle2`

## Module

1D Metrology
