# text_line_slant (Operator)

## Name

`text_line_slant` — Determines the slant of characters of a text line or paragraph.

## Signature

`def text_line_slant(region: HObject, image: HObject, char_height: int, slant_from: float, slant_to: float) -> Sequence[float]`

`def text_line_slant_s(region: HObject, image: HObject, char_height: int, slant_from: float, slant_to: float) -> float`

## Description

`text_line_slant` determines the slant of a single text line or a
paragraph.

The parameter *`region`* specifies the area of the image in which the
text lines are located. The *`region`* is only used to reduce the
working area. To determine the slant, the gray values inside that area
are used. The text lines are segmented by the operator
`text_line_slant` itself. If more than one region is passed, the
numerical values of the orientation angle are stored in a tuple, the
position of a value in the tuple corresponding to the position of the
region in the input tuple.

*`char_height`* specifies the approximately high of the existing text
lines in the region *`region`*. It's assumed, that the text lines are
darker than the background.

The search area can be restricted by the parameters *`slant_from`* and
*`slant_to`*, whereby also the runtime of the operator is influenced.

With the calculated slant angle *`slant_angle`* and operators for
affine transformations, the slant can be removed from the characters. This
may simplify the character separation for OCR applications. To work
correctly all characters of a region should have nearly the same slant.

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

**`slant_from`** (input_control)  angle.rad `→` float

Minimum slant of the characters

Default:
-0.523599

Value range:
`-0.785398
≤
slant_from
≤
0.785398`

Restriction:
`SlantFrom <= SlantTo`

**`slant_to`** (input_control)  angle.rad `→` float

Maximum slant of the characters

Default:
0.523599

Value range:
`-0.785398
≤
slant_to
≤
0.785398`

Restriction:
`SlantFrom <= SlantTo`

**`slant_angle`** (output_control)  angle.rad(-array) `→` Sequence[float]

Calculated slant of the characters in the region

## Example (HDevelop)

```
hom_mat2d_identity(HomMat2DIdentity)
read_image(Image,'dot_print_slanted')
* correct slant
text_line_slant(Image,Image,50,rad(-45),rad(45),SlantAngle)
hom_mat2d_slant(HomMat2DIdentity,-SlantAngle,'x',0,0,HomMat2DSlant)
affine_trans_image(Image,Image,HomMat2DSlant,'constant','true')
```

## Result

If the input parameters are set correctly, the operator
`text_line_slant` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Successors

`hom_mat2d_slant`,
`affine_trans_image`,
`affine_trans_image_size`

## Module

Foundation
