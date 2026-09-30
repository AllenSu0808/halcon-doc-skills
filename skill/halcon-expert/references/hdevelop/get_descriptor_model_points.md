# get_descriptor_model_points (Operator)

## Name

`get_descriptor_model_points` — Query the interest points of the descriptor model or the last processed
search image.

## Signature

`get_descriptor_model_points( : : ModelID, Set, Subset : Row, Column)`

## Description

With the operator `get_descriptor_model_points` interest points
of the descriptor model or the last processed search image can be
queried. It requires a *`ModelID`* returned by
[`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md),
[`create_calib_descriptor_model`](create_calib_descriptor_model.md), or [`read_descriptor_model`](read_descriptor_model.md).

The interest points stored in the model can always be queried by setting
*`Set`* to *'model'* and *`Subset`* to *'all'*.
If a [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) or
[`find_calib_descriptor_model`](find_calib_descriptor_model.md) precedes, with
`get_descriptor_model_points` the interest points of the last
search image can be queried as well by setting *`Set`* to
*'search'* and *`Subset`* to *'all'*. Additionally, the
matched (corresponding) points for each object instance found can be
queried by setting *`Set`* to *'model'* or *'search'*
(for the correspondences on the model or search image side, respectively)
and *`Subset`* to the result number of the instance. The image
coordinates of the queried points are returned in *`Row`* and
*`Column`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  descriptor_model `→`  (handle)

The handle to the descriptor model.

**`Set`** (input_control)  string `→`  (string)

Set of interest points.

Default:
'model'

List of values:
'model', 'search'

**`Subset`** (input_control)  integer `→`  (integer / string)

Subset of interest points.

Default:
'all'

Suggested values:
'all', 0, 1, 2

**`Row`** (output_control)  point.y-array `→`  (real / integer)

Row coordinates of interest points.

**`Column`** (output_control)  point.x-array `→`  (real / integer)

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

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`,
`find_uncalib_descriptor_model`,
`find_calib_descriptor_model`,
`read_descriptor_model`

## See also

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`

## Module

Matching
