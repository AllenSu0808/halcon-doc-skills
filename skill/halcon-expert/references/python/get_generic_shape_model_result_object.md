# get_generic_shape_model_result_object (Operator)

## Name

`get_generic_shape_model_result_object` — Get objects from a shape matching result.

## Signature

`def get_generic_shape_model_result_object(match_result_id: HHandle, match_selector: Sequence[Union[str, int]], gen_param_name: Union[str, HHandle]) -> HObject`

## Description

`get_generic_shape_model_result_object` returns iconic results of
shape-based matching in *`objects`*.
The results are contained in *`match_result_id`*.

The parameter *`match_selector`* is used
to select from which matches the result values shall be returned. For more
information and the list of supported values for *`match_selector`*
see [`get_generic_shape_model_result`](get_generic_shape_model_result.md).

*`gen_param_name`* specifies which object result value will
be returned. The following values are possible:

- ***"contours"*:** —

  Model contours transformed according to the matching result.

  Attention:
   Model contours are only available if the search was
  conducted with *"prepare_contours_for_visualization"* set to
  *"true"*.
- ***"clutter_region"*:** —

  Region where no clutter should occur.

  Attention:
   The clutter region is only available if a clutter region
  was added to the model and the search was conducted with
  *"prepare_clutter_region_for_visualization"* set to *"true"*.
- **A dictionary:** —

  Parameters which require additional information to get an iconic result are
  passed as a dictionary with the key `'param_name'` with additional
  key/value pairs depending on the queried `'param_name'`.
  Unknown keys are ignored.
  The following parameters can be queried:

  - `score_visualization_contours`:
    Parts of model contours where the model point score contributions are
    within the given interval.
    The contours are transformed according to the corresponding match.
    The following additional keys are required to get
    `score_visualization_contours`:

    - `low`:
      Low threshold of the interval.
      Model contours with score contributions greater or equal `low`
      are returned.
      `low` is either a real valued number in the range
      [*-1.0*, *1.0*] or the string *"min"* as the lowest
      possible value.
    - `high`:
      High threshold of the interval.
      Model contours with score contributions smaller than `high` are
      returned.
      `high` is either a real valued number in the range
      [*-1.0*, *1.0*] or the string *"max"* as the highest
      possible value. Note that for *1.0* and *"max"* the
      threshold is treated inclusively, i.e. contour parts with score
      contributions smaller than and equal to *1.0* and *"max"*
      are returned.

    The score contributions are calculated in
    [`find_generic_shape_model`](find_generic_shape_model.md) for each model point. All contour parts,
    for which the median of their surrounding score contributions is higher
    or equal `'low'` and less than `'high'`, are returned.

    Details about the selection
    - 16 score contributions are considered for the median.
    - For contours with less than 16 score contributions, the median of
      all score contributions is evaluated once and compared to the
      thresholds.
    - For longer closed contours, the window in which score
      contributions are taken into account continues over the start and end
      point of closed contours.
    - For longer open contours, the first or last score contribution is
      repeated at the start or end respectively.

    Note that depending on *"metric"* used in each model during
    [`find_generic_shape_model`](find_generic_shape_model.md) the range of score contributions is
    different.

    Attention:
     The score contributions are only available if the search
    was conducted with *"score_visualization"* set to
    *"true"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objects`** (output_object)  (multichannel-)object(-array) `→` HObject

Objects of the queried result.

**`match_result_id`** (input_control)  generic_shape_model_result `→` HHandle

Handle of the shape model matches.

**`match_selector`** (input_control)  string-array `→` Sequence[Union[str, int]]

Selector for the matching results to be queried.

Default:
"all"

List of values:
"all", "best"

**`gen_param_name`** (input_control)  attribute.name `→` Union[str, HHandle]

Name of the queried result object.

Default:
"contours"

List of values:
"clutter_region", "contours"

## Example (HDevelop)

```
* Get score visualization contours by passing a dictionary for GenParamName.
GenParamName := dict{param_name: 'score_visualization_contours'}
GenParamName.low := 0.25
GenParamName.high := 'max'
get_generic_shape_model_result_object (ScoreVisContour, MatchResultID, \
                                      'all', GenParamName)
```

## Result

If the parameters are valid, the operator
`get_generic_shape_model_result_object` returns the value 2 (
H_MSG_TRUE)
.
If necessary an exception is raised.

## Possible Predecessors

`find_generic_shape_model`

## Module

Matching
