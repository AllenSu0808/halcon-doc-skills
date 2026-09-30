# get_surface_matching_result (Operator)

## Name

`get_surface_matching_result` — Get details of a result from surface based matching.

## Signature

`def get_surface_matching_result(surface_matching_result_id: HHandle, result_name: MaybeSequence[str], result_index: int) -> Sequence[HTupleElementType]`

`def get_surface_matching_result_s(surface_matching_result_id: HHandle, result_name: MaybeSequence[str], result_index: int) -> HTupleElementType`

## Description

The operator `get_surface_matching_result` returns details about
the results of surface based matching or the surface pose refinement.
The results are
stored in *`surface_matching_result_id`*, which must have been created
by [`find_surface_model`](find_surface_model.md) or [`refine_surface_model_pose`](refine_surface_model_pose.md).

The parameter *`result_name`* is used to select which result detail
shall be returned. If details about one of the results shall be retrieved,
*`result_index`* selects the result index, where *0* selects
the first result.
*`result_index`* is ignored for certain values of *`result_name`*.

The following values are possible for *`result_name`* if
*`surface_matching_result_id`* was created by [`find_surface_model`](find_surface_model.md)
or [`find_surface_model_image`](find_surface_model_image.md):

- ***"sampled_scene"*:** —

  A 3D object model handle is returned that
  contains the sampled scene points that were used in the
  approximate matching step.
  This is helpful for tuning the sampling distance for the
  matching (see parameter RelSamplingDistance of operator
  [`find_surface_model`](find_surface_model.md)).
  The parameter *`result_index`* is ignored.
- ***"key_points"*:** —

  A 3D object model handle is returned that
  contains all points from the 3D scene that were used as key
  points in the matching process.
  This is helpful for tuning the sampling
  distance and key point rate for the matching (see parameter
  KeyPointFraction of operator [`find_surface_model`](find_surface_model.md)).
  The parameter *`result_index`* is ignored.
  At least 10 key points should be on the object of interest for
  stable results.
- ***"score_unrefined"*:** —

  The score of the result before the
  dense pose refinement is returned. If the sparse pose refinement was
  disabled, this is the score of the approximate matching. Otherwise the
  score of the sparse pose refinement is returned.
  See [`find_surface_model`](find_surface_model.md) for details about the score.
  In *`result_index`* the index of the result must be specified.
  If *`surface_matching_result_id`* was created by
  [`refine_surface_model_pose`](refine_surface_model_pose.md), 0 is returned.
- ***"sampled_3d_edges"*:** —

  If the surface model was trained with *"train_3d_edges"*
  enabled, a 3D object model handle is returned that
  contains the sampled 3D edge points that were used in the
  approximate matching step and in the sparse refinement step.
  The parameter *`result_index`* is ignored.

The following values are always possible for *`result_name`*,
regardless the operator *`surface_matching_result_id`* was created with:

- ***"pose"*:** —

  Returns the pose of the matching or refinement result.
  In *`result_index`* the index of the result must be specified.
- ***"score_refined"*:** —

  Returns the score of the result after the dense pose refinement.
  See [`find_surface_model`](find_surface_model.md) for details about this score.
  In *`result_index`* the index of the result must be specified.
  If *`surface_matching_result_id`* was created by
  [`find_surface_model`](find_surface_model.md) and dense pose refinement was disabled,
  *0* is returned.
- ***"score"*:** —

  Returns the combined score of the result indexed in *`result_index`*,
  thus this parameter is equal to `score` returned in
  [`find_surface_model`](find_surface_model.md).
- ***"score_surface"*:** —

  Returns the surface-based score of the result indexed in
  *`result_index`*.
  If not specifically set otherwise, this score is equal to
  *"score_refined"*.
- ***"score_3d_edges"*:** —

  Returns the 3D edge score of the result indexed in
  *`result_index`*.
  This score is only applicable for edged-supported surface-based matching.
- ***"score_2d_edges"*:** —

  Returns the 2D edge score of the result indexed in
  *`result_index`*.
  This score is only applicable for edged-supported surface-based matching.
- ***"score_view_based"*:** —

  Returns the view-based score of the result indexed in
  *`result_index`*.
  This score is only applicable if the surface model supports view-based
  score computation.
- ***"all_scores"*:** —

  Returns for the result indexed in *`result_index`*
  the values of the five scores
  *"score"*, *"score_surface"*, *"score_3d_edges"*,
  *"score_2d_edges"*, and *"score_view_based"*.
  Thereby the scores have the same order as the thresholds given through the
  parameter `min_score` in the matching and refinement operators.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`surface_matching_result_id`** (input_control)  surface_matching_result `→` HHandle

Handle of the surface matching result.

**`result_name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the result property.

Default:
"pose"

List of values:
"all_scores", "key_points", "pose", "sampled_3d_edges", "sampled_scene", "score", "score_2d_edges", "score_3d_edges", "score_refined", "score_surface", "score_unrefined", "score_view_based"

**`result_index`** (input_control)  integer `→` int

Index of the matching result, starting with 0.

Default:
0

Suggested values:
0, 1, 2, 3

Restriction:
`ResultIndex >= 0`

**`result_value`** (output_control)  integer(-array) `→` Sequence[HTupleElementType]

Value of the result property.

## Result

If the handle of the result is valid, the operator
`get_surface_matching_result` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`find_surface_model`,
`refine_surface_model_pose`

## Possible Successors

`clear_surface_model`

## See also

`find_surface_model`,
`refine_surface_model_pose`,
`read_surface_model`,
`write_surface_model`,
`clear_surface_model`

## Module

3D Metrology
