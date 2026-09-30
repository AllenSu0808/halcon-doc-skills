# FuzzyMeasurePairs (Operator)

## Name

`FuzzyMeasurePairs` — Extract straight edge pairs perpendicular to a rectangle or an annular arc.

## Signature

`static void HOperatorSet.FuzzyMeasurePairs(HObject image, HTuple measureHandle, HTuple sigma, HTuple ampThresh, HTuple fuzzyThresh, HTuple transition, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple rowEdgeCenter, out HTuple columnEdgeCenter, out HTuple fuzzyScore, out HTuple intraDistance, out HTuple interDistance)`

`void HMeasure.FuzzyMeasurePairs(HImage image, double sigma, double ampThresh, double fuzzyThresh, string transition, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple rowEdgeCenter, out HTuple columnEdgeCenter, out HTuple fuzzyScore, out HTuple intraDistance, out HTuple interDistance)`

`void HImage.FuzzyMeasurePairs(HMeasure measureHandle, double sigma, double ampThresh, double fuzzyThresh, string transition, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple rowEdgeCenter, out HTuple columnEdgeCenter, out HTuple fuzzyScore, out HTuple intraDistance, out HTuple interDistance)`

## Description

`FuzzyMeasurePairs` serves to extract *straight* edge
pairs which lie *perpendicular* to the major axis of a
rectangle or an annular arc. In addition to [`MeasurePairs`](measure_pairs.md) it uses
fuzzy functions to evaluate and select the edge pairs.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The extraction algorithm of `FuzzyMeasurePairs`
is identical to [`FuzzyMeasurePos`](fuzzy_measure_pos.md). In
addition, neighboring edges are grouped to pairs. To extract pairs that
intersect or include each other, use [`FuzzyMeasurePairing`](fuzzy_measure_pairing.md).

If *`transition`* =
*"positive"*, the edge points with a dark-to-light transition in the
direction of the major axis of the rectangle or annular arc are returned in
*`rowEdgeFirst`* and *`columnEdgeFirst`*. In this case, the
corresponding edges with a light-to-dark transition are returned in
*`rowEdgeSecond`* and *`columnEdgeSecond`*. If *`transition`*
= *"negative"*, the behavior is exactly opposite. If
*`transition`* = *"all"*, the first detected edge defines the
transition for *`rowEdgeFirst`* and *`columnEdgeFirst`*. I.e.,
dependent on the positioning of the measure object, edge pairs with a
light-dark-light transition or edge pairs with a dark-light-dark transition
are returned. This is suited, e.g., to measure objects with different
brightness relative to the background.

Having extracted subpixel edge locations, the edges are paired. The
pairing algorithm groups the edges such that
interleavings and inclusions of pairs are prohibited. The features
of an edge pair
are evaluated by a fuzzy function, which can be set by
[`SetFuzzyMeasure`](set_fuzzy_measure.md) or [`SetFuzzyMeasureNormPair`](set_fuzzy_measure_norm_pair.md).
Which edge pairs are selected can be
determined with the parameter *`fuzzyThresh`*, which constitutes a
threshold on the weight over all fuzzy sets, i.e., the geometric
mean of the weights of the defined fuzzy functions.

The selected edges are returned as single points, which lie on the
major axis of the rectangle or annular arc. The corresponding edge
amplitudes are
returned in *`amplitudeFirst`* and *`amplitudeSecond`*, the
fuzzy scores in *`fuzzyScore`*.
In addition, the distance between each edge pair is returned in
*`intraDistance`* and the distance between consecutive edge
pairs is returned in *`interDistance`*. Here, IntraDistance[i]
corresponds to the distance between EdgeFirst[i] and EdgeSecond[i],
while InterDistance[i] corresponds to the distance between
EdgeSecond[i] and EdgeFirst[i+1], i.e., the tuple
*`interDistance`* contains one element less than the tuples of
the edge pairs.

## Attention

`FuzzyMeasurePairs` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle or annular arc are fulfilled. Thus, it
should not be used to extract edges from curved objects, for
example. Furthermore, the user should ensure that the rectangle or
a annular arc is as close to perpendicular as possible to the edges
in the image. Additionally, *`sigma`* must not become larger
than approx. 0.5 * Length1 (for Length1 see
[`GenMeasureRectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `FuzzyMeasurePairs` ignores
the domain of *`image`* for efficiency reasons. If certain
regions in the image should be excluded from the measurement a new
measure object with appropriately modified parameters should be
generated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2 / real)

Input image.

**`measureHandle`** (input_control)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

**`sigma`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Sigma of Gaussian smoothing.

Default:
1.0

Suggested values:
0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0

Value range:
`0.4
≤
sigma
≤
100` (lin)

Minimum increment:
0.01

Recommended increment:
0.1

**`ampThresh`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum edge amplitude.

Default:
30.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 90.0, 110.0

Value range:
`1
≤
ampThresh
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
2

**`fuzzyThresh`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum fuzzy value.

Default:
0.5

Suggested values:
0.1, 0.3, 0.5, 0.7, 0.9

Value range:
`0.0
≤
fuzzyThresh
≤
1.0` (lin)

Recommended increment:
0.1

**`transition`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Select the first gray value transition of the edge pairs.

Default:
"all"

List of values:
"all", "negative", "positive"

**`rowEdgeFirst`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the first edge point.

**`columnEdgeFirst`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the first edge point.

**`amplitudeFirst`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Edge amplitude of the first edge (with sign).

**`rowEdgeSecond`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the second edge point.

**`columnEdgeSecond`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the second edge point.

**`amplitudeSecond`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Edge amplitude of the second edge (with sign).

**`rowEdgeCenter`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the edge pair.

**`columnEdgeCenter`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the edge pair.

**`fuzzyScore`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Fuzzy evaluation of the edge pair.

**`intraDistance`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Distance between edges of an edge pair.

**`interDistance`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Distance between consecutive edge pairs.

## Result

If the parameter values are correct the operator
`FuzzyMeasurePairs` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`,
`GenMeasureArc`,
`SetFuzzyMeasure`

## Possible Successors

`CloseMeasure`

## Alternatives

`EdgesSubPix`,
`FuzzyMeasurePairing`,
`MeasurePairs`

## See also

`FuzzyMeasurePos`,
`MeasurePos`

## Module

1D Metrology
