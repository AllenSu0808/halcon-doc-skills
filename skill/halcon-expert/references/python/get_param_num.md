# get_param_num (Operator)

## Name

`get_param_num` — Get number of the different parameter classes of a HALCON-operator.

## Signature

`def get_param_num(operator_name: str) -> Tuple[str, int, int, int, int, str]`

## Description

The operator `get_param_num` returns the number of the input and
output object parameters, as well as the input and output control parameters for
the indicated HALCON-operator. Further, you will receive the name of the
C-function (*`cname`*) called by the operator.
The output parameter *`type`* indicates, whether the operator
is a system operator or an user procedure.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  proc_name `→` str

Name of the operator.

Default:
"get_param_num"

**`cname`** (output_control)  string `→` str

Name of the called C-function.

**`inp_obj_par`** (output_control)  integer `→` int

Number of the input object parameters.

**`outp_obj_par`** (output_control)  integer `→` int

Number of the output object parameters.

**`inp_ctrl_par`** (output_control)  integer `→` int

Number of the input control parameters.

**`outp_ctrl_par`** (output_control)  integer `→` int

Number of the output control parameters.

**`type`** (output_control)  string `→` str

System operator or user procedure.

Suggested values:
"system", "user"

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
