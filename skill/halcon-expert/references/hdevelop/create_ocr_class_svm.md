# create_ocr_class_svm (Operator)

## Name

`create_ocr_class_svm` — Create an OCR classifier using a support vector machine.

## Signature

`create_ocr_class_svm( : : WidthCharacter, HeightCharacter, Interpolation, Features, Characters, KernelType, KernelParam, Nu, Mode, Preprocessing, NumComponents : OCRHandle)`

## Description

`create_ocr_class_svm` creates an OCR classifier that uses a
support vector machine (SVM). The handle of the OCR classifier is
returned in *`OCRHandle`*.

For a description on how an SVM works, see [`create_class_svm`](create_class_svm.md).
`create_ocr_class_svm` creates an SVM for classification with
the classification mode given by *`Mode`*. The length of the
feature vector of the SVM (`NumFeatures` in
[`create_class_svm`](create_class_svm.md)) is determined from the features that are
used for the OCR, which are passed in *`Features`*. The
features are described below. The kernel is parametrized with
*`KernelType`*, *`KernelParam`* and *`Nu`* like in
[`create_class_svm`](create_class_svm.md). The number of classes of the SVM
(`NumClasses` in [`create_class_svm`](create_class_svm.md)) is determined from
the names of the characters to be used in the OCR, which are passed
in *`Characters`*. As described with [`create_class_svm`](create_class_svm.md),
the parameters *`Preprocessing`* and *`NumComponents`* can
be used to specify a preprocessing of the data (i.e., the feature
vectors). For the sake of numerical stability, *`Preprocessing`*
can typically be set to *'normalization'*. In order to speed
up classification time, *'principal_components'* or
*'canonical_variates'* can be used, as the number of input
features can be significantly reduced without deterioration of the
recognition rate.

The features to be used for the classification are determined by
*`Features`*. *`Features`* can contain a tuple of
feature names. Each of these feature names results in one or more
features to be calculated for the classifier. Some of the feature
names compute gray value features (e.g., *'pixel_invar'*).
Because a classifier requires a constant number of features (input
variables), a character to be classified is transformed to a
standard size, which is determined by *`WidthCharacter`* and
*`HeightCharacter`*. The interpolation to be used for the
transformation is determined by *`Interpolation`*. It has the
same meaning as in [`affine_trans_image`](affine_trans_image.md). The interpolation
should be chosen such that no aliasing effects occur in the
transformation. For most applications, *`Interpolation`* =
*'constant'* should be used. It should be noted that the
size of the transformed character is not chosen too large, because
the generalization properties of the classifier may become bad for
large sizes. In particular, for large sizes small segmentation errors
will have a large influence on the computed features if gray value features
are used. This happens because segmentation errors will change the smallest
enclosing rectangle of the regions, thus the character is zoomed differently
than the characters in the training set. In most applications, sizes
between 6x8 and 10x14 should be used.

The parameter *`Features`* can contain the following feature
names for the classification of the characters.

- ***'default'*** —

  *'ratio'* and *'pixel_invar'* are selected.
- ***'pixel'*** —

  Gray values of the character (*`WidthCharacter`* x
  *`HeightCharacter`* features).
- ***'pixel_invar'*** —

  Gray values of the character with maximum scaling of the gray
  values (*`WidthCharacter`* x *`HeightCharacter`*
  features).
- ***'pixel_binary'*** —

  Region of the character as a binary image zoomed to a size of
  *`WidthCharacter`* x *`HeightCharacter`*
  (*`WidthCharacter`* x *`HeightCharacter`*
  features).
- ***'gradient_8dir'*** —

  Gradients are computed on the character image. The gradient
  directions are discretized into 8 directions. The amplitude image
  is decomposed into 8 channels according to these discretized
  directions. 25 samples on a 5x5 grid are extracted from
  each channel. These samples are used as features (200 features).
- ***'projection_horizontal'*** —

  Horizontal projection of the gray values (see
  [`gray_projections`](gray_projections.md), *`HeightCharacter`* features).
- ***'projection_horizontal_invar'*** —

  Maximally scaled horizontal projection of the gray values
  (*`HeightCharacter`* features).
- ***'projection_vertical'*** —

  Vertical projection of the gray values (see
  [`gray_projections`](gray_projections.md), *`WidthCharacter`* features).
- ***'projection_vertical_invar'*** —

  Maximally scaled vertical projection of the gray values
  (*`WidthCharacter`* features).
- ***'ratio'*** —

  Aspect ratio of the character (see
  [`height_width_ratio`](height_width_ratio.md), 1 feature).
- ***'anisometry'*** —

  Anisometry of the character (see [`eccentricity`](eccentricity.md), 1 feature).
- ***'width'*** —

  Width of the character before scaling the character to the
  standard size (not scale-invariant, see
  [`height_width_ratio`](height_width_ratio.md), 1 feature).
- ***'height'*** —

  Height of the character before scaling the character to the
  standard size (not scale-invariant, see
  [`height_width_ratio`](height_width_ratio.md), 1 feature).
- ***'zoom_factor'*** —

  Difference in size between the character and the values of
  *`WidthCharacter`* and *`HeightCharacter`* (not
  scale-invariant, 1 feature).
- ***'foreground'*** —

  Fraction of pixels in the foreground (1 feature).
- ***'foreground_grid_9'*** —

  Fraction of pixels in the foreground in a 3x3 grid within
  the smallest enclosing rectangle of the character (9 features).
- ***'foreground_grid_16'*** —

  Fraction of pixels in the foreground in a 4x4 grid within
  the smallest enclosing rectangle of the character (16 features).
- ***'compactness'*** —

  Compactness of the character (see [`compactness`](compactness.md), 1 feature).
- ***'convexity'*** —

  Convexity of the character (see [`convexity`](convexity.md), 1 feature).
- ***'moments_region_2nd_invar'*** —

  Normalized 2nd moments of the character (see
  [`moments_region_2nd_invar`](moments_region_2nd_invar.md), 3 features).
- ***'moments_region_2nd_rel_invar'*** —

  Normalized 2nd relative moments of the character (see
  [`moments_region_2nd_rel_invar`](moments_region_2nd_rel_invar.md), 2 features).
- ***'moments_region_3rd_invar'*** —

  Normalized 3rd moments of the character (see
  [`moments_region_3rd_invar`](moments_region_3rd_invar.md), 4 features).
- ***'moments_central'*** —

  Normalized central moments of the character (see
  [`moments_region_central`](moments_region_central.md), 4 features).
- ***'moments_gray_plane'*** —

  Normalized gray value moments and the angle of the gray value
  plane (see [`moments_gray_plane`](moments_gray_plane.md), 4 features).
- ***'phi'*** —

  Orientation (angle) of the character (see [`elliptic_axis`](elliptic_axis.md), 1
  feature).
- ***'num_connect'*** —

  Number of connected components (see [`connect_and_holes`](connect_and_holes.md), 1
  feature).
- ***'num_holes'*** —

  Number of holes (see [`connect_and_holes`](connect_and_holes.md), 1 feature).
- ***'cooc'*** —

  Values of the binary co-occurrence matrix (see
  [`gen_cooc_matrix`](gen_cooc_matrix.md), 12 features).
- ***'num_runs'*** —

  Number of runs in the region normalized by the height (1 feature).
- ***'chord_histo'*** —

  Frequency of the runs per row (not scale-invariant, *`HeightCharacter`* features).

After the classifier has been created, it is trained using
[`trainf_ocr_class_svm`](trainf_ocr_class_svm.md). After this, the classifier can be
saved using [`write_ocr_class_svm`](write_ocr_class_svm.md). Alternatively, the
classifier can be used immediately after training to classify
characters using [`do_ocr_single_class_svm`](do_ocr_single_class_svm.md) or
[`do_ocr_multi_class_svm`](do_ocr_multi_class_svm.md).

A comparison of SVM and the multi-layer perceptron (MLP) (see
[`create_ocr_class_mlp`](create_ocr_class_mlp.md)) typically shows that SVMs are
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

**`WidthCharacter`** (input_control)  integer `→`  (integer)

Width of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
8

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`4
≤
WidthCharacter
≤
20`

**`HeightCharacter`** (input_control)  integer `→`  (integer)

Height of the rectangle to which the gray values
of the segmented character are zoomed.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20

Value range:
`4
≤
HeightCharacter
≤
20`

**`Interpolation`** (input_control)  string `→`  (string)

Interpolation mode for the zooming of the characters.

Default:
'constant'

List of values:
'bicubic', 'bilinear', 'constant', 'nearest_neighbor', 'weighted'

**`Features`** (input_control)  string(-array) `→`  (string)

Features to be used for classification.

Default:
'default'

List of values:
'anisometry', 'chord_histo', 'compactness', 'convexity', 'cooc', 'default', 'foreground', 'foreground_grid_16', 'foreground_grid_9', 'gradient_8dir', 'height', 'moments_central', 'moments_gray_plane', 'moments_region_2nd_invar', 'moments_region_2nd_rel_invar', 'moments_region_3rd_invar', 'num_connect', 'num_holes', 'num_runs', 'phi', 'pixel', 'pixel_binary', 'pixel_invar', 'projection_horizontal', 'projection_horizontal_invar', 'projection_vertical', 'projection_vertical_invar', 'ratio', 'width', 'zoom_factor'

**`Characters`** (input_control)  string-array `→`  (string)

All characters of the character set to be read.

Default:
['0','1','2','3','4','5','6','7','8','9']

**`KernelType`** (input_control)  string `→`  (string)

The kernel type.

Default:
'rbf'

List of values:
'linear', 'polynomial_homogeneous', 'polynomial_inhomogeneous', 'rbf'

**`KernelParam`** (input_control)  real `→`  (real)

Additional parameter for the kernel function.

Default:
0.02

Suggested values:
0.01, 0.02, 0.05, 0.1, 0.5

**`Nu`** (input_control)  real `→`  (real)

Regularization constant of the SVM.

Default:
0.05

Suggested values:
0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.3

Restriction:
`Nu > 0.0 && Nu < 1.0`

**`Mode`** (input_control)  string `→`  (string)

The mode of the SVM.

Default:
'one-versus-one'

List of values:
'one-versus-all', 'one-versus-one'

**`Preprocessing`** (input_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

Default:
'normalization'

List of values:
'canonical_variates', 'none', 'normalization', 'principal_components'

**`NumComponents`** (input_control)  integer `→`  (integer)

Preprocessing parameter: Number of transformed
features (ignored for *`Preprocessing`* =
*'none'* and *`Preprocessing`* =
*'normalization'*).

Default:
10

Suggested values:
1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

Restriction:
`NumComponents >= 1`

**`OCRHandle`** (output_control)  ocr_svm `→`  (handle)

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
create_ocr_class_svm (8, 10, 'constant', 'default', CharacterNames, \
                      'rbf', 0.01, 0.01, 'one-versus-all', \
                      'principal_components', 10, OCRHandle)
trainf_ocr_class_svm (OCRHandle, 'letters.trf', 0.001, 'default')
* Re-classify the characters in the image.
do_ocr_multi_class_svm (Characters, Image, OCRHandle, Class)
```

## Result

If the parameters are valid the operator
`create_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Successors

`trainf_ocr_class_svm`

## Alternatives

`create_ocr_class_mlp`

## See also

`do_ocr_single_class_svm`,
`do_ocr_multi_class_svm`,
`clear_ocr_class_svm`,
`create_class_svm`,
`train_class_svm`,
`classify_class_svm`

## Module

OCR/OCV
