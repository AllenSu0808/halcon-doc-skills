# text_line_orientation (Operator)

## Name

`text_line_orientation` — Determines the orientation of a text line or paragraph.

## Signature

`text_line_orientation(Region, Image : : CharHeight, OrientationFrom, OrientationTo : OrientationAngle)`

## Description

`text_line_orientation` determines the orientation of a single text
line or a paragraph in relation to the horizontal image axis. If the
orientation of a single text line should be determined, the range for the
*`OrientationFrom`* and *`OrientationTo`* should be in the interval
from -pi/4 to pi/4.

The parameter *`Region`* specifies the area of the image in which the
text lines are located. The *`Region`* is only used to reduce the
working area. To determine the slant, the gray values inside that area
are used.
The text lines are segmented by the operator `text_line_orientation`
itself. If more than one region is passed, the numerical values of the
orientation angle are stored in a tuple, the position of a value in the
tuple corresponding to the position of the region in the input tuple.

*`CharHeight`* specifies the approximately height of the existing text
lines in the region *`Region`*. It's assumed, that the text lines are
darker than the background.

The search area can be restricted by the parameters *`OrientationFrom`*
and *`OrientationTo`*, whereby also the runtime of the operator is
influenced.

With the calculated angle *`OrientationAngle`* and operators like
[`affine_trans_image`](affine_trans_image.md), the region *`Region`* of the image
*`Image`* can be rotated such, that the text lines lie horizontally
in the image. This may simplify the character segmentation for OCR
applications.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Area of text lines.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`CharHeight`** (input_control)  integer `→`  (integer)

Height of the text lines.

Default:
25

Value range:
`1
≤
CharHeight`

Restriction:
`CharHeight >= 1`

**`OrientationFrom`** (input_control)  angle.rad `→`  (real)

Minimum rotation of the text lines.

Default:
-0.523599

Value range:
`-3.141593
≤
OrientationFrom
≤
3.141593`

Restriction:
`OrientationFrom <= OrientationTo`

**`OrientationTo`** (input_control)  angle.rad `→`  (real)

Maximum rotation of the text lines.

Default:
0.523599

Value range:
`-3.141593
≤
OrientationTo
≤
3.141593`

Restriction:
`OrientationFrom <= OrientationTo && OrientationTo < OrientationFrom + pi`

**`OrientationAngle`** (output_control)  angle.rad(-array) `→`  (real)

Calculated rotation angle of the text lines.

## Example (HDevelop)

```
read_image(Image,'letters')
text_line_orientation(Image,Image,50,rad(-80),rad(80),OrientationAngle)
rotate_image(Image,ImageRotate,-OrientationAngle/rad(180)*180,'constant')
```

## Result

If the input parameters are set correctly, the operator
`text_line_orientation` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Successors

`rotate_image`,
`affine_trans_image`,
`affine_trans_image_size`

## Module

Foundation
