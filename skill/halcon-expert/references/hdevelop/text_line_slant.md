# text_line_slant (Operator)

## Name

`text_line_slant` — Determines the slant of characters of a text line or paragraph.

## Signature

`text_line_slant(Region, Image : : CharHeight, SlantFrom, SlantTo : SlantAngle)`

## Description

`text_line_slant` determines the slant of a single text line or a
paragraph.

The parameter *`Region`* specifies the area of the image in which the
text lines are located. The *`Region`* is only used to reduce the
working area. To determine the slant, the gray values inside that area
are used. The text lines are segmented by the operator
`text_line_slant` itself. If more than one region is passed, the
numerical values of the orientation angle are stored in a tuple, the
position of a value in the tuple corresponding to the position of the
region in the input tuple.

*`CharHeight`* specifies the approximately high of the existing text
lines in the region *`Region`*. It's assumed, that the text lines are
darker than the background.

The search area can be restricted by the parameters *`SlantFrom`* and
*`SlantTo`*, whereby also the runtime of the operator is influenced.

With the calculated slant angle *`SlantAngle`* and operators for
affine transformations, the slant can be removed from the characters. This
may simplify the character separation for OCR applications. To work
correctly all characters of a region should have nearly the same slant.

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

**`SlantFrom`** (input_control)  angle.rad `→`  (real)

Minimum slant of the characters

Default:
-0.523599

Value range:
`-0.785398
≤
SlantFrom
≤
0.785398`

Restriction:
`SlantFrom <= SlantTo`

**`SlantTo`** (input_control)  angle.rad `→`  (real)

Maximum slant of the characters

Default:
0.523599

Value range:
`-0.785398
≤
SlantTo
≤
0.785398`

Restriction:
`SlantFrom <= SlantTo`

**`SlantAngle`** (output_control)  angle.rad(-array) `→`  (real)

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
