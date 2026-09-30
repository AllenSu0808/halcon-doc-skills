# GetDeformableSurfaceModelParam (Operator)

## Name

`GetDeformableSurfaceModelParam` — Return the parameters and properties of a deformable surface model.

## Signature

`static void HOperatorSet.GetDeformableSurfaceModelParam(HTuple deformableSurfaceModel, HTuple genParamName, out HTuple genParamValue)`

`HTuple HDeformableSurfaceModel.GetDeformableSurfaceModelParam(HTuple genParamName)`

`HTuple HDeformableSurfaceModel.GetDeformableSurfaceModelParam(string genParamName)`

## Description

The operator `GetDeformableSurfaceModelParam` returns parameters and
properties of the surface model *`deformableSurfaceModel`*.
The surface model must have been created with, for example,
[`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).

The following values are possible for *`genParamName`*:

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
  [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md), and the 3D object models
  added with [`AddDeformableSurfaceModelSample`](add_deformable_surface_model_sample.md).
- ***"reference_points_x"*:** —
- ***"reference_points_y"*:** —
- ***"reference_points_z"*:** —

  Returns the x-, y- or z-coordinates of all reference points added
  with the operator [`AddDeformableSurfaceModelReferencePoint`](add_deformable_surface_model_reference_point.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`deformableSurfaceModel`** (input_control)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the parameter.

Default:
"sampled_model"

List of values:
"diameter", "original_model", "reference_points_x", "reference_points_y", "reference_points_z", "sampled_model", "sampled_pose_refinement", "training_models"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / string / int / long)

Value of the parameter.

## Result

`GetDeformableSurfaceModelParam` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`CreateDeformableSurfaceModel`,
`ReadDeformableSurfaceModel`,
`AddDeformableSurfaceModelReferencePoint`

## Possible Successors

`FindDeformableSurfaceModel`,
`RefineDeformableSurfaceModel`,
`WriteDeformableSurfaceModel`

## See also

`CreateDeformableSurfaceModel`

## Module

3D Metrology
