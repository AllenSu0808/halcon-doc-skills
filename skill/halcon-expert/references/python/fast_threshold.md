# fast_threshold (Operator)

## Name

`fast_threshold` — Fast thresholding of images using global thresholds.

## Signature

`def fast_threshold(image: HObject, min_gray: Union[int, float], max_gray: Union[int, float], min_size: int) -> HObject`

## Description

`fast_threshold` selects the pixels from the input image
whose gray values g fulfill the following condition:

$$\texttt{MinGray}\le g\le\texttt{MaxGray}.$$

To reduce the processing time, the selection is done in two steps: At first,
all points lying on selected horizontal lines that are specified by their
distance *`min_size`* are processed. In the next step the neighborhood
(size (2*MinSize+1) x
(2*MinSize+1)) of all previously selected points are
processed.

## Attention

On multi-core computers supporting the SSE2 instruction set, [`threshold`](threshold.md)
is most likely faster than `fast_threshold`.
`fast_threshold` may only be preferred to [`threshold`](threshold.md) if those
features are not available, e.g., on embedded platforms.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / direction / cyclic / real)

Input image.

**`region`** (output_object)  region(-array) `→` HObject

Segmented regions.

**`min_gray`** (input_control)  number `→` Union[int, float]

Lower threshold for the gray values.

Default:
128

Suggested values:
0.0, 10.0, 30.0, 64.0, 128.0, 200.0, 220.0, 255.0

Value range:
`0.0
≤
min_gray
≤
255.0` (lin)

Minimum increment:
1

Recommended increment:
5.0

**`max_gray`** (input_control)  number `→` Union[int, float]

Upper threshold for the gray values.

Default:
255.0

Suggested values:
0.0, 10.0, 30.0, 64.0, 128.0, 200.0, 220.0, 255.0

Value range:
`0.0
≤
max_gray
≤
255.0` (lin)

Minimum increment:
1

Recommended increment:
5.0

**`min_size`** (input_control)  number `→` int

Minimum size of objects to be extracted.

Default:
20

Suggested values:
5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 100

Value range:
`2
≤
min_size
≤
200` (lin)

Minimum increment:
1

Recommended increment:
2

## Complexity

Let A be the area of the output region and height the
height of *`image`*. Then the runtime
complexity is O(A + height / *`min_size`*).

## Result

`fast_threshold` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior with respect to the input images and output regions
can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`histo_to_thresh`,
`min_max_gray`,
`sobel_amp`,
`binomial_filter`,
`gauss_filter`,
`reduce_domain`,
`fill_interlace`

## Possible Successors

`connection`,
`dilation1`,
`erosion1`,
`opening`,
`closing`,
`rank_region`,
`shape_trans`,
`skeleton`

## Alternatives

`threshold`,
`gen_grid_region`,
`dilation_rectangle1`,
`dyn_threshold`

## See also

`class_2dim_sup`,
`hysteresis_threshold`

## Module

Foundation
