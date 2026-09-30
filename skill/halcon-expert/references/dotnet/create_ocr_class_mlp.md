# CreateOcrClassMlp (Operator)

## Name

`CreateOcrClassMlp` — Create an OCR classifier using a multilayer perceptron.

## Signature

`static void HOperatorSet.CreateOcrClassMlp(HTuple widthCharacter, HTuple heightCharacter, HTuple interpolation, HTuple features, HTuple characters, HTuple numHidden, HTuple preprocessing, HTuple numComponents, HTuple randSeed, out HTuple OCRHandle)`

`public HOCRMlp(int widthCharacter, int heightCharacter, string interpolation, HTuple features, HTuple characters, int numHidden, string preprocessing, int numComponents, int randSeed)`

`public HOCRMlp(int widthCharacter, int heightCharacter, string interpolation, string features, HTuple characters, int numHidden, string preprocessing, int numComponents, int randSeed)`

`void HOCRMlp.CreateOcrClassMlp(int widthCharacter, int heightCharacter, string interpolation, HTuple features, HTuple characters, int numHidden, string preprocessing, int numComponents, int randSeed)`

`void HOCRMlp.CreateOcrClassMlp(int widthCharacter, int heightCharacter, string interpolation, string features, HTuple characters, int numHidden, string preprocessing, int numComponents, int randSeed)`

## Description

`CreateOcrClassMlp` creates an OCR classifier that uses a
multilayer perceptron (MLP). The handle of the OCR classifier is
returned in *`OCRHandle`*.

For a description on how an MLP works, see [`CreateClassMlp`](create_class_mlp.md).
`CreateOcrClassMlp` creates an MLP with
`outputFunction` = *"softmax"*. The length of the
feature vector of the MLP (`numInput` in
[`CreateClassMlp`](create_class_mlp.md)) is determined from the features that are
used for the OCR, which are passed in *`features`*. The
features are described below. The number of units in the hidden
layer is determined by *`numHidden`*. The number of output
variables of the MLP (`numOutput` in
[`CreateClassMlp`](create_class_mlp.md)) is determined from the names of the
characters to be used in the OCR, which are passed in
*`characters`*. As described with [`CreateClassMlp`](create_class_mlp.md),
the parameters *`preprocessing`* and *`numComponents`* can
be used to specify a preprocessing of the data (i.e., the feature
vectors). The OCR already approximately normalizes the features.
Hence, *`preprocessing`* can typically be set to
*"none"*. The parameter *`randSeed`* has the same
meaning as in [`CreateClassMlp`](create_class_mlp.md). Furthermore, like for
general MLP classifiers (see [`CreateClassMlp`](create_class_mlp.md) and
[`SetRegularizationParamsClassMlp`](set_regularization_params_class_mlp.md)), it may be desirable to
regularize OCR classifiers. This can be achieved by calling
[`SetRegularizationParamsOcrClassMlp`](set_regularization_params_ocr_class_mlp.md) before training the
OCR classifier. In addition, like for general MLP classifiers (see
[`CreateClassMlp`](create_class_mlp.md) and
[`SetRejectionParamsClassMlp`](set_rejection_params_class_mlp.md)), it might be desirable to
equip the OCR classifiers with the capability to reject unknown
characters. The rejection class is by convention an additional
symbol chr(26) that must be provided in *`characters`*. The
parameters of the rejection class can be set by calling
[`SetRejectionParamsOcrClassMlp`](set_rejection_params_ocr_class_mlp.md) before training the OCR
classifier.

The features to be used for the classification are determined by
*`features`*. *`features`* can contain a tuple of several
feature names. Each of these feature names results in one or more
features to be calculated for the classifier. Some of the feature
names compute gray value features (e.g., *"pixel_invar"*).
Because a classifier requires a constant number of features (input
variables), a character to be classified is transformed to a
standard size, which is determined by *`widthCharacter`* and
*`heightCharacter`*. The interpolation to be used for the
transformation is determined by *`interpolation`*. It has the
same meaning as in [`AffineTransImage`](affine_trans_image.md). The interpolation
should be chosen such that no aliasing effects occur in the
transformation. For most applications, *`interpolation`* =
*"constant"* should be used. It should be noted that the
size of the transformed character is not chosen too large, because
the generalization properties of the classifier may become bad for
large sizes. In particular, large sizes will lead to the fact that
small segmentation errors will have a large influence on the
computed features if gray value features are used. This happens
because segmentation errors will change the smallest enclosing
rectangle of the regions, which leads to the fact that the character
is zoomed differently than the characters in the training set. In
most applications, sizes between 6x8 and
10x14 should be used.

The parameter *`features`* can contain the following feature
names for the classification of the characters.

- ***"default"*** —

  *"ratio"* and *"pixel_invar"* are selected.
- ***"pixel"*** —

  Gray values of the character (*`widthCharacter`* x
  *`heightCharacter`* features).
- ***"pixel_invar"*** —

  Gray values of the character with maximum scaling of the gray
  values (*`widthCharacter`* x *`heightCharacter`*
  features).
- ***"pixel_binary"*** —

  Region of the character as a binary image zoomed to a size of
  *`widthCharacter`* x *`heightCharacter`*
  (*`widthCharacter`* x *`heightCharacter`*
  features).
- ***"gradient_8dir"*** —

  Gradients are computed on the character image. The gradient
  directions are discretized into 8 directions. The amplitude image
  is decomposed into 8 channels according to these discretized
  directions. 25 samples on a 5x5 grid are extracted from
  each channel. These samples are used as features (200 features).
- ***"projection_horizontal"*** —

  Horizontal projection of the gray values (see
  [`GrayProjections`](gray_projections.md), *`heightCharacter`* features).
- ***"projection_horizontal_invar"*** —

  Maximally scaled horizontal projection of the gray values
  (*`heightCharacter`* features).
- ***"projection_vertical"*** —

  Vertical projection of the gray values (see
  [`GrayProjections`](gray_projections.md), *`widthCharacter`* features).
- ***"projection_vertical_invar"*** —

  Maximally scaled vertical projection of the gray values
  (*`widthCharacter`* features).
- ***"ratio"*** —

  Aspect ratio of the character (see
  [`HeightWidthRatio`](height_width_ratio.md), 1 feature).
- ***"anisometry"*** —

  Anisometry of the character (see [`Eccentricity`](eccentricity.md), 1 feature).
- ***"width"*** —

  Width of the character before scaling the character to the standard
  size (not scale-invariant, see
  [`HeightWidthRatio`](height_width_ratio.md), 1 feature).
- ***"height"*** —

  Height of the character before scaling the character to the
  standard size (not scale-invariant, see
  [`HeightWidthRatio`](height_width_ratio.md), 1 feature).
- ***"zoom_factor"*** —

  Difference in size between the character and the values of
  *`widthCharacter`* and *`heightCharacter`* (not
  scale-invariant, 1 feature).
- ***"foreground"*** —

  Fraction of pixels in the foreground (1 feature).
- ***"foreground_grid_9"*** —

  Fraction of pixels in the foreground in a 3x3 grid within
  the smallest enclosing rectangle of the character (9 features).
- ***"foreground_grid_16"*** —

  Fraction of pixels in the foreground in a 4x4 grid within
  the smallest enclosing rectangle of the character (16 features).
- ***"compactness"*** —

  Compactness of the character (see [`Compactness`](compactness.md), 1 feature).
- ***"convexity"*** —

  Convexity of the character (see [`Convexity`](convexity.md), 1 feature).
- ***"moments_region_2nd_invar"*** —

  Normalized 2nd moments of the character (see
  [`MomentsRegion2ndInvar`](moments_region_2nd_invar.md), 3 features).
- ***"moments_region_2nd_rel_invar"*** —

  Normalized 2nd relative moments of the character (see
  [`MomentsRegion2ndRelInvar`](moments_region_2nd_rel_invar.md), 2 features).
- ***"moments_region_3rd_invar"*** —

  Normalized 3rd moments of the character (see
  [`MomentsRegion3rdInvar`](moments_region_3rd_invar.md), 4 features).
- ***"moments_central"*** —

  Normalized central moments of the character (see
  [`MomentsRegionCentral`](moments_region_central.md), 4 features).
- ***"moments_gray_plane"*** —

  Normalized gray value moments and the angle of the gray value
  plane (see [`MomentsGrayPlane`](moments_gray_plane.md), 4 features).
- ***"phi"*** —

  Sinus and cosinus of the orientation (angle) of the character
  (see [`EllipticAxis`](elliptic_axis.md), 2 feature).
- ***"num_connect"*** —

  Number of connected components (see [`ConnectAndHoles`](connect_and_holes.md), 1
  feature).
- ***"num_holes"*** —

  Number of holes (see [`ConnectAndHoles`](connect_and_holes.md), 1 feature).
- ***"cooc"*** —

  Values of the binary co-occurrence matrix (see
  [`GenCoocMatrix`](gen_cooc_matrix.md), 8 features).
- ***"num_runs"*** —

  Number of runs in the region normalized by the height (1 feature).
- ***"chord_histo"*** —

  Frequency of the runs per row (not scale-invariant,
  *`heightCharacter`* features).

After the classifier has been created, it is trained using
[`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md). After this, the classifier can be
saved using [`WriteOcrClassMlp`](write_ocr_class_mlp.md). Alternatively, the
classifier can be used immediately after training to classify
characters using [`DoOcrSingleClassMlp`](do_ocr_single_class_mlp.md) or
[`DoOcrMultiClassMlp`](do_ocr_multi_class_mlp.md).

HALCON provides a number of pretrained OCR classifiers (see the
`“Solution Guide I”`, chapter 'OCR', section 'Pretrained OCR
Fonts'). These
pretrained OCR classifiers can be read directly with
[`ReadOcrClassMlp`](read_ocr_class_mlp.md) and make it possible to read a wide
variety of different fonts without the need to train an OCR
classifier. Therefore, it is recommended to try if one of the
pretrained OCR classifiers can be used successfully. If this is the
case, it is not necessary to create and train an OCR classifier.

A comparison of the MLP and the support vector machine (SVM) (see
[`CreateOcrClassSvm`](create_ocr_class_svm.md)) typically shows that SVMs are
generally faster at training, especially for huge training sets, and
achieve slightly better recognition rates than MLPs. The MLP is
faster at classification and should therefore be preferred in time
critical applications. Please note that this guideline assumes
optimal tuning of the parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`widthCharacter`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
8

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`4
≤
widthCharacter
≤
20`

**`heightCharacter`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`4
≤
heightCharacter
≤
20`

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation mode for the zooming of the characters.

Default:
"constant"

List of values:
"bicubic", "bilinear", "constant", "nearest_neighbor", "weighted"

**`features`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Features to be used for classification.

Default:
"default"

List of values:
"anisometry", "chord_histo", "compactness", "convexity", "cooc", "default", "foreground", "foreground_grid_16", "foreground_grid_9", "gradient_8dir", "height", "moments_central", "moments_gray_plane", "moments_region_2nd_invar", "moments_region_2nd_rel_invar", "moments_region_3rd_invar", "num_connect", "num_holes", "num_runs", "phi", "pixel", "pixel_binary", "pixel_invar", "projection_horizontal", "projection_horizontal_invar", "projection_vertical", "projection_vertical_invar", "ratio", "width", "zoom_factor"

**`characters`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

All characters of the character set to be read.

Default:
["0","1","2","3","4","5","6","7","8","9"]

**`numHidden`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of hidden units of the MLP.

Default:
80

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 150

Restriction:
`NumHidden >= 1`

**`preprocessing`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

Default:
"none"

List of values:
"canonical_variates", "none", "normalization", "principal_components"

**`numComponents`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Preprocessing parameter: Number of transformed
features (ignored for *`preprocessing`* =
*"none"* and *`preprocessing`* =
*"normalization"*).

Default:
10

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumComponents >= 1`

**`randSeed`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Seed value of the random number generator that
is used to initialize the MLP with random values.

Default:
42

**`OCRHandle`** (output_control)  ocr_mlp `→` [HOCRMlp](HOCRMlp.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

## Example (HDevelop)

```
read_image (Image, 'letters')
* Segment the image.
binary_threshold(Image,&Region, 'otsu', 'dark', &UsedThreshold);
dilation_circle (Region, RegionDilation, 3.5)
connection (RegionDilation, ConnectedRegions)
intersection (ConnectedRegions, Region, RegionIntersection)
sort_region (RegionIntersection, Characters, 'character', 'true', 'row')
* Generate the training file.
count_obj (Characters, Number)
Classes := []
for J := 0 to 25 by 1
    Classes := [Classes,gen_tuple_const(20,chr(ord('a')+J))]
endfor
Classes := [Classes,gen_tuple_const(20,'.')]
write_ocr_trainf (Characters, Image, Classes, 'letters.trf')
* Generate and train the classifier.
read_ocr_trainf_names ('letters.trf', CharacterNames, CharacterCount)
create_ocr_class_mlp (8, 10, 'constant', 'default', CharacterNames, 20, \
                      'none', 81, 42, OCRHandle)
trainf_ocr_class_mlp (OCRHandle, 'letters.trf', 100, 0.01, 0.01, Error, \
                      ErrorLog)
* Re-classify the characters in the image.
do_ocr_multi_class_mlp (Characters, Image, OCRHandle, Class, Confidence)
```

## Result

If the parameters are valid, the operator
`CreateOcrClassMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Successors

`TrainfOcrClassMlp`,
`SetRegularizationParamsOcrClassMlp`,
`SetRejectionParamsOcrClassMlp`

## Alternatives

`CreateOcrClassSvm`

## See also

`DoOcrSingleClassMlp`,
`DoOcrMultiClassMlp`,
`ClearOcrClassMlp`,
`CreateClassMlp`,
`TrainClassMlp`,
`ClassifyClassMlp`

## Module

OCR/OCV
