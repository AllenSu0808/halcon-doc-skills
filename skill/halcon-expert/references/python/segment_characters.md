# segment_characters (Operator)

## Name

`segment_characters` — Segments characters in a given region of an image.

## Signature

`def segment_characters(region: HObject, image: HObject, method: str, eliminate_lines: str, dot_print: str, stroke_width: str, char_width: Sequence[int], char_height: Sequence[int], threshold_offset: int, contrast: int) -> Tuple[HObject, HObject, Sequence[int]]`

`def segment_characters_s(region: HObject, image: HObject, method: str, eliminate_lines: str, dot_print: str, stroke_width: str, char_width: Sequence[int], char_height: Sequence[int], threshold_offset: int, contrast: int) -> Tuple[HObject, HObject, int]`

## Description

This operator is used to segment characters in a given *`region`* of an
*`image`*. The *`region`* is only used to reduce the working area.
The segmented characters are returned in *`region_foreground`*.

Two different methods to detect the characters are supplied.
All segmentation methods assume that the text is darker than the
background. If this is not the case, please invert the image with
[`invert_image`](invert_image.md).

The parameter *`method`* determines the algorithm for text
segmentation. The possible values are

- ***"local_contrast_best"*** —

  This method extracts text that differ locally from the
  background. Therefore, it is suited for images with
  inhomogeneous illumination. The enhancement of the text
  borders, leads to a more accurate determination of the
  outline of the text. Which is especially useful if the
  background is highly textured. The parameter
  *`contrast`* defines the minimum contrast,i.e.,
  the minimum gray value difference between symbols and
  background.
- ***"local_auto_shape"*** —

  The minimum contrast is estimated automatically such
  that the number of very small regions is reduced. This
  method is especially suitable for noisy images. The
  parameter *`threshold_offset`* can be used to adjust
  the threshold.
  Let g(x,y) be the gray value at position (x,y) in the
  input *`image`*. The threshold condition is
  determined by:

  $$g(x,y)\le\texttt{UsedThreshold}+\texttt{ThresholdOffset}$$.

Select *`eliminate_lines`* if the extraction of characters is disturbed
by lines that are horizontal or vertical with respect to the lines of
text and set its value to *"true"*. The elimination is influenced by the
maximum of *`char_width`* and the maximum of *`char_height`*.
For further information see the description of these parameters.

*`dot_print`*:
Should be set to *"true"* if dot prints should be read, else to
*"false"*.

*`stroke_width`*:
Specifies the stroke width of the text. It is used to calculate internally
used mask sizes to determine the characters. This mask sizes are also
influenced through the parameters *`dot_print`*, the average
*`char_width`*, and the average *`char_height`*.

*`char_width`*:
This can be a tuple with up to three values. The first value is the
average width of a character. The second is the minimum width of a
character and the third is the maximum width of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on the average *`char_width`*. The same is
the case if the maximum is not set. Some examples:

[10] sets the average character width to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character width to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] sets the average character width to 10, the minimum to 5,
and the maximum to 20.

*`char_height`*:
This can be a tuple with up to three values. The first value is the
average height of a character. The second is the minimum height of a
character and the third is the maximum height of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on the average *`char_height`*. The same is
the case if the maximum is not set. Some examples:

[10] sets the average character height to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character height to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] this sets the average character height to 10, the minimum to 5,
and the maximum to 20.

*`threshold_offset`*:
This parameter can be used to adjust the threshold, which is used when the
segmentation method *"local_auto_shape"* is chosen.

*`contrast`*:
Defines the minimum contrast between the text and the background. This
parameter is used if the segmentation method *"local_contrast_best"*
is selected.

*`used_threshold`*:
After the execution, this parameter returns the threshold used to
segment the characters.

*`image_foreground`* returns the image that was internally used for the
segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Area in the image where the text lines are located.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image.

**`image_foreground`** (output_object)  image(-array) `→` HObject (byte / uint2)

Image used for the segmentation.

**`region_foreground`** (output_object)  singlechannelregion(-array) `→` HObject

Region of characters.

**`method`** (input_control)  string `→` str

Method to segment the characters.

Default:
"local_auto_shape"

List of values:
"local_auto_shape", "local_contrast_best"

**`eliminate_lines`** (input_control)  string `→` str

Eliminate horizontal and vertical lines?

Default:
"false"

List of values:
"false", "true"

**`dot_print`** (input_control)  string `→` str

Should dot print characters be detected?

Default:
"false"

List of values:
"false", "true"

**`stroke_width`** (input_control)  string `→` str

Stroke width of a character.

Default:
"medium"

List of values:
"bold", "light", "medium", "ultra_light"

**`char_width`** (input_control)  integer-array `→` Sequence[int]

Width of a character.

Default:
25

Value range:
`1
≤
char_width`

**`char_height`** (input_control)  integer-array `→` Sequence[int]

Height of a character.

Default:
25

Value range:
`1
≤
char_height`

**`threshold_offset`** (input_control)  integer `→` int

Value to adjust the segmentation.

Default:
0

**`contrast`** (input_control)  integer `→` int

Minimum gray value difference between text and
background.

Default:
10

**`used_threshold`** (output_control)  integer(-array) `→` Sequence[int]

Threshold used to segment the characters.

## Example (HDevelop)

```
for Index := 1 to 5 by 1
  read_image (Image, 'dot_print_rotated/dot_print_rotated_'+Index$'02d')
  text_line_orientation (Image, Image, 50, rad(-30), rad(30), \
                         OrientationAngle)
  rotate_image (Image, ImageRotate, deg(-OrientationAngle), 'constant')
  segment_characters (ImageRotate, ImageRotate, ImageForeground, \
                      RegionForeground, 'local_auto_shape', 'false', \
                      'false', 'medium', 25, 25, 0, 10, UsedThreshold)
endfor
```

## Result

If the input parameters are set correctly, the operator
`segment_characters` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception will be raised.

## Possible Predecessors

`text_line_orientation`

## Possible Successors

`select_characters`,
`connection`

## Alternatives

`threshold`

## Module

Foundation
