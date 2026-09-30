# create_surface_model (Operator)

## Name

`create_surface_model` — Create the data structure needed to perform surface-based matching.

## Signature

`create_surface_model( : : ObjectModel3D, RelSamplingDistance, GenParamName, GenParamValue : SurfaceModelID)`

## Description

The operator `create_surface_model` creates a model for surface-based
matching for the 3D object model *`ObjectModel3D`*.
The 3D object model can, for example, have been read previously from a file
by using [`read_object_model_3d`](read_object_model_3d.md), or been created by using
[`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).
The created surface model is returned in *`SurfaceModelID`*.

Additional parameters of the surface model can be set with
[`set_surface_model_param`](set_surface_model_param.md) after the model was created.

The creation of the surface model requires that the 3D object model
contains points and normals. The following combinations are possible:

- points and point normals;
- points and a triangular or polygon mesh, e.g., from a CAD file;
- points and a 2D-Mapping, e.g., an XYZ image triple converted with
  [`xyz_to_object_model_3d`](xyz_to_object_model_3d.md).

Note that the direction and orientation (inward or outward) of the normals
of the model are important for matching.
For edge-supported surface-based matching the normals need to point inwards
and further the model must contain a triangular or polygon mesh (see below).

The surface model is created by sampling the 3D object model with a certain
distance.
The sampling distance must be specified in the parameter
*`RelSamplingDistance`* and is parametrized relative to the diameter
of the axis-parallel bounding box of the 3D object model.
For example, if *`RelSamplingDistance`* is set to *0.05* and
the diameter of *`ObjectModel3D`* is *10 cm*, the points
sampled from the object's surface will be approximately *5 mm*
apart.
The sampled points are used for the approximate matching in the
operator [`find_surface_model`](find_surface_model.md) (see below).
The sampled points can be obtained with the operator
[`get_surface_model_param`](get_surface_model_param.md) using the value *'sampled_model'*.
Note that outlier points in the object model should be avoided, as they would
corrupt the diameter.
Reducing *`RelSamplingDistance`* leads to more points, and in turn
to a more stable but slower matching. Increasing
*`RelSamplingDistance`* leads to less points, and in turn to a less
stable but faster matching.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/030e47a431e61de4.svg) | ![figure](../assets/5d7237c57f6ab936.svg) | ![figure](../assets/828c81224b55bc7d.svg) | ![figure](../assets/fd3aa3ea4b54bbeb.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Original 3D model. (2) 3D model sampled with
*`RelSamplingDistance`*  *= 0.02*.
(3) *`RelSamplingDistance`*  *= 0.03*.
(4) *`RelSamplingDistance`*  *= 0.05*.

The sampled points are used for finding the object model in a scene by using
the operator [`find_surface_model`](find_surface_model.md).
For this, all possible pairs of points from the point set are examined, and
the distance and relative surface orientation of each pair is computed. Both
values are discretized and stored for matching. The generic parameters
*'feat_step_size_rel'* and *'feat_angle_resolution'* can be
used to set the discretization of the distance and the orientation angles,
respectively (see below).

The 3D object model is sampled a second time for the pose refinement.
The second sampling is done with a smaller sampling distance, leading to
more points.
The generic parameter *'pose_ref_rel_sampling_distance'* sets the
sampling distance relative to the object's diameter.
Decreasing the value results in a more accurate pose refinement but a
larger model and a slower model generation and matching.
Increasing the value leads to a less accurate pose refinement but
a smaller model and faster model generation and matching (see below).

Surface-based matching can additionally use 3D edges to improve the
alignment.
This is particularly helpful for
objects that are planar or contain larger planar sides, such that they
are found in incorrect rotations or in a background plane.
In order to allow [`find_surface_model`](find_surface_model.md) to also align edges, the
surface model must be trained by setting the generic parameter
*'train_3d_edges'* to *'true'*.
In this case, the model must contain a triangular or polygon mesh where
the order of the points results in normals that point inwards.
Also, the training for edge-supported surface-based matching
requires OpenGL 2.1, GLSL 1.2, and the OpenGL extensions
GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit.
Note that the training can take significantly longer than without
edge-support.

Additionally, the model can be prepared to support view-based score
computation. This is particularly helpful for models where only a small
part of the 3D object model is visible, which results in low scores if the
ratio to the total number of points is used. Accordingly, the view-based
score is computed using the ratio of the matched points to the maximum number
of potentially visible model points from a certain viewpoint.
In order to allow [`find_surface_model`](find_surface_model.md) to compute a view-based score,
the surface model must be trained by setting the generic parameter
*'train_view_based'* to *'true'*.
Similar to *'train_3d_edges'*, the model must contain a triangular
or polygon mesh where the order of the points results in normals that
point inwards.

Note that using noisy data for the creation of your 3D object model results
in the computation of deficient surface normals. Especially when the model is
prepared for the use with 3D edges or the support of view-based score, this
can lead to unreliable scores.
In order to reduce noisy 3D data you can, e.g., use
[`smooth_object_model_3d`](smooth_object_model_3d.md) or [`simplify_object_model_3d`](simplify_object_model_3d.md).

The generic parameter pair *`GenParamName`* and *`GenParamValue`*
are used to set additional parameters for the model generation.
*`GenParamName`* contains the tuple of parameter names that shall be
set and *`GenParamValue`* contains the corresponding values.
The following values are possible for *`GenParamName`*:

- ***'model_invert_normals'*:** —

  Invert the orientation of the surface normals of the model.
  The normal orientation needs to be known for the model generation.
  If both the model and the scene are acquired with the same setup,
  the normals will already point in the same direction.
  If the model was loaded from a CAD file, the normals might point
  into the opposite direction. If you experience the effect that the
  model is found on the 'outside' of the scene surface and the
  model was created from a CAD file, try to set this parameter to
  *'true'*.
  Also, make sure that the normals in the CAD file all point either
  outward or inward, i.e., are oriented consistently.
  The normal direction is irrelevant for the pose refinement of
  the surface model. Therefore, if the object model is only used with the
  operator [`refine_surface_model_pose`](refine_surface_model_pose.md), the value of
  *'model_invert_normals'* has no effect on the result.

  List of values:
   *'false'*, *'true'*

  Default:
   *'false'*
- ***'pose_ref_rel_sampling_distance'*:** —

  Set the sampling distance for the pose refinement relative to the
  object's diameter.
  Decreasing this value leads to a more accurate pose refinement but a
  larger model and slower model generation and refinement.
  Increasing the value leads to a less accurate pose refinement but a
  smaller model and faster model generation and matching.

  Suggested values:
   *0.05*, *0.02*, *0.01*,
  *0.005*

  Default:
   *0.01*

  Restriction:
   *0* < *'pose_ref_rel_sampling_distance'* < *1*
- ***'feat_step_size_rel'*:** —

  Set the discretization distance of the point pair distance relative to
  the object's diameter.
  This value defaults to the value of *`RelSamplingDistance`*.
  It is not recommended to change this value.
  For very noisy scenes, the value can be increased to improve the
  robustness of the matching against noisy points.

  Suggested values:
   *0.1*, *0.05*, *0.03*

  Default:
   Value of *`RelSamplingDistance`*

  Restriction:
   *0* < *'feat_step_size_rel'* < *1*
- ***'feat_angle_resolution'*:** —

  Set the discretization of the point pair orientation as the number of
  subdivisions of the angle.
  It is recommended to not change this value.
  Increasing the value increases the precision of the matching but
  decreases the robustness against incorrect normal directions.
  Decreasing the value decreases the precision of the matching but
  increases the robustness against incorrect normal directions.
  For very noisy scenes where the normal directions can not be computed
  accurately, the value can be set to *25* or *20*.

  Suggested values:
   *20*, *25*, *30*

  Default:
   *30*

  Restriction:
   *'feat_angle_resolution'* > *1*
- ***'train_3d_edges'*:** —

  Enable the training for edge-supported surface-based matching and
  refinement.
  In this case the model must contain a mesh, i.e. triangles or polygons.
  Also, it is important that the computed normal vectors point inwards.
  This parameter requires OpenGL.

  List of values:
   *'false'*, *'true'*

  Default:
   *'false'*
- ***'train_view_based'*:** —

  Enable the training for view-based score computation for surface-based
  matching and refinement.
  In this case the model must contain a mesh, i.e. triangles or polygons.
  Also, it is important that the computed normal vectors point inwards.
  This parameter requires OpenGL.

  List of values:
   *'false'*, *'true'*

  Default:
   *'false'*
- ***'train_self_similar_poses'*:** —

  Prepares the surface model for optimizations regarding self-similar,
  almost symmetric poses.
  For this, poses are found under which the model is very similar
  to itself, i.e., poses that can be distinguished only by very
  small properties of the model (such as boreholes) and that
  can be confused by [`find_surface_model`](find_surface_model.md).
  When calling [`find_surface_model`](find_surface_model.md), it will automatically be determined
  which of those self-similar poses are correct.

  List of values:
   *'false'*, *'true'*

  Default:
   *'false'*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator supports canceling timeouts and interrupts.

## Parameters

**`ObjectModel3D`** (input_control)  object_model_3d `→`  (handle)

Handle of the 3D object model.

**`RelSamplingDistance`** (input_control)  real `→`  (real)

Sampling distance relative to the object's diameter

Default:
0.03

Suggested values:
0.1, 0.05, 0.03, 0.02, 0.01

Restriction:
`0 < RelSamplingDistance < 1`

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of the generic parameters.

Default:
[]

Suggested values:
'model_invert_normals', 'pose_ref_rel_sampling_distance', 'feat_step_size_rel', 'feat_angle_resolution', 'train_3d_edges', 'train_view_based', 'train_self_similar_poses'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / real / integer)

Values of the generic parameters.

Default:
[]

Suggested values:
0, 1, 'true', 'false', 0.005, 0.01, 0.02, 0.05, 0.1

**`SurfaceModelID`** (output_control)  surface_model `→`  (handle)

Handle of the surface model.

## Result

`create_surface_model` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`get_object_model_3d_params`,
`surface_normals_object_model_3d`

## Possible Successors

`find_surface_model`,
`refine_surface_model_pose`,
`get_surface_model_param`,
`write_surface_model`,
`clear_surface_model`,
`set_surface_model_param`

## Alternatives

`read_surface_model`

## See also

`find_surface_model`,
`refine_surface_model_pose`,
`read_surface_model`,
`write_surface_model`,
`clear_surface_model`,
`set_surface_model_param`

## References

Bertram Drost, Markus Ulrich, Nassir Navab, Slobodan Ilic: “Model
Globally, Match Locally: Efficient and Robust 3D Object Recognition.”
Computer Vision and Pattern Recognition, pp. 998-1005, 2010.

## Module

3D Metrology
