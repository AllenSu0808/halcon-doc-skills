# get_deformable_surface_matching_result (Operator)

## Name

`get_deformable_surface_matching_result` — Get details of a result from deformable surface based matching.

## Signature

`def get_deformable_surface_matching_result(deformable_surface_matching_result: HHandle, result_name: MaybeSequence[str], result_index: MaybeSequence[Union[int, str]]) -> Sequence[HTupleElementType]`

`def get_deformable_surface_matching_result_s(deformable_surface_matching_result: HHandle, result_name: MaybeSequence[str], result_index: MaybeSequence[Union[int, str]]) -> HTupleElementType`

## Description

The operator `get_deformable_surface_matching_result` returns details about
the results of deformable surface based matching or the
deformable surface refinement.
The results are
stored in *`deformable_surface_matching_result`*, which must have been created
by [`find_deformable_surface_model`](find_deformable_surface_model.md) or
[`refine_deformable_surface_model`](refine_deformable_surface_model.md).

The parameter *`result_name`* is used to select which result detail
shall be returned. For some result details, *`result_index`*
selects the index of the result detail.
*`result_index`* is ignored for certain values of *`result_name`*.

The following values are possible for *`result_name`*:

- ***"sampled_scene"*:** —

  A 3D object model handle is returned that
  contains the sampled scene points that were used in the
  matching or refinement.
  This is helpful for tuning the sampling distance of the scene
  (see parameter RelSamplingDistance of operators
  [`find_deformable_surface_model`](find_deformable_surface_model.md) and
  [`refine_deformable_surface_model`](refine_deformable_surface_model.md)).
  The parameter *`result_index`* is ignored.
- ***"rigid_pose"*:** —

  If *`deformable_surface_matching_result`* was created by
  [`find_deformable_surface_model`](find_deformable_surface_model.md), a rigid pose is returned
  that approximates the deformable matching result.
  The parameter *`result_index`* is ignored.
  This parameter is not available if
  *`deformable_surface_matching_result`* was
  created by [`refine_deformable_surface_model`](refine_deformable_surface_model.md).
- ***"reference_point_x"*:** —
- ***"reference_point_y"*:** —
- ***"reference_point_z"*:** —

  Returns the x-, y- or z-coordinates of a transformed reference point.
  The reference point must have been added to the deformable surface model
  using the operator [`add_deformable_surface_model_reference_point`](add_deformable_surface_model_reference_point.md).
  The indices of the reference points to be returned are passed in
  *`result_index`*.
  If *"all"* is passed in *`result_index`*, the position
  of all reference points is returned.
- ***"deformed_model"*:** —

  Returns a deformed variant of the 3D object model that was originally
  passed to [`create_deformable_surface_model`](create_deformable_surface_model.md).
  The 3D object model is deformed with the reconstructed deformation.
  Triangles, polygons and extended attributes contained in the original
  3D object model are maintained.
  The parameter *`result_index`* is ignored.
- ***"deformed_sampled_model"*:** —

  Returns a deformed variant of the 3D object model that was sampled
  by [`create_deformable_surface_model`](create_deformable_surface_model.md).
  The returned 3D object model has the same number of points as the
  original, undeformed sampled model, and the points are in the same
  order.
  Details about the sampling are described in
  [`create_deformable_surface_model`](create_deformable_surface_model.md).
  The original, undeformed sampled model can be obtained with
  [`get_deformable_surface_model_param`](get_deformable_surface_model_param.md).
  The parameter *`result_index`* is ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`deformable_surface_matching_result`** (input_control)  deformable_surface_matching_result `→` HHandle

Handle of the deformable
surface matching result.

**`result_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the result property.

Default:
"sampled_scene"

List of values:
"deformed_model", "deformed_sampled_model", "reference_point_x", "reference_point_y", "reference_point_z", "rigid_pose", "sampled_scene"

**`result_index`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Index of the result property.

Default:
0

Suggested values:
0, 1, 2, 3, "all"

Restriction:
`ResultIndex >= 0`

**`result_value`** (output_control)  integer(-array) `→` Sequence[HTupleElementType]

Value of the result property.

## Result

If the handle of the result is valid, the operator
`get_deformable_surface_matching_result` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`find_deformable_surface_model`,
`refine_deformable_surface_model`

## Possible Successors

`clear_deformable_surface_model`

## See also

`find_deformable_surface_model`,
`refine_deformable_surface_model`,
`read_deformable_surface_model`,
`write_deformable_surface_model`,
`clear_deformable_surface_model`

## Module

3D Metrology
