# emphasize (Operator)

## Name

`emphasize` — Enhance contrast of the image.

## Signature

`def emphasize(image: HObject, mask_width: int, mask_height: int, factor: float) -> HObject`

## Description

The operator `emphasize` emphasizes high frequency areas of the
image (edges and corners). The resulting images appears sharper.

First the procedure carries out a filtering with the low pass
([`mean_image`](mean_image.md)). The resulting gray values (res) are calculated
from the obtained gray values (mean) and the original gray values
(orig) as follows:
res := round((orig - mean) * Factor) + orig
*`factor`* serves as measurement of the increase in contrast.
The division frequency is determined via the size of the filter matrix:
The larger the matrix, the lower the division frequency.

As an edge treatment the gray values are mirrored at the edges of the image.
Overflow and/or underflow of gray values is clipped.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2)

Image to be enhanced.

**`image_emphasize`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2)

contrast enhanced image.

**`mask_width`** (input_control)  extent.x `→` int

Width of low pass mask.

Default:
7

Suggested values:
3, 5, 7, 9, 11, 15, 21, 25, 31, 39

Value range:
`3
≤
mask_width`

Minimum increment:
2

Recommended increment:
2

**`mask_height`** (input_control)  extent.y `→` int

Height of the low pass mask.

Default:
7

Suggested values:
3, 5, 7, 9, 11, 15, 21, 25, 31, 39

Value range:
`3
≤
mask_height`

Minimum increment:
2

Recommended increment:
2

**`factor`** (input_control)  real `→` float

Intensity of contrast emphasis.

Default:
1.0

Suggested values:
0.3, 0.5, 0.7, 1.0, 1.4, 1.8, 2.0

Value range:
`0.0
≤
factor` (sqrt)

Recommended increment:
0.2

## Result

If the parameter values are correct the operator `emphasize`
returns the value 2 (
H_MSG_TRUE)
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`disp_image`

## Alternatives

`mean_image`,
`sub_image`,
`laplace`,
`add_image`

## See also

`mean_image`,
`highpass_image`

## Module

Foundation
