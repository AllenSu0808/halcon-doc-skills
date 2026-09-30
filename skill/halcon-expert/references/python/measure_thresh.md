# measure_thresh (Operator)

## Name

`measure_thresh` — Extracting points with a particular gray value along a rectangle or an
annular arc.

## Signature

`def measure_thresh(image: HObject, measure_handle: HHandle, sigma: float, threshold: float, select: str) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

## Description

`measure_thresh` extracts points for which the gray value
within an one-dimensional gray value profile is equal to the specified
threshold *`threshold`*. The gray value profile is projected
onto the major axis of the measure rectangle which is passed with
the parameter *`measure_handle`*, so the threshold points
calculated within the gray value profile correspond to certain image
coordinates on the rectangle's major axis. These coordinates are
returned as the operator results in *`row_thresh`* and
*`column_thresh`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

If the gray value profile intersects the threshold line for several times,
the parameter *`select`* determines which values to return.
Possible settings are *"first"*, *"last"*,
*"first_last"* (first and last) or *"all"*. For the
last two cases *`distance`* returns the distances between
the calculated points.

The gray value profile is created by averaging the gray values along
all line segments, which are defined by the measure rectangle as follows:

1. The segments are perpendicular to the major axis of the rectangle,
2. they have an integer distance to the center of the rectangle,
3. the rectangle bounds the segments.

For every line segment, the average of the gray values of all points
with an integer distance to the major axis is calculated.
Due to translation and rotation of the measure rectangle with respect to
the image coordinates the input image *`image`* is in general
sampled at subpixel positions.

Since this involves some calculations which can be used repeatedly
in several projections, the operator [`gen_measure_rectangle2`](gen_measure_rectangle2.md)
is used to perform these calculations only once in advance. Here,
the measure object *`measure_handle`* is generated and different
interpolation schemes can be selected.

## Attention

`measure_thresh` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle are fulfilled. Thus, it should not be
used to extract edges from curved objects, for example.
Furthermore, the user should ensure that the rectangle is as close
to perpendicular as possible to the edges in the image. Additionally,
*`sigma`* must not become larger than approx. 0.5 * Length1
(for Length1 see [`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `measure_thresh` ignores the
domain of *`image`* for efficiency reasons. If certain regions
in the image should be excluded from the measurement a new measure
object with appropriately modified parameters should be generated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Input image.

**`measure_handle`** (input_control)  measure `→` HHandle

Measure object handle.

**`sigma`** (input_control)  number `→` float

Sigma of gaussian smoothing.

Default:
1.0

Suggested values:
0.0, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0

Value range:
`0.0
≤
sigma
≤
100` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`threshold`** (input_control)  number `→` float

Threshold.

Default:
128.0

Value range:
`0
≤
threshold
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
1

**`select`** (input_control)  string `→` str

Selection of points.

Default:
"all"

List of values:
"all", "first", "first_last", "last"

**`row_thresh`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of points with threshold value.

**`column_thresh`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of points with threshold value.

**`distance`** (output_control)  real-array `→` Sequence[float]

Distance between consecutive points.

## Result

If the parameter values are correct the operator `measure_thresh`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`

## Possible Successors

`close_measure`

## Alternatives

`measure_pos`,
`edges_sub_pix`,
`measure_pairs`

## Module

1D Metrology
