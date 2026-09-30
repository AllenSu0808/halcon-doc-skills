# get_param_info (Operator)

## Name

`get_param_info` — Get information concerning the operator parameters.

## Signature

`def get_param_info(operator_name: str, param_name: str, slot: str) -> Sequence[str]`

`def get_param_info_s(operator_name: str, param_name: str, slot: str) -> str`

## Description

The operator `get_param_info` is used for calling up the
online-texts assigned to a parameter of an indicated operator. The
form of information available for each parameter (*`slot`*),
can be called up by using the operator [`query_param_info`](query_param_info.md).
Possible slots are given in the list below.
For a more extensive description of the entries and their possible
values we refer to the `“Extension Package Programmer’s Manual”`.

- ***"description"*:** —

  Description of the parameter.
- ***"parameter_class"*:** —

  Parameter classes.

  *"input_object"*

  *"output_object"*

  *"input_control"*

  *"output_control"*
- ***"type_list"*:** —

  Permitted type(s) of data for parameter values.
- ***"default_type"*:** —

  Default-type for parameter values (for control parameters only).
  This type of parameter is the one HALCON/C uses in the
  “simple mode”. If *"none"* is indicated, the “tuple mode”
  must be used.
- ***"sem_type"*:** —

  Semantic type of the parameter. This is important to allow the
  assignment of the parameters to object classes in object-oriented
  languages (C++, .NET, COM). If more than one parameter belongs
  semantically to one type, this fact is indicated as well.
- ***"default_value"*:** —

  Default value for the parameter
  (for input control parameters only).
  It is the question of mere information only (the parameter
  value must be transmitted explicitly, even if the
  default value is used). This entry serves only as a notice, a
  point of departure for own experiments. The values have been
  selected so that they normally do not cause any errors but
  generate something that makes sense.
- ***"modified"*:** —

  *"true"*, if the operator modifies this input parameter.
- ***"multivalue"*:** —

  *"true"*, if an array of values must be passed,

  *"false"*, if exactly one value must be passed, and

  *"optional"* allows both.
- ***"multichannel"*:** —

  *"true"*, in case the input image object may be multichannel.
- ***"multiinstance"*:** —

  *"true"*, if an array of semantic tuples (e.g., poses, camera
  parameters, etc.) must be passed,

  *"false"*, if exactly one semantic tuple must be passed, and

  *"optional"* allows both.
- ***"mixed_type"*:** —

  For control parameters exclusively and only if value tuples
  (*"multivalue"*-*"true"*/*"optional"*) and various
  types of data are permitted for the parameter values
  ('type_list' having more than one value).
  In this case *`slot`* indicates, whether values of various
  types may be mixed in one tuple (*"true"* or *"false"*).
- ***"values"*:** —

  Selection of values (optional).
- ***"value_list"*:** —

  In case a parameter can take only a limited number of values, this
  fact will be indicated explicitly (optional).
- ***"valuemin"*:** —

  Minimum value of a value interval.
- ***"valuemax"*:** —

  Maximum value of a value interval.
- ***"valuefunction"*:** —

  Function describing the course of the values for a series of tests
  (lin, log, quadr, ...).
- ***"steprec"*:** —

  Recommended step width for the parameter values in a series of tests.
- ***"stepmin"*:** —

  Minimum step width of the parameter values in a series of tests.
- ***"valuenumber"*:** —

  Expression describing the number of parameters as such or in relation
  to other parameters.
- ***"assertion"*:** —

  Expression describing the parameter values as such or in
  relation to other parameters.
- **'cd_type_list.[compute_device]':** —

  List of input image types the compute device implementation of the
  operator supports for a specific device (use 'cd_type_list.opencl' for
  OpenCL devices).
- **'cd_value_list.[compute_device]':** —

  List of input control parameters the compute device implementation of
  the operator supports for a specific device (use 'cd_value_list.opencl'
  for OpenCL devices).

The online-texts will be taken from the files `operators_[LANG].ref`,
`operators_[LANG].sta`, `operators_[LANG].key`,
`operators_[LANG].num` and `operators_[LANG].idx`,
which will be searched by HALCON in the currently used
directory or the directory 'help_dir' (see also [`get_system`](get_system.md) and
[`set_system`](set_system.md)).

## Attention

The encoding of the result is UTF-8.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`operator_name`** (input_control)  proc_name `→` str

Name of the operator on whose parameter more information
is needed.

Default:
"get_param_info"

**`param_name`** (input_control)  string `→` str

Name of the parameter on which more information is needed.

Default:
"Slot"

**`slot`** (input_control)  string `→` str

Desired information.

Default:
"description"

List of values:
"assertion", "cd_type_list.opencl", "cd_value_list.opencl", "default_type", "default_value", "description", "mixed_type", "modified", "multichannel", "multivalue", "sem_type", "step_min", "step_rec", "type_list", "value_function", "value_list", "value_max", "value_min", "value_number", "values"

**`information`** (output_control)  string(-array) `→` Sequence[str]

Information (empty in case there is no information
available).

## Result

The operator `get_param_info` returns the value 2 (
H_MSG_TRUE)
if the
parameters are correct and the helpfiles are available. Otherwise an
exception is raised.

## Possible Predecessors

`get_keywords`,
`search_operator`

## Alternatives

`get_param_names`,
`get_param_num`,
`get_param_types`

## See also

`query_param_info`,
`get_operator_info`,
`get_operator_name`

## Module

Foundation
