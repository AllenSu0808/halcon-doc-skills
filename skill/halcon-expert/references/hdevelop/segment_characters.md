# segment_characters (Operator)

## Name

`segment_characters` — Segments characters in a given region of an image.

## Signature

`segment_characters(Region, Image : ImageForeground, RegionForeground : Method, EliminateLines, DotPrint, StrokeWidth, CharWidth, CharHeight, ThresholdOffset, Contrast : UsedThreshold)`

## Description

This operator is used to segment characters in a given *`Region`* of an
*`Image`*. The *`Region`* is only used to reduce the working area.
The segmented characters are returned in *`RegionForeground`*.

Two different methods to detect the characters are supplied.
All segmentation methods assume that the text is darker than the
background. If this is not the case, please invert the image with
[`invert_image`](invert_image.md).

The parameter *`Method`* determines the algorithm for text
segmentation. The possible values are

- ***'local_contrast_best'*** —

  This method extracts text that differ locally from the
  background. Therefore, it is suited for images with
  inhomogeneous illumination. The enhancement of the text
  borders, leads to a more accurate determination of the
  outline of the text. Which is especially useful if the
  background is highly textured. The parameter
  *`Contrast`* defines the minimum contrast,i.e.,
  the minimum gray value difference between symbols and
  background.
- ***'local_auto_shape'*** —

  The minimum contrast is estimated automatically such
  that the number of very small regions is reduced. This
  method is especially suitable for noisy images. The
  parameter *`ThresholdOffset`* can be used to adjust
  the threshold.
  Let g(x,y) be the gray value at position (x,y) in the
  input *`Image`*. The threshold condition is
  determined by:

  $$g(x,y)\le\texttt{UsedThreshold}+\texttt{ThresholdOffset}$$.

Select *`EliminateLines`* if the extraction of characters is disturbed
by lines that are horizontal or vertical with respect to the lines of
text and set its value to *'true'*. The elimination is influenced by the
maximum of *`CharWidth`* and the maximum of *`CharHeight`*.
For further information see the description of these parameters.

*`DotPrint`*:
Should be set to *'true'* if dot prints should be read, else to
*'false'*.

*`StrokeWidth`*:
Specifies the stroke width of the text. It is used to calculate internally
used mask sizes to determine the characters. This mask sizes are also
influenced through the parameters *`DotPrint`*, the average
*`CharWidth`*, and the average *`CharHeight`*.

*`CharWidth`*:
This can be a tuple with up to three values. The first value is the
average width of a character. The second is the minimum width of a
character and the third is the maximum width of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on the average *`CharWidth`*. The same is
the case if the maximum is not set. Some examples:

[10] sets the average character width to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character width to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] sets the average character width to 10, the minimum to 5,
and the maximum to 20.

*`CharHeight`*:
This can be a tuple with up to three values. The first value is the
average height of a character. The second is the minimum height of a
character and the third is the maximum height of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on the average *`CharHeight`*. The same is
the case if the maximum is not set. Some examples:

[10] sets the average character height to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character height to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] this sets the average character height to 10, the minimum to 5,
and the maximum to 20.

*`ThresholdOffset`*:
This parameter can be used to adjust the threshold, which is used when the
segmentation method *'local_auto_shape'* is chosen.

*`Contrast`*:
Defines the minimum contrast between the text and the background. This
parameter is used if the segmentation method *'local_contrast_best'*
is selected.

*`UsedThreshold`*:
After the execution, this parameter returns the threshold used to
segment the characters.

*`ImageForeground`* returns the image that was internally used for the
segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Area in the image where the text lines are located.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`ImageForeground`** (output_object)  image(-array) `→` object (byte / uint2)

Image used for the segmentation.

**`RegionForeground`** (output_object)  singlechannelregion(-array) `→` object

Region of characters.

**`Method`** (input_control)  string `→`  (string)

Method to segment the characters.

Default:
'local_auto_shape'

List of values:
'local_auto_shape', 'local_contrast_best'

**`EliminateLines`** (input_control)  string `→`  (string)

Eliminate horizontal and vertical lines?

Default:
'false'

List of values:
'false', 'true'

**`DotPrint`** (input_control)  string `→`  (string)

Should dot print characters be detected?

Default:
'false'

List of values:
'false', 'true'

**`StrokeWidth`** (input_control)  string `→`  (string)

Stroke width of a character.

Default:
'medium'

List of values:
'bold', 'light', 'medium', 'ultra_light'

**`CharWidth`** (input_control)  integer-array `→`  (integer)

Width of a character.

Default:
25

Value range:
`1
≤
CharWidth`

**`CharHeight`** (input_control)  integer-array `→`  (integer)

Height of a character.

Default:
25

Value range:
`1
≤
CharHeight`

**`ThresholdOffset`** (input_control)  integer `→`  (integer)

Value to adjust the segmentation.

Default:
0

**`Contrast`** (input_control)  integer `→`  (integer)

Minimum gray value difference between text and
background.

Default:
10

**`UsedThreshold`** (output_control)  integer(-array) `→`  (integer)

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
