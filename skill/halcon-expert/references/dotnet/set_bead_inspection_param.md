# SetBeadInspectionParam (Operator)

## Name

`SetBeadInspectionParam` — Set parameters of the bead inspection model.

## Signature

`static void HOperatorSet.SetBeadInspectionParam(HTuple beadInspectionModel, HTuple genParamName, HTuple genParamValue)`

`void HBeadInspectionModel.SetBeadInspectionParam(HTuple genParamName, HTuple genParamValue)`

`void HBeadInspectionModel.SetBeadInspectionParam(string genParamName, string genParamValue)`

## Description

The operator `SetBeadInspectionParam` is used to set parameters
of a bead inspection model in order to adapt it to a particular inspection
task. All parameters except for the model's contour can be set with this
operator. A new bead
inspection model should be used when a new contour is introduced.
The current values of all parameters can be queried with the operator
[`GetBeadInspectionParam`](get_bead_inspection_param.md).

**Parameters that can be set**

The following parameters are essential and inspection model specific. It
is vital for the inspection's success to identify accurate values for
those parameters:

- ***"target_thickness"*:** —

  sets the `targetThickness`.
- ***"thickness_tolerance"*:** —

  sets the
  `thicknessTolerance`.
- ***"position_tolerance"*:** —

  sets the
  `positionTolerance`.
- ***"polarity"*:** —

  sets the bead's `polarity`.
- ***"sigma"*** —
- ***"threshold"*** —

For more details, refer to the parameters' description in
[`CreateBeadInspectionModel`](create_bead_inspection_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- beadInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`beadInspectionModel`** (input_control, state is modified)  bead_inspection_model `→` [HBeadInspectionModel](HBeadInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bead inspection model.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the model parameter that shall be adjusted for
the specified bead inspection model.

Default:
"target_thickness"

List of values:
"polarity", "position_tolerance", "sigma", "target_thickness", "thickness_tolerance", "threshold"

**`genParamValue`** (input_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the model parameter that shall be adjusted
for the specified bead inspection model.

Default:
40

Suggested values:
40, 10, 15, 0.6, 1.0, 4.0, 5.0, "light", "dark"

## Result

The operator `SetBeadInspectionParam` returns the value 2 (
H_MSG_TRUE)
if the given parameters are valid and within acceptable range.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBeadInspectionModel`

## Possible Successors

`ApplyBeadInspectionModel`,
`GetBeadInspectionParam`

## Alternatives

`CreateBeadInspectionModel`

## See also

`CreateBeadInspectionModel`,
`ClearBeadInspectionModel`

## Module

2D Metrology
