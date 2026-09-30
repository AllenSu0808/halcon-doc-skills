# SearchOperator (Operator)

## Name

`SearchOperator` — Search names of all operators assigned to one keyword.

## Signature

`static void HOperatorSet.SearchOperator(HTuple keyword, out HTuple operatorNames)`

`static HTuple HInfo.SearchOperator(string keyword)`

## Description

The operator `SearchOperator` returns the names of all operators
whose online-texts include the keyword *`keyword`* (see also
[`GetOperatorInfo`](get_operator_info.md)).
All available keywords are called by using the operator
`get_keywords(::”: <keywords>)`.
The online-texts are taken from the files `operators_[LANG].ref`,
`operators_[LANG].sta`, `operators_[LANG].key`,
`operators_[LANG].num` and `operators_[LANG].idx`,
which are searched by HALCON in the currently used
directory or the directory 'help_dir' (see also [`GetSystem`](get_system.md) and
[`GetSystem`](get_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`keyword`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Keyword for which corresponding operators are searched.

Default:
"Information"

**`operatorNames`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Operators whose slot 'keyword' contains the keyword.

## Result

The operator `SearchOperator` returns the value 2 (
H_MSG_TRUE)
if the parameters
are correct and the helpfiles are available.
Otherwise an exception is raised.

## Possible Predecessors

`GetKeywords`

## See also

`GetKeywords`,
`GetOperatorInfo`,
`GetParamInfo`

## Module

Foundation
