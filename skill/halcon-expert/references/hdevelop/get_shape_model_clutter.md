# get_shape_model_clutter (Operator)

## Name

`get_shape_model_clutter` — Get the clutter parameters of a shape model.

## Signature

`get_shape_model_clutter( : ClutterRegion : ModelID, GenParamName : GenParamValue, HomMat2D, ClutterContrast)`

## Description

The operator `get_shape_model_clutter` can be used to inspect clutter
parameters of the shape model *`ModelID`*, which have been set
previously using [`set_shape_model_clutter`](set_shape_model_clutter.md). Also, the value of
*'use_clutter'*, which can be set using
[`set_shape_model_param`](set_shape_model_param.md), can be queried by setting
*`GenParamName`* to *'use_clutter'*. For a description of the
parameters, please see [`set_shape_model_clutter`](set_shape_model_clutter.md) and
[`set_shape_model_param`](set_shape_model_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ClutterRegion`** (output_object)  region `→` object

Region where no clutter should occur.

**`ModelID`** (input_control)  shape_model `→`  (handle)

Handle of the model.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Parameter names.

Default:
'use_clutter'

List of values:
'clutter_border_mode', 'use_clutter'

**`GenParamValue`** (output_control)  attribute.name(-array) `→`  (string / real / integer)

Parameter values.

**`HomMat2D`** (output_control)  hom_mat2d `→`  (real)

Transformation matrix.

**`ClutterContrast`** (output_control)  number `→`  (integer)

Minimum contrast of clutter in the search images.

## Result

If the parameters are valid, the operator `get_shape_model_clutter`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`set_shape_model_clutter`,
`read_shape_model`,
`deserialize_shape_model`

## Possible Successors

`find_shape_model`,
`find_scaled_shape_model`,
`find_aniso_shape_model`,
`find_shape_models`,
`find_scaled_shape_models`,
`find_aniso_shape_models`

## See also

`create_shape_model`,
`create_scaled_shape_model`,
`create_aniso_shape_model`,
`set_shape_model_param`

## Module

Matching
