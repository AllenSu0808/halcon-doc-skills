# close_edges_length (Operator)

## Name

`close_edges_length` — Close edge gaps using the edge amplitude image.

## Signature

`def close_edges_length(edges: HObject, gradient: HObject, min_amplitude: int, max_gap_length: int) -> HObject`

## Description

`close_edges_length` closes gaps in the output of an edge
detector, and thus tries to produce complete object contours. This
operator expects as input the edges (*`edges`*) and amplitude
image (*`gradient`*) returned by typical edge operators,
such as [`edges_image`](edges_image.md) or [`sobel_amp`](sobel_amp.md).

Contours are closed in two steps: First, one pixel wide gaps in the
input contours are closed, and isolated points are eliminated. After
this, open contours are extended by up to *`max_gap_length`*
points by adding edge points until either the contour is closed or
no more significant edge points can be found. A gradient is
regarded as significant if it is larger than
*`min_amplitude`*. The neighboring points examined as
possible new edge points are the point in the direction of the
contour and its two adjacent points in an 8-neighborhood. For each
of these points, the sum of its gradient and the maximum gradient of
that points three possible neighbors is calculated
(*look ahead* of length 1). The point with the maximum
sum is then chosen as the new edge point.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`edges`** (input_object)  region(-array) `→` HObject

Region containing one pixel thick edges.

**`gradient`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Edge amplitude (gradient) image.

**`closed_edges`** (output_object)  region(-array) `→` HObject

Region containing closed edges.

**`min_amplitude`** (input_control)  integer `→` int

Minimum edge amplitude.

Default:
16

Suggested values:
5, 8, 10, 12, 16, 20, 25, 30, 40, 50

Value range:
`0
≤
min_amplitude
≤
255`

Minimum increment:
1

Recommended increment:
1

**`max_gap_length`** (input_control)  integer `→` int

Maximal number of points by which edges are extended.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30, 40, 50, 70, 100

Value range:
`1
≤
max_gap_length
≤
127`

Minimum increment:
1

Recommended increment:
1

## Example (C)

```
sobel_amp(Image,&EdgeAmp,"sum_abs",5);
threshold(EdgeAmp,&EdgeRegion,40.0,255.0);
skeleton(EdgeRegion,&ThinEdge);
close_edges_length(ThinEdge,EdgeAmp,&CloseEdges,15,3);
```

## Result

`close_edges_length` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`edges_image`,
`sobel_amp`,
`threshold`,
`skeleton`

## Alternatives

`close_edges`,
`dilation1`,
`closing`

## References

M. Üsbeck: “Untersuchungen zur echtzeitfähigen Segmentierung”;
Studienarbeit, Bayerisches Forschungszentrum für Wissensbasierte
Systeme (FORWISS), Erlangen, 1993.

## Module

Foundation
