# GenDiscSe (Operator)

## Name

`GenDiscSe` — Generate ellipsoidal structuring elements for gray morphology.

## Signature

`static void HOperatorSet.GenDiscSe(out HObject SE, HTuple type, HTuple width, HTuple height, HTuple smax)`

`void HImage.GenDiscSe(string type, int width, int height, HTuple smax)`

`void HImage.GenDiscSe(string type, int width, int height, double smax)`

## Description

`GenDiscSe` generates an ellipsoidal structuring element
(*`SE`*) for gray morphology of images. The parameter
*`type`* determines the image type. It must match the image
type of the image to be processed in subsequent operator calls using
this structuring element. The parameters *`width`* and
*`height`* determine the length of the two major axes of the
ellipse. The value of *`smax`* determines the maximum gray
value of the structuring element. For the generation of arbitrary
structuring elements, see [`ReadGraySe`](read_gray_se.md). The structuring
element can be saved as image with the help of the operator
[`WriteImage`](write_image.md). However, take care to use an image format that
supports alpha channels to save the shape of the structuring element
such as 'tiff', 'jp2' or 'png'. These files can then be loaded
again with the operator [`ReadImage`](read_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SE`** (output_object)  image `→` [HImage](HImage.md) (byte / uint2 / real)

Generated structuring element.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Pixel type.

Default:
"byte"

List of values:
"byte", "real", "uint2"

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the structuring element.

Default:
5

Suggested values:
0, 1, 2, 3, 4, 5, 10, 15, 20

Value range:
`0
≤
width
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the structuring element.

Default:
5

Suggested values:
0, 1, 2, 3, 4, 5, 10, 15, 20

Value range:
`0
≤
height
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`smax`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum gray value of the structuring element.

Default:
0

Suggested values:
0, 1, 2, 5, 10, 20, 30, 40

## Result

`GenDiscSe` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
If necessary, an exception is raised.

## Possible Successors

`GrayErosion`,
`GrayDilation`,
`GrayOpening`,
`GrayClosing`,
`GrayTophat`,
`GrayBothat`,
`WriteImage`

## Alternatives

`ReadGraySe`,
`ReadImage`

## See also

`PaintRegion`,
`PaintGray`,
`CropPart`

## Module

Foundation
