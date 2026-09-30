# Emphasize (Operator)

## Name

`Emphasize` — Enhance contrast of the image.

## Signature

`static void HOperatorSet.Emphasize(HObject image, out HObject imageEmphasize, HTuple maskWidth, HTuple maskHeight, HTuple factor)`

`HImage HImage.Emphasize(int maskWidth, int maskHeight, double factor)`

## Description

The operator `Emphasize` emphasizes high frequency areas of the
image (edges and corners). The resulting images appears sharper.

First the procedure carries out a filtering with the low pass
([`MeanImage`](mean_image.md)). The resulting gray values (res) are calculated
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Image to be enhanced.

**`imageEmphasize`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

contrast enhanced image.

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of low pass mask.

Default:
7

Suggested values:
3, 5, 7, 9, 11, 15, 21, 25, 31, 39

Value range:
`3
≤
maskWidth`

Minimum increment:
2

Recommended increment:
2

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the low pass mask.

Default:
7

Suggested values:
3, 5, 7, 9, 11, 15, 21, 25, 31, 39

Value range:
`3
≤
maskHeight`

Minimum increment:
2

Recommended increment:
2

**`factor`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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

If the parameter values are correct the operator `Emphasize`
returns the value 2 (
H_MSG_TRUE)
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`DispImage`

## Alternatives

`MeanImage`,
`SubImage`,
`Laplace`,
`AddImage`

## See also

`MeanImage`,
`HighpassImage`

## Module

Foundation
