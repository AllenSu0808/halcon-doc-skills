# CloseEdges (Operator)

## Name

`CloseEdges` — Close edge gaps using the edge amplitude image.

## Signature

`static void HOperatorSet.CloseEdges(HObject edges, HObject edgeImage, out HObject regionResult, HTuple minAmplitude)`

`HRegion HRegion.CloseEdges(HImage edgeImage, int minAmplitude)`

## Description

`CloseEdges` closes gaps in the output of an edge
detector, and thus tries to produce complete object contours. This
is done by examining the neighbors of each edge point to determine
the point with maximum amplitude (i.e., maximum gradient), and
adding the point to the edge if its amplitude is larger than the
minimum amplitude passed in *`minAmplitude`*. This operator
expects as input the edges (*`edges`*) and amplitude image
(*`edgeImage`*) returned by typical edge operators, such as
[`EdgesImage`](edges_image.md) or [`SobelAmp`](sobel_amp.md).
`CloseEdges` does not take into account the edge
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

**`edges`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region containing one pixel thick edges.

**`edgeImage`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2 / int4)

Edge amplitude (gradient) image.

**`regionResult`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Region containing closed edges.

**`minAmplitude`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum edge amplitude.

Default:
16

Suggested values:
5, 8, 10, 12, 16, 20, 25, 30, 40, 50

Value range:
`1
≤
minAmplitude`

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

`CloseEdges` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`EdgesImage`,
`SobelAmp`,
`Threshold`,
`Skeleton`

## Possible Successors

`Skeleton`

## Alternatives

`CloseEdgesLength`,
`Dilation1`,
`Closing`

## See also

`GraySkeleton`

## Module

Foundation
