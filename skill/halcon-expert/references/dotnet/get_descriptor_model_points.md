# GetDescriptorModelPoints (Operator)

## Name

`GetDescriptorModelPoints` — Query the interest points of the descriptor model or the last processed
search image.

## Signature

`static void HOperatorSet.GetDescriptorModelPoints(HTuple modelID, HTuple set, HTuple subset, out HTuple row, out HTuple column)`

`void HDescriptorModel.GetDescriptorModelPoints(string set, HTuple subset, out HTuple row, out HTuple column)`

`void HDescriptorModel.GetDescriptorModelPoints(string set, int subset, out HTuple row, out HTuple column)`

## Description

With the operator `GetDescriptorModelPoints` interest points
of the descriptor model or the last processed search image can be
queried. It requires a *`modelID`* returned by
[`CreateUncalibDescriptorModel`](create_uncalib_descriptor_model.md),
[`CreateCalibDescriptorModel`](create_calib_descriptor_model.md), or [`ReadDescriptorModel`](read_descriptor_model.md).

The interest points stored in the model can always be queried by setting
*`set`* to *"model"* and *`subset`* to *"all"*.
If a [`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md) or
[`FindCalibDescriptorModel`](find_calib_descriptor_model.md) precedes, with
`GetDescriptorModelPoints` the interest points of the last
search image can be queried as well by setting *`set`* to
*"search"* and *`subset`* to *"all"*. Additionally, the
matched (corresponding) points for each object instance found can be
queried by setting *`set`* to *"model"* or *"search"*
(for the correspondences on the model or search image side, respectively)
and *`subset`* to the result number of the instance. The image
coordinates of the queried points are returned in *`row`* and
*`column`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

The handle to the descriptor model.

**`set`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Set of interest points.

Default:
"model"

List of values:
"model", "search"

**`subset`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Subset of interest points.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of interest points.

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of interest points.

## Example (HDevelop)

```
create_uncalib_descriptor_model (Template,'harris',[],[],[],[],42, \
                                 ModelID)
* Model points can be queried from a model, even if just created
get_descriptor_model_points (ModelID,'model','all',ModelRow,ModelColumn)
find_uncalib_descriptor_model (Image,ModelID,[],[],[],[],0.2,1, \
                               'num_points',HomMat2D,Score)
* Search points can be queried only after a
* find_[un]calib_descriptor_model was executed
get_descriptor_model_points (ModelID,'search','all',SearchRow,SearchColumn)
* Additionally, correspondences for the results can be queried
NumObjects := |HomMat2D|/9
for I := 0 to NumObjects-1 by 1
    * Query corresponding points in the model
    get_descriptor_model_points (ModelID,'model',I, \
                                 CorrModelRow,CorrModelColumn)
    * Query corresponding points in the search image
    get_descriptor_model_points (ModelID,'search',I, \
                                 CorrSearchRow,CorrSearchColumn)
    * Those points are typically for visualizational purposes
    gen_cross_contour_xld (CrossModel,CorrModelRow,CorrModelColumn, \
                           6,0.78)
    gen_cross_contour_xld (CrossSearch,CorrSearchRow,CorrSearchColumn, \
                           6,0.78)

    * ....

endfor
```

## Possible Predecessors

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`,
`FindUncalibDescriptorModel`,
`FindCalibDescriptorModel`,
`ReadDescriptorModel`

## See also

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`

## Module

Matching
