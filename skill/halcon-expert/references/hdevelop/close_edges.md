# close_edges (Operator)

## Name

`close_edges` — Close edge gaps using the edge amplitude image.

## Signature

`close_edges(Edges, EdgeImage : RegionResult : MinAmplitude : )`

## Description

`close_edges` closes gaps in the output of an edge
detector, and thus tries to produce complete object contours. This
is done by examining the neighbors of each edge point to determine
the point with maximum amplitude (i.e., maximum gradient), and
adding the point to the edge if its amplitude is larger than the
minimum amplitude passed in *`MinAmplitude`*. This operator
expects as input the edges (*`Edges`*) and amplitude image
(*`EdgeImage`*) returned by typical edge operators, such as
[`edges_image`](edges_image.md) or [`sobel_amp`](sobel_amp.md).
`close_edges` does not take into account the edge
directions that may be returned by an edge operator. Thus, in areas
where the gradient is almost constant the edges may become rather
“wiggly.”

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Edges`** (input_object)  region(-array) `→` object

Region containing one pixel thick edges.

**`EdgeImage`** (input_object)  singlechannelimage `→` object (byte / uint2 / int4)

Edge amplitude (gradient) image.

**`RegionResult`** (output_object)  region(-array) `→` object

Region containing closed edges.

**`MinAmplitude`** (input_control)  integer `→`  (integer)

Minimum edge amplitude.

Default:
16

Suggested values:
5, 8, 10, 12, 16, 20, 25, 30, 40, 50

Value range:
`1
≤
MinAmplitude`

Minimum increment:
1

Recommended increment:
1

## Example (C)

```
sobel_amp(Image,&EdgeAmp,"sum_abs",5);
threshold(EdgeAmp,&EdgeRegion,40.0,255.0);
skeleton(EdgeRegion,&ThinEdge);
close_edges(ThinEdge,EdgeAmp,&CloseEdges,15);
skeleton(CloseEdges,&ThinCloseEdges);
```

## Result

`close_edges` returns 2 (
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

## Possible Successors

`skeleton`

## Alternatives

`close_edges_length`,
`dilation1`,
`closing`

## See also

`gray_skeleton`

## Module

Foundation
