# gen_disc_se (Operator)

## Name

`gen_disc_se` — Generate ellipsoidal structuring elements for gray morphology.

## Signature

`gen_disc_se( : SE : Type, Width, Height, Smax : )`

## Description

`gen_disc_se` generates an ellipsoidal structuring element
(*`SE`*) for gray morphology of images. The parameter
*`Type`* determines the image type. It must match the image
type of the image to be processed in subsequent operator calls using
this structuring element. The parameters *`Width`* and
*`Height`* determine the length of the two major axes of the
ellipse. The value of *`Smax`* determines the maximum gray
value of the structuring element. For the generation of arbitrary
structuring elements, see [`read_gray_se`](read_gray_se.md). The structuring
element can be saved as image with the help of the operator
[`write_image`](write_image.md). However, take care to use an image format that
supports alpha channels to save the shape of the structuring element
such as 'tiff', 'jp2' or 'png'. These files can then be loaded
again with the operator [`read_image`](read_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SE`** (output_object)  image `→` object (byte / uint2 / real)

Generated structuring element.

**`Type`** (input_control)  string `→`  (string)

Pixel type.

Default:
'byte'

List of values:
'byte', 'real', 'uint2'

**`Width`** (input_control)  integer `→`  (integer)

Width of the structuring element.

Default:
5

Suggested values:
0, 1, 2, 3, 4, 5, 10, 15, 20

Value range:
`0
≤
Width
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Height`** (input_control)  integer `→`  (integer)

Height of the structuring element.

Default:
5

Suggested values:
0, 1, 2, 3, 4, 5, 10, 15, 20

Value range:
`0
≤
Height
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Smax`** (input_control)  number `→`  (real / integer)

Maximum gray value of the structuring element.

Default:
0

Suggested values:
0, 1, 2, 5, 10, 20, 30, 40

## Result

`gen_disc_se` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`gray_erosion`,
`gray_dilation`,
`gray_opening`,
`gray_closing`,
`gray_tophat`,
`gray_bothat`,
`write_image`

## Alternatives

`read_gray_se`,
`read_image`

## See also

`paint_region`,
`paint_gray`,
`crop_part`

## Module

Foundation
