# control_image_source (Operator)

## Name

`control_image_source` — Control actions available for an image source.

## Signature

`control_image_source( : : ImageSourceHandle, Action, GenParamName, GenParamValue : Result)`

## Description

`control_image_source` initiates actions for the
image source specified in *`ImageSourceHandle`*. If the action
returns a value, it is passed back in *`Result`*.

For further information about the image source concept see
[Image Source](toc_imagesource.md).

The requested action is determined in *`Action`*. Actions can be
global or targeting the individual module in the image source.
Some actions depend on whether the image source is in a connected state or
not.
The options for *`Action`* available for every image source are:

- ***'enumerate_groups'*** —

  Returns all parameter group names. When
  querying *'enumerate_groups'*, the generic parameters
  *`GenParamName`* and *`GenParamValue`* need to remain empty.
- ***'enumerate_params'*** —

  Returns all parameters available in the
  group that is set in *`GenParamValue`*.
  This action is specific to an image source module and therefore a
  parameter group has to be specified using generic parameters.

  *'group'* is the only option for *`GenParamName`*.
  Specify the parameter group in *`GenParamValue`* by setting one
  of these options:

  - *'image_source'*,
  - *'plugin'*,
  - *'interface'*,
  - *'local_device'*,
  - *'device'*,
  - *'stream'*.

  When no generic parameters are set, *`GenParamName`* = *'group'*
  and *`GenParamValue`* = *'device'* are assumed by default.
- ***'query_param_tree'*** —

  Returns a nested HALCON dictionary
  containing all parameter categories, sub-categories, and their parameters.
  For each contained parameter, its parameter type is also reported.

  This action is specific to an image source module and therefore a
  parameter group has to be specified using generic parameters.

  *'group'* is the only option for *`GenParamName`*.
  Specify the parameter group in *`GenParamValue`* by setting one
  of these options:

  - *'image_source'*,
  - *'plugin'*,
  - *'interface'*,
  - *'local_device'*,
  - *'device'*,
  - *'stream'*.

  When no generic parameters are set, *`GenParamName`* = *'group'*
  and *`GenParamValue`* = *'device'* are assumed by default.
- ***'write_state_string'*** —

  Returns a string containing information required to restore the values of
  all persistable parameters of the specified group. Only parameters
  whose parameter property *'persistable'* is *'true'* are
  included.

  This action is specific to an image source module and therefore a parameter
  group has to be specified using generic parameters.

  *'group'* is the only option for *`GenParamName`*. Specify the
  parameter group in *`GenParamValue`* by setting one of these options:

  - *'plugin'*,
  - *'interface'*,
  - *'local_device'*,
  - *'device'*,
  - *'stream'*.

  When no generic parameters are set, *`GenParamName`* is assumed to be
  *'group'* and *`GenParamValue`* is assumed to be
  *'device'*.

  This action cannot be used for the *'image_source'* group.
- ***'read_state_string'*** —

  Restores all persistable parameters of the
  specified group from the state string passed in the generic parameter
  *'state_string'*.

  *'group'* and *'state_string'* are the valid options for
  *`GenParamName`*.

  The generic parameter *'state_string'* is mandatory and must contain the
  state string, which can be obtained using the *'write_state_string'*
  action.

  This action is specific to an image source module and therefore a
  parameter group has to be specified using generic parameters. Specify the
  parameter group in *`GenParamValue`* by setting one of these options:

  - *'plugin'*,
  - *'interface'*,
  - *'local_device'*,
  - *'device'*,
  - *'stream'*.

  When the generic parameter *'group'* is not set, the value
  *'device'* is assumed by default.

  This action cannot be used for the *'image_source'* group.
- ***'write_config_file'*** —

  Writes an image source configuration file, containing information required
  for a successful connection as well as to restore the values of
  all persistable parameters of all parameter groups.

  Writing the configuration file is allowed in the connected as well as in
  the unconnected state. If written in the unconnected state, it will not
  contain any information regarding the persistable parameters of the
  image source modules (device, plugin, ...).

  This action requires a path to the file that should be written. It must
  be passed together with *`GenParamName`* = *'file_name'* in the
  corresponding *`GenParamValue`*.

  The default HALCON file extension for the image source configuration files
  is '.hisc'. If no extension is specified it will be appended automatically.

  To read these configuration files (and restore image source handles from them)
  refer to [`create_image_source`](create_image_source.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageSourceHandle`** (input_control)  image_source `→`  (handle)

Image source handle.

**`Action`** (input_control)  string `→`  (string)

Action to be carried out.

Default:
'enumerate_params'

Suggested values:
'enumerate_params', 'enumerate_groups', 'query_param_tree', 'write_state_string', 'read_state_string', 'write_config_file'

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic parameter name.

Default:
[]

Suggested values:
'group', 'state_string', 'file_name'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

Generic parameter value.

Default:
[]

Suggested values:
'image_source', 'plugin', 'interface', 'local_device', 'device', 'stream'

**`Result`** (output_control)  string-array `→`  (string / real / integer / handle)

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
