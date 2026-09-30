# TextLineOrientation (Operator)

## Name

`TextLineOrientation` — Determines the orientation of a text line or paragraph.

## Signature

`static void HOperatorSet.TextLineOrientation(HObject region, HObject image, HTuple charHeight, HTuple orientationFrom, HTuple orientationTo, out HTuple orientationAngle)`

`HTuple HRegion.TextLineOrientation(HImage image, int charHeight, double orientationFrom, double orientationTo)`

## Description

`TextLineOrientation` determines the orientation of a single text
line or a paragraph in relation to the horizontal image axis. If the
orientation of a single text line should be determined, the range for the
*`orientationFrom`* and *`orientationTo`* should be in the interval
from -pi/4 to pi/4.

The parameter *`region`* specifies the area of the image in which the
text lines are located. The *`region`* is only used to reduce the
working area. To determine the slant, the gray values inside that area
are used.
The text lines are segmented by the operator `TextLineOrientation`
itself. If more than one region is passed, the numerical values of the
orientation angle are stored in a tuple, the position of a value in the
tuple corresponding to the position of the region in the input tuple.

*`charHeight`* specifies the approximately height of the existing text
lines in the region *`region`*. It's assumed, that the text lines are
darker than the background.

The search area can be restricted by the parameters *`orientationFrom`*
and *`orientationTo`*, whereby also the runtime of the operator is
influenced.

With the calculated angle *`orientationAngle`* and operators like
[`AffineTransImage`](affine_trans_image.md), the region *`region`* of the image
*`image`* can be rotated such, that the text lines lie horizontally
in the image. This may simplify the character segmentation for OCR
applications.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Area of text lines.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`charHeight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the text lines.

Default:
25

Value range:
`1
≤
charHeight`

Restriction:
`CharHeight >= 1`

**`orientationFrom`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Minimum rotation of the text lines.

Default:
-0.523599

Value range:
`-3.141593
≤
orientationFrom
≤
3.141593`

Restriction:
`OrientationFrom <= OrientationTo`

**`orientationTo`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Maximum rotation of the text lines.

Default:
0.523599

Value range:
`-3.141593
≤
orientationTo
≤
3.141593`

Restriction:
`OrientationFrom <= OrientationTo && OrientationTo < OrientationFrom + pi`

**`orientationAngle`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Calculated rotation angle of the text lines.

## Example (HDevelop)

```
read_image(Image,'letters')
text_line_orientation(Image,Image,50,rad(-80),rad(80),OrientationAngle)
rotate_image(Image,ImageRotate,-OrientationAngle/rad(180)*180,'constant')
```

## Result

If the input parameters are set correctly, the operator
`TextLineOrientation` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Successors

`RotateImage`,
`AffineTransImage`,
`AffineTransImageSize`

## Module

Foundation
