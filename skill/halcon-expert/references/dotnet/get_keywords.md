# GetKeywords (Operator)

## Name

`GetKeywords` — Get keywords which are assigned to operators.

## Signature

`static void HOperatorSet.GetKeywords(HTuple operatorName, out HTuple keywords)`

`static HTuple HInfo.GetKeywords(string operatorName)`

## Description

The operator `GetKeywords` returns all the keywords in
the online-texts corresponding to those operators which have the indicated
substring *`operatorName`* in their name. If instead of *`operatorName`*
the empty string is transmitted, the operator `GetKeywords`
returns all keywords.
The keywords of an individual operator can also be called by using the
operator [`GetOperatorInfo`](get_operator_info.md).
The online-texts will be taken from the files `operators_[LANG].ref`,
`operators_[LANG].sta`, `operators_[LANG].key`,
`operators_[LANG].num` and `operators_[LANG].idx`,
which are searched by HALCON in the currently used
directory and in the directory 'help_dir' (see also [`GetSystem`](get_system.md) and
[`SetSystem`](set_system.md)).

## Attention

The encoding of the result is UTF-8.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operatorName`** (input_control)  proc_name `→` [HTuple](HTuple.md) (*string*)

Substring in the names of those operators for which
keywords are needed.

Default:
"get_keywords"

**`keywords`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Keywords for the operators.

## Result

The operator `GetKeywords` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct and the helpfiles are available.
Otherwise an exception is raised.

## Possible Predecessors

`GetChapterInfo`

## Alternatives

`GetOperatorInfo`

## See also

`GetOperatorName`,
`SearchOperator`,
`GetParamInfo`

## Module

Foundation
