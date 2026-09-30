# refine_deformable_surface_model (Operator)

## Name

`refine_deformable_surface_model` — Refine the position and deformation of a deformable surface model in a
3D scene.

## Signature

`def refine_deformable_surface_model(deformable_surface_model: HHandle, object_model_3d: HHandle, rel_sampling_distance: float, initial_deformation_object_model_3d: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[str, float, int]]) -> Tuple[Sequence[float], Sequence[HHandle]]`

`def refine_deformable_surface_model_s(deformable_surface_model: HHandle, object_model_3d: HHandle, rel_sampling_distance: float, initial_deformation_object_model_3d: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[str, float, int]]) -> Tuple[float, HHandle]`

## Description

The operator `refine_deformable_surface_model` refines the initial
position and deformation given in *`initial_deformation_object_model_3d`*
of the surface model *`deformable_surface_model`* in
the 3D scene *`object_model_3d`*.
The deformable surface model *`deformable_surface_model`* must have been
created previously with, for example, [`create_deformable_surface_model`](create_deformable_surface_model.md).

`refine_deformable_surface_model` is useful if the position and deformation
of an object in a scene is approximately known and only needs to be refined.
Additional information about the output parameters can be found in
[`find_deformable_surface_model`](find_deformable_surface_model.md).

*`initial_deformation_object_model_3d`* must contain as many points as the
sampled deformation model obtained by
[`get_deformable_surface_model_param`](get_deformable_surface_model_param.md) and in the same order.

The score of the refined result is returned in *`score`* and
a deformable surface matching result handle is
returned in *`deformable_surface_matching_result`*.
Details of the result, such as the deformed model and the position
of the reference points, can be queried with the operator
[`get_deformable_surface_matching_result`](get_deformable_surface_matching_result.md) using the result handle.

The score is normalized between *0* and *1* and represents
the amount of model surface visible in the scene. A value of
*1* represents a perfect match.

The parameters *`gen_param_name`* and *`gen_param_value`* are used
to set generic parameters.
Details about the generic parameters are described in the
documentation of [`find_deformable_surface_model`](find_deformable_surface_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`deformable_surface_model`** (input_control)  deformable_surface_model `→` HHandle

Handle of the deformable surface model.

**`object_model_3d`** (input_control)  object_model_3d `→` HHandle

Handle of the 3D object model containing
the scene.

**`rel_sampling_distance`** (input_control)  real `→` float

Relative sampling distance of the scene.

Default:
0.05

Suggested values:
0.1, 0.07, 0.05, 0.04, 0.03

Restriction:
`0 < RelSamplingDistance < 1`

**`initial_deformation_object_model_3d`** (input_control)  object_model_3d `→` HHandle

Initial deformation of the 3D object
model

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters.

Default:
[]

List of values:
"pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_scoring_dist_abs", "pose_ref_scoring_dist_rel", "scene_normal_computation"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[str, float, int]]

Values of the generic parameters.

Default:
[]

Suggested values:
"fast", "mls", 0, 1, 10, 25, 50, 0.05, 0.1, 0.25, 0.3, 0.05, 0.03, 0.005

**`score`** (output_control)  real(-array) `→` Sequence[float]

Score of the refined model.

**`deformable_surface_matching_result`** (output_control)  deformable_surface_matching_result(-array) `→` Sequence[HHandle]

Handle of the matching result.

## Result

`refine_deformable_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`get_object_model_3d_params`,
`read_deformable_surface_model`,
`create_deformable_surface_model`,
`get_deformable_surface_model_param`,
`find_deformable_surface_model`

## Possible Successors

`get_deformable_surface_matching_result`,
`clear_deformable_surface_matching_result`,
`clear_object_model_3d`

## Alternatives

`find_deformable_surface_model`

## See also

`create_deformable_surface_model`,
`find_deformable_surface_model`

## Module

3D Metrology
