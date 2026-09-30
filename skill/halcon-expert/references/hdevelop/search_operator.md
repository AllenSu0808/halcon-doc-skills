# search_operator (Operator)

## Name

`search_operator` — Search names of all operators assigned to one keyword.

## Signature

`search_operator( : : Keyword : OperatorNames)`

## Description

The operator `search_operator` returns the names of all operators
whose online-texts include the keyword *`Keyword`* (see also
[`get_operator_info`](get_operator_info.md)).
All available keywords are called by using the operator
`get_keywords(::”: <keywords>)`.
The online-texts are taken from the files `operators_[LANG].ref`,
`operators_[LANG].sta`, `operators_[LANG].key`,
`operators_[LANG].num` and `operators_[LANG].idx`,
which are searched by HALCON in the currently used
directory or the directory 'help_dir' (see also [`get_system`](get_system.md) and
[`get_system`](get_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Keyword`** (input_control)  string `→`  (string)

Keyword for which corresponding operators are searched.

Default:
'Information'

**`OperatorNames`** (output_control)  string-array `→`  (string)

Operators whose slot 'keyword' contains the keyword.

## Result

The operator `search_operator` returns the value 2 (
H_MSG_TRUE)
if the parameters
are correct and the helpfiles are available.
Otherwise an exception is raised.

## Possible Predecessors

`get_keywords`

## See also

`get_keywords`,
`get_operator_info`,
`get_param_info`

## Module

Foundation
