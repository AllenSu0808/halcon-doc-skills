# GetDescriptorModelResults (Operator)

## Name

`GetDescriptorModelResults` — Query alphanumerical results that were accumulated during descriptor-based
matching.

## Signature

`static void HOperatorSet.GetDescriptorModelResults(HTuple modelID, HTuple objectID, HTuple resultNames, out HTuple results)`

`HTuple HDescriptorModel.GetDescriptorModelResults(HTuple objectID, string resultNames)`

`HTuple HDescriptorModel.GetDescriptorModelResults(int objectID, string resultNames)`

## Description

The operator `GetDescriptorModelResults` allows to access
alphanumeric results of the descriptor based matching process. The results
are stored in a descriptor based model specified by *`modelID`*.
*`objectID`* specifies for which object the results should be
returned. The objects are 0-based indexed and in the same order as they
are detected by [`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md) or
[`FindCalibDescriptorModel`](find_calib_descriptor_model.md), respectively. Results can be queried
for all objects at once by specifying *"all"* in *`objectID`*,
if they are single valued (e.g., *`resultNames`*=*"num_points"*
or *`resultNames`*=*"inlier_ratio"*).

The results returned in *`results`* can be selected by setting
*`resultNames`* to:

- ***"num_points"*:** —

  number of object points that correspond to model points.
- ***"inlier_ratio"*:** —

  ratio of successfully matched object points relative to
  all descriptor model points.
- ***"homography"*:** —

  a 3x3 projective transformation matrix which transforms model
  points into object points. Note that the result of the mapping depends
  on the selected model origin (see [`SetDescriptorModelOrigin`](set_descriptor_model_origin.md)).
- ***"pose"*:** —

  returns the estimated object pose. Note that this result can only be
  queried after [`FindCalibDescriptorModel`](find_calib_descriptor_model.md) was called.
- ***"point_classification"*:** —

  returns concatenated triads representing the classification results for
  the interest points extracted from the search image during the last call
  of [`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md) or
  [`FindCalibDescriptorModel`](find_calib_descriptor_model.md). Each triad consists of a
  *search point index* on the first, a *model point index*
  on the second, and a *classification score* on the third
  position. The search and model point indices correspond to the point
  coordinates returned by [`GetDescriptorModelPoints`](get_descriptor_model_points.md) with
  the parameter `subset` set to *"all"* and the parameter
  `set` set to *"search"* and *"model"*,
  respectively. If a number is passed in *`objectID`* only the
  classification results for the points matched to this object are
  returned. If *"all"* is passed in *`objectID`* the
  classification results for all points, including the points not matched
  to any object, are returned. The triads are sorted in descending order
  with respect to their score. Points having a score less than
  the value of the descriptor parameter *"min_score_descr"* (see
  [`FindCalibDescriptorModel`](find_calib_descriptor_model.md) or
  [`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md)) are rejected and are not listed
  in the resulting classification results.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a descriptor model.

**`objectID`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Handle of the object for which the results are
queried.

Default:
"all"

Suggested values:
"all", 0, 1, 2, 3

**`resultNames`** (input_control)  attribute.name `→` [HTuple](HTuple.md) (*string*)

Name of the results to be queried.

Default:
"num_points"

List of values:
"homography", "inlier_ratio", "num_points", "point_classification", "pose"

**`results`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Returned results.

## Possible Predecessors

`FindUncalibDescriptorModel`,
`FindCalibDescriptorModel`

## See also

`GetDescriptorModelOrigin`,
`GetDescriptorModelParams`,
`GetDescriptorModelPoints`

## Module

Matching
