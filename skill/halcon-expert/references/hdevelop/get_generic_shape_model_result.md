# get_generic_shape_model_result (Operator)

## Name

`get_generic_shape_model_result` — Get alphanumerical values from a shape matching result.

## Signature

`get_generic_shape_model_result( : : MatchResultID, MatchSelector, GenParamName : GenParamValue)`

## Description

`get_generic_shape_model_result` returns alphanumerical results of
shape-based matching in *`GenParamValue`*. The matches are contained in
*`MatchResultID`* and sorted by descending score.

The parameter *`MatchSelector`* is used
to select from which matches the result values shall be returned.
The sorting remains according to their score.
Hence, it is independent of the order of the selection criteria passed in
*`MatchSelector`*. Furthermore, a matching result is only returned once
even if it meets more than one selection criterion.

*`MatchSelector`* processes selection criteria of the following types or
combinations of them:

- *'all'*:

  All matching results are selected.
- *'best'*:

  The match with the highest score is selected.
- Result index:

  By setting *`MatchSelector`* to an integer, the index of the match in
  *`MatchResultID`* is determined.

  Value range:
   0 to n-1 (with n as the total number of results).

  If the index is outside the valid range, an exception is raised.
- Shape model identifier:

  All matches found with a specific shape model are selected. For this
  you can pass the respective model identifier *'model_identifier'*
  as a string to *`MatchSelector`*.
- Shape model handle:

  All matches found with a specific shape model are selected. For this
  you can pass the respective shape model handle to
  *`MatchSelector`*.

If *`MatchSelector`* is no valid selection criterion, an exception
is raised.

*`GenParamName`* specifies which alphanumerical result value will
be returned. The following values are possible:

- *'num_match_result'*:

  Number of matches. The accumulated number of matches is returned in case
  multiple selections are made in *`MatchSelector`*.
- *'model_identifier'*:

  String identifying the model the match was found with.
- *'score'*:

  Score of the found match. It is a number between 0 and 1 and an approximate
  measure of how good the model is found in the image. For further
  information on scores, see
  `“Solution Guide II-B - Matching”`, Chapter 'General Topics',
  section 'About the Score'.
- *'angle'*:

  Rotation angle of the found match.

  Value range:
   *-3.14* $\le$ *'angle'*
  $\le$ *3.14* (=$\pi$).
- *'row'*:

  Row coordinate of the found match in the search image.
  The coordinate relates to the origin of the shape model.
- *'column'*:

  Column coordinate of the found match in the search image.
  The coordinate relates to the origin of the shape model.
- *'scale_row'*:

  Scale of the found match in row direction.
- *'scale_column'*:

  Scale of the found match in column direction.
- *'hom_mat_2d'*:

  Homographic transformation matrix to transform the contours of the shape
  model from its origin to the found location in the search image. Position,
  rotation, and scaling in row and column direction are taken into account.
  For more information on transformations with homographic matrices see
  [`affine_trans_point_2d`](affine_trans_point_2d.md).
- *'clutter_score'*:

  Clutter score of the found match. It is a number between 0 and 1 and an
  approximate measure of how much clutter edges are present in the clutter
  region.
- *'clutter_hom_mat_2d'*:

  Homographic transformation matrix to transform the clutter region of the
  shape model from its origin to the found location in the search image.
  Position, rotation, and scaling in row and column direction are taken into
  account.
- *'match'*:

  Dictionary containing the coordinate *'row'*, *'column'*, the
  rotation angle *'angle'*, the scale *'scale_row'*,
  *'scale_column'*, the score *'score'*, and the homographic
  transformation *'hom_mat_2d'* of the found match. Additionally, the
  two clutter-specific results *'clutter_score'* and
  *'clutter_hom_mat_2d'* are contained in the dictionary if clutter
  has been trained and used (see [`set_generic_shape_model_object`](set_generic_shape_model_object.md) with
  *'clutter_region'*).
- *'time_measurement'*:

  A dictionary containing the different time measurements that where
  conducted during the search. Note that their sum is less then the total time
  spent on the operator call.
  The dictionary contains time measurements for the four main
  steps of the search pipeline
  *'pipeline'*:

  - *'pyramid'*:

    Time spent constructing the image pyramid.
  - *'top_level'*:

    Time spent searching for candidates on highest pyramid level.
  - *'tracking'*:

    Time spent tracking candidates from the highest pyramid level to the
    lowest.
  - *'subpixel_refinement'*:

    Time spent conducting the refinement at the end of the search.

  Restriction:
   *`MatchSelector`* must be set to *'all'*.

Note that for values regarding the location of the matches
coordinates are given as edge centered coordinates. For more information
on edge centered coordinates see the chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatchResultID`** (input_control)  generic_shape_model_result `→`  (handle)

Handle of the shape model matches.

**`MatchSelector`** (input_control)  string-array `→`  (string / integer)

Selector for the matching results to be queried.

Default:
'all'

List of values:
'all', 'best'

**`GenParamName`** (input_control)  attribute.name `→`  (string)

Name of the queried result parameter.

Default:
'score'

List of values:
'angle', 'clutter_hom_mat_2d', 'clutter_score', 'column', 'hom_mat_2d', 'match', 'model_identifier', 'num_match_result', 'row', 'scale_column', 'scale_row', 'score', 'time_measurement'

**`GenParamValue`** (output_control)  attribute.value-array `→`  (real / integer / string)

Value of the queried result parameter.

## Result

If the parameters are valid, the operator
`get_generic_shape_model_result` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`find_generic_shape_model`

## Module

Matching
