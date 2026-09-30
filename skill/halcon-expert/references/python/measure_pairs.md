# measure_pairs (Operator)

## Name

`measure_pairs` — Extract straight edge pairs perpendicular to a rectangle or annular arc.

## Signature

`def measure_pairs(image: HObject, measure_handle: HHandle, sigma: float, threshold: float, transition: str, select: str) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`measure_pairs` serves to extract *straight* edge pairs
which lie *perpendicular* to the major axis of a rectangle or
annular arc.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The extraction algorithm of `measure_pairs`
is identical to [`measure_pos`](measure_pos.md). In addition
the edges are grouped to pairs: If *`transition`* = *"positive"*,
the edge points with a dark-to-light transition in the direction of the major
axis of the rectangle are returned in *`row_edge_first`* and
*`column_edge_first`*. In this case, the corresponding edges with a
light-to-dark transition are returned in *`row_edge_second`* and
*`column_edge_second`*. If *`transition`* = *"negative"*, the
behavior is exactly opposite. If *`transition`* = *"all"*, the
first detected edge defines the transition for *`row_edge_first`* and
*`column_edge_first`*. I.e., dependent on the positioning of the measure
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
returned in *`amplitude_first`* and *`amplitude_second`*.
In addition, the distance between each edge pair is returned in
*`intra_distance`* and the distance between consecutive edge
pairs is returned in *`inter_distance`*. Here, IntraDistance[i]
corresponds to the distance between EdgeFirst[i] and EdgeSecond[i],
while InterDistance[i] corresponds to the distance between
EdgeSecond[i] and EdgeFirst[i+1], i.e., the tuple
*`inter_distance`* contains one element less than the tuples
of the edge pairs.

## Attention

`measure_pairs` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle are fulfilled. Thus, it should not be
used to extract edges from curved objects, for example.
Furthermore, the user should ensure that the rectangle is as close
to perpendicular as possible to the edges in the image. Additionally,
*`sigma`* must not become larger than approx. 0.5 * Length1
(for Length1 see [`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `measure_pairs` ignores the
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

**`threshold`** (input_control)  number `→` float

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

**`transition`** (input_control)  string `→` str

Type of gray value transition that determines
how edges are grouped to edge pairs.

Default:
"all"

List of values:
"all", "all_strongest", "negative", "negative_strongest", "positive", "positive_strongest"

**`select`** (input_control)  string `→` str

Selection of edge pairs.

Default:
"all"

List of values:
"all", "first", "last"

**`row_edge_first`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the center of the first edge.

**`column_edge_first`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the center of the first edge.

**`amplitude_first`** (output_control)  real-array `→` Sequence[float]

Edge amplitude of the first edge (with sign).

**`row_edge_second`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the center of the second edge.

**`column_edge_second`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the center of the second
edge.

**`amplitude_second`** (output_control)  real-array `→` Sequence[float]

Edge amplitude of the second edge (with sign).

**`intra_distance`** (output_control)  real-array `→` Sequence[float]

Distance between edges of an edge pair.

**`inter_distance`** (output_control)  real-array `→` Sequence[float]

Distance between consecutive edge pairs.

## Result

If the parameter values are correct the operator `measure_pairs`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`

## Possible Successors

`close_measure`

## Alternatives

`edges_sub_pix`,
`fuzzy_measure_pairs`,
`fuzzy_measure_pairing`

## See also

`measure_pos`,
`fuzzy_measure_pos`

## Module

1D Metrology
