# FuzzyMeasurePairing (Operator)

## Name

`FuzzyMeasurePairing` — Extract straight edge pairs perpendicular to a rectangle or an
annular arc.

## Signature

`static void HOperatorSet.FuzzyMeasurePairing(HObject image, HTuple measureHandle, HTuple sigma, HTuple ampThresh, HTuple fuzzyThresh, HTuple transition, HTuple pairing, HTuple numPairs, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple rowPairCenter, out HTuple columnPairCenter, out HTuple fuzzyScore, out HTuple intraDistance)`

`void HMeasure.FuzzyMeasurePairing(HImage image, double sigma, double ampThresh, double fuzzyThresh, string transition, string pairing, int numPairs, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple rowPairCenter, out HTuple columnPairCenter, out HTuple fuzzyScore, out HTuple intraDistance)`

`void HImage.FuzzyMeasurePairing(HMeasure measureHandle, double sigma, double ampThresh, double fuzzyThresh, string transition, string pairing, int numPairs, out HTuple rowEdgeFirst, out HTuple columnEdgeFirst, out HTuple amplitudeFirst, out HTuple rowEdgeSecond, out HTuple columnEdgeSecond, out HTuple amplitudeSecond, out HTuple rowPairCenter, out HTuple columnPairCenter, out HTuple fuzzyScore, out HTuple intraDistance)`

## Description

`FuzzyMeasurePairing` serves to extract *straight* edge
pairs that lie *perpendicular* to the major axis of a
rectangle or an annular arc.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The extraction algorithm of `FuzzyMeasurePairing`
is identical to [`FuzzyMeasurePairs`](fuzzy_measure_pairs.md)
(see there for details) with the exception, that it is also possible to
extract interleaving and included pairs using the parameter *`pairing`*.
Currently only *"no_restriction"* is available, which returns
all possible edge pairs, allowing interleaving and inclusion of pairs.

Only the best scored *`numPairs`* edge pairs are returned, whereas 0
indicates to return all possible found edge combinations.

The selected edges are returned as single points, which lie on the
major axis of the rectangle or annular arc. The corresponding edge
amplitudes are returned in *`amplitudeFirst`* and
*`amplitudeSecond`*, the fuzzy scores in *`fuzzyScore`*.
In addition, the distance between each edge pair is returned in
*`intraDistance`*, corresponding to the distance
between EdgeFirst[i] and EdgeSecond[i].

## Attention

`FuzzyMeasurePairing` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle or annular arc are fulfilled. Thus, it
should not be used to extract edges from curved objects, for
example. Furthermore, the user should ensure that the rectangle or
annular arc is as close to perpendicular as possible to the edges in
the image. Additionally, *`sigma`* must not become larger than
approx. 0.5 * Length1 (for Length1 see
[`GenMeasureRectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `FuzzyMeasurePairing` ignores
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

**`pairing`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Constraint of pairing.

Default:
"no_restriction"

List of values:
"no_restriction"

**`numPairs`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Number of edge pairs.

Default:
10

Suggested values:
0, 1, 10, 20, 50

Value range:
`0
≤
numPairs`

Recommended increment:
1

**`rowEdgeFirst`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the first edge.

**`columnEdgeFirst`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the first edge.

**`amplitudeFirst`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Edge amplitude of the first edge (with sign).

**`rowEdgeSecond`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the second edge.

**`columnEdgeSecond`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the second edge.

**`amplitudeSecond`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Edge amplitude of the second edge (with sign).

**`rowPairCenter`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the edge pair.

**`columnPairCenter`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the center of the edge pair.

**`fuzzyScore`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Fuzzy evaluation of the edge pair.

**`intraDistance`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Distance between the edges of the edge pair.

## Result

If the parameter values are correct the operator
`FuzzyMeasurePairing` returns the value 2 (
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
`FuzzyMeasurePairs`,
`MeasurePairs`

## See also

`FuzzyMeasurePos`,
`MeasurePos`

## Module

1D Metrology
