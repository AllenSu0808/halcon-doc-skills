# measure_pos (Operator)

## Name

`measure_pos` — Extract straight edges perpendicular to a rectangle or annular arc.

## Signature

`def measure_pos(image: HObject, measure_handle: HHandle, sigma: float, threshold: float, transition: str, select: str) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

## Description

`measure_pos` extracts *straight* edges which
lie *perpendicular* to the major axis of a rectangle or annular arc.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The algorithm of `measure_pos`
works by averaging the gray values in “slices”
perpendicular to the major axis of the rectangle or annular arc
in order to obtain
a one-dimensional edge profile. The sampling is done at subpixel
positions in the image *`image`* at integer row and column
distances (in the coordinate frame of the rectangle) from the center
of the rectangle. Since this involves some calculations which can
be used repeatedly in several measurements, the operator
[`gen_measure_rectangle2`](gen_measure_rectangle2.md) or [`gen_measure_arc`](gen_measure_arc.md) is used to
perform these calculations
only once, thus increasing the speed of `measure_pos`
significantly. Since there is a trade-off between accuracy and
speed in the subpixel calculations of the gray values, and thus in
the accuracy of the extracted edge positions, different
interpolation schemes can be selected in
[`gen_measure_rectangle2`](gen_measure_rectangle2.md). (The interpolation only influences
rectangles not aligned with the image axes.) The measure object
generated with [`gen_measure_rectangle2`](gen_measure_rectangle2.md) is passed in
*`measure_handle`*.

After the one-dimensional edge profile has been calculated, subpixel
edge locations are computed by convolving the profile with the
derivatives of a Gaussian smoothing kernel of standard deviation
*`sigma`*. Salient edges can be selected with the parameter
*`threshold`*, which constitutes a threshold on the amplitude
values (*`amplitude`*), i.e., the absolute value of the first
derivative of the edge.
Note that the amplitude values are scaled by the factor
$\Sigma \cdot \sqrt{2\pi}$ ![figure](../assets/bfc51c2923f487d0.svg).
Additionally, it is possible to select only positive edges, i.e.,
edges which constitute a dark-to-light transition in the direction
of the major axis of the rectangle or the arc (*`transition`* =
*"positive"*), only negative edges, i.e., light-to-dark
transitions (*`transition`* = *"negative"*), or both
types of edges (*`transition`* = *"all"*). Finally, it
is possible to select which edge points are returned. If
*`select`* is set to *"all"*, all edge points are
returned. If it is set to *"first"*, only the first of the
extracted edge points is returned, while it is set to
*"last"*, only the last one is returned.

The extracted edges are returned as single points which lie on the
major axis of the rectangle or arc in (*`row_edge`*, *`column_edge`*).
The corresponding edge amplitudes are returned in
*`amplitude`*. In addition, the distance between consecutive
edge points is returned in *`distance`*. Here, Distance[i]
corresponds to the distance between Edge[i] and Edge[i+1], i.e., the
tuple *`distance`* contains one element less than the tuples
*`row_edge`* and *`column_edge`*.

## Attention

`measure_pos` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle or arc are fulfilled. Thus, it should
not be used to extract edges from curved objects, for example.
Furthermore, the user should ensure that the rectangle or arc is as
close to perpendicular as possible to the edges in the image. Additionally,
*`sigma`* must not become larger than approx. 0.5 * `length_1`
(for `length_1` see [`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `measure_pos` ignores the
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

Light/dark or dark/light edge.

Default:
"all"

List of values:
"all", "negative", "positive"

**`select`** (input_control)  string `→` str

Selection of end points.

Default:
"all"

List of values:
"all", "first", "last"

**`row_edge`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the center of the edge.

**`column_edge`** (output_control)  point.x-array `→` Sequence[float]

Column coordinate of the center of the edge.

**`amplitude`** (output_control)  real-array `→` Sequence[float]

Edge amplitude of the edge (with sign).

**`distance`** (output_control)  real-array `→` Sequence[float]

Distance between consecutive edges.

## Result

If the parameter values are correct the operator `measure_pos`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`

## Possible Successors

`close_measure`

## Alternatives

`edges_sub_pix`,
`fuzzy_measure_pos`

## See also

`measure_pairs`,
`fuzzy_measure_pairs`,
`fuzzy_measure_pairing`

## Module

1D Metrology
