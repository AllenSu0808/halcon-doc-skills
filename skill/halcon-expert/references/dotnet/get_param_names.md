# GetParamNames (Operator)

## Name

`GetParamNames` — Get the names of the parameters of a HALCON-operator.

## Signature

`static void HOperatorSet.GetParamNames(HTuple operatorName, out HTuple inpObjPar, out HTuple outpObjPar, out HTuple inpCtrlPar, out HTuple outpCtrlPar)`

`static HTuple HInfo.GetParamNames(string operatorName, out HTuple outpObjPar, out HTuple inpCtrlPar, out HTuple outpCtrlPar)`

## Description

For the HALCON-operator indicated in *`operatorName`* the operator
`GetParamNames` returns the names of the input objects, the output objects,
of the input control parameters and the output control parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operatorName`** (input_control)  proc_name `→` [HTuple](HTuple.md) (*string*)

Name of the operator.

Default:
"get_param_names"

**`inpObjPar`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the input objects.

**`outpObjPar`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the output objects.

**`inpCtrlPar`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the input control parameters.

**`outpCtrlPar`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Names of the output control parameters.

## Result

The operator `GetParamNames` returns the value 2 (
H_MSG_TRUE)
if the name of
the operator exists and the helpfiles are available.
Otherwise an exception is raised.

## Possible Predecessors

`GetKeywords`,
`SearchOperator`,
`GetOperatorName`,
`GetOperatorInfo`

## Possible Successors

`GetParamNum`,
`GetParamTypes`

## Alternatives

`GetOperatorInfo`,
`GetParamInfo`

## See also

`GetParamNum`,
`GetParamTypes`,
`GetOperatorName`

## Module

Foundation
