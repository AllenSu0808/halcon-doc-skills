# FindLocalDeformableModel (Operator)

## Name

`FindLocalDeformableModel` — Find the best matches of a local deformable model in an image.

## Signature

`static void HOperatorSet.FindLocalDeformableModel(HObject image, out HObject imageRectified, out HObject vectorField, out HObject deformedContours, HTuple modelID, HTuple angleStart, HTuple angleExtent, HTuple scaleRMin, HTuple scaleRMax, HTuple scaleCMin, HTuple scaleCMax, HTuple minScore, HTuple numMatches, HTuple maxOverlap, HTuple numLevels, HTuple greediness, HTuple resultType, HTuple genParamName, HTuple genParamValue, out HTuple score, out HTuple row, out HTuple column)`

`HImage HDeformableModel.FindLocalDeformableModel(HImage image, out HImage vectorField, out HXLDCont deformedContours, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, int numLevels, double greediness, HTuple resultType, HTuple genParamName, HTuple genParamValue, out HTuple score, out HTuple row, out HTuple column)`

`HImage HImage.FindLocalDeformableModel(out HImage vectorField, out HXLDCont deformedContours, HDeformableModel modelID, double angleStart, double angleExtent, double scaleRMin, double scaleRMax, double scaleCMin, double scaleCMax, double minScore, int numMatches, double maxOverlap, int numLevels, double greediness, HTuple resultType, HTuple genParamName, HTuple genParamValue, out HTuple score, out HTuple row, out HTuple column)`

## Description

The operator `FindLocalDeformableModel` finds the best
*`numMatches`* instances of the locally deformable
model *`modelID`* in the input *`image`*. The model must have been
created previously by calling [`CreateLocalDeformableModel`](create_local_deformable_model.md) or
[`ReadDeformableModel`](read_deformable_model.md).

The model is searched within those points of the domain of the
image in which the model lies completely within the image.
This means that the model will not be found if it extends beyond
the borders of the image, even if it would achieve a score
greater than *`minScore`*. Note that, if for a certain pyramid
level the model touches the image border, it might not be found
even if it lies completely within the original image.
As a rule of thumb, the model might not be found if its distance to
an image border falls below $2^{NumLevels-1}$.
This behavior can be changed with
`set_system('border_shape_models','true')`, which will cause
models that extend beyond the image border to be found if they
achieve a score greater than *`minScore`*. Here, points lying
outside the image are regarded as being occluded, i.e., they lower
the score. It should be noted that the runtime of the search will
increase in this mode.
Note further, that in rare cases, which occur typically only for
artificial images, the model might not be found also if for certain
pyramid levels them model touches the border of the reduced domain.
Then, it may help to enlarge the reduced domain by
$2^{NumLevels-1}$ using, e.g.,
[`DilationCircle`](dilation_circle.md).

The operator
`FindLocalDeformableModel` returns the *`row`* and
*`column`* coordinates of the found instances.
Additionally, a rectified part of the image, the respective vector field, and
the contours of the found deformed model instance can be returned in
*`imageRectified`*, *`vectorField`*, and *`deformedContours`*.
By default, these iconic objects are not returned. In case they are
needed the parameter *`resultType`* should be set to
*"image_rectified"*, *"vector_field"* or
*"deformed_contours"*.
The size of *`imageRectified`* and *`vectorField`* is the smallest
axis-aligned rectangle of the domain of the image that was used to create
the local deformable model with [`CreateLocalDeformableModel`](create_local_deformable_model.md).
The size of the rectified image and the vector field can be expanded in all
directions by setting *`genParamName`* to *"expand_border"* and the
respective *`genParamValue`* to the number of pixels. Optionally, a
specific direction can be selected with *"expand_border_top"*,
*"expand_border_bottom"*, *"expand_border_left"*, or
*"expand_border_right"*.
Please note that the returned *`vectorField`* is in absolute coordinates
and can be used for [`ConvertMapType`](convert_map_type.md).

The smoothness of the estimated deformation can be selected with
*`genParamName`* set to *"deformation_smoothness"*. The value for
*"deformation_smoothness"* can be imagined as the size of a smoothing
filter to the estimated deformation field. A too small value expects
a strong deformation a too big value expects a rigid object. The
minimal value for *"deformation_smoothness"* is *3*,
a typical value is *11*, and the value can be increased further for
only small global deformations.

Finally, the score of each found instance is returned in *`score`*.
The score is a number between 0 and 1, which is an approximate measure of how
much of the model is visible in the image.

For further explanation on the parameters used for the search of a local
deformable model we refer to the description of
[`FindPlanarUncalibDeformableModel`](find_planar_uncalib_deformable_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / uint2)

Input image in which the model should be found.

**`imageRectified`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Rectified image of the found model.

**`vectorField`** (output_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (vector_field)

Vector field of the rectification transformation.

**`deformedContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contours of the found instances of the model.

**`modelID`** (input_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the model.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39, 0.0

Restriction:
`AngleExtent >= 0`

**`scaleRMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the model in row direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleRMin > 0`

**`scaleRMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the model in row direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleRMax >= ScaleRMin`

**`scaleCMin`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the model in column direction.

Default:
1.0

Suggested values:
0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Restriction:
`ScaleCMin > 0`

**`scaleCMax`** (input_control)  number `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the model in column direction.

Default:
1.0

Suggested values:
1.0, 1.1, 1.2, 1.3, 1.4, 1.5

Restriction:
`ScaleCMax >= ScaleCMin`

**`minScore`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Minimum score of the instances of the model to
be found.

Default:
0.5

Suggested values:
0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
minScore
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`numMatches`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of instances of the model to be found
(or 0 for all matches).

Default:
1

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20

**`maxOverlap`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Maximum overlap of the instances of the model
to be found.

Default:
1.0

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
maxOverlap
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`numLevels`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of pyramid levels used in the matching.

Default:
0

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**`greediness`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

“Greediness” of the search heuristic (0: safe
but slow; 1: fast but matches may be missed).

Default:
0.9

Suggested values:
0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0

Value range:
`0
≤
greediness
≤
1`

Minimum increment:
0.01

Recommended increment:
0.05

**`resultType`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Switch for requested iconic result.

Default:
[]

List of values:
[], "deformed_contours", "image_rectified", "vector_field"

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

The general parameter names.

Default:
[]

List of values:
[], "angle_step", "deformation_smoothness", "expand_border", "expand_border_bottom", "expand_border_left", "expand_border_right", "expand_border_top", "scale_c_step", "scale_r_step", "subpixel"

**`genParamValue`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the general parameters.

Default:
[]

List of values:
[], "least_squares", "least_squares_high", "least_squares_very_high", "none"

**`score`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Scores of the found instances of the model.

**`row`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the found instances of the model.

**`column`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the found instances of the model.

## Result

If the parameters are valid, the operator
`FindLocalDeformableModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateLocalDeformableModel`,
`CreateLocalDeformableModelXld`,
`ReadDeformableModel`

## Module

Matching
