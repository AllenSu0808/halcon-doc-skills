# fuzzy_measure_pairing (Operator)

## Name

`fuzzy_measure_pairing` — Extract straight edge pairs perpendicular to a rectangle or an
annular arc.

## Signature

`fuzzy_measure_pairing(Image : : MeasureHandle, Sigma, AmpThresh, FuzzyThresh, Transition, Pairing, NumPairs : RowEdgeFirst, ColumnEdgeFirst, AmplitudeFirst, RowEdgeSecond, ColumnEdgeSecond, AmplitudeSecond, RowPairCenter, ColumnPairCenter, FuzzyScore, IntraDistance)`

## Description

`fuzzy_measure_pairing` serves to extract *straight* edge
pairs that lie *perpendicular* to the major axis of a
rectangle or an annular arc.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The extraction algorithm of `fuzzy_measure_pairing`
is identical to [`fuzzy_measure_pairs`](fuzzy_measure_pairs.md)
(see there for details) with the exception, that it is also possible to
extract interleaving and included pairs using the parameter *`Pairing`*.
Currently only *'no_restriction'* is available, which returns
all possible edge pairs, allowing interleaving and inclusion of pairs.

Only the best scored *`NumPairs`* edge pairs are returned, whereas 0
indicates to return all possible found edge combinations.

The selected edges are returned as single points, which lie on the
major axis of the rectangle or annular arc. The corresponding edge
amplitudes are returned in *`AmplitudeFirst`* and
*`AmplitudeSecond`*, the fuzzy scores in *`FuzzyScore`*.
In addition, the distance between each edge pair is returned in
*`IntraDistance`*, corresponding to the distance
between EdgeFirst[i] and EdgeSecond[i].

## Attention

`fuzzy_measure_pairing` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle or annular arc are fulfilled. Thus, it
should not be used to extract edges from curved objects, for
example. Furthermore, the user should ensure that the rectangle or
annular arc is as close to perpendicular as possible to the edges in
the image. Additionally, *`Sigma`* must not become larger than
approx. 0.5 * Length1 (for Length1 see
[`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `fuzzy_measure_pairing` ignores
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

**`Pairing`** (input_control)  string `→`  (string)

Constraint of pairing.

Default:
'no_restriction'

List of values:
'no_restriction'

**`NumPairs`** (input_control)  number `→`  (integer)

Number of edge pairs.

Default:
10

Suggested values:
0, 1, 10, 20, 50

Value range:
`0
≤
NumPairs`

Recommended increment:
1

**`RowEdgeFirst`** (output_control)  point.y-array `→`  (real)

Row coordinate of the first edge.

**`ColumnEdgeFirst`** (output_control)  point.x-array `→`  (real)

Column coordinate of the first edge.

**`AmplitudeFirst`** (output_control)  real-array `→`  (real)

Edge amplitude of the first edge (with sign).

**`RowEdgeSecond`** (output_control)  point.y-array `→`  (real)

Row coordinate of the second edge.

**`ColumnEdgeSecond`** (output_control)  point.x-array `→`  (real)

Column coordinate of the second edge.

**`AmplitudeSecond`** (output_control)  real-array `→`  (real)

Edge amplitude of the second edge (with sign).

**`RowPairCenter`** (output_control)  point.y-array `→`  (real)

Row coordinate of the center of the edge pair.

**`ColumnPairCenter`** (output_control)  point.x-array `→`  (real)

Column coordinate of the center of the edge pair.

**`FuzzyScore`** (output_control)  real-array `→`  (real)

Fuzzy evaluation of the edge pair.

**`IntraDistance`** (output_control)  real-array `→`  (real)

Distance between the edges of the edge pair.

## Result

If the parameter values are correct the operator
`fuzzy_measure_pairing` returns the value 2 (
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
`fuzzy_measure_pairs`,
`measure_pairs`

## See also

`fuzzy_measure_pos`,
`measure_pos`

## Module

1D Metrology
