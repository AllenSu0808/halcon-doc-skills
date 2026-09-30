# GetShapeModelClutter (Operator)

## Name

`GetShapeModelClutter` — Get the clutter parameters of a shape model.

## Signature

`static void HOperatorSet.GetShapeModelClutter(out HObject clutterRegion, HTuple modelID, HTuple genParamName, out HTuple genParamValue, out HTuple homMat2D, out HTuple clutterContrast)`

`HRegion HShapeModel.GetShapeModelClutter(HTuple genParamName, out HTuple genParamValue, out HHomMat2D homMat2D, out int clutterContrast)`

`HRegion HShapeModel.GetShapeModelClutter(string genParamName, out string genParamValue, out HHomMat2D homMat2D, out int clutterContrast)`

`static HRegion HImage.GetShapeModelClutter(HShapeModel modelID, HTuple genParamName, out HTuple genParamValue, out HHomMat2D homMat2D, out int clutterContrast)`

`static HRegion HImage.GetShapeModelClutter(HShapeModel modelID, string genParamName, out string genParamValue, out HHomMat2D homMat2D, out int clutterContrast)`

## Description

The operator `GetShapeModelClutter` can be used to inspect clutter
parameters of the shape model *`modelID`*, which have been set
previously using [`SetShapeModelClutter`](set_shape_model_clutter.md). Also, the value of
*"use_clutter"*, which can be set using
[`SetShapeModelParam`](set_shape_model_param.md), can be queried by setting
*`genParamName`* to *"use_clutter"*. For a description of the
parameters, please see [`SetShapeModelClutter`](set_shape_model_clutter.md) and
[`SetShapeModelParam`](set_shape_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`clutterRegion`** (output_object)  region `→` [HRegion](HRegion.md)

Region where no clutter should occur.

**`modelID`** (input_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
"use_clutter"

List of values:
"clutter_border_mode", "use_clutter"

**`genParamValue`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Parameter values.

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

**`clutterContrast`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Minimum contrast of clutter in the search images.

## Result

If the parameters are valid, the operator `GetShapeModelClutter`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`SetShapeModelClutter`,
`ReadShapeModel`,
`DeserializeShapeModel`

## Possible Successors

`FindShapeModel`,
`FindScaledShapeModel`,
`FindAnisoShapeModel`,
`FindShapeModels`,
`FindScaledShapeModels`,
`FindAnisoShapeModels`

## See also

`CreateShapeModel`,
`CreateScaledShapeModel`,
`CreateAnisoShapeModel`,
`SetShapeModelParam`

## Module

Matching
