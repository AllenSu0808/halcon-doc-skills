# get_bead_inspection_param (Operator)

## Name

`get_bead_inspection_param` — Get the value of a parameter in a specific bead inspection model.

## Signature

`get_bead_inspection_param( : : BeadInspectionModel, GenParamName : GenParamValue)`

## Description

The operator `get_bead_inspection_param` is used to query the values
of the different parameters of a bead inspection model. The names of the
desired parameters are passed in the parameter *`GenParamName`*,
the corresponding values are returned in *`GenParamValue`*.
All these parameters can be set and changed at any time with the operator
[`set_bead_inspection_param`](set_bead_inspection_param.md). Multiple parameters can be queried
with a single call to `get_bead_inspection_param`.

The parameters that can be queried are *'target_thickness'*,
*'thickness_tolerance'*, *'position_tolerance'*,
*'polarity'*, *'sigma'* and *'threshold'*.
Only the model's contour cannot
be queried. Refer to [`set_bead_inspection_param`](set_bead_inspection_param.md) and
[`create_bead_inspection_model`](create_bead_inspection_model.md) for a detailed description of all
supported parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`BeadInspectionModel`** (input_control)  bead_inspection_model `→`  (handle)

Handle of the bead inspection model.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the model parameter that is queried.

Default:
'target_thickness'

List of values:
'polarity', 'position_tolerance', 'sigma', 'target_thickness', 'thickness_tolerance', 'threshold'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (integer / real / string)

Value of the queried model parameter.

## Result

The operator `get_bead_inspection_param` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_bead_inspection_model`,
`set_bead_inspection_param`

## Possible Successors

`apply_bead_inspection_model`,
`set_bead_inspection_param`

## See also

`create_bead_inspection_model`,
`set_bead_inspection_param`

## Module

2D Metrology
