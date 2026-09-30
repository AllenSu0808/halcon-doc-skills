# get_param_types (Operator)

## Name

`get_param_types` — Get default data type for the control parameters of a HALCON-operator.

## Signature

`def get_param_types(operator_name: str) -> Tuple[Sequence[str], Sequence[str]]`

## Description

The operator `get_param_types` returns the default data type
for each input and output control parameter.
The default type of a parameter is the type used in “simple mode” in
HALCON/C. This concerns parameters which allow more than one type
as for example [`write_string`](write_string.md).
Hereby the types of input parameters are combined in the
variable *`inp_ctrl_par_type`*, whereas the types of output
parameters are combined in the variable *`outp_ctrl_par_type`*.
The following types are possible:

- ***"integer"*:** —

  an integer.
- **'integer tuple':** —

  an integer or a tuple of integers.
- ***"real"*:** —

  a floating point number.
- **'real tuple':** —

  a floating point number or a tuple of floating point numbers.
- ***"string"*:** —

  a string.
- **'string tuple':** —

  a string or a tuple of strings.
- ***"no_default"*:** —

  individual value of which the type cannot be determined.
- **'no_default tuple':** —

  individual value or tuple of values of which the type
  cannot be determined.
- ***"default"*:** —

  individual value of unknown type, whereby the systems assumes it to
  be an `integer`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  proc_name `→` str

Name of the operator.

Default:
"get_param_types"

**`inp_ctrl_par_type`** (output_control)  string-array `→` Sequence[str]

Default type of the input control parameters.

**`outp_ctrl_par_type`** (output_control)  string-array `→` Sequence[str]

Default type of the output control parameters.

## Result

The operator `get_param_types` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct and the helpfiles are available. Otherwise an
exception is raised.

## Possible Predecessors

`get_keywords`,
`search_operator`,
`get_operator_name`,
`get_operator_info`

## Alternatives

`get_param_info`

## See also

`get_param_names`,
`get_param_num`,
`get_operator_info`,
`get_operator_name`

## Module

Foundation
