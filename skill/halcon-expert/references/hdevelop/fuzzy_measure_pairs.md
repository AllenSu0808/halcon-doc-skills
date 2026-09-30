# fuzzy_measure_pairs (Operator)

## Name

`fuzzy_measure_pairs` — Extract straight edge pairs perpendicular to a rectangle or an annular arc.

## Signature

`fuzzy_measure_pairs(Image : : MeasureHandle, Sigma, AmpThresh, FuzzyThresh, Transition : RowEdgeFirst, ColumnEdgeFirst, AmplitudeFirst, RowEdgeSecond, ColumnEdgeSecond, AmplitudeSecond, RowEdgeCenter, ColumnEdgeCenter, FuzzyScore, IntraDistance, InterDistance)`

## Description

`fuzzy_measure_pairs` serves to extract *straight* edge
pairs which lie *perpendicular* to the major axis of a
rectangle or an annular arc. In addition to [`measure_pairs`](measure_pairs.md) it uses
fuzzy functions to evaluate and select the edge pairs.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The extraction algorithm of `fuzzy_measure_pairs`
is identical to [`fuzzy_measure_pos`](fuzzy_measure_pos.md). In
addition, neighboring edges are grouped to pairs. To extract pairs that
intersect or include each other, use [`fuzzy_measure_pairing`](fuzzy_measure_pairing.md).

If *`Transition`* =
*'positive'*, the edge points with a dark-to-light transition in the
direction of the major axis of the rectangle or annular arc are returned in
*`RowEdgeFirst`* and *`ColumnEdgeFirst`*. In this case, the
corresponding edges with a light-to-dark transition are returned in
*`RowEdgeSecond`* and *`ColumnEdgeSecond`*. If *`Transition`*
= *'negative'*, the behavior is exactly opposite. If
*`Transition`* = *'all'*, the first detected edge defines the
transition for *`RowEdgeFirst`* and *`ColumnEdgeFirst`*. I.e.,
dependent on the positioning of the measure object, edge pairs with a
light-dark-light transition or edge pairs with a dark-light-dark transition
are returned. This is suited, e.g., to measure objects with different
brightness relative to the background.

Having extracted subpixel edge locations, the edges are paired. The
pairing algorithm groups the edges such that
interleavings and inclusions of pairs are prohibited. The features
of an edge pair
are evaluated by a fuzzy function, which can be set by
[`set_fuzzy_measure`](set_fuzzy_measure.md) or [`set_fuzzy_measure_norm_pair`](set_fuzzy_measure_norm_pair.md).
Which edge pairs are selected can be
determined with the parameter *`FuzzyThresh`*, which constitutes a
threshold on the weight over all fuzzy sets, i.e., the geometric
mean of the weights of the defined fuzzy functions.

The selected edges are returned as single points, which lie on the
major axis of the rectangle or annular arc. The corresponding edge
amplitudes are
returned in *`AmplitudeFirst`* and *`AmplitudeSecond`*, the
fuzzy scores in *`FuzzyScore`*.
In addition, the distance between each edge pair is returned in
*`IntraDistance`* and the distance between consecutive edge
pairs is returned in *`InterDistance`*. Here, IntraDistance[i]
corresponds to the distance between EdgeFirst[i] and EdgeSecond[i],
while InterDistance[i] corresponds to the distance between
EdgeSecond[i] and EdgeFirst[i+1], i.e., the tuple
*`InterDistance`* contains one element less than the tuples of
the edge pairs.

## Attention

`fuzzy_measure_pairs` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle or annular arc are fulfilled. Thus, it
should not be used to extract edges from curved objects, for
example. Furthermore, the user should ensure that the rectangle or
a annular arc is as close to perpendicular as possible to the edges
in the image. Additionally, *`Sigma`* must not become larger
than approx. 0.5 * Length1 (for Length1 see
[`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `fuzzy_measure_pairs` ignores
the domain of *`Image`* for efficiency reasons. If certain
regions in the image should be excluded from the measurement a new
measure object with appropriately modified parameters should be
generated.

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

Sigma of Gaussian smoothing.

Default:
1.0

Suggested values:
0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0

Value range:
`0.4
≤
Sigma
≤
100` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`AmpThresh`** (input_control)  number `→`  (real)

Minimum edge amplitude.

Default:
30.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 90.0, 110.0

Value range:
`1
≤
AmpThresh
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
2

**`FuzzyThresh`** (input_control)  number `→`  (real)

Minimum fuzzy value.

Default:
0.5

Suggested values:
0.1, 0.3, 0.5, 0.7, 0.9

Value range:
`0.0
≤
FuzzyThresh
≤
1.0` (lin)

Recommended increment:
0.1

**`Transition`** (input_control)  string `→`  (string)

Select the first gray value transition of the edge pairs.

Default:
'all'

List of values:
'all', 'negative', 'positive'

**`RowEdgeFirst`** (output_control)  point.y-array `→`  (real)

Row coordinate of the first edge point.

**`ColumnEdgeFirst`** (output_control)  point.x-array `→`  (real)

Column coordinate of the first edge point.

**`AmplitudeFirst`** (output_control)  real-array `→`  (real)

Edge amplitude of the first edge (with sign).

**`RowEdgeSecond`** (output_control)  point.y-array `→`  (real)

Row coordinate of the second edge point.

**`ColumnEdgeSecond`** (output_control)  point.x-array `→`  (real)

Column coordinate of the second edge point.

**`AmplitudeSecond`** (output_control)  real-array `→`  (real)

Edge amplitude of the second edge (with sign).

**`RowEdgeCenter`** (output_control)  point.y-array `→`  (real)

Row coordinate of the center of the edge pair.

**`ColumnEdgeCenter`** (output_control)  point.x-array `→`  (real)

Column coordinate of the center of the edge pair.

**`FuzzyScore`** (output_control)  real-array `→`  (real)

Fuzzy evaluation of the edge pair.

**`IntraDistance`** (output_control)  real-array `→`  (real)

Distance between edges of an edge pair.

**`InterDistance`** (output_control)  real-array `→`  (real)

Distance between consecutive edge pairs.

## Result

If the parameter values are correct the operator
`fuzzy_measure_pairs` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`,
`gen_measure_arc`,
`set_fuzzy_measure`

## Possible Successors

`close_measure`

## Alternatives

`edges_sub_pix`,
`fuzzy_measure_pairing`,
`measure_pairs`

## See also

`fuzzy_measure_pos`,
`measure_pos`

## Module

1D Metrology
