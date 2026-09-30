# register_object_model_3d_global (Operator)

## Name

`register_object_model_3d_global` — Improve the relative transformations between 3D object models based on
their overlaps.

## Signature

`def register_object_model_3d_global(object_models_3d: MaybeSequence[HHandle], hom_mats_3d: Sequence[Union[int, float]], from_val: MaybeSequence[Union[int, str]], to: MaybeSequence[int], gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, str, float]]) -> Tuple[Sequence[Union[int, float]], Sequence[float]]`

## Description

`register_object_model_3d_global` improves the relative transformations
between 3D object models, which is called global registration.
In particular, under the assumption that all input 3D objects
models in *`object_models_3d`* have a known approximated
spatial relation,
all possible pairwise overlapping areas are calculated and optimized for
a better alignment. The resulting offset is
then synchronously minimized for all pairs. The entire
process is then repeated iteratively from the newly resulting starting poses.
The result in *`hom_mats_3dout`* describes a transformation that
can be applied with [`affine_trans_object_model_3d`](affine_trans_object_model_3d.md) to the input
3D object models to transform all in a common reference frame.
*`scores`* contains for every 3D object model the number of found
neighbors with a sufficient
overlap. If no overlap is found for at least one object, an exception is
raised.

Three types for the interpretation of the starting poses in
*`hom_mats_3d`* are available, which is controlled by the parameters
*`from`* and *`to`*:

First, if *`from`* is set to *"global"*, the
parameter *`hom_mats_3d`* must contain a rigid transformation with
12 entries for each 3D object model in *`object_models_3d`* that
describes its position in relation to a common global reference frame. In
this case, *`to`* must be empty. This case is suitable, e.g.,
if transformations are applied by a turning table or a robot to either
the camera or the object. In this case, all neighborhoods that are possible
are considered for the global optimization.

Second, if *`from`* is set to
*"previous"*, the parameter *`hom_mats_3d`* must contain a
rigid transformation for each subsequent pair of 3D object models in
*`object_models_3d`* (one less than for the first case).
An example for this
situation might be a matching applied consecutively to the previous
frame (e.g., with [`register_object_model_3d_pair`](register_object_model_3d_pair.md)). *`to`* must
be empty again. In this case, all neighborhoods that are possible
are considered for the global optimization.

Third, you can describe any transformation in *`hom_mats_3d`*
by setting *`from`* and *`to`* to the indices of the
3D object models for which the corresponding transformation is valid.
That is, a given transformation describes the transformation that is needed
to move the 3D object model with the index that is specified in
*`from`* into the coordinate system of the 3D object model with the
corresponding index that is specified in *`to`*.
In this case, *`hom_mats_3d`*
should contain all possible neighborhood relations between the objects,
since no other than these neighborhoods are considered for
the optimization. Please consider, that for all 3D object
models at least one path of transformations to each other 3D object
model must be contained in the such specified transformations.

If *`object_models_3d`* contains 3D-primitives, they will internally
be transformed into point clouds and will be considered as such.

The accuracy of the returned poses is limited to around
0.1% of the size of the point clouds due to numerical reasons. The accuracy
further depends on the noise of the data points, the number of
data points and the shape of the point clouds.

The process of the global registration can be controlled further
by the following generic parameters in
*`gen_param_name`* and *`gen_param_value`*:

- ***"default_parameters"*:** —

  Allows to choose between two
  default parameter sets, i.e., it allows to switch between a
  *"fast"* and an *"accurate"* set
  of parameters.

  List of values:
   *"fast"*, *"accurate"*.

  Default:
   *"accurate"*.
- ***"rel_sampling_distance"*:** —

  The relative
  sampling rate of the 3D object models.
  This value is relative to the object's diameter and refers to
  the minimal distance between two sampled points. A higher value
  leads to faster results, whereas a lower value leads to more accurate
  results.

  Suggested values:
   *0.03*, *0.05*, *0.07*.

  Default:
   *0.05* (*"default_parameters"* =
  *"accurate"*),
  *0.07* (*"default_parameters"* = *"fast"*).

  Restriction:
   0 < *"rel_sampling_distance"* < 1
- ***"pose_ref_sub_sampling"*:** —

  Number of points that are skipped
  for the pose refinement. The value specifies the number of points
  that are skipped per selected point. Increasing this value
  allows faster convergence at the cost of less accurate results.
  The internally used method for the refinement is asymmetric and
  this parameter only affects the second model of each tested pair.

  Suggested values:
   *1*, *2*, *20*.

  Default:
   *2* (*"default_parameters"* =
  *"accurate"*),
  *10* (*"default_parameters"* = *"fast"*).

  Restriction:
   *"pose_ref_sub_sampling"* > 0
- ***"max_num_iterations"*:** —

  Number of iterations applied
  to adjust the initial alignment. The better the initial alignment is,
  the less iterations are necessary.

  Suggested values:
   *1*, *3*, *10*.

  Default:
   *3*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

## Parameters

**`object_models_3d`** (input_control)  object_model_3d(-array) `→` MaybeSequence[HHandle]

Handles of several 3D object models.

**`hom_mats_3d`** (input_control)  hom_mat3d-array `→` Sequence[Union[int, float]]

Approximate relative transformations between
the 3D object models.

**`from`** (input_control)  number(-array) `→` MaybeSequence[Union[int, str]]

Type of interpretation for the transformations.

Default:
"global"

List of values:
0, 1, 2, 3, 4, "global", "previous"

**`to`** (input_control)  number(-array) `→` MaybeSequence[int]

Target indices of the transformations if
*`from`* specifies the source indices, otherwise
the parameter must be empty.

Default:
[]

List of values:
0, 1, 2, 3, 4

**`gen_param_name`** (input_control)  string-array `→` Sequence[str]

Names of the generic parameters that can be adjusted
for the global 3D object model registration.

Default:
[]

List of values:
"default_parameters", "max_num_iterations", "pose_ref_sub_sampling", "rel_sampling_distance"

**`gen_param_value`** (input_control)  number-array `→` Sequence[Union[int, str, float]]

Values of the generic parameters that can be adjusted
for the global 3D object model registration.

Default:
[]

Suggested values:
0.03, 0.05, 0.07, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, "fast", "accurate"

**`hom_mats_3dout`** (output_control)  hom_mat3d-array `→` Sequence[Union[int, float]]

Resulting Transformations.

**`scores`** (output_control)  number-array `→` Sequence[float]

Number of overlapping neighbors for each
3D object model.

## Result

`register_object_model_3d_global` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`xyz_to_object_model_3d`,
`register_object_model_3d_pair`,
`gen_object_model_3d_from_points`

## Possible Successors

`affine_trans_object_model_3d`,
`union_object_model_3d`,
`sample_object_model_3d`,
`triangulate_object_model_3d`

## See also

`register_object_model_3d_pair`,
`find_surface_model`,
`refine_surface_model_pose`

## Module

3D Metrology
