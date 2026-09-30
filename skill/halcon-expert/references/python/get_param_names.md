# get_param_names (Operator)

## Name

`get_param_names` — Get the names of the parameters of a HALCON-operator.

## Signature

`def get_param_names(operator_name: str) -> Tuple[Sequence[str], Sequence[str], Sequence[str], Sequence[str]]`

## Description

For the HALCON-operator indicated in *`operator_name`* the operator
`get_param_names` returns the names of the input objects, the output objects,
of the input control parameters and the output control parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  proc_name `→` str

Name of the operator.

Default:
"get_param_names"

**`inp_obj_par`** (output_control)  string-array `→` Sequence[str]

Names of the input objects.

**`outp_obj_par`** (output_control)  string-array `→` Sequence[str]

Names of the output objects.

**`inp_ctrl_par`** (output_control)  string-array `→` Sequence[str]

Names of the input control parameters.

**`outp_ctrl_par`** (output_control)  string-array `→` Sequence[str]

Names of the output control parameters.

## Result

The operator `get_param_names` returns the value 2 (
H_MSG_TRUE)
if the name of
the operator exists and the helpfiles are available.
Otherwise an exception is raised.

## Possible Predecessors

`get_keywords`,
`search_operator`,
`get_operator_name`,
`get_operator_info`

## Possible Successors

`get_param_num`,
`get_param_types`

## Alternatives

`get_operator_info`,
`get_param_info`

## See also

`get_param_num`,
`get_param_types`,
`get_operator_name`

## Module

Foundation
