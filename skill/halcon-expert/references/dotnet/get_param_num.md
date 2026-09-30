# GetParamNum (Operator)

## Name

`GetParamNum` — Get number of the different parameter classes of a HALCON-operator.

## Signature

`static void HOperatorSet.GetParamNum(HTuple operatorName, out HTuple CName, out HTuple inpObjPar, out HTuple outpObjPar, out HTuple inpCtrlPar, out HTuple outpCtrlPar, out HTuple type)`

`static string HInfo.GetParamNum(string operatorName, out int inpObjPar, out int outpObjPar, out int inpCtrlPar, out int outpCtrlPar, out string type)`

## Description

The operator `GetParamNum` returns the number of the input and
output object parameters, as well as the input and output control parameters for
the indicated HALCON-operator. Further, you will receive the name of the
C-function (*`CName`*) called by the operator.
The output parameter *`type`* indicates, whether the operator
is a system operator or an user procedure.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operatorName`** (input_control)  proc_name `→` [HTuple](HTuple.md) (*string*)

Name of the operator.

Default:
"get_param_num"

**`CName`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the called C-function.

**`inpObjPar`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of the input object parameters.

**`outpObjPar`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of the output object parameters.

**`inpCtrlPar`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of the input control parameters.

**`outpCtrlPar`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of the output control parameters.

**`type`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

System operator or user procedure.

Suggested values:
"system", "user"

## Result

The operator `GetParamNum` returns the value 2 (
H_MSG_TRUE)
if the
name of the operator exists.
Otherwise an exception is raised.

## Possible Predecessors

`GetKeywords`,
`SearchOperator`,
`GetOperatorName`,
`GetOperatorInfo`

## Possible Successors

`GetParamTypes`

## Alternatives

`GetOperatorInfo`,
`GetParamInfo`

## See also

`GetParamNames`,
`GetParamTypes`,
`GetOperatorName`

## Module

Foundation
