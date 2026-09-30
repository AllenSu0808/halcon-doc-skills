# get_deformable_surface_model_param (Operator)

## Name

`get_deformable_surface_model_param` — Return the parameters and properties of a deformable surface model.

## Signature

`def get_deformable_surface_model_param(deformable_surface_model: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[Union[str, float, int]]`

`def get_deformable_surface_model_param_s(deformable_surface_model: HHandle, gen_param_name: MaybeSequence[str]) -> Union[str, float, int]`

## Description

The operator `get_deformable_surface_model_param` returns parameters and
properties of the surface model *`deformable_surface_model`*.
The surface model must have been created with, for example,
[`create_deformable_surface_model`](create_deformable_surface_model.md).

The following values are possible for *`gen_param_name`*:

- ***"diameter"*:** —

  Diameter of the model point cloud. The diameter is the length of the
  diagonal of the axis-parallel bounding box.
- ***"sampled_model"*:** —

  The 3D points sampled from the model for matching.
  This returns a 3D object model that contains all points sampled from the
  model surface for matching.
- ***"training_models"*:** —

  This returns all 3D object models that were used for the training of
  the deformable surface model. This includes the
  3D object model passed to and sampled by
  [`create_deformable_surface_model`](create_deformable_surface_model.md), and the 3D object models
  added with [`add_deformable_surface_model_sample`](add_deformable_surface_model_sample.md).
- ***"reference_points_x"*:** —
- ***"reference_points_y"*:** —
- ***"reference_points_z"*:** —

  Returns the x-, y- or z-coordinates of all reference points added
  with the operator [`add_deformable_surface_model_reference_point`](add_deformable_surface_model_reference_point.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deformable_surface_model`** (input_control)  deformable_surface_model `→` HHandle

Handle of the deformable surface model.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the parameter.

Default:
"sampled_model"

List of values:
"diameter", "original_model", "reference_points_x", "reference_points_y", "reference_points_z", "sampled_model", "sampled_pose_refinement", "training_models"

**`gen_param_value`** (output_control)  attribute.value(-array) `→` Sequence[Union[str, float, int]]

Value of the parameter.

## Result

`get_deformable_surface_model_param` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`create_deformable_surface_model`,
`read_deformable_surface_model`,
`add_deformable_surface_model_reference_point`

## Possible Successors

`find_deformable_surface_model`,
`refine_deformable_surface_model`,
`write_deformable_surface_model`

## See also

`create_deformable_surface_model`

## Module

3D Metrology
