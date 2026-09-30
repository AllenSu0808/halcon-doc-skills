# get_surface_matching_result (Operator)

## Name

`get_surface_matching_result` — Get details of a result from surface based matching.

## Signature

`get_surface_matching_result( : : SurfaceMatchingResultID, ResultName, ResultIndex : ResultValue)`

## Description

The operator `get_surface_matching_result` returns details about
the results of surface based matching or the surface pose refinement.
The results are
stored in *`SurfaceMatchingResultID`*, which must have been created
by [`find_surface_model`](find_surface_model.md) or [`refine_surface_model_pose`](refine_surface_model_pose.md).

The parameter *`ResultName`* is used to select which result detail
shall be returned. If details about one of the results shall be retrieved,
*`ResultIndex`* selects the result index, where *0* selects
the first result.
*`ResultIndex`* is ignored for certain values of *`ResultName`*.

The following values are possible for *`ResultName`* if
*`SurfaceMatchingResultID`* was created by [`find_surface_model`](find_surface_model.md)
or [`find_surface_model_image`](find_surface_model_image.md):

- ***'sampled_scene'*:** —

  A 3D object model handle is returned that
  contains the sampled scene points that were used in the
  approximate matching step.
  This is helpful for tuning the sampling distance for the
  matching (see parameter RelSamplingDistance of operator
  [`find_surface_model`](find_surface_model.md)).
  The parameter *`ResultIndex`* is ignored.
- ***'key_points'*:** —

  A 3D object model handle is returned that
  contains all points from the 3D scene that were used as key
  points in the matching process.
  This is helpful for tuning the sampling
  distance and key point rate for the matching (see parameter
  KeyPointFraction of operator [`find_surface_model`](find_surface_model.md)).
  The parameter *`ResultIndex`* is ignored.
  At least 10 key points should be on the object of interest for
  stable results.
- ***'score_unrefined'*:** —

  The score of the result before the
  dense pose refinement is returned. If the sparse pose refinement was
  disabled, this is the score of the approximate matching. Otherwise the
  score of the sparse pose refinement is returned.
  See [`find_surface_model`](find_surface_model.md) for details about the score.
  In *`ResultIndex`* the index of the result must be specified.
  If *`SurfaceMatchingResultID`* was created by
  [`refine_surface_model_pose`](refine_surface_model_pose.md), 0 is returned.
- ***'sampled_3d_edges'*:** —

  If the surface model was trained with *'train_3d_edges'*
  enabled, a 3D object model handle is returned that
  contains the sampled 3D edge points that were used in the
  approximate matching step and in the sparse refinement step.
  The parameter *`ResultIndex`* is ignored.

The following values are always possible for *`ResultName`*,
regardless the operator *`SurfaceMatchingResultID`* was created with:

- ***'pose'*:** —

  Returns the pose of the matching or refinement result.
  In *`ResultIndex`* the index of the result must be specified.
- ***'score_refined'*:** —

  Returns the score of the result after the dense pose refinement.
  See [`find_surface_model`](find_surface_model.md) for details about this score.
  In *`ResultIndex`* the index of the result must be specified.
  If *`SurfaceMatchingResultID`* was created by
  [`find_surface_model`](find_surface_model.md) and dense pose refinement was disabled,
  *0* is returned.
- ***'score'*:** —

  Returns the combined score of the result indexed in *`ResultIndex`*,
  thus this parameter is equal to `Score` returned in
  [`find_surface_model`](find_surface_model.md).
- ***'score_surface'*:** —

  Returns the surface-based score of the result indexed in
  *`ResultIndex`*.
  If not specifically set otherwise, this score is equal to
  *'score_refined'*.
- ***'score_3d_edges'*:** —

  Returns the 3D edge score of the result indexed in
  *`ResultIndex`*.
  This score is only applicable for edged-supported surface-based matching.
- ***'score_2d_edges'*:** —

  Returns the 2D edge score of the result indexed in
  *`ResultIndex`*.
  This score is only applicable for edged-supported surface-based matching.
- ***'score_view_based'*:** —

  Returns the view-based score of the result indexed in
  *`ResultIndex`*.
  This score is only applicable if the surface model supports view-based
  score computation.
- ***'all_scores'*:** —

  Returns for the result indexed in *`ResultIndex`*
  the values of the five scores
  *'score'*, *'score_surface'*, *'score_3d_edges'*,
  *'score_2d_edges'*, and *'score_view_based'*.
  Thereby the scores have the same order as the thresholds given through the
  parameter `MinScore` in the matching and refinement operators.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SurfaceMatchingResultID`** (input_control)  surface_matching_result `→`  (handle)

Handle of the surface matching result.

**`ResultName`** (input_control)  string(-array) `→`  (string)

Name of the result property.

Default:
'pose'

List of values:
'all_scores', 'key_points', 'pose', 'sampled_3d_edges', 'sampled_scene', 'score', 'score_2d_edges', 'score_3d_edges', 'score_refined', 'score_surface', 'score_unrefined', 'score_view_based'

**`ResultIndex`** (input_control)  integer `→`  (integer)

Index of the matching result, starting with 0.

Default:
0

Suggested values:
0, 1, 2, 3

Restriction:
`ResultIndex >= 0`

**`ResultValue`** (output_control)  integer(-array) `→`  (integer / string / real / handle)

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
