# get_operator_info (Operator)

## Name

`get_operator_info` — Get information concerning a HALCON-operator.

## Signature

`get_operator_info( : : OperatorName, Slot : Information)`

## Description

With the help of the operator `get_operator_info` the
online-texts concerning a certain operator can be called (see also
[`get_operator_name`](get_operator_name.md)). The form of information available for
all operators (*`Slot`*) can be called using the operator
[`query_operator_info`](query_operator_info.md). For the time being the following slots
are available:

- ***'short'*:** —

  Short description of the operator.
- ***'abstract'*:** —

  Description of the operator.
- ***'chapter'*:** —

  Name(s) of the chapter(s) in the operator hierarchy (chapter,
  subchapter in the HALCON manual).
- ***'functionality'*:** —

  Functionality is equivalent to the object class to which
  the operator can be assigned.
- ***'keywords'*:** —

  Keywords of the operator (optional).
- ***'example'*:** —

  Example for the use of the operator (optional). The operator
  'example.LANGUAGE' $$\text{(LANGU A GE}\in\text{\{trias,c,c++,c\#,vb .net\})}$$
  calls up examples for a certain language if available. If the
  language is not indicated or if no example is available in this
  language, the TRIAS-example will be returned.
- ***'complexity'*:** —

  Complexity of the operator (optional).
- ***'effect'*:** —

  Not in use so far.
- ***'parallelization'*:** —

  Characteristic timeout and parallel behavior of an operator.
- **'execution information':** —

  Characteristic timeout and parallel behavior of an operator.
- ***'parallel_method'*:** —

  Method of automatic operator parallelization.
- ***'interrupt_mode'*:** —

  Modes of interruption the operator can deal with. See
  [`set_operator_timeout`](set_operator_timeout.md) and [`interrupt_operator`](interrupt_operator.md)
  on how to use and set these interrupt modes.
- ***'alternatives'*:** —

  Alternative operators (optional).
- ***'see_also'*:** —

  Operators containing further information (optional).
- ***'predecessor'*:** —

  Possible and sensible predecessor
- ***'successor'*:** —

  Possible and sensible successor
- ***'result_state'*:** —

  Return value of the operator (2 (
  H_MSG_TRUE)
  , 3 (
  H_MSG_FALSE)
  , 5 (
  H_MSG_FAIL)
  , 4 (
  H_MSG_VOID)
  or EXCEPTION).
- ***'attention'*:** —

  Restrictions and advice concerning the correct use of the
  operator (optional).
- ***'parameter'*:** —

  Names of the parameter of the operator (see also
  [`get_param_info`](get_param_info.md)).
- ***'references'*:** —

  Literary references (optional).
- ***'module'*:** —

  The module to which the operator is assigned.
- ***'dynamic_modules'*:** —

  List of modules the operator can be assigned to by
  dynamic licensing (depending on its usage).
- ***'html_path'*:** —

  The directory where the HTML documentation of the operator resides.
- ***'warning'*:** —

  Possible warnings for using the operator.
- ***'compute_device'*:** —

  List of compute devices supported by the operator.

The texts will be taken from the `operators_[LANG].ref`,
`operators_[LANG].sta`, `operators_[LANG].key`,
`operators_[LANG].num` and `operators_[LANG].idx`,
which will be searched by HALCON in the currently used
directory or in the directory 'help_dir' (respectively 'user_help_dir') (see
also [`get_system`](get_system.md) and [`set_system`](set_system.md)).

## Attention

The encoding of the result is UTF-8.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OperatorName`** (input_control)  proc_name `→`  (string)

Name of the operator on which more information
is needed.

Default:
'get_operator_info'

**`Slot`** (input_control)  string `→`  (string)

Desired information.

Default:
'abstract'

List of values:
'abstract', 'alternatives', 'attention', 'chapter', 'chapter_id', 'complexity', 'compute_device', 'dynamic_modules', 'example', 'execution information', 'functionality', 'html_path', 'interrupt_mode', 'keywords', 'module', 'parallel_method', 'parallelization', 'parameter', 'predecessor', 'references', 'result_state', 'see_also', 'short', 'successor', 'warning'

**`Information`** (output_control)  string(-array) `→`  (string)

Information (empty if no information is available)

## Result

The operator `get_operator_info` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct and the helpfiles are available. Otherwise an
exception is raised.

## Possible Predecessors

`get_keywords`,
`search_operator`,
`get_operator_name`,
`query_operator_info`,
`query_param_info`,
`get_param_info`

## Possible Successors

`get_param_names`,
`get_param_num`,
`get_param_types`

## Alternatives

`get_param_names`

## See also

`query_operator_info`,
`get_param_info`,
`get_operator_name`,
`get_param_num`,
`get_param_types`

## Module

Foundation
