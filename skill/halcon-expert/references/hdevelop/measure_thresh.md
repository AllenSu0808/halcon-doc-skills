# measure_thresh (Operator)

## Name

`measure_thresh` — Extracting points with a particular gray value along a rectangle or an
annular arc.

## Signature

`measure_thresh(Image : : MeasureHandle, Sigma, Threshold, Select : RowThresh, ColumnThresh, Distance)`

## Description

`measure_thresh` extracts points for which the gray value
within an one-dimensional gray value profile is equal to the specified
threshold *`Threshold`*. The gray value profile is projected
onto the major axis of the measure rectangle which is passed with
the parameter *`MeasureHandle`*, so the threshold points
calculated within the gray value profile correspond to certain image
coordinates on the rectangle's major axis. These coordinates are
returned as the operator results in *`RowThresh`* and
*`ColumnThresh`*.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

If the gray value profile intersects the threshold line for several times,
the parameter *`Select`* determines which values to return.
Possible settings are *'first'*, *'last'*,
*'first_last'* (first and last) or *'all'*. For the
last two cases *`Distance`* returns the distances between
the calculated points.

The gray value profile is created by averaging the gray values along
all line segments, which are defined by the measure rectangle as follows:

1. The segments are perpendicular to the major axis of the rectangle,
2. they have an integer distance to the center of the rectangle,
3. the rectangle bounds the segments.

For every line segment, the average of the gray values of all points
with an integer distance to the major axis is calculated.
Due to translation and rotation of the measure rectangle with respect to
the image coordinates the input image *`Image`* is in general
sampled at subpixel positions.

Since this involves some calculations which can be used repeatedly
in several projections, the operator [`gen_measure_rectangle2`](gen_measure_rectangle2.md)
is used to perform these calculations only once in advance. Here,
the measure object *`MeasureHandle`* is generated and different
interpolation schemes can be selected.

## Attention

`measure_thresh` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle are fulfilled. Thus, it should not be
used to extract edges from curved objects, for example.
Furthermore, the user should ensure that the rectangle is as close
to perpendicular as possible to the edges in the image. Additionally,
*`Sigma`* must not become larger than approx. 0.5 * Length1
(for Length1 see [`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `measure_thresh` ignores the
domain of *`Image`* for efficiency reasons. If certain regions
in the image should be excluded from the measurement a new measure
object with appropriately modified parameters should be generated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2 / real)

Input image.

**`MeasureHandle`** (input_control)  measure `→`  (handle)

Measure object handle.

**`Sigma`** (input_control)  number `→`  (real)

Sigma of gaussian smoothing.

Default:
1.0

Suggested values:
0.0, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0

Value range:
`0.0
≤
Sigma
≤
100` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`Threshold`** (input_control)  number `→`  (real)

Threshold.

Default:
128.0

Value range:
`0
≤
Threshold
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
1

**`Select`** (input_control)  string `→`  (string)

Selection of points.

Default:
'all'

List of values:
'all', 'first', 'first_last', 'last'

**`RowThresh`** (output_control)  point.y-array `→`  (real)

Row coordinates of points with threshold value.

**`ColumnThresh`** (output_control)  point.x-array `→`  (real)

Column coordinates of points with threshold value.

**`Distance`** (output_control)  real-array `→`  (real)

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
