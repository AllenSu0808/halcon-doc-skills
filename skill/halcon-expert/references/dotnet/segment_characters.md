# SegmentCharacters (Operator)

## Name

`SegmentCharacters` — Segments characters in a given region of an image.

## Signature

`static void HOperatorSet.SegmentCharacters(HObject region, HObject image, out HObject imageForeground, out HObject regionForeground, HTuple method, HTuple eliminateLines, HTuple dotPrint, HTuple strokeWidth, HTuple charWidth, HTuple charHeight, HTuple thresholdOffset, HTuple contrast, out HTuple usedThreshold)`

`HImage HRegion.SegmentCharacters(HImage image, out HRegion regionForeground, string method, string eliminateLines, string dotPrint, string strokeWidth, HTuple charWidth, HTuple charHeight, int thresholdOffset, int contrast, out HTuple usedThreshold)`

`HImage HRegion.SegmentCharacters(HImage image, out HRegion regionForeground, string method, string eliminateLines, string dotPrint, string strokeWidth, HTuple charWidth, HTuple charHeight, int thresholdOffset, int contrast, out int usedThreshold)`

## Description

This operator is used to segment characters in a given *`region`* of an
*`image`*. The *`region`* is only used to reduce the working area.
The segmented characters are returned in *`regionForeground`*.

Two different methods to detect the characters are supplied.
All segmentation methods assume that the text is darker than the
background. If this is not the case, please invert the image with
[`InvertImage`](invert_image.md).

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
  parameter *`thresholdOffset`* can be used to adjust
  the threshold.
  Let g(x,y) be the gray value at position (x,y) in the
  input *`image`*. The threshold condition is
  determined by:

  $$g(x,y)\le\texttt{UsedThreshold}+\texttt{ThresholdOffset}$$.

Select *`eliminateLines`* if the extraction of characters is disturbed
by lines that are horizontal or vertical with respect to the lines of
text and set its value to *"true"*. The elimination is influenced by the
maximum of *`charWidth`* and the maximum of *`charHeight`*.
For further information see the description of these parameters.

*`dotPrint`*:
Should be set to *"true"* if dot prints should be read, else to
*"false"*.

*`strokeWidth`*:
Specifies the stroke width of the text. It is used to calculate internally
used mask sizes to determine the characters. This mask sizes are also
influenced through the parameters *`dotPrint`*, the average
*`charWidth`*, and the average *`charHeight`*.

*`charWidth`*:
This can be a tuple with up to three values. The first value is the
average width of a character. The second is the minimum width of a
character and the third is the maximum width of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on the average *`charWidth`*. The same is
the case if the maximum is not set. Some examples:

[10] sets the average character width to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character width to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] sets the average character width to 10, the minimum to 5,
and the maximum to 20.

*`charHeight`*:
This can be a tuple with up to three values. The first value is the
average height of a character. The second is the minimum height of a
character and the third is the maximum height of a character.
If the minimum is not set or equal -1, the operator automatically sets
these value depending on the average *`charHeight`*. The same is
the case if the maximum is not set. Some examples:

[10] sets the average character height to 10, the minimum and
maximum are calculated by the operator.

[10,-1,20] sets the average character height to 10, the minimum value is
calculated by the system, and the maximum is set to 20.

[10,5,20] this sets the average character height to 10, the minimum to 5,
and the maximum to 20.

*`thresholdOffset`*:
This parameter can be used to adjust the threshold, which is used when the
segmentation method *"local_auto_shape"* is chosen.

*`contrast`*:
Defines the minimum contrast between the text and the background. This
parameter is used if the segmentation method *"local_contrast_best"*
is selected.

*`usedThreshold`*:
After the execution, this parameter returns the threshold used to
segment the characters.

*`imageForeground`* returns the image that was internally used for the
segmentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Area in the image where the text lines are located.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`imageForeground`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / uint2)

Image used for the segmentation.

**`regionForeground`** (output_object)  singlechannelregion(-array) `→` [HRegion](HRegion.md)

Region of characters.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method to segment the characters.

Default:
"local_auto_shape"

List of values:
"local_auto_shape", "local_contrast_best"

**`eliminateLines`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Eliminate horizontal and vertical lines?

Default:
"false"

List of values:
"false", "true"

**`dotPrint`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should dot print characters be detected?

Default:
"false"

List of values:
"false", "true"

**`strokeWidth`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Stroke width of a character.

Default:
"medium"

List of values:
"bold", "light", "medium", "ultra_light"

**`charWidth`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Width of a character.

Default:
25

Value range:
`1
≤
charWidth`

**`charHeight`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Height of a character.

Default:
25

Value range:
`1
≤
charHeight`

**`thresholdOffset`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Value to adjust the segmentation.

Default:
0

**`contrast`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum gray value difference between text and
background.

Default:
10

**`usedThreshold`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

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
`SegmentCharacters` returns the value 2 (
H_MSG_TRUE)
. Otherwise an
exception will be raised.

## Possible Predecessors

`TextLineOrientation`

## Possible Successors

`SelectCharacters`,
`Connection`

## Alternatives

`Threshold`

## Module

Foundation
