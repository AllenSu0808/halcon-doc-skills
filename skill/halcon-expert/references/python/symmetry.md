# symmetry (Operator)

## Name

`symmetry` — Symmetry of gray values along a row.

## Signature

`def symmetry(image: HObject, mask_size: int, direction: float, exponent: float) -> HObject`

## Description

`symmetry` calculates the symmetry along a line.
For each pixel the gray values of both sides of the line are
compared: The absolute value of the differences of gray values with
same distance to the pixel is computed. Each of these differences
is weighted by the exponent (after division by 255) and then
summed up.
$$sym := 255 - \frac{255}{MaskSize} \sum_{i=1}^{MaskSize} \left( \frac{g(i) - g(-i)}{255} \right)$$ ![figure](../assets/3a5092b79c42e0cd.svg)
Pixels with a high symmetry have large gray values.

## Attention

Currently only horizontal search lines are implemented.
Note that the parameter *`direction`* exists for future extensions and can
currently only have the value 0.0.

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

Input image.

**`image_symmetry`** (output_object)  (multichannel-)image(-array) `→` HObject (byte)

Symmetry image.

**`mask_size`** (input_control)  number `→` int

Extension of search area.

Default:
40

Suggested values:
3, 5, 7, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 100, 120, 140, 180

Value range:
`3
≤
mask_size
≤
1000`

Minimum increment:
1

Recommended increment:
2

**`direction`** (input_control)  number `→` float

Angle of test direction.

Default:
0.0

Suggested values:
0.0

Value range:
`0.0
≤
direction
≤
0.0`

**`exponent`** (input_control)  number `→` float

Exponent for weighting.

Default:
0.5

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 0.9, 1.0

Minimum increment:
0.01

Recommended increment:
0.1

Restriction:
`0 < Exponent && Exponent <= 100`

## Example (HDevelop)

```
read_image(Image,'monkey')
symmetry(Image,ImageSymmetry,70,0.0,0.5)
threshold(ImageSymmetry,SymmPoints,170,255)
```

## Result

If the parameter values are correct the operator `symmetry`
returns the value 2 (
H_MSG_TRUE)
The behavior in case of empty input (no input images available) is
set via the operator
`set_system(::'no_object_result',<Result>:)`.
If necessary an exception is raised.

## Possible Successors

`threshold`

## Module

Foundation
