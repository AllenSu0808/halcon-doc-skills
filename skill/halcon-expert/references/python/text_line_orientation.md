# text_line_orientation (Operator)

## Name

`text_line_orientation` — Determines the orientation of a text line or paragraph.

## Signature

`def text_line_orientation(region: HObject, image: HObject, char_height: int, orientation_from: float, orientation_to: float) -> Sequence[float]`

`def text_line_orientation_s(region: HObject, image: HObject, char_height: int, orientation_from: float, orientation_to: float) -> float`

## Description

`text_line_orientation` determines the orientation of a single text
line or a paragraph in relation to the horizontal image axis. If the
orientation of a single text line should be determined, the range for the
*`orientation_from`* and *`orientation_to`* should be in the interval
from -pi/4 to pi/4.

The parameter *`region`* specifies the area of the image in which the
text lines are located. The *`region`* is only used to reduce the
working area. To determine the slant, the gray values inside that area
are used.
The text lines are segmented by the operator `text_line_orientation`
itself. If more than one region is passed, the numerical values of the
orientation angle are stored in a tuple, the position of a value in the
tuple corresponding to the position of the region in the input tuple.

*`char_height`* specifies the approximately height of the existing text
lines in the region *`region`*. It's assumed, that the text lines are
darker than the background.

The search area can be restricted by the parameters *`orientation_from`*
and *`orientation_to`*, whereby also the runtime of the operator is
influenced.

With the calculated angle *`orientation_angle`* and operators like
[`affine_trans_image`](affine_trans_image.md), the region *`region`* of the image
*`image`* can be rotated such, that the text lines lie horizontally
in the image. This may simplify the character segmentation for OCR
applications.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Area of text lines.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image.

**`char_height`** (input_control)  integer `→` int

Height of the text lines.

Default:
25

Value range:
`1
≤
char_height`

Restriction:
`CharHeight >= 1`

**`orientation_from`** (input_control)  angle.rad `→` float

Minimum rotation of the text lines.

Default:
-0.523599

Value range:
`-3.141593
≤
orientation_from
≤
3.141593`

Restriction:
`OrientationFrom <= OrientationTo`

**`orientation_to`** (input_control)  angle.rad `→` float

Maximum rotation of the text lines.

Default:
0.523599

Value range:
`-3.141593
≤
orientation_to
≤
3.141593`

Restriction:
`OrientationFrom <= OrientationTo && OrientationTo < OrientationFrom + pi`

**`orientation_angle`** (output_control)  angle.rad(-array) `→` Sequence[float]

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
