# GetBeadInspectionParam (Operator)

## Name

`GetBeadInspectionParam` — Get the value of a parameter in a specific bead inspection model.

## Signature

`static void HOperatorSet.GetBeadInspectionParam(HTuple beadInspectionModel, HTuple genParamName, out HTuple genParamValue)`

`HTuple HBeadInspectionModel.GetBeadInspectionParam(HTuple genParamName)`

`HTuple HBeadInspectionModel.GetBeadInspectionParam(string genParamName)`

## Description

The operator `GetBeadInspectionParam` is used to query the values
of the different parameters of a bead inspection model. The names of the
desired parameters are passed in the parameter *`genParamName`*,
the corresponding values are returned in *`genParamValue`*.
All these parameters can be set and changed at any time with the operator
[`SetBeadInspectionParam`](set_bead_inspection_param.md). Multiple parameters can be queried
with a single call to `GetBeadInspectionParam`.

The parameters that can be queried are *"target_thickness"*,
*"thickness_tolerance"*, *"position_tolerance"*,
*"polarity"*, *"sigma"* and *"threshold"*.
Only the model's contour cannot
be queried. Refer to [`SetBeadInspectionParam`](set_bead_inspection_param.md) and
[`CreateBeadInspectionModel`](create_bead_inspection_model.md) for a detailed description of all
supported parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`beadInspectionModel`** (input_control)  bead_inspection_model `→` [HBeadInspectionModel](HBeadInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bead inspection model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the model parameter that is queried.

Default:
"target_thickness"

List of values:
"polarity", "position_tolerance", "sigma", "target_thickness", "thickness_tolerance", "threshold"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Value of the queried model parameter.

## Result

The operator `GetBeadInspectionParam` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBeadInspectionModel`,
`SetBeadInspectionParam`

## Possible Successors

`ApplyBeadInspectionModel`,
`SetBeadInspectionParam`

## See also

`CreateBeadInspectionModel`,
`SetBeadInspectionParam`

## Module

2D Metrology
