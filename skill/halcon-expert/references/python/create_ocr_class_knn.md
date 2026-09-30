# create_ocr_class_knn (Operator)

## Name

`create_ocr_class_knn` — Create an OCR classifier using a k-Nearest Neighbor (k-NN) classifier.

## Signature

`def create_ocr_class_knn(width_character: int, height_character: int, interpolation: str, features: MaybeSequence[str], characters: Sequence[str], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, str]]) -> HHandle`

## Description

`create_ocr_class_knn` creates an OCR classifier that uses a
k-Nearest Neighbor (k-NN). The handle of the k-NN classifier is
returned in *`ocrhandle`*.

For a description on how a k-NN works, see [`create_class_knn`](create_class_knn.md).

The length of the feature vector of the k-NN is determined from the
features that are used for the OCR, which are passed in *`features`*.
The features are described below. The number of classes is determined
from the names of the characters which are passed in *`characters`*.

*`features`* can contain a tuple of several
feature names. Each of these names results in one or more
features to be calculated for the classifier. Some of the feature
names compute gray value features (e.g., *"pixel_invar"*).
Because a classifier requires a constant number of features (input
variables), a character to be classified is transformed to a
standard size, which is determined by *`width_character`* and
*`height_character`*. The interpolation to be used for the
transformation is determined by *`interpolation`*. It has the
same meaning as in [`affine_trans_image`](affine_trans_image.md). The interpolation
should be chosen such that no aliasing effects occur in the
transformation. For most applications, *`interpolation`* =
*"constant"* should be used. It should be noted that the
size of the transformed character is not chosen too large, because
the generalization properties of the classifier may become bad for
large sizes. In particular, large sizes will cause
small segmentation errors to have a large influence on the
computed features if gray value features are used. This happens
because segmentation errors will change the smallest enclosing
rectangle of the regions, which results in characters
are zoomed differently than the characters in the training set. In
most applications, sizes between 6x8 and
10x14 should be used.

The parameter *`features`* can contain the following feature
names for the classification of the characters.

- ***"default"*:** —

  *"ratio"* and *"pixel_invar"* are selected.
- ***"pixel"*:** —

  Gray values of the character (*`width_character`* x
  *`height_character`* features).
- ***"pixel_invar"*:** —

  Gray values of the character with maximum scaling of the gray
  values (*`width_character`* x *`height_character`*
  features).
- ***"pixel_binary"*:** —

  Region of the character as a binary image zoomed to a size of
  *`width_character`* x *`height_character`*
  (*`width_character`* x *`height_character`*
  features).
- ***"gradient_8dir"*:** —

  Gradients are computed on the character image. The gradient
  directions are discretized into 8 directions. The amplitude image
  is decomposed into 8 channels according to these discretized
  directions. 25 samples on a 5x5 grid are extracted from
  each channel. These samples are used as features (200 features).
- ***"projection_horizontal"*:** —

  Horizontal projection of the gray values (see
  [`gray_projections`](gray_projections.md), *`height_character`* features).
- ***"projection_horizontal_invar"*:** —

  Maximally scaled horizontal projection of the gray values
  (*`height_character`* features).
- ***"projection_vertical"*:** —

  Vertical projection of the gray values (see
  [`gray_projections`](gray_projections.md), *`width_character`* features).
- ***"projection_vertical_invar"*:** —

  Maximally scaled vertical projection of the gray values
  (*`width_character`* features).
- ***"ratio"*:** —

  Aspect ratio of the character (see
  [`height_width_ratio`](height_width_ratio.md), 1 feature).
- ***"anisometry"*:** —

  Anisometry of the character (see [`eccentricity`](eccentricity.md), 1 feature).
- ***"width"*:** —

  Width of the character before scaling the character to the
  standard size (not scale-invariant, see
  [`height_width_ratio`](height_width_ratio.md), 1 feature).
- ***"height"*:** —

  Height of the character before scaling the character to the
  standard size (not scale-invariant, see
  [`height_width_ratio`](height_width_ratio.md), 1 feature).
- ***"zoom_factor"*:** —

  Difference in size between the character and the values
  *`width_character`* and *`height_character`* (not
  scale-invariant, 1 feature).
- ***"foreground"*:** —

  Fraction of pixels in the foreground (1 feature).
- ***"foreground_grid_9"*:** —

  Fraction of pixels in the foreground in a 3x3 grid within
  the smallest enclosing rectangle of the character (9 features).
- ***"foreground_grid_16"*:** —

  Fraction of pixels in the foreground in a 4x4 grid within
  the smallest enclosing rectangle of the character (16 features).
- ***"compactness"*:** —

  Compactness of the character (see [`compactness`](compactness.md), 1 feature).
- ***"convexity"*:** —

  Convexity of the character (see [`convexity`](convexity.md), 1 feature).
- ***"moments_region_2nd_invar"*:** —

  Normalized 2nd moments of the character (see
  [`moments_region_2nd_invar`](moments_region_2nd_invar.md), 3 features).
- ***"moments_region_2nd_rel_invar"*:** —

  Normalized 2nd relative moments of the character (see
  [`moments_region_2nd_rel_invar`](moments_region_2nd_rel_invar.md), 2 features).
- ***"moments_region_3rd_invar"*:** —

  Normalized 3rd moments of the character (see
  [`moments_region_3rd_invar`](moments_region_3rd_invar.md), 4 features).
- ***"moments_central"*:** —

  Normalized central moments of the character (see
  [`moments_region_central`](moments_region_central.md), 4 features).
- ***"moments_gray_plane"*:** —

  Normalized gray value moments and the angle of the gray value
  plane (see [`moments_gray_plane`](moments_gray_plane.md), 4 features).
- ***"phi"*:** —

  Sinus and cosinus of the orientation (angle) of the character
  (see [`elliptic_axis`](elliptic_axis.md), 2 feature).
- ***"num_connect"*:** —

  Number of connected components (see [`connect_and_holes`](connect_and_holes.md), 1
  feature).
- ***"num_holes"*:** —

  Number of holes (see [`connect_and_holes`](connect_and_holes.md), 1 feature).
- ***"cooc"*:** —

  Values of the binary co-occurrence matrix (see
  [`gen_cooc_matrix`](gen_cooc_matrix.md), 8 features).
- ***"num_runs"*:** —

  Number of runs in the region normalized by the height (1 feature).
- ***"chord_histo"*:** —

  Frequency of the runs per row (not scale-invariant,
  *`height_character`* features).

After the classifier has been created, it is trained using
[`trainf_ocr_class_knn`](trainf_ocr_class_knn.md). After this, the classifier can be
saved using [`write_ocr_class_knn`](write_ocr_class_knn.md). Alternatively, the
classifier can be used immediately after training to classify
characters using [`do_ocr_single_class_knn`](do_ocr_single_class_knn.md) or
[`do_ocr_multi_class_knn`](do_ocr_multi_class_knn.md).

A comparison of the k-NN and the support vector machine (SVM) (see
[`create_ocr_class_svm`](create_ocr_class_svm.md)) typically shows that SVMs are
generally slower at training, especially for huge training sets, but
achieve slightly better recognition rates than k-NNs. Please note that
this guideline assumes optimal tuning of the parameters of the SVM.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`width_character`** (input_control)  integer `→` int

Width of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
8

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`4
≤
width_character
≤
20`

**`height_character`** (input_control)  integer `→` int

Height of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`4
≤
height_character
≤
20`

**`interpolation`** (input_control)  string `→` str

Interpolation mode for the zooming of the characters.

Default:
"constant"

List of values:
"bicubic", "bilinear", "constant", "nearest_neighbor", "weighted"

**`features`** (input_control)  string(-array) `→` MaybeSequence[str]

Features to be used for classification.

Default:
"default"

List of values:
"anisometry", "chord_histo", "compactness", "convexity", "cooc", "default", "foreground", "foreground_grid_16", "foreground_grid_9", "gradient_8dir", "height", "moments_central", "moments_gray_plane", "moments_region_2nd_invar", "moments_region_2nd_rel_invar", "moments_region_3rd_invar", "num_connect", "num_holes", "num_runs", "phi", "pixel", "pixel_binary", "pixel_invar", "projection_horizontal", "projection_horizontal_invar", "projection_vertical", "projection_vertical_invar", "ratio", "width", "zoom_factor"

**`characters`** (input_control)  string-array `→` Sequence[str]

All characters of the character set to be read.

Default:
["0","1","2","3","4","5","6","7","8","9"]

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

This parameter is not yet supported.

Default:
[]

List of values:
[]

**`gen_param_value`** (input_control)  number-array `→` Sequence[Union[int, str]]

This parameter is not yet supported.

Default:
[]

List of values:
[]

**`ocrhandle`** (output_control)  ocr_knn `→` HHandle

Handle of the k-NN classifier.

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
create_ocr_class_knn (8, 10, 'constant', 'default', CharacterNames, \
                      [], [], OCRHandle)
trainf_ocr_class_knn (OCRHandle, 'letters.trf', [], [])
* Re-classify the characters in the image.
do_ocr_multi_class_knn (Characters, Image, OCRHandle, Class, Confidence)
```

## Result

If the parameters are valid, the operator
`create_ocr_class_knn` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Successors

`trainf_ocr_class_knn`

## Alternatives

`create_ocr_class_svm`

## See also

`do_ocr_single_class_knn`,
`do_ocr_multi_class_knn`,
`clear_class_knn`,
`create_class_knn`,
`trainf_ocr_class_knn`,
`classify_class_knn`

## Module

OCR/OCV
