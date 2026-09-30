# GetShapeModelParams (Operator)

## Name

`GetShapeModelParams` — Return the parameters of a shape model.

## Signature

`static void HOperatorSet.GetShapeModelParams(HTuple modelID, out HTuple numLevels, out HTuple angleStart, out HTuple angleExtent, out HTuple angleStep, out HTuple scaleMin, out HTuple scaleMax, out HTuple scaleStep, out HTuple metric, out HTuple minContrast)`

`HTuple HShapeModel.GetShapeModelParams(out double angleStart, out double angleExtent, out double angleStep, out HTuple scaleMin, out HTuple scaleMax, out HTuple scaleStep, out string metric, out int minContrast)`

`int HShapeModel.GetShapeModelParams(out double angleStart, out double angleExtent, out double angleStep, out double scaleMin, out double scaleMax, out double scaleStep, out string metric, out int minContrast)`

## Description

The operator `GetShapeModelParams` returns the parameters
of the shape model *`modelID`* that were used to create it
using [`CreateShapeModel`](create_shape_model.md), [`CreateScaledShapeModel`](create_scaled_shape_model.md),
or [`CreateAnisoShapeModel`](create_aniso_shape_model.md). In particular, this output can
be used to check the parameters *`numLevels`*,
*`angleStep`*, *`scaleStep`*, and *`minContrast`* if
they were determined automatically during the model creation with
[`CreateShapeModel`](create_shape_model.md), [`CreateScaledShapeModel`](create_scaled_shape_model.md), or
[`CreateAnisoShapeModel`](create_aniso_shape_model.md).

If the *`modelID`* was adapted with
[`AdaptShapeModelHighNoise`](adapt_shape_model_high_noise.md), NumLevels contains two values: the
highest pyramid level and the estimated lowest pyramid level.

If the shape model was created using [`CreateShapeModel`](create_shape_model.md) or
[`CreateScaledShapeModel`](create_scaled_shape_model.md) a single value is returned in
*`scaleMin`*, *`scaleMax`*, and *`scaleStep`*. This
parameters corresponds to the isotropic scaling parameters of the
shape model. If the shape model was created using
[`CreateAnisoShapeModel`](create_aniso_shape_model.md) two values each are returned in the
above three parameters. Here, the first value of the respective
parameter refers to the scaling in the row direction, while the
second value refers to the scaling in the column direction.

Note that the parameters `optimization` and
`contrast` that also can be determined automatically during
the model creation cannot be queried by using
`GetShapeModelParams`. If their value is of interest
[`DetermineShapeModelParams`](determine_shape_model_params.md) should be used instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`numLevels`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of pyramid levels.

**`angleStart`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Smallest rotation of the pattern.

**`angleExtent`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Extent of the rotation angles.

Assertion:
`AngleExtent >= 0`

**`angleStep`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Step length of the angles (resolution).

Assertion:
`AngleStep >= 0 && AngleStep <= pi / 2`

**`scaleMin`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum scale of the pattern.

Assertion:
`ScaleMin > 0`

**`scaleMax`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum scale of the pattern.

Assertion:
`ScaleMax >= ScaleMin`

**`scaleStep`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Scale step length (resolution).

Assertion:
`ScaleStep >= 0`

**`metric`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Match metric.

**`minContrast`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Minimum contrast of the objects in the search images.

## Result

If the handle of the model is valid, the operator
`GetShapeModelParams` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateShapeModel`,
`CreateScaledShapeModel`,
`CreateAnisoShapeModel`,
`ReadShapeModel`

## Alternatives

`GetGenericShapeModelParam`

## See also

`FindShapeModel`,
`FindScaledShapeModel`,
`FindAnisoShapeModel`,
`FindShapeModels`,
`FindScaledShapeModels`,
`FindAnisoShapeModels`

## Module

Matching
