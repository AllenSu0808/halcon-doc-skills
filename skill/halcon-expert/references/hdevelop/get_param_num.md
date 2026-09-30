# get_param_num (Operator)

## Name

`get_param_num` — Get number of the different parameter classes of a HALCON-operator.

## Signature

`get_param_num( : : OperatorName : CName, InpObjPar, OutpObjPar, InpCtrlPar, OutpCtrlPar, Type)`

## Description

The operator `get_param_num` returns the number of the input and
output object parameters, as well as the input and output control parameters for
the indicated HALCON-operator. Further, you will receive the name of the
C-function (*`CName`*) called by the operator.
The output parameter *`Type`* indicates, whether the operator
is a system operator or an user procedure.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OperatorName`** (input_control)  proc_name `→`  (string)

Name of the operator.

Default:
'get_param_num'

**`CName`** (output_control)  string `→`  (string)

Name of the called C-function.

**`InpObjPar`** (output_control)  integer `→`  (integer)

Number of the input object parameters.

**`OutpObjPar`** (output_control)  integer `→`  (integer)

Number of the output object parameters.

**`InpCtrlPar`** (output_control)  integer `→`  (integer)

Number of the input control parameters.

**`OutpCtrlPar`** (output_control)  integer `→`  (integer)

Number of the output control parameters.

**`Type`** (output_control)  string `→`  (string)

System operator or user procedure.

Suggested values:
'system', 'user'

## Result

The operator `get_param_num` returns the value 2 (
H_MSG_TRUE)
if the
name of the operator exists.
Otherwise an exception is raised.

## Possible Predecessors

`get_keywords`,
`search_operator`,
`get_operator_name`,
`get_operator_info`

## Possible Successors

`get_param_types`

## Alternatives

`get_operator_info`,
`get_param_info`

## See also

`get_param_names`,
`get_param_types`,
`get_operator_name`

## Module

Foundation
