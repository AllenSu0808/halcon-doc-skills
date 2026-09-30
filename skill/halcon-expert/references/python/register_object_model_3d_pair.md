# register_object_model_3d_pair (Operator)

## Name

`register_object_model_3d_pair` — Search for a transformation between two 3D object models.

## Signature

`def register_object_model_3d_pair(object_model_3d1: HHandle, object_model_3d2: HHandle, method: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, str, float]]) -> Tuple[Sequence[Union[int, float]], Sequence[float]]`

## Description

`register_object_model_3d_pair` searches for a transformation
between two 3D object models having an optimal alignment.
This process is called registration.
The transformation that is returned
in *`pose`* can be used to transform *`object_model_3d1`*
to the reference frame of the second object *`object_model_3d2`*.
*`score`* returns the ratio of the overlapping
parts to the not overlapping parts of the two 3D object models.
If the two objects are not overlapping, no pose is returned.
The parameter *`method`* decides if the initial relative
position is calculated by *"matching"* or if only
the pose refinement is performed in relation to the then assumed
common global reference frame, which can be selected directly with
*"icp"*.

The accuracy of the returned pose is limited to around
0.1% of the size of the point clouds due to numerical reasons. The accuracy
further depends on the noise of the data points, the number of
data points and the shape of the point clouds.

The matching process and the following refinement can be controlled using
the following name-value pairs in
*`gen_param_name`* and *`gen_param_value`*:

- ***"default_parameters"*:** —

  To allow an easy control over the
  parameters, three different sets of parameters are available.
  Selecting the *"fast"*
  parameter set allows a shorter calculation time.
  *"accurate"* will give more accurate results.
  *"robust"* additionally improves the quality of the resulting
  *`score`* at the cost of calculation time.

  List of values:
   *"fast"*, *"accurate"*,
  *"robust"*.

  Default:
   *"accurate"*.
- ***"rel_sampling_distance"*:** —

  This parameter controls the relative sampling rate of the 3D object
  models that is used to represent the surfaces for the computation.
  This value is relative to the diameter of the respective object
  and defines the minimal distance between two sampled points.
  A higher value will lead to faster and a lower value to more
  accurate results. This parameter can also be set for each object
  independently by using *"rel_sampling_distance_obj1"* and
  *"rel_sampling_distance_obj2"*.

  Suggested values:
   *0.03*, *0.05*, *0.07*.

  Default:
   *0.05*.
- ***"key_point_fraction"*:** —

  This parameter controls the ratio
  of sampled points that are considered as key points for the matching
  process. The number is relative to the sampled points of the model.
  Reducing this ratio speeds up the process, whereas increasing
  leads to more robust results. This parameter can be also set
  for each object independently by using
  *"key_point_fraction_obj1"* and
  *"key_point_fraction_obj2"*.

  Suggested values:
   *0.2*, *0.3*, *0.4*.

  Default:
   *0.3*.
- ***"pose_ref_num_steps"*:** —

  The number of iterative steps
  used for the pose refinement.

  Suggested values:
   *5*, *7*, *10*.

  Default:
   *5*.
- ***"pose_ref_sub_sampling"*:** —

  Number of points that are skipped
  for the pose refinement. The value specifies the number of points
  that are skipped per selected point. Increasing this value
  allows faster convergence at the cost of less accurate results.
  This parameter is only relevant for the smaller of the two objects.

  Suggested values:
   *1*, *2*, *20*.

  Default:
   *2*.
- ***"pose_ref_dist_threshold_rel"*:** —

  Maximum distance that two
  faces might have to be considered as potentially overlapping.
  This value is relative to the diameter of the larger object.

  Suggested values:
   *0.05*, *0.1*, *0.15*.

  Default:
   *0.1*.
- ***"pose_ref_dist_threshold_abs"*:** —

  Maximum distance that two
  faces might have to be considered as potentially overlapping, as
  absolute value.
- ***"model_invert_normals"*:** —

  Invert the normals of the smaller
  object, if its normals are inverted relative to the other object.

  List of values:
   *"true"*, *"false"*.

  Default:
   *"false"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator supports canceling timeouts and interrupts.

## Parameters

**`object_model_3d1`** (input_control)  object_model_3d `→` HHandle

Handle of the first 3D object model.

**`object_model_3d2`** (input_control)  object_model_3d `→` HHandle

Handle of the second 3D object model.

**`method`** (input_control)  string `→` str

Method for the registration.

Default:
"matching"

List of values:
"icp", "matching"

**`gen_param_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Names of the generic parameters.

Default:
[]

List of values:
"default_parameters", "key_point_fraction", "key_point_fraction_obj1", "key_point_fraction_obj2", "model_invert_normals", "pose_ref_dist_threshold_abs", "pose_ref_dist_threshold_rel", "pose_ref_num_steps", "pose_ref_sub_sampling", "rel_sampling_distance", "rel_sampling_distance_obj1", "rel_sampling_distance_obj2"

**`gen_param_value`** (input_control)  number(-array) `→` MaybeSequence[Union[int, str, float]]

Values of the generic parameters.

Default:
[]

Suggested values:
"fast", "accurate", "robust", 0.1, 0.25, 0.5, 1, "true", "false"

**`pose`** (output_control)  pose `→` Sequence[Union[int, float]]

Pose to transform *`object_model_3d1`* in
the reference frame of *`object_model_3d2`*.

**`score`** (output_control)  number-array `→` Sequence[float]

Overlapping of the two 3D object models.

## Example (HDevelop)

```
* Generate two boxes
gen_box_object_model_3d ([0,0,0,0,0,0,0],3,2,1, ObjectModel3D1)
gen_box_object_model_3d ([0,0,0.5,15,0,0,0],3,2,1, ObjectModel3D2)
* Match them
register_object_model_3d_pair (ObjectModel3D1, ObjectModel3D2, 'matching',\
                              [], [], Pose, Score)
```

## Result

`register_object_model_3d_pair` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`read_object_model_3d`,
`gen_object_model_3d_from_points`,
`xyz_to_object_model_3d`

## Possible Successors

`register_object_model_3d_global`,
`affine_trans_object_model_3d`,
`union_object_model_3d`

## See also

`register_object_model_3d_global`,
`find_surface_model`

## Module

3D Metrology
