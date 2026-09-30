# emphasize (Operator)

## Name

`emphasize` — Enhance contrast of the image.

## Signature

`emphasize(Image : ImageEmphasize : MaskWidth, MaskHeight, Factor : )`

## Description

The operator `emphasize` emphasizes high frequency areas of the
image (edges and corners). The resulting images appears sharper.

First the procedure carries out a filtering with the low pass
([`mean_image`](mean_image.md)). The resulting gray values (res) are calculated
from the obtained gray values (mean) and the original gray values
(orig) as follows:
res := round((orig - mean) * Factor) + orig
*`Factor`* serves as measurement of the increase in contrast.
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2)

Image to be enhanced.

**`ImageEmphasize`** (output_object)  (multichannel-)image(-array) `→` object (byte / int2 / uint2)

contrast enhanced image.

**`MaskWidth`** (input_control)  extent.x `→`  (integer)

Width of low pass mask.

Default:
7

Suggested values:
3, 5, 7, 9, 11, 15, 21, 25, 31, 39

Value range:
`3
≤
MaskWidth`

Minimum increment:
2

Recommended increment:
2

**`MaskHeight`** (input_control)  extent.y `→`  (integer)

Height of the low pass mask.

Default:
7

Suggested values:
3, 5, 7, 9, 11, 15, 21, 25, 31, 39

Value range:
`3
≤
MaskHeight`

Minimum increment:
2

Recommended increment:
2

**`Factor`** (input_control)  real `→`  (real)

Intensity of contrast emphasis.

Default:
1.0

Suggested values:
0.3, 0.5, 0.7, 1.0, 1.4, 1.8, 2.0

Value range:
`0.0
≤
Factor` (sqrt)

Recommended increment:
0.2

## Example (HDevelop)

```
read_image(Image,'mreut')
dev_display (Image)
draw_region(Region,WindowHandle)
reduce_domain(Image,Region,Mask)
emphasize(Mask,Sharp,7,7,2.0)
dev_display (Sharp)
```

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
