# set_image_source_param (Operator)

## Name

`set_image_source_param` — Set a parameter of an image source.

## Signature

`set_image_source_param( : : ImageSourceHandle, Param, GenParamName, GenParamValue, Value : )`

## Description

The operator `set_image_source_param` sets the parameter
values for an image source handle *`ImageSourceHandle`* to
*`Value`*.

For further information about the image source concept see
[Image Source](toc_imagesource.md).

The parameter needs to be specified using *`Param`*.
The parameter group can be specified using the generic parameters.
You have the following options for *`GenParamName`*:

- ***'group'*** —

  Specify the parameter group the parameter is found
  in with *`GenParamValue`* by setting one of these options:

  - *'image_source'*,
  - *'plugin'*,
  - *'interface'*,
  - *'local_device'*,
  - *'device'*,
  - *'stream'*.

  When setting no generic parameters, *`GenParamName`* = *'group'*
  and *`GenParamValue`* = *'device'* are assumed by default.
- ***'command_wait'*** —

  Wait for the end of the command execution
  (blocking operation).

  List of values:
   *'false'*, *'true'*

  Default:
   *'true'*

  Restriction:
   Only valid for a *`Param`* of type
  *'command'*.
- ***'command_wait_interval'*** —

  Polling interval in [ms] to check if
  the command execution finished.

  Default:
   *100*

  Restriction:
   Only valid for a *`Param`* of type
  *'command'*.
- ***'command_wait_timeout'*** —

  Time in [ms] to wait for end of the
  command execution.

  Default:
   *5000*

  Restriction:
   Only valid for a *`Param`* of type
  *'command'*.

It depends on the image source and its state, which parameters *`Param`*
can be set. While some parameters are specific to the
hardware or software manufacturer and some depend on whether the image source
is in a connected state or not, the parameters of the *'image_source'*
group are always available.
The following list gives an overview, which of those parameters can be set
using `set_image_source_param`. A description of the parameters can be
found in [`get_image_source_param`](get_image_source_param.md).

- ***'device_access_flags'*** —
- ***'device_id'*** —
- ***'device_query_timeout'*** —
- ***'device_user_name'*** —
- ***'device_serial_number'*** —
- ***'fetch_timeout'*** —
- ***'interface_id'*** —
- ***'interface_query_timeout'*** —
- ***'num_buffers'*** —
- ***'plugin_name'*** —
- ***'plugin_path'*** —
- ***'stream_id'*** —

For plugins provided by MVTec, the
[MVTec Interfaces Reference Documentation](https://docs.mvtec.com/interfaces/index.html) describes all plugin-specific parameters.

*`Param`* is used to determine the desired parameter.
The value, the parameter should be set to is passed in *`Value`*.
Parameters of type *'command'* can be executed by
setting *`Value`* to *'execute'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageSourceHandle`** (input_control)  image_source `→`  (handle)

Image source handle.

**`Param`** (input_control)  string `→`  (string)

Parameter whose value is to be set.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic parameter name.

Default:
[]

Suggested values:
'group', 'command_wait', 'command_wait_timeout', 'command_wait_interval'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

Generic parameter value.

Default:
[]

Suggested values:
'image_source', 'plugin', 'interface', 'local_device', 'device', 'stream', 1, 5000, 100

**`Value`** (input_control)  string-array `→`  (string / real / integer)

Value to be set.

## Example (HDevelop)

```
* Configure or change the 'device_id' of the ImageSource (before the connect).
set_image_source_param (ImageSourceHandle,'device_id', 'group', 'image_source', '<desired_device_id>')
* Configure the ExposureTime of the connected camera (notice per default 'group'='device').
set_image_source_param (ImageSourceHandle, 'ExposureTime', [], [], 50000)
* Execute a software trigger (notice per default 'group'='device') without waiting for the end of the execution.
set_image_source_param (ImageSourceHandle, 'TriggerSoftware', 'command_wait', 0,'execute')
* Configure the handling of image buffers in the stream module.
set_image_source_param (ImageSourceHandle, 'StreamBufferHandlingMode', 'group', 'stream', 'NewestOnly')
```

## Result

If the parameter values are correct, `set_image_source_param`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`query_image_sources`,
`create_image_source`,
`connect_image_source`

## Possible Successors

`get_image_source_param`,
`disconnect_image_source`

## See also

`get_image_source_param`

## Module

Foundation
