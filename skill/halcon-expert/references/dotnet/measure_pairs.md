# MeasurePairs (Operator)

## Name

`MeasurePairs` — Extract straight edge pairs perpendicular to a rectangle or annular arc.

## Signature

`static void HOperatorSet.MeasurePairs(HObject image, HTuple measureHandle, HTuple sigma, HTuple threshold, HTuple transition, HTuple select, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple intraDistance, out HTuple interDistance)`

`void HMeasure.MeasurePairs(HImage image, double sigma, double threshold, string transition, string select, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple intraDistance, out HTuple interDistance)`

`void HImage.MeasurePairs(HMeasure measureHandle, double sigma, double threshold, string transition, string select, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple intraDistance, out HTuple interDistance)`

## Description

`MeasurePairs` serves to extract *straight* edge pairs
which lie *perpendicular* to the major axis of a rectangle or
annular arc.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The extraction algorithm of `MeasurePairs`
is identical to [`MeasurePos`](measure_pos.md). In addition
the edges are grouped to pairs: If *`transition`* = *"positive"*,
the edge points with a dark-to-light transition in the direction of the major
axis of the rectangle are returned in *`rowEdgeFirst`* and
*`columnEdgeFirst`*. In this case, the corresponding edges with a
light-to-dark transition are returned in *`rowEdgeSecond`* and
*`columnEdgeSecond`*. If *`transition`* = *"negative"*, the
behavior is exactly opposite. If *`transition`* = *"all"*, the
first detected edge defines the transition for *`rowEdgeFirst`* and
*`columnEdgeFirst`*. I.e., dependent on the positioning of the measure
object, edge pairs with a light-dark-light transition or edge pairs with a
dark-light-dark transition are returned. This is suited, e.g., to measure
objects with different brightness relative to the background.

If more than one consecutive edge with
the same transition is found, the first one is used as a pair element. This
behavior may cause problems in applications in which the threshold
*`threshold`* cannot be selected high enough to suppress consecutive
edges of the same transition. For these applications, a second pairing mode
exists that only selects the respective strongest edges of a sequence of
consecutive rising and falling edges. This mode is selected by appending
*"_strongest"* to any of the above modes for *`transition`*,
e.g., *"negative_strongest"*. Finally, it is possible to select which
edge pairs are returned. If *`select`* is set to *"all"*, all
edge pairs are returned. If it is set to *"first"*, only the first of
the extracted edge pairs is returned, while it is set to *"last"*,
only the last one is returned.

The extracted edges are returned as single points which lie on the
major axis of the rectangle. The corresponding edge amplitudes are
returned in *`amplitudeFirst`* and *`amplitudeSecond`*.
In addition, the distance between each edge pair is returned in
*`intraDistance`* and the distance between consecutive edge
pairs is returned in *`interDistance`*. Here, IntraDistance[i]
corresponds to the distance between EdgeFirst[i] and EdgeSecond[i],
while InterDistance[i] corresponds to the distance between
EdgeSecond[i] and EdgeFirst[i+1], i.e., the tuple
*`interDistance`* contains one element less than the tuples
of the edge pairs.

## Attention

`MeasurePairs` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle are fulfilled. Thus, it should not be
used to extract edges from curved objects, for example.
Furthermore, the user should ensure that the rectangle is as close
to perpendicular as possible to the edges in the image. Additionally,
*`sigma`* must not become larger than approx. 0.5 * Length1
(for Length1 see [`GenMeasureRectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `MeasurePairs` ignores the
domain of *`image`* for efficiency reasons. If certain regions
in the image should be excluded from the measurement a new measure
object with appropriately modified parameters should be generated.

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

Sigma of gaussian smoothing.

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

**`threshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum edge amplitude.

Default:
30.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 90.0, 110.0

Value range:
`1
≤
threshold
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
2

**`transition`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of gray value transition that determines
how edges are grouped to edge pairs.

Default:
"all"

List of values:
"all", "all_strongest", "negative", "negative_strongest", "positive", "positive_strongest"

**`select`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Selection of edge pairs.

Default:
"all"

List of values:
"all", "first", "last"

**`rowEdgeFirst`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the first edge.

**`columnEdgeFirst`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the first edge.

**`amplitudeFirst`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Edge amplitude of the first edge (with sign).

**`rowEdgeSecond`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the second edge.

**`columnEdgeSecond`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the second
edge.

**`amplitudeSecond`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Edge amplitude of the second edge (with sign).

**`intraDistance`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Distance between edges of an edge pair.

**`interDistance`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Distance between consecutive edge pairs.

## Result

If the parameter values are correct the operator `MeasurePairs`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`

## Possible Successors

`CloseMeasure`

## Alternatives

`EdgesSubPix`,
`FuzzyMeasurePairs`,
`FuzzyMeasurePairing`

## See also

`MeasurePos`,
`FuzzyMeasurePos`

## Module

1D Metrology
