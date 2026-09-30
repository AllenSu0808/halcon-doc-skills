# fuzzy_measure_pairing (Operator)

## Name

`fuzzy_measure_pairing` — Extract straight edge pairs perpendicular to a rectangle or an
annular arc.

## Signature

`def fuzzy_measure_pairing(image: HObject, measure_handle: HHandle, sigma: float, amp_thresh: float, fuzzy_thresh: float, transition: str, pairing: str, num_pairs: int) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`fuzzy_measure_pairing` serves to extract *straight* edge
pairs that lie *perpendicular* to the major axis of a
rectangle or an annular arc.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The extraction algorithm of `fuzzy_measure_pairing`
is identical to [`fuzzy_measure_pairs`](fuzzy_measure_pairs.md)
(see there for details) with the exception, that it is also possible to
extract interleaving and included pairs using the parameter *`pairing`*.
Currently only *"no_restriction"* is available, which returns
all possible edge pairs, allowing interleaving and inclusion of pairs.

Only the best scored *`num_pairs`* edge pairs are returned, whereas 0
indicates to return all possible found edge combinations.

The selected edges are returned as single points, which lie on the
major axis of the rectangle or annular arc. The corresponding edge
amplitudes are returned in *`amplitude_first`* and
*`amplitude_second`*, the fuzzy scores in *`fuzzy_score`*.
In addition, the distance between each edge pair is returned in
*`intra_distance`*, corresponding to the distance
between EdgeFirst[i] and EdgeSecond[i].

## Attention

`fuzzy_measure_pairing` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle or annular arc are fulfilled. Thus, it
should not be used to extract edges from curved objects, for
example. Furthermore, the user should ensure that the rectangle or
annular arc is as close to perpendicular as possible to the edges in
the image. Additionally, *`sigma`* must not become larger than
approx. 0.5 * Length1 (for Length1 see
[`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `fuzzy_measure_pairing` ignores
the domain of *`image`* for efficiency reasons. If certain
regions in the image should be excluded from the measurement a new
measure object with appropriately modified parameters should be
generated.

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

**`amp_thresh`** (input_control)  number `→` float

Minimum edge amplitude.

Default:
30.0

Suggested values:
5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 90.0, 110.0

Value range:
`1
≤
amp_thresh
≤
255` (lin)

Minimum increment:
0.5

Recommended increment:
2

**`fuzzy_thresh`** (input_control)  number `→` float

Minimum fuzzy value.

Default:
0.5

Suggested values:
0.1, 0.3, 0.5, 0.7, 0.9

Value range:
`0.0
≤
fuzzy_thresh
≤
1.0` (lin)

Recommended increment:
0.1

**`transition`** (input_control)  string `→` str

Select the first gray value transition of the edge pairs.

Default:
"all"

List of values:
"all", "negative", "positive"

**`pairing`** (input_control)  string `→` str

Constraint of pairing.

Default:
"no_restriction"

List of values:
"no_restriction"

**`num_pairs`** (input_control)  number `→` int

Number of edge pairs.

Default:
10

Suggested values:
0, 1, 10, 20, 50

Value range:
`0
≤
num_pairs`

Recommended increment:
1

**`row_edge_first`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the first edge.

**`column_edge_first`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the first edge.

**`amplitude_first`** (output_control)  real-array `→` Sequence[float]

Edge amplitude of the first edge (with sign).

**`row_edge_second`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the second edge.

**`column_edge_second`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the second edge.

**`amplitude_second`** (output_control)  real-array `→` Sequence[float]

Edge amplitude of the second edge (with sign).

**`row_pair_center`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the center of the edge pair.

**`column_pair_center`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the center of the edge pair.

**`fuzzy_score`** (output_control)  real-array `→` Sequence[float]

Fuzzy evaluation of the edge pair.

**`intra_distance`** (output_control)  real-array `→` Sequence[float]

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
