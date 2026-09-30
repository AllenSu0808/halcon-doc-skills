# fuzzy_measure_pos (Operator)

## Name

`fuzzy_measure_pos` — Extract straight edges perpendicular to a rectangle or an annular arc.

## Signature

`fuzzy_measure_pos(Image : : MeasureHandle, Sigma, AmpThresh, FuzzyThresh, Transition : RowEdge, ColumnEdge, Amplitude, FuzzyScore, Distance)`

## Description

`fuzzy_measure_pos` extracts *straight* edges which lie
*perpendicular* to the major axis of a rectangle or an annular arc.
In addition to [`measure_pos`](measure_pos.md) it uses fuzzy functions to
evaluate and select the edges.

For an explanation of the concept of 1D measuring see the introduction of
chapter [1D Measuring](toc_1dmeasuring.md).

The algorithm of `fuzzy_measure_pos`
works by averaging the gray values in “slices”
perpendicular to the major axis of the rectangle or annular arc
in order to obtain
a one-dimensional edge profile. The sampling is done at subpixel
positions in the image *`Image`* at integer row and column
distances (in the coordinate frame of the rectangle) from the center
of the rectangle. Since this involves some calculations which can
be used repeatedly in several measurements, the operator
[`gen_measure_rectangle2`](gen_measure_rectangle2.md) is used to perform these
calculations only once, thus increasing the speed of
`fuzzy_measure_pos` significantly. Since there is a trade-off
between accuracy and speed in the subpixel calculations of the gray
values, and thus in the accuracy of the extracted edge positions,
different interpolation schemes can be selected in
[`gen_measure_rectangle2`](gen_measure_rectangle2.md). (The interpolation only
influences rectangles not aligned with the image axes and annular arcs.)
The measure
object generated with [`gen_measure_rectangle2`](gen_measure_rectangle2.md) is passed
in *`MeasureHandle`*.

After the one-dimensional edge profile has been calculated, subpixel
edge locations are computed by convolving the profile with the
derivatives of a Gaussian smoothing kernel of standard deviation
*`Sigma`*. Salient edges can be selected with the parameter
*`AmpThresh`*, which constitutes a threshold on the amplitude,
i.e., the absolute value of the first derivative of the edge.
Additionally, it is possible to select only positive edges, i.e.,
edges which constitute a dark-to-light transition in the direction
of the major axis of the rectangle (*`Transition`* =
*'positive'*), only negative edges, i.e., light-to-dark
transitions (*`Transition`* = *'negative'*), or both
types of edges (*`Transition`* = *'all'*). Finally, it
is possible to select which edge points are returned.

Having extracted subpixel edge locations,
features of these edges are evaluated by a corresponding fuzzy
function, which can be set by [`set_fuzzy_measure`](set_fuzzy_measure.md). Which edges
are selected can be determined with the parameter *`FuzzyThresh`*,
which constitutes a threshold on the weight over all fuzzy sets, i.e., the
geometric mean of the weights of the defined sets.

The selected edges are returned as single points, which lie on the
major axis of the rectangle or annular arc, in
(*`RowEdge`*, *`ColumnEdge`*). The corresponding edge
amplitudes are returned in *`Amplitude`*, the fuzzy scores in
*`FuzzyScore`*. In addition, the
distance between consecutive edge points is returned in
*`Distance`*. Here, Distance[i] corresponds to the distance
between Edge[i] and Edge[i+1], i.e., the tuple *`Distance`*
contains one element less than the tuples *`RowEdge`* and
*`ColumnEdge`*.

## Attention

`fuzzy_measure_pos` only returns meaningful results if the
assumptions that the edges are straight and perpendicular to the
major axis of the rectangle are fulfilled. Thus, it should not be
used to extract edges from curved objects, for example.
Furthermore, the user should ensure that the rectangle is as close
to perpendicular as possible to the edges in the image. Additionally,
*`Sigma`* must not become larger than approx. 0.5 * Length1
(for Length1 see [`gen_measure_rectangle2`](gen_measure_rectangle2.md)).

It should be kept in mind that `fuzzy_measure_pos` ignores the
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
0.1, 0.3, 0.5, 0.6, 0.7, 0.9

Value range:
`0.0
≤
FuzzyThresh
≤
1.0` (lin)

Recommended increment:
0.1

**`Transition`** (input_control)  string `→`  (string)

Select light/dark or dark/light edges.

Default:
'all'

List of values:
'all', 'negative', 'positive'

**`RowEdge`** (output_control)  point.y-array `→`  (real)

Row coordinate of the edge point.

**`ColumnEdge`** (output_control)  point.x-array `→`  (real)

Column coordinate of the edge point.

**`Amplitude`** (output_control)  real-array `→`  (real)

Edge amplitude of the edge (with sign).

**`FuzzyScore`** (output_control)  real-array `→`  (real)

Fuzzy evaluation of the edges.

**`Distance`** (output_control)  real-array `→`  (real)

Distance between consecutive edges.

## Result

If the parameter values are correct the operator
`fuzzy_measure_pos` returns the value 2 (
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
`measure_pos`

## See also

`fuzzy_measure_pairing`,
`fuzzy_measure_pairs`,
`measure_pairs`

## Module

1D Metrology
