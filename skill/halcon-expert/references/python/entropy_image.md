# entropy_image (Operator)

## Name

`entropy_image` — Calculate the entropy of gray values within a rectangular window.

## Signature

`def entropy_image(image: HObject, width: int, height: int) -> HObject`

## Description

`entropy_image` calculates the entropy of gray values in the
image *`image`* within a rectangular mask of size
(*`height`*, *`width`*). The resulting image is
returned in *`image_entropy`*, in which the entropy is
multiplied by 32. If the parameters *`height`* and
*`width`* are even, they are changed to the next larger odd
value. At the image borders the gray values are mirrored.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte)

Image for which the entropy is to be calculated.

**`image_entropy`** (output_object)  (multichannel-)image(-array) `→` HObject (byte)

Entropy image.

**`width`** (input_control)  extent.x `→` int

Width of the mask in which the entropy is calculated.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25

Restriction:
`3 <= Width && odd(Width)`

**`height`** (input_control)  extent.y `→` int

Height of the mask in which the entropy is calculated.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25

Restriction:
`3 <= Height && odd(Height)`

## Result

`entropy_image` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If
necessary, an exception is raised.

## Possible Successors

`disp_image`

## Alternatives

`entropy_gray`

## See also

`energy_gabor`,
`entropy_gray`

## Module

Foundation
