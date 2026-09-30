# corner_response (Operator)

## Name

`corner_response` — Searching corners in images.

## Signature

`def corner_response(image: HObject, size: int, weight: float) -> HObject`

## Description

The operator `corner_response` extracts gray value corners in
an image. The formula for the calculation of the response is:
$$R(x,y) = A(x,y) \cdot B(x,y) - C^2(x,y) - Weight \cdot (A(x,y) + B(x,y))^2 \\ A(x,y) = W(u,v) * (\nabla_x I(x,y))^2 \\ abla_x I(x,y) abla_y I(x,y) ?$$ ![figure](../assets/17f1631a3255597f.svg)

with
I: input image,
R: output image of the filter,
A, and B: smoothed directional derivatives,
C: smoothing of the products of the directional derivatives.
The operator [`gauss_image`](gauss_image.md) is used for smoothing (W), the
operator [`sobel_amp`](sobel_amp.md) is used for calculating the
derivative $(\nabla)$.

The corner response function is invariant with regard to rotation.
In order to achieve a suitable dependency of the function R(x,y)
on the local gradient, the parameter *`weight`* must be set to
0.04. With this, only gray value corners will return positive
values for R(x,y), while straight edges will receive negative
values. The output image type is identical to the input image
type. Therefore, the negative output values are set to 0 if byte
images are used as input images. If this is not desired, the input
image should be converted into a real or int2 image with
[`convert_image_type`](convert_image_type.md).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2 / int2 / real)

Input image.

**`image_corner`** (output_object)  multichannel-image(-array) `→` HObject (byte / uint2 / int2 / real)

Result of the filtering.

Number of elements:
ImageCorner == Image

**`size`** (input_control)  integer `→` int

Desired filtersize of the graymask.

Default:
3

Suggested values:
3, 5, 7, 9, 11

**`weight`** (input_control)  real `→` float

Weighting.

Default:
0.04

Value range:
`0.0
≤
weight
≤
0.3`

Minimum increment:
0.001

Recommended increment:
0.01

## Example (C)

```
read_image(&Fabrik,"fabrik");
corner_response(Fabrik,&CornerResponse,3,0.04);
local_max(CornerResponse,&LocalMax);
disp_image(Fabrik,WindowHandle);
set_color(WindowHandle,"red");
disp_region(LocalMax,WindowHandle);
```

## Possible Successors

`local_max`,
`threshold`

## See also

`gauss_filter`,
`sobel_amp`,
`convert_image_type`

## References

C.G. Harris, M.J. Stephens,
“A combined corner and edge detector”';
Proc. of the 4th Alvey Vision Conference; August 1988; pp. 147-152.
  
H. Breit,
“Bestimmung der Kameraeigenbewegung und Gewinnung von
Tiefendaten aus monokularen Bildfolgen”;
Diplomarbeit am Lehrstuhl für Nachrichtentechnik der TU München;
30. September 1990.

## Module

Foundation
