# get_keywords (Operator)

## Name

`get_keywords` — Get keywords which are assigned to operators.

## Signature

`get_keywords( : : OperatorName : Keywords)`

## Description

The operator `get_keywords` returns all the keywords in
the online-texts corresponding to those operators which have the indicated
substring *`OperatorName`* in their name. If instead of *`OperatorName`*
the empty string is transmitted, the operator `get_keywords`
returns all keywords.
The keywords of an individual operator can also be called by using the
operator [`get_operator_info`](get_operator_info.md).
The online-texts will be taken from the files `operators_[LANG].ref`,
`operators_[LANG].sta`, `operators_[LANG].key`,
`operators_[LANG].num` and `operators_[LANG].idx`,
which are searched by HALCON in the currently used
directory and in the directory 'help_dir' (see also [`get_system`](get_system.md) and
[`set_system`](set_system.md)).

## Attention

The encoding of the result is UTF-8.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OperatorName`** (input_control)  proc_name `→`  (string)

Substring in the names of those operators for which
keywords are needed.

Default:
'get_keywords'

**`Keywords`** (output_control)  string-array `→`  (string)

Keywords for the operators.

## Result

The operator `get_keywords` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct and the helpfiles are available.
Otherwise an exception is raised.

## Possible Predecessors

`get_chapter_info`

## Alternatives

`get_operator_info`

## See also

`get_operator_name`,
`search_operator`,
`get_param_info`

## Module

Foundation
