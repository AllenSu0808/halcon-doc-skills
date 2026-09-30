# RefineDeformableSurfaceModel (Operator)

## Name

`RefineDeformableSurfaceModel` — Refine the position and deformation of a deformable surface model in a
3D scene.

## Signature

`static void HOperatorSet.RefineDeformableSurfaceModel(HTuple deformableSurfaceModel, HTuple objectModel3D, HTuple relSamplingDistance, HTuple initialDeformationObjectModel3D, HTuple genParamName, HTuple genParamValue, out HTuple score, out HTuple deformableSurfaceMatchingResult)`

`HTuple HObjectModel3D.RefineDeformableSurfaceModel(HDeformableSurfaceModel deformableSurfaceModel, double relSamplingDistance, HObjectModel3D initialDeformationObjectModel3D, HTuple genParamName, HTuple genParamValue, out HDeformableSurfaceMatchingResult[] deformableSurfaceMatchingResult)`

`double HObjectModel3D.RefineDeformableSurfaceModel(HDeformableSurfaceModel deformableSurfaceModel, double relSamplingDistance, HObjectModel3D initialDeformationObjectModel3D, string genParamName, string genParamValue, out HDeformableSurfaceMatchingResult deformableSurfaceMatchingResult)`

`HTuple HDeformableSurfaceModel.RefineDeformableSurfaceModel(HObjectModel3D objectModel3D, double relSamplingDistance, HObjectModel3D initialDeformationObjectModel3D, HTuple genParamName, HTuple genParamValue, out HDeformableSurfaceMatchingResult[] deformableSurfaceMatchingResult)`

`double HDeformableSurfaceModel.RefineDeformableSurfaceModel(HObjectModel3D objectModel3D, double relSamplingDistance, HObjectModel3D initialDeformationObjectModel3D, string genParamName, string genParamValue, out HDeformableSurfaceMatchingResult deformableSurfaceMatchingResult)`

`static HTuple HDeformableSurfaceMatchingResult.RefineDeformableSurfaceModel(HDeformableSurfaceModel deformableSurfaceModel, HObjectModel3D objectModel3D, double relSamplingDistance, HObjectModel3D initialDeformationObjectModel3D, HTuple genParamName, HTuple genParamValue, out HDeformableSurfaceMatchingResult[] deformableSurfaceMatchingResult)`

`double HDeformableSurfaceMatchingResult.RefineDeformableSurfaceModel(HDeformableSurfaceModel deformableSurfaceModel, HObjectModel3D objectModel3D, double relSamplingDistance, HObjectModel3D initialDeformationObjectModel3D, string genParamName, string genParamValue)`

## Description

The operator `RefineDeformableSurfaceModel` refines the initial
position and deformation given in *`initialDeformationObjectModel3D`*
of the surface model *`deformableSurfaceModel`* in
the 3D scene *`objectModel3D`*.
The deformable surface model *`deformableSurfaceModel`* must have been
created previously with, for example, [`CreateDeformableSurfaceModel`](create_deformable_surface_model.md).

`RefineDeformableSurfaceModel` is useful if the position and deformation
of an object in a scene is approximately known and only needs to be refined.
Additional information about the output parameters can be found in
[`FindDeformableSurfaceModel`](find_deformable_surface_model.md).

*`initialDeformationObjectModel3D`* must contain as many points as the
sampled deformation model obtained by
[`GetDeformableSurfaceModelParam`](get_deformable_surface_model_param.md) and in the same order.

The score of the refined result is returned in *`score`* and
a deformable surface matching result handle is
returned in *`deformableSurfaceMatchingResult`*.
Details of the result, such as the deformed model and the position
of the reference points, can be queried with the operator
[`GetDeformableSurfaceMatchingResult`](get_deformable_surface_matching_result.md) using the result handle.

The score is normalized between *0* and *1* and represents
the amount of model surface visible in the scene. A value of
*1* represents a perfect match.

The parameters *`genParamName`* and *`genParamValue`* are used
to set generic parameters.
Details about the generic parameters are described in the
documentation of [`FindDeformableSurfaceModel`](find_deformable_surface_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`deformableSurfaceModel`** (input_control)  deformable_surface_model `→` [HDeformableSurfaceModel](HDeformableSurfaceModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the deformable surface model.

**`objectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D object model containing
the scene.

**`relSamplingDistance`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Relative sampling distance of the scene.

Default:
0.05

Suggested values:
0.1, 0.07, 0.05, 0.04, 0.03

Restriction:
`0 < RelSamplingDistance < 1`

**`initialDeformationObjectModel3D`** (input_control)  object_model_3d `→` [HObjectModel3D](HObjectModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Initial deformation of the 3D object
model

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
[]

List of values:
"pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_scoring_dist_abs", "pose_ref_scoring_dist_rel", "scene_normal_computation"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Values of the generic parameters.

Default:
[]

Suggested values:
"fast", "mls", 0, 1, 10, 25, 50, 0.05, 0.1, 0.25, 0.3, 0.05, 0.03, 0.005

**`score`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Score of the refined model.

**`deformableSurfaceMatchingResult`** (output_control)  deformable_surface_matching_result(-array) `→` [HDeformableSurfaceMatchingResult](HDeformableSurfaceMatchingResult.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the matching result.

## Result

`RefineDeformableSurfaceModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`ReadObjectModel3d`,
`XyzToObjectModel3d`,
`GetObjectModel3dParams`,
`ReadDeformableSurfaceModel`,
`CreateDeformableSurfaceModel`,
`GetDeformableSurfaceModelParam`,
`FindDeformableSurfaceModel`

## Possible Successors

`GetDeformableSurfaceMatchingResult`,
`ClearDeformableSurfaceMatchingResult`,
`ClearObjectModel3d`

## Alternatives

`FindDeformableSurfaceModel`

## See also

`CreateDeformableSurfaceModel`,
`FindDeformableSurfaceModel`

## Module

3D Metrology
