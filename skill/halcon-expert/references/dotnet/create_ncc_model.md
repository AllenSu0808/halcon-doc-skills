# CreateNccModel (Operator)

## Name

`CreateNccModel` — Prepare an NCC model for matching.

## Signature

`static void HOperatorSet.CreateNccModel(HObject template, HTuple numLevels, HTuple angleStart, HTuple angleExtent, HTuple angleStep, HTuple metric, out HTuple modelID)`

`public HNCCModel(HImage template, HTuple numLevels, double angleStart, double angleExtent, HTuple angleStep, string metric)`

`public HNCCModel(HImage template, int numLevels, double angleStart, double angleExtent, double angleStep, string metric)`

`void HNCCModel.CreateNccModel(HImage template, HTuple numLevels, double angleStart, double angleExtent, HTuple angleStep, string metric)`

`void HNCCModel.CreateNccModel(HImage template, int numLevels, double angleStart, double angleExtent, double angleStep, string metric)`

`HNCCModel HImage.CreateNccModel(HTuple numLevels, double angleStart, double angleExtent, HTuple angleStep, string metric)`

`HNCCModel HImage.CreateNccModel(int numLevels, double angleStart, double angleExtent, double angleStep, string metric)`

## Description

The operator `CreateNccModel` prepares a template, which is
passed in the image *`template`*, as an NCC model used for
matching using the normalized cross correlation (NCC). The ROI of
the model is passed as the domain of *`template`*.

The model is generated using multiple image pyramid levels at
multiple rotations on each level and is stored in memory. The
output parameter *`modelID`* is a handle for this model, which
is used in subsequent calls to [`FindNccModel`](find_ncc_model.md).

The number of pyramid levels is determined with the parameter
*`numLevels`*. It should be chosen as large as possible
because by this the time necessary to find the object is
significantly reduced. On the other hand, *`numLevels`* must
be chosen such that the model is still recognizable and contains a
sufficient number of points (at least eight) on the highest pyramid
level. This can be checked using the domains of the output images
of [`GenGaussPyramid`](gen_gauss_pyramid.md). If not enough model points are
generated, the number of pyramid levels is reduced internally until
enough model points are found on the highest pyramid level. If this
procedure would lead to a model with no pyramid levels, i.e., if the
number of model points is already too small on the lowest pyramid
level, `CreateNccModel` returns an error message. If
*`numLevels`* is set to *"auto"* or *0*,
`CreateNccModel` determines the number of pyramid levels
automatically. The automatically computed number of pyramid levels
can be queried using [`GetNccModelParams`](get_ncc_model_params.md). In rare cases,
it might happen that `CreateNccModel` determines a value for
the number of pyramid levels that is too large or too small. If the
number of pyramid levels is chosen too large, the model may not be
recognized in the image or it may be necessary to select very low
parameters for `minScore` in [`FindNccModel`](find_ncc_model.md) in order
to find the model. If the number of pyramid levels is chosen too
small, the time required to find the model in [`FindNccModel`](find_ncc_model.md)
may increase. In these cases, the number of pyramid levels should
be selected by inspecting the output of [`GenGaussPyramid`](gen_gauss_pyramid.md).
Here, `mode` = *"constant"* and
`scale` = *0.5* should be used.

The parameters *`angleStart`* and *`angleExtent`*
determine the range of possible rotations, in which the model can
occur in the image. Note that the model can only be found in this
range of angles by [`FindNccModel`](find_ncc_model.md). The parameter
*`angleStep`* determines the step length within the selected
range of angles. Hence, if subpixel accuracy is not specified in
[`FindNccModel`](find_ncc_model.md), this parameter specifies the accuracy that
is achievable for the angles in [`FindNccModel`](find_ncc_model.md).
*`angleStep`* should be chosen based on the size of the object.
Smaller models do not possess many different discrete rotations in
the image, and hence *`angleStep`* should be chosen larger for
smaller models. If *`angleExtent`* is not an integer multiple
of *`angleStep`*, *`angleStep`* is modified accordingly.
To ensure a sampling of the range of possible rotations that is
independent of the given *`angleStart`*, the range of possible
rotations is modified as follows: If there is no positive integer
value n such that *`angleStart`* plus n times
*`angleStep`* is exactly 0.0, *`angleStart`* is decreased
by up to *`angleStep`* and *`angleExtent`* is increased by
*`angleStep`*.

The model is pre-generated for the selected angle range and stored
in memory. The memory required to store the model is proportional
to the number of angle steps and the number of points in the model.
Hence, if *`angleStep`* is too small or *`angleExtent`*
too big, it may happen that the model no longer fits into the
(virtual) memory. In this case, either *`angleStep`* must be
enlarged or *`angleExtent`* must be reduced. In any case, it
is desirable that the model completely fits into the main memory,
because this avoids paging by the operating system, and hence the
time to find the object will be much smaller. Since angles can be
determined with subpixel resolution by [`FindNccModel`](find_ncc_model.md),
*`angleStep`* >= 1 can be
selected for models of a diameter smaller than about 200 pixels. If
*`angleStep`* =
*"auto"* or *0* is selected,
`CreateNccModel` automatically determines a suitable angle
step length based on the size of the model. The automatically
computed angle step length can be queried using
[`GetNccModelParams`](get_ncc_model_params.md).

The parameter *`metric`* determines the conditions under which
the model is recognized in the image. If *`metric`* =
*"use_polarity"*, the object in the image and the model must
have the same contrast. If, for example, the model is a bright
object on a dark background, the object is found only if it is also
brighter than the background. If *`metric`* =
*"ignore_global_polarity"*, the object is found in the image
also if the contrast reverses globally. In the above example, the
object hence is also found if it is darker than the background. The
runtime of [`FindNccModel`](find_ncc_model.md) will increase slightly in this
case.

The center of gravity of the domain (region) of the model image
*`template`* is used as the origin (reference point) of the
model. A different origin can be set with
[`SetNccModelOrigin`](set_ncc_model_origin.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`template`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image whose domain will be used to create
the model.

**`numLevels`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Maximum number of pyramid levels.

Default:
"auto"

List of values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "auto"

**`angleStart`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the pattern.

Default:
-0.39

Suggested values:
-3.14, -1.57, -0.79, -0.39, -0.20, 0.0

**`angleExtent`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Default:
0.79

Suggested values:
6.29, 3.14, 1.57, 0.79, 0.39

Restriction:
`AngleExtent >= 0`

**`angleStep`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / string)

Step length of the angles (resolution).

Default:
"auto"

Suggested values:
"auto", 0.0, 0.0175, 0.0349, 0.0524, 0.0698, 0.0873

Restriction:
`AngleStep >= 0 && AngleStep <= pi / 16`

**`metric`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Match metric.

Default:
"use_polarity"

List of values:
"ignore_global_polarity", "use_polarity"

**`modelID`** (output_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator `CreateNccModel`
returns the value 2 (
H_MSG_TRUE)
. If the parameter *`numLevels`* are
chosen such that the model contains too few points, the error 8506
is raised.

## Possible Predecessors

`DrawRegion`,
`ReduceDomain`,
`Threshold`

## Possible Successors

`FindNccModel`,
`GetNccModelParams`,
`ClearNccModel`,
`WriteNccModel`,
`SetNccModelOrigin`,
`SetNccModelParam`,
`FindNccModels`

## Alternatives

`CreateGenericShapeModel`

## Module

Matching
