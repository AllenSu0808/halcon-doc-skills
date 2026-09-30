# get_operator_name (Operator)

## Name

`get_operator_name` — Get operators with the given string as a substring of their name.

## Signature

`def get_operator_name(pattern: str) -> Sequence[str]`

## Description

The operator `get_operator_name` takes a string (*`pattern`*)
as input and searches all HALCON-operators having this string as a substring
in their name. If an empty string is entered, the names of all operators available
will be returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`pattern`** (input_control)  string `→` str

Substring of the sought names (empty <=> all names).

Default:
"info"

**`operator_names`** (output_control)  string-array `→` Sequence[str]

Detected operator names.

## Result

The operator `get_operator_name` returns the value 2 (
H_MSG_TRUE)
if the helpfiles are
available.
Otherwise an exception is raised.

## Possible Successors

`get_operator_info`,
`get_param_names`,
`get_param_num`,
`get_param_types`

## Alternatives

`search_operator`

## See also

`get_operator_info`,
`get_param_names`,
`get_param_num`,
`get_param_types`

## Module

Foundation
