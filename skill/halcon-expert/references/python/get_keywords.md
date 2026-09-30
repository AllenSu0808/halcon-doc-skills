# get_keywords (Operator)

## Name

`get_keywords` — Get keywords which are assigned to operators.

## Signature

`def get_keywords(operator_name: str) -> Sequence[str]`

## Description

The operator `get_keywords` returns all the keywords in
the online-texts corresponding to those operators which have the indicated
substring *`operator_name`* in their name. If instead of *`operator_name`*
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

**`operator_name`** (input_control)  proc_name `→` str

Substring in the names of those operators for which
keywords are needed.

Default:
"get_keywords"

**`keywords`** (output_control)  string-array `→` Sequence[str]

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
