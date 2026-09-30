# CreateOcrClassBox (Operator)

## Name

`CreateOcrClassBox` — Create a new OCR-classifier.

## Warning

**`CreateOcrClassBox` is obsolete and is only provided for
reasons of backward compatibility. New applications should use the
MLP, SVM or CNN based operators instead.**

## Signature

`static void HOperatorSet.CreateOcrClassBox(HTuple widthPattern, HTuple heightPattern, HTuple interpolation, HTuple features, HTuple character, out HTuple ocrHandle)`

`public HOCRBox(int widthPattern, int heightPattern, int interpolation, HTuple features, HTuple character)`

`public HOCRBox(int widthPattern, int heightPattern, int interpolation, string features, HTuple character)`

`void HOCRBox.CreateOcrClassBox(int widthPattern, int heightPattern, int interpolation, HTuple features, HTuple character)`

`void HOCRBox.CreateOcrClassBox(int widthPattern, int heightPattern, int interpolation, string features, HTuple character)`

## Description

The operator `CreateOcrClassBox` creates a new OCR classifier.
This classifier must then be trained with the help of the operators
[`TraindOcrClassBox`](traind_ocr_class_box.md) or [`TrainfOcrClassBox`](trainf_ocr_class_box.md).

The parameters *`widthPattern`* and *`heightPattern`*
indicate the size of the input-layer of the network. This size is
used for the features *"projection_horizontal"*,
*"projection_vertical"*, *"pixel"*,
*"pixel_invar"*, and *"pixel_binary"* to transform the
character to a standard size. The bigger the standard size is, the
more characters can be distinguished. Hereby the amount of time
necessary for the training (as well as the number of training random
samples) and the time necessary for the recognition, however, will
increase as well. The parameter *`interpolation`* indicates
the interpolation mode concerning the adaptation of characters in
the image to the network. For more detailed information on this
parameter see also [`AffineTransImage`](affine_trans_image.md). The value *0*
results in the same interpolation as *"nearest_neighbor"* in
[`AffineTransImage`](affine_trans_image.md), i.e., no interpolation is performed.
For *1*, the same behavior as *"constant"* in
[`AffineTransImage`](affine_trans_image.md) is obtained, i.e., equally weighted
interpolation between adjacent pixels is used. Finally, *2*
results in the same interpolation as *"weighted"*, i.e.,
Gaussian interpolation between adjacent pixels is used. The
parameter *`interpolation`* must be chosen such that no
aliasing occurs when the character is scaled to the standard size.
Typically, this means that *`interpolation`* should be set to
*1*, except in cases where the characters are scaled down by
a large amount, in which case *`interpolation`* = *2*
should be chosen. *`interpolation`* = *0* should only
be chosen if the characters will not be scaled.

The parameter *`character`* determines all the characters
which have to be recognized. Normally the transmitted strings
consist of one character (e.g., alphabet). But also strings of
any length can be learned. The number of distinguishable
characters (number of strings in *`character`*) is limited
to *2048*.

The parameter *`features`* helps to chose additional
features besides gray values in order to recognize characters.

The following features are available:

- ***"default"*** —

  *"ratio"* and *"pixel_invar"* are selected.
- ***"ratio"*** —

  Ratio of the character.
- ***"width"*** —

  Width of the character (not invariant to scaling).
- ***"height"*** —

  Height of the character (not invariant to scaling).
- ***"zoom_factor"*** —

  Difference in size between the current character and the
  values of *`widthPattern`* and *`heightPattern`*
  (not invariant to scaling).
- ***"foreground"*** —

  Relative number of pixels in the foreground.
- ***"foreground_grid_9"*** —

  Relative number of foreground pixels in a 3x3 grid within
  the surrounding rectangle of the character.
- ***"foreground_grid_16"*** —

  Relative number of foreground pixels in a 4x4 grid within
  the surrounding rectangle of the character.
- ***"anisometry"*** —

  Form feature anisometry.
- ***"compactness"*** —

  Form feature compactness.
- ***"convexity"*** —

  Form feature convexity.
- ***"moments_region_2nd_invar"*** —

  Normed 2nd geometric moments of the region. See also
  [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md).
- ***"moments_region_2nd_rel_invar"*** —

  Normed 2nd relative geometric moments of the region. See also
  [`MomentsRegion2ndRelInvar`](moments_region_2nd_rel_invar.md).
- ***"moments_region_3rd_invar"*** —

  Normed 3rd geometric moments of the region. See also
  [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md).
- ***"moments_central"*** —

  Normed central geometric moments of the region. See also
  [`MomentsRegionCentral`](moments_region_central.md).
- ***"phi"*** —

  Sine and cosine of the orientation (angle) of the character.
- ***"num_connect"*** —

  Number of connecting components.
- ***"num_holes"*** —

  Number of holes.
- ***"projection_horizontal"*** —

  Horizontal projection of the gray values.
- ***"projection_horizontal_invar"*** —

  Horizontal projection of the gray values with are automatically
  scaled to maximum range.
- ***"projection_vertical"*** —

  Vertical projection of the gray values.
- ***"projection_vertical_invar"*** —

  Vertical projection of the gray values with are automatically
  scaled to maximum range.
- ***"cooc"*** —

  Values of the binary co-occurrence matrix.
- ***"moments_gray_plane"*** —

  Normed gray value moments and the angles of the gray value level.
- ***"num_runs"*** —

  Number of chords in the region normed to the height.
- ***"chord_histo"*** —

  Frequency of the chords per row (not scale-invariant).
- ***"pixel"*** —

  Gray value of the character.
- ***"pixel_invar"*** —

  Gray values of the character with automatic maximal scaling
  of the gray values.
- ***"pixel_binary"*** —

  Region of the character as a binary image zoomed to a size of
  *`widthPattern`* x *`heightPattern`*.
- ***"gradient_8dir"*** —

  Gradients are computed on the character image. The gradient
  directions are discretized into 8 directions. The amplitude image
  is decomposed into 8 channels according to these discretized
  directions. 25 samples on a 5x5 grid are extracted from
  each channel. These samples are used as features.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`widthPattern`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the input layer of the network.

Default:
8

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`1
≤
widthPattern
≤
100`

**`heightPattern`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the input layer of the network.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`1
≤
heightPattern
≤
100`

**`interpolation`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Interpolation mode concerning scaling of characters.

Default:
1

List of values:
0, 1, 2

**`features`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Additional features.

Default:
"default"

List of values:
"anisometry", "chord_histo", "compactness", "convexity", "cooc", "default", "foreground", "foreground_grid_16", "foreground_grid_9", "gradient_8dir", "height", "moments_central", "moments_gray_plane", "moments_region_2nd_invar", "moments_region_2nd_rel_invar", "moments_region_3rd_invar", "num_connect", "num_holes", "num_runs", "phi", "pixel", "pixel_binary", "pixel_invar", "projection_horizontal", "projection_horizontal_invar", "projection_vertical", "projection_vertical_invar", "ratio", "width", "zoom_factor"

**`character`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

All characters of a set.

Default:
["a","b","c"]

**`ocrHandle`** (output_control)  ocr_box `→` [HOCRBox](HOCRBox.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the created OCR classifier.

## Result

If the parameters are correct, the operator
`CreateOcrClassBox` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`ResetObjDb`

## Possible Successors

`TraindOcrClassBox`,
`TrainfOcrClassBox`,
`InfoOcrClassBox`,
`WriteOcr`,
`OcrChangeChar`

## Alternatives

`CreateOcrClassMlp`,
`CreateOcrClassSvm`

## See also

`AffineTransImage`,
`OcrChangeChar`,
`MomentsRegion2ndInvar`,
`MomentsRegion2ndRelInvar`,
`MomentsRegion3rdInvar`,
`MomentsRegionCentral`

## Module

OCR/OCV
