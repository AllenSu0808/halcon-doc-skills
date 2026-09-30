# find_deformable_surface_model (Operator)

## Name

`find_deformable_surface_model` — Find the best match of a deformable surface model in a 3D scene.

## Signature

`find_deformable_surface_model( : : DeformableSurfaceModel, ObjectModel3D, RelSamplingDistance, MinScore, GenParamName, GenParamValue : Score, DeformableSurfaceMatchingResult)`

## Description

The operator `find_deformable_surface_model` finds the best match of
the deformable surface model *`DeformableSurfaceModel`* in the 3D scene
*`ObjectModel3D`*.
The deformable surface model must have been
created previously with, for example, [`create_deformable_surface_model`](create_deformable_surface_model.md).

The matching requires that the 3D object model *`ObjectModel3D`*
contains points and normals.
The scene shall provide one of the following options:

- points and point normals
- points and a 2D-Mapping, e.g., an XYZ image triple converted with
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md)

It is important for an accurate pose that the normals of the scene
and the model point in the same direction (see
*'scene_invert_normals'*).
Note that triangles or polygons in the passed scene are ignored.
Instead, only the vertices are used for matching.
It is thus in general not recommended to use this operator on meshed scenes,
such as CAD data.
Instead, such a scene must be sampled beforehand using
[`sample_object_model_3d`](sample_object_model_3d.md) to create points and normals.
When using noisy point clouds, e.g., from time-of-flight cameras, the
generic parameter *'scene_normal_computation'* should be set to
*'mls'* in order to obtain more robust results (see below).

First, points are sampled uniformly from the scene passed in
*`ObjectModel3D`*. The sampling distance is controlled with
the parameter *`RelSamplingDistance`*, and is given relative
to the diameter of the surface model.
Decreasing *`RelSamplingDistance`* leads to more sampled points,
and in turn to a more stable but slower matching. Increasing
*`RelSamplingDistance`* reduces the number of sampled scene
points, which leads to a less stable but faster matching. For an
illustration showing different values for *`RelSamplingDistance`*,
please refer to the operator [`create_deformable_surface_model`](create_deformable_surface_model.md).

The operator [`get_deformable_surface_matching_result`](get_deformable_surface_matching_result.md) can be used to
retrieve the sampled scene points for visual inspection.
For a robust matching it is recommended that at least 50-100
scene points are sampled for each object instance.

The method first finds an approximate position of the object.
This position is then refined.
The generic parameters controlling the deformation are described
further down.

If a match was found, the score of the match is returned in *`Score`*
and a deformable surface matching result handle is
returned in *`DeformableSurfaceMatchingResult`*.
Details of the matching result, such as the deformed model and the position
of the reference points, can be queried with the operator
[`get_deformable_surface_matching_result`](get_deformable_surface_matching_result.md) using the result handle.

The score is normalized between *0* and *1* and represents
the amount of model surface visible in the scene. A value of
*1* represents a perfect match.
The parameter *`MinScore`* can be used to filter the result.
A match is returned only if its score exceeds the value of
*`MinScore`*.

The parameters *`GenParamName`* and *`GenParamValue`* are used
to set generic parameters. Both get a tuple of equal length, where the
tuple passed to *`GenParamName`* contains the names of the
parameters to set, and the tuple passed to *`GenParamValue`* contains
the corresponding values. The possible parameter names and values
are described below.

- ***'scene_normal_computation'*:** —

  This parameter controls the normal computation of the sampled
  scene.
  In the default mode *'fast'*, normals are computed based on
  a small neighborhood of points.
  In the mode *'mls'*, normals are computed based on a larger
  neighborhood and using the more complex but more accurate
  *'mls'* method.
  A more detailed description of the *'mls'* method can be
  found in the description of the operator
  [`surface_normals_object_model_3d`](surface_normals_object_model_3d.md).
  The *'mls'* mode is intended for noisy data, such as images
  from time-of-flight cameras.

  List of values:
   *'fast'*, *'mls'*

  Default:
   *'fast'*
- ***'scene_invert_normals'*:** —

  Invert the orientation of the surface normals of the scene.
  The orientation of surface normals of the scene have to match with the
  orientation of the model.
  If both the model and the scene are acquired with the same setup,
  the normals will already point in the same direction.
  If you experience the effect that the
  model is found on the 'outside' of the scene surface, try to set this
  parameter to *'true'*.
  Also, make sure that the normals in the scene all point either
  outward or inward, i.e., are oriented consistently.

  List of values:
   *'false'*, *'true'*

  Default:
   *'false'*
- ***'pose_ref_num_steps'*:** —

  Number of iterations for the refinement. Increasing the
  number of iteration leads to a more accurate position at the expense of
  runtime.
  However, once convergence is reached, the accuracy can no longer be
  increased, even if the number of steps is increased.

  Suggested values:
  *1*, *10*, *25*,
  *50*

  Default:
   *25*

  Restriction:
   *'pose_ref_num_steps'* > *0*
- ***'pose_ref_dist_threshold_rel'*:** —

  Set the distance threshold for refinement relative to the
  diameter of the surface model.
  Only scene points that are closer to the object than this distance
  are used for the optimization. Scene points further
  away are ignored.

  Suggested values:
  *0.05*, *0.1*,
  *0.25*, *0.3*

  Default:
   *0.25*

  Restriction:
   *0* < *'pose_ref_dist_threshold_rel'*
- ***'pose_ref_dist_threshold_abs'*:** —

  Set the distance threshold for dense pose refinement as absolute
  value.
  See *'pose_ref_dist_threshold_rel'* for a detailed
  description.
  Only one of the parameters *'pose_ref_dist_threshold_rel'* and
  *'pose_ref_dist_threshold_abs'* can be set. If both are set,
  only the value of the last parameter is used.

  Restriction:
   *0* < *'pose_ref_dist_threshold_abs'*
- ***'pose_ref_scoring_dist_rel'*:** —

  Set the distance threshold for scoring relative to the
  diameter of the surface model. See the following
  *'pose_ref_scoring_dist_abs'* for a detailed description.
  Only one of the parameters *'pose_ref_scoring_dist_rel'* and
  *'pose_ref_scoring_dist_abs'* can be set. If both are set,
  only the value of the last parameter is used.

  Suggested values:
  *0.1*, *0.05*,
  *0.03*, *0.005*

  Default:
   *0.03*

  Restriction:
   *0* < *'pose_ref_scoring_dist_rel'*
- ***'pose_ref_scoring_dist_abs'*:** —

  Set the distance threshold for scoring.
  Only scene points that are closer to the object than this distance
  are considered to be 'on the model' when computing the score after
  the refinement. All other scene points are considered not to be
  on the model.
  The value should correspond to the amount of noise on the coordinates
  of the scene points.
  Only one of the parameters *'pose_ref_scoring_dist_rel'* and
  *'pose_ref_scoring_dist_abs'* can be set. If both are set,
  only the value of the last parameter is used.

  Restriction:
   *0* < *'pose_ref_scoring_dist_abs'*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`DeformableSurfaceModel`** (input_control)  deformable_surface_model `→`  (handle)

Handle of the deformable surface model.

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model containing the
scene.

**`RelSamplingDistance`** (input_control)  real `→`  (real)

Scene sampling distance relative to the diameter
of the surface model.

Default:
0.05

Suggested values:
0.1, 0.07, 0.05, 0.04, 0.03

Restriction:
`0 < RelSamplingDistance < 1`

**`MinScore`** (input_control)  real `→`  (real / integer)

Minimum score of the returned match.

Default:
0

Restriction:
`MinScore >= 0`

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Names of the generic parameters.

Default:
[]

List of values:
'pose_ref_dist_threshold_abs', 'pose_ref_dist_threshold_rel', 'pose_ref_num_steps', 'pose_ref_scoring_dist_abs', 'pose_ref_scoring_dist_rel', 'scene_invert_normals', 'scene_normal_computation'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
'fast', 'mls', 0, 1, 10, 25, 50, 0.05, 0.1, 0.25, 0.3, 0.05, 0.03, 0.005

**`Score`** (output_control)  real(-array) `→`  (real)

Score of the found instance of the surface
model.

**`DeformableSurfaceMatchingResult`** (output_control)  deformable_surface_matching_result(-array) `→`  (handle)

Handle of the matching result.

## Result

`find_deformable_surface_model` returns 2 (
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
`add_deformable_surface_model_reference_point`,
`add_deformable_surface_model_sample`

## Possible Successors

`refine_deformable_surface_model`,
`get_deformable_surface_matching_result`,
`clear_deformable_surface_matching_result`,
`clear_object_model_3d`

## Alternatives

`refine_deformable_surface_model`

## See also

`refine_deformable_surface_model`

## Module

3D Metrology
