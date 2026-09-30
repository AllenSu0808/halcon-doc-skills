# entropy_image (Operator)

## Name

`entropy_image` — Calculate the entropy of gray values within a rectangular window.

## Signature

`entropy_image(Image : ImageEntropy : Width, Height : )`

## Description

`entropy_image` calculates the entropy of gray values in the
image *`Image`* within a rectangular mask of size
(*`Height`*, *`Width`*). The resulting image is
returned in *`ImageEntropy`*, in which the entropy is
multiplied by 32. If the parameters *`Height`* and
*`Width`* are even, they are changed to the next larger odd
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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte)

Image for which the entropy is to be calculated.

**`ImageEntropy`** (output_object)  (multichannel-)image(-array) `→` object (byte)

Entropy image.

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the mask in which the entropy is calculated.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25

Restriction:
`3 <= Width && odd(Width)`

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the mask in which the entropy is calculated.

Default:
9

Suggested values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25

Restriction:
`3 <= Height && odd(Height)`

## Example (HDevelop)

```
read_image(Image,'fabrik')
dev_display(Image)
entropy_image(Image,Entropy,9,9)
dev_display(Entropy)
```

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
