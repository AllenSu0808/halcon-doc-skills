# GetParamTypes (Operator)

## Name

`GetParamTypes` — Get default data type for the control parameters of a HALCON-operator.

## Signature

`static void HOperatorSet.GetParamTypes(HTuple operatorName, out HTuple inpCtrlParType, out HTuple outpCtrlParType)`

`static HTuple HInfo.GetParamTypes(string operatorName, out HTuple outpCtrlParType)`

## Description

The operator `GetParamTypes` returns the default data type
for each input and output control parameter.
The default type of a parameter is the type used in “simple mode” in
HALCON/C. This concerns parameters which allow more than one type
as for example [`WriteString`](write_string.md).
Hereby the types of input parameters are combined in the
variable *`inpCtrlParType`*, whereas the types of output
parameters are combined in the variable *`outpCtrlParType`*.
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

**`operatorName`** (input_control)  proc_name `→` [HTuple](HTuple.md) (*string*)

Name of the operator.

Default:
"get_param_types"

**`inpCtrlParType`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Default type of the input control parameters.

**`outpCtrlParType`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Default type of the output control parameters.

## Result

The operator `GetParamTypes` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct and the helpfiles are available. Otherwise an
exception is raised.

## Possible Predecessors

`GetKeywords`,
`SearchOperator`,
`GetOperatorName`,
`GetOperatorInfo`

## Alternatives

`GetParamInfo`

## See also

`GetParamNames`,
`GetParamNum`,
`GetOperatorInfo`,
`GetOperatorName`

## Module

Foundation
