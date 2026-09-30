# get_descriptor_model_results (Operator)

## Name

`get_descriptor_model_results` — Query alphanumerical results that were accumulated during descriptor-based
matching.

## Signature

`def get_descriptor_model_results(model_id: HHandle, object_id: Union[int, str], result_names: str) -> Sequence[Union[int, float, str]]`

`def get_descriptor_model_results_s(model_id: HHandle, object_id: Union[int, str], result_names: str) -> Union[int, float, str]`

## Description

The operator `get_descriptor_model_results` allows to access
alphanumeric results of the descriptor based matching process. The results
are stored in a descriptor based model specified by *`model_id`*.
*`object_id`* specifies for which object the results should be
returned. The objects are 0-based indexed and in the same order as they
are detected by [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) or
[`find_calib_descriptor_model`](find_calib_descriptor_model.md), respectively. Results can be queried
for all objects at once by specifying *"all"* in *`object_id`*,
if they are single valued (e.g., *`result_names`*=*"num_points"*
or *`result_names`*=*"inlier_ratio"*).

The results returned in *`results`* can be selected by setting
*`result_names`* to:

- ***"num_points"*:** —

  number of object points that correspond to model points.
- ***"inlier_ratio"*:** —

  ratio of successfully matched object points relative to
  all descriptor model points.
- ***"homography"*:** —

  a 3x3 projective transformation matrix which transforms model
  points into object points. Note that the result of the mapping depends
  on the selected model origin (see [`set_descriptor_model_origin`](set_descriptor_model_origin.md)).
- ***"pose"*:** —

  returns the estimated object pose. Note that this result can only be
  queried after [`find_calib_descriptor_model`](find_calib_descriptor_model.md) was called.
- ***"point_classification"*:** —

  returns concatenated triads representing the classification results for
  the interest points extracted from the search image during the last call
  of [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) or
  [`find_calib_descriptor_model`](find_calib_descriptor_model.md). Each triad consists of a
  *search point index* on the first, a *model point index*
  on the second, and a *classification score* on the third
  position. The search and model point indices correspond to the point
  coordinates returned by [`get_descriptor_model_points`](get_descriptor_model_points.md) with
  the parameter `subset` set to *"all"* and the parameter
  `set` set to *"search"* and *"model"*,
  respectively. If a number is passed in *`object_id`* only the
  classification results for the points matched to this object are
  returned. If *"all"* is passed in *`object_id`* the
  classification results for all points, including the points not matched
  to any object, are returned. The triads are sorted in descending order
  with respect to their score. Points having a score less than
  the value of the descriptor parameter *"min_score_descr"* (see
  [`find_calib_descriptor_model`](find_calib_descriptor_model.md) or
  [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md)) are rejected and are not listed
  in the resulting classification results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  descriptor_model `→` HHandle

Handle of a descriptor model.

**`object_id`** (input_control)  integer `→` Union[int, str]

Handle of the object for which the results are
queried.

Default:
"all"

Suggested values:
"all", 0, 1, 2, 3

**`result_names`** (input_control)  attribute.name `→` str

Name of the results to be queried.

Default:
"num_points"

List of values:
"homography", "inlier_ratio", "num_points", "point_classification", "pose"

**`results`** (output_control)  attribute.value(-array) `→` Sequence[Union[int, float, str]]

Returned results.

## Possible Predecessors

`find_uncalib_descriptor_model`,
`find_calib_descriptor_model`

## See also

`get_descriptor_model_origin`,
`get_descriptor_model_params`,
`get_descriptor_model_points`

## Module

Matching
