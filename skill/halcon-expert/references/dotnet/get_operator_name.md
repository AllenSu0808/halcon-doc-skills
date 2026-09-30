# GetOperatorName (Operator)

## Name

`GetOperatorName` — Get operators with the given string as a substring of their name.

## Signature

`static void HOperatorSet.GetOperatorName(HTuple pattern, out HTuple operatorNames)`

`static HTuple HInfo.GetOperatorName(string pattern)`

## Description

The operator `GetOperatorName` takes a string (*`pattern`*)
as input and searches all HALCON-operators having this string as a substring
in their name. If an empty string is entered, the names of all operators available
will be returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pattern`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Substring of the sought names (empty <=> all names).

Default:
"info"

**`operatorNames`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Detected operator names.

## Result

The operator `GetOperatorName` returns the value 2 (
H_MSG_TRUE)
if the helpfiles are
available.
Otherwise an exception is raised.

## Possible Successors

`GetOperatorInfo`,
`GetParamNames`,
`GetParamNum`,
`GetParamTypes`

## Alternatives

`SearchOperator`

## See also

`GetOperatorInfo`,
`GetParamNames`,
`GetParamNum`,
`GetParamTypes`

## Module

Foundation
