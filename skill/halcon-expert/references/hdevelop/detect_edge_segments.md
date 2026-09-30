# detect_edge_segments (Operator)

## Name

`detect_edge_segments` — Detect straight edge segments.

## Signature

`detect_edge_segments(Image : : SobelSize, MinAmplitude, MaxDistance, MinLength : BeginRow, BeginCol, EndRow, EndCol)`

## Description

`detect_edge_segments` detects straight edge segments in the gray
image *`Image`*. The extracted edge segments are returned as
line segments with start point (*`BeginRow`*,*`BeginCol`*)
and end point (*`EndRow`*,*`EndCol`*). Edge detection
is based on the Sobel filter, using *'sum_abs'* as parameter and
*`SobelSize`* as the filter mask size (see
[`sobel_amp`](sobel_amp.md)). Only pixels with a filter response larger
than *`MinAmplitude`* are used as candidates for edge points.
These thresholded edge points are thinned and split into straight
segments. Due to technical reasons, edge points in which several
edges meet are lost. Therefore, `detect_edge_segments` usually
does not return closed object contours. The parameter
*`MaxDistance`* controls the maximum allowed distance of an
edge point to its approximating line. For efficiency reasons, the
sum of the absolute values of the coordinate differences is used
instead of the Euclidean distance. *`MinLength`* controls
the minimum length of the line segments. Lines shorter than
*`MinLength`* are not returned.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Input image.

**`SobelSize`** (input_control)  integer `→`  (integer)

Mask size of the Sobel operator.

Default:
5

List of values:
3, 5, 7, 9, 11, 13

**`MinAmplitude`** (input_control)  integer `→`  (integer)

Minimum edge strength.

Default:
32

Suggested values:
10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 110

Value range:
`1
≤
MinAmplitude
≤
255`

Minimum increment:
1

Recommended increment:
1

**`MaxDistance`** (input_control)  integer `→`  (integer)

Maximum distance of the approximating line to
its original edge.

Default:
3

Suggested values:
2, 3, 4, 5, 6, 7, 8

Value range:
`0
≤
MaxDistance`

Minimum increment:
1

Recommended increment:
1

**`MinLength`** (input_control)  integer `→`  (integer)

Minimum length of to resulting line segments.

Default:
10

Suggested values:
3, 5, 7, 9, 11, 13, 16, 20

Value range:
`1
≤
MinLength`

Minimum increment:
1

Recommended increment:
1

**`BeginRow`** (output_control)  line.begin.y-array `→`  (integer)

Row coordinate of the line segments' start points.

**`BeginCol`** (output_control)  line.begin.x-array `→`  (integer)

Column coordinate of the line segments' start points.

**`EndRow`** (output_control)  line.end.y-array `→`  (integer)

Row coordinate of the line segments' end points.

**`EndCol`** (output_control)  line.end.x-array `→`  (integer)

Column coordinate of the line segments' end points.

## Example (C)

```
Htuple  SobelSize,MinAmplitude,MaxDistance,MinLength;
Htuple  RowBegin,ColBegin,RowEnd,ColEnd;

create_tuple(&SobelSize,1);
set_i(SobelSize,5,0);
create_tuple(&MinAmplitude,1);
set_i(MinAmplitude,32,0);
create_tuple(&MaxDistance,1);
set_i(MaxDistance,3,0);
create_tuple(&MinLength,1);
set_i(MinLength,10,0);
T_detect_edge_segments(Image,SobelSize,MinAmplitude,MaxDistance,MinLength,
                &RowBegin,&ColBegin,&RowEnd,&ColEnd);
```

## Result

`detect_edge_segments` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Predecessors

`sigma_image`,
`median_image`

## Possible Successors

`partition_lines`,
`line_position`,
`line_orientation`

## Alternatives

`sobel_amp`,
`threshold`,
`skeleton`

## Module

Foundation
