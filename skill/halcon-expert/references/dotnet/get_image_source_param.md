# GetImageSourceParam (Operator)

## Name

`GetImageSourceParam` — Return the value of an image source parameter.

## Signature

`static void HOperatorSet.GetImageSourceParam(HTuple imageSourceHandle, HTuple param, HTuple genParamName, HTuple genParamValue, out HTuple value)`

`HTuple HImageSource.GetImageSourceParam(string param, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `GetImageSourceParam` returns the parameter
values or parameter properties for an image source handle
*`imageSourceHandle`* in *`value`*.

For further information about the image source concept see
[Image Source](toc_imagesource.md).

The parameter needs to be specified using *`param`*.
The parameter group can be specified using the generic parameters.
There are two types of information to be retrieved from the parameter
*`param`*. Use the generic parameter *`genParamName`* to
differentiate whether you want to get the value or meta information
regarding the parameter.
You have the following options for *`genParamName`*:

- ***"group"*** —

  Specify the parameter group the parameter is found in with
  *`genParamValue`* by setting one of these options:

  - *"image_source"*,
  - *"plugin"*,
  - *"interface"*,
  - *"local_device"*,
  - *"device"*,
  - *"stream"*.

  When setting no generic parameters, *`genParamName`* = *"group"*
  and *`genParamValue`* = *"device"* are assumed by default.

  The group *"image_source"* is always available, whereas a connection
  is needed for the other parameter groups.
- ***"property"*** —

  Retrieve meta information about *`param`*.
  Specify the requested parameter property with *`genParamValue`*
  by setting one of these options:

  - *"access"*: Provides access permissions as a string.

    List of values:
     *"na"* ((currently) not available),
    *"ro"* (read-only),
    *"rw"* (read/write),
    *"wo"* (write-only).
  - *"description"*: Provides a description of the parameter as a
    string.
  - *"display_name"*: Provides the display name of the parameter
    as a string.
  - *"increment"*: Provides the step width of the parameter as a
    real or integer value, depending on the data type of the parameter.
  - *"max"*: Provides the maximum value of the parameter as a
    real or integer value, depending on the data type of the parameter.
  - *"min"*: Provides the minimum value of the parameter as a
    real or integer value, depending on the data type of the parameter.
  - *"persistable"*: Provides information about the persistence
    of the parameter as an integer.

    List of values:
     *0* (false), *1* (true).
  - *"tooltip"*: Provides a short description of the parameter.
  - *"type"*: Provides the parameter type as a string.

    List of values:
     *"boolean"*, *"command"*, *"enumeration"*
    (string out of a list of allowed strings), *"integer"*,
    *"real"*, *"register"*, *"string"*.
  - *"values"*: Provides a list of all allowed values for
    parameters of *"type"* = *"enumeration"* and for some
    of *"type"* *"integer"* and *"real"*.
  - *"visibility"*: Provides information about the visibility
    of the parameter.

    List of values:
     *"basic"*, *"advanced"*, *"all"*.

### Image Source Handle Parameters

It depends on the image source and its state, which parameters *`param`*
can be retrieved. While some parameters are specific to the
hardware or software manufacturer and some depend on whether the image source
is in a connected state or not, the parameters of the *"image_source"*
group are always available. The following table gives an overview, which
of those parameters can be set using [`SetImageSourceParam`](set_image_source_param.md) and
which can be retrieved using `GetImageSourceParam`.
A description of the parameters can be found below the table.

| *`genParamName`* | `set` | `get` |
| --- | --- | --- |
| *"device_access_flags"* | `x` | `x` |
| *"device_access_status"* |  | `x` |
| *"device_connect_mode"* |  | `x` |
| *"device_id"* | `x` | `x` |
| *"device_is_connected"* |  | `x` |
| *"device_query_timeout"* | `x` | `x` |
| *"device_user_name"* | `x` | `x` |
| *"device_serial_number"* | `x` | `x` |
| *"fetch_timeout"* | `x` | `x` |
| *"interface_connect_mode"* |  | `x` |
| *"interface_display_name"* |  | `x` |
| *"interface_id"* | `x` | `x` |
| *"interface_is_connected"* |  | `x` |
| *"interface_query_timeout"* | `x` | `x` |
| *"num_buffers"* | `x` | `x` |
| *"plugin_connect_mode"* |  | `x` |
| *"plugin_is_connected"* |  | `x` |
| *"plugin_name"* | `x` | `x` |
| *"plugin_path"* | `x` | `x` |
| *"stream_connect_mode"* |  | `x` |
| *"stream_id"* | `x` | `x` |
| *"stream_is_connected"* |  | `x` |
| *"stream_state"* |  | `x` |
| *"version"* |  | `x` |

- ***"device_access_flags"*** —

  GenTL access flags used when attempting
  to connect to the device.

  - *"control"*: Open the device in a way that other
    hosts/processes can have read-only access to the device. Device access
    level is read/write for this process.
  - *"exclusive"*: Open the device in a way that only this
    host/process can have access to the device. Device access level is
    read/write for this process.
  - *"none"*: Either the device is not open because it
    was not opened before or the access to it was denied.
  - *"read_only"*: Open the device read-only. All port functions
    can only read from the device.
  - *"unknown"*: Not used in a command. Can be used to initialize
    a variable to query that information.
- ***"device_access_status"*** —

  Current GenTL access status of the
  device.

  - *"busy"*: Device has already been opened in
    *"exclusive"* mode by another process/host.
  - *"open_read_only"*: Device has already been opened by this
    process. Connection is set up in read-only mode, a different application
    has the *"control"* mode (see *"device_access_flags"*).
  - *"open_read_write"*: Device has already been opened by this
    process and handled in *"exclusive"* or *"control"* mode
    (see *"device_access_flags"*).
  - *"no_access"*: Device is not accessible
    (no connection possible).
  - *"read_only"*: Device is available for read-only access.
  - *"read_write"*: Device is available for read/write access
    (see *"device_access_flags"*).
  - *"unknown"*: Device accessibility is not known.
- ***"device_connect_mode"*** —

  Connect mode for the device module.

  - *"automatic"*: No identifier is provided, the required module
    will be automatically found and connected.
  - *"exact"*: A module identifier has been indicated for the
    module connection.
  - *"none"*: Module connection not needed.
- ***"device_id"*** —

  ID of the device as a string. It can be
  used to specify the device module to open during
  [`ConnectImageSource`](connect_image_source.md).
- ***"device_is_connected"*** —

  Connection status of the device as an
  integer.

  List of values:
   *0* (unconnected), *1* (connected).
- ***"device_query_timeout"*** —

  Desired timeout [ms] for
  aborting a pending device query. Is used as the device discovery timeout
  in GigEVision transport layers.
  If *-1* is specified, the timeout is set to infinite.

  Default:
   *1100*
- ***"device_serial_number"*** —

  Serial number of the device as a
  string. It can be used to specify which device to connect to when
  preferring not to use *"device_id"*.
- ***"device_user_name"*** —

  User name of the device as a string.
  It can be used to specify which device to connect to when
  preferring not to use *"device_id"*.
- ***"fetch_timeout"*** —

  Desired timeout [ms] for aborting a
  pending grab. If *-1* is specified, the timeout is set to infinite.

  Default:
   *5000*
- ***"interface_connect_mode"*** —

  Connect mode for the interface
  module.

  - *"automatic"*: No identifier is provided, the required module
    will be automatically found and connected.
  - *"exact"*: A module identifier has been indicated for the
    module connection.
  - *"none"*: Module connection not needed.
- ***"interface_display_name"*** —

  Provides a human-readable secondary
  identifier for the interface module as a string.
- ***"interface_id"*** —

  ID of the interface as a string. It can be
  used to specify the interface module to open during
  [`ConnectImageSource`](connect_image_source.md).
- ***"interface_is_connected"*** —

  Connection status of the interface
  as an integer.

  List of values:
   *0* (unconnected), *1* (connected).
- ***"interface_query_timeout"*** —

  Desired timeout [ms]
  for aborting a pending interface query.
  If *-1* is specified, the timeout is set to infinite.

  Default:
   *1100*
- ***"num_buffers"*** —

  Number of buffers that will be prepared
  by [`StartImageSource`](start_image_source.md) for receiving images.
  A larger number of buffers can help preventing image loss in short
  peak loads of the host system.
  The number of buffers can only be changed before starting the acquisition
  with [`StartImageSource`](start_image_source.md).

  Default:
   *4*
- ***"plugin_connect_mode"*** —

  Connect mode for the plugin module.

  - *"automatic"*: No identifier is provided, the required module
    will be automatically found and connected.
  - *"exact"*: A module identifier has been indicated for the
    module connection.
  - *"none"*: Module connection not needed.
- ***"plugin_is_connected"*** —

  Connection status of the plugin as an
  integer.

  List of values:
   *0* (unconnected), *1* (connected).
- ***"plugin_name"*** —

  Name of the plugin as a string.
- ***"plugin_path"*** —

  Path to the `.cti` plugin file.
  Can be used to specify the plugin file even when the GenTL environment
  variables to detect plugins do not contain the location of the desired
  plugin file.
- ***"stream_connect_mode"*** —

  Connect mode for the stream module.

  - *"automatic"*: No identifier is provided, the required module
    will be automatically found and connected.
  - *"exact"*: A module identifier has been indicated for the
    module connection.
  - *"none"*: Module connection not needed.
- ***"stream_id"*** —

  ID of the stream as a string. Can be
  used to specify the stream module to open during
  [`ConnectImageSource`](connect_image_source.md).
- ***"stream_is_connected"*** —

  Connection status of the stream as an
  integer.

  List of values:
   *0* (unconnected), *1* (connected).
- ***"stream_state"*** —

  Current state of the stream.

  - *"initialized"*: Stream is initialized but not running.
  - *"running"*: Stream is currently running. This means
    resources like threads and buffers are allocated in order to receive
    images.
    Depending on the device configuration, images are constantly
    transmitted in the background in this state.
- ***"version"*** —

  Version of the image source library.

For plugins provided by MVTec, the
[MVTec Interfaces Reference Documentation](https://docs.mvtec.com/interfaces/index.html) describes all plugin-specific parameters.

For further parameters, check the documentation of the respective software
or hardware manufacturer.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageSourceHandle`** (input_control)  image_source `→` [HImageSource](HImageSource.md), [HTuple](HTuple.md) (*IntPtr*)

Image source handle.

**`param`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Parameter to be retrieved.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

Suggested values:
"group", "property"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Generic parameter value.

Default:
[]

Suggested values:
"image_source", "plugin", "interface", "local_device", "device", "stream", "tooltip", "description", "display_name", "visibility", "access", "type", "persistable", "min", "max", "increment", "values"

**`value`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Retrieved value.

## Example (HDevelop)

```
* Get current selected pixel format (notice per default 'group'='device').
get_image_source_param (ImageSourceHandle, 'PixelFormat', [], [], PixelFormat)
* Get list of supported pixel formats by the device.
get_image_source_param (ImageSourceHandle, 'PixelFormat', 'property', 'values', AvailablePixelFormats)
* Get the version information of the plugin.
get_image_source_param (ImageSourceHandle, 'TLVersion', 'group', 'plugin', Version)
```

## Result

If the parameter values are correct, `GetImageSourceParam`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`QueryImageSources`,
`CreateImageSource`,
`ConnectImageSource`

## Possible Successors

`SetImageSourceParam`,
`DisconnectImageSource`

## See also

`SetImageSourceParam`

## Module

Foundation
