# set_image_source_param (Operator)

## Name

`set_image_source_param` — Set a parameter of an image source.

## Signature

`def set_image_source_param(image_source_handle: HHandle, param: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]], value: Sequence[Union[str, float, int]]) -> None`

## Description

The operator `set_image_source_param` sets the parameter
values for an image source handle *`image_source_handle`* to
*`value`*.

For further information about the image source concept see
[Image Source](toc_imagesource.md).

The parameter needs to be specified using *`param`*.
The parameter group can be specified using the generic parameters.
You have the following options for *`gen_param_name`*:

- ***"group"*** —

  Specify the parameter group the parameter is found
  in with *`gen_param_value`* by setting one of these options:

  - *"image_source"*,
  - *"plugin"*,
  - *"interface"*,
  - *"local_device"*,
  - *"device"*,
  - *"stream"*.

  When setting no generic parameters, *`gen_param_name`* = *"group"*
  and *`gen_param_value`* = *"device"* are assumed by default.
- ***"command_wait"*** —

  Wait for the end of the command execution
  (blocking operation).

  List of values:
   *"false"*, *"true"*

  Default:
   *"true"*

  Restriction:
   Only valid for a *`param`* of type
  *"command"*.
- ***"command_wait_interval"*** —

  Polling interval in [ms] to check if
  the command execution finished.

  Default:
   *100*

  Restriction:
   Only valid for a *`param`* of type
  *"command"*.
- ***"command_wait_timeout"*** —

  Time in [ms] to wait for end of the
  command execution.

  Default:
   *5000*

  Restriction:
   Only valid for a *`param`* of type
  *"command"*.

It depends on the image source and its state, which parameters *`param`*
can be set. While some parameters are specific to the
hardware or software manufacturer and some depend on whether the image source
is in a connected state or not, the parameters of the *"image_source"*
group are always available.
The following list gives an overview, which of those parameters can be set
using `set_image_source_param`. A description of the parameters can be
found in [`get_image_source_param`](get_image_source_param.md).

- ***"device_access_flags"*** —
- ***"device_id"*** —
- ***"device_query_timeout"*** —
- ***"device_user_name"*** —
- ***"device_serial_number"*** —
- ***"fetch_timeout"*** —
- ***"interface_id"*** —
- ***"interface_query_timeout"*** —
- ***"num_buffers"*** —
- ***"plugin_name"*** —
- ***"plugin_path"*** —
- ***"stream_id"*** —

For plugins provided by MVTec, the
[MVTec Interfaces Reference Documentation](https://docs.mvtec.com/interfaces/index.html) describes all plugin-specific parameters.

*`param`* is used to determine the desired parameter.
The value, the parameter should be set to is passed in *`value`*.
Parameters of type *"command"* can be executed by
setting *`value`* to *"execute"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_source_handle`** (input_control)  image_source `→` HHandle

Image source handle.

**`param`** (input_control)  string `→` str

Parameter whose value is to be set.

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic parameter name.

Default:
[]

Suggested values:
"group", "command_wait", "command_wait_timeout", "command_wait_interval"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Generic parameter value.

Default:
[]

Suggested values:
"image_source", "plugin", "interface", "local_device", "device", "stream", 1, 5000, 100

**`value`** (input_control)  string-array `→` Sequence[Union[str, float, int]]

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
