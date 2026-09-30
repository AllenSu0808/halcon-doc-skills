# control_image_source (Operator)

## Name

`control_image_source` — Control actions available for an image source.

## Signature

`def control_image_source(image_source_handle: HHandle, action: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> Sequence[HTupleElementType]`

## Description

`control_image_source` initiates actions for the
image source specified in *`image_source_handle`*. If the action
returns a value, it is passed back in *`result`*.

For further information about the image source concept see
[Image Source](toc_imagesource.md).

The requested action is determined in *`action`*. Actions can be
global or targeting the individual module in the image source.
Some actions depend on whether the image source is in a connected state or
not.
The options for *`action`* available for every image source are:

- ***"enumerate_groups"*** —

  Returns all parameter group names. When
  querying *"enumerate_groups"*, the generic parameters
  *`gen_param_name`* and *`gen_param_value`* need to remain empty.
- ***"enumerate_params"*** —

  Returns all parameters available in the
  group that is set in *`gen_param_value`*.
  This action is specific to an image source module and therefore a
  parameter group has to be specified using generic parameters.

  *"group"* is the only option for *`gen_param_name`*.
  Specify the parameter group in *`gen_param_value`* by setting one
  of these options:

  - *"image_source"*,
  - *"plugin"*,
  - *"interface"*,
  - *"local_device"*,
  - *"device"*,
  - *"stream"*.

  When no generic parameters are set, *`gen_param_name`* = *"group"*
  and *`gen_param_value`* = *"device"* are assumed by default.
- ***"query_param_tree"*** —

  Returns a nested HALCON dictionary
  containing all parameter categories, sub-categories, and their parameters.
  For each contained parameter, its parameter type is also reported.

  This action is specific to an image source module and therefore a
  parameter group has to be specified using generic parameters.

  *"group"* is the only option for *`gen_param_name`*.
  Specify the parameter group in *`gen_param_value`* by setting one
  of these options:

  - *"image_source"*,
  - *"plugin"*,
  - *"interface"*,
  - *"local_device"*,
  - *"device"*,
  - *"stream"*.

  When no generic parameters are set, *`gen_param_name`* = *"group"*
  and *`gen_param_value`* = *"device"* are assumed by default.
- ***"write_state_string"*** —

  Returns a string containing information required to restore the values of
  all persistable parameters of the specified group. Only parameters
  whose parameter property *"persistable"* is *"true"* are
  included.

  This action is specific to an image source module and therefore a parameter
  group has to be specified using generic parameters.

  *"group"* is the only option for *`gen_param_name`*. Specify the
  parameter group in *`gen_param_value`* by setting one of these options:

  - *"plugin"*,
  - *"interface"*,
  - *"local_device"*,
  - *"device"*,
  - *"stream"*.

  When no generic parameters are set, *`gen_param_name`* is assumed to be
  *"group"* and *`gen_param_value`* is assumed to be
  *"device"*.

  This action cannot be used for the *"image_source"* group.
- ***"read_state_string"*** —

  Restores all persistable parameters of the
  specified group from the state string passed in the generic parameter
  *"state_string"*.

  *"group"* and *"state_string"* are the valid options for
  *`gen_param_name`*.

  The generic parameter *"state_string"* is mandatory and must contain the
  state string, which can be obtained using the *"write_state_string"*
  action.

  This action is specific to an image source module and therefore a
  parameter group has to be specified using generic parameters. Specify the
  parameter group in *`gen_param_value`* by setting one of these options:

  - *"plugin"*,
  - *"interface"*,
  - *"local_device"*,
  - *"device"*,
  - *"stream"*.

  When the generic parameter *"group"* is not set, the value
  *"device"* is assumed by default.

  This action cannot be used for the *"image_source"* group.
- ***"write_config_file"*** —

  Writes an image source configuration file, containing information required
  for a successful connection as well as to restore the values of
  all persistable parameters of all parameter groups.

  Writing the configuration file is allowed in the connected as well as in
  the unconnected state. If written in the unconnected state, it will not
  contain any information regarding the persistable parameters of the
  image source modules (device, plugin, ...).

  This action requires a path to the file that should be written. It must
  be passed together with *`gen_param_name`* = *"file_name"* in the
  corresponding *`gen_param_value`*.

  The default HALCON file extension for the image source configuration files
  is '.hisc'. If no extension is specified it will be appended automatically.

  To read these configuration files (and restore image source handles from them)
  refer to [`create_image_source`](create_image_source.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_source_handle`** (input_control)  image_source `→` HHandle

Image source handle.

**`action`** (input_control)  string `→` str

Action to be carried out.

Default:
"enumerate_params"

Suggested values:
"enumerate_params", "enumerate_groups", "query_param_tree", "write_state_string", "read_state_string", "write_config_file"

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic parameter name.

Default:
[]

Suggested values:
"group", "state_string", "file_name"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Generic parameter value.

Default:
[]

Suggested values:
"image_source", "plugin", "interface", "local_device", "device", "stream"

**`result`** (output_control)  string-array `→` Sequence[HTupleElementType]

Action result, if available.

## Result

If the parameter values are correct, `control_image_source`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`query_image_sources`,
`create_image_source`,
`connect_image_source`

## Possible Successors

`disconnect_image_source`

## See also

`set_image_source_param`,
`get_image_source_param`

## Module

Foundation
