# CreateImageSource (Operator)

## Name

`CreateImageSource` — Create an image source handle.

## Signature

`static void HOperatorSet.CreateImageSource(HTuple pluginName, HTuple deviceID, HTuple genParamName, HTuple genParamValue, out HTuple imageSourceHandle)`

`public HImageSource(string pluginName, string deviceID, HTuple genParamName, HTuple genParamValue)`

`void HImageSource.CreateImageSource(string pluginName, string deviceID, HTuple genParamName, HTuple genParamValue)`

## Description

`CreateImageSource` creates an image source handle and returns it
in *`imageSourceHandle`*. The created handle is in an unconnected
state. The parameters *`pluginName`* and *`deviceID`* can be used
to specify the plugin and device module of the image source handle.
Alternatively, the generic parameters *`genParamName`* and
*`genParamValue`* can be used to specify modules using identifiers
other than plugin name and device ID.

The image source handle can also be created with its modules already
specified by reading an image source configuration file. Other parameters
in the image source handle will also be set to the values configured
in this file. The image source configuration files can also store
the values of the persistable parameters of the image source modules
(device, plugin, ...), which will be applied during the call to
[`ConnectImageSource`](connect_image_source.md). To write such configuration files
(for later use) refer to [`ControlImageSource`](control_image_source.md).

For further information about the image source concept see
[Image Source](toc_imagesource.md). See the
[MVTec Interfaces Reference Documentation](https://docs.mvtec.com/interfaces/index.html) for the documentation of individual MVTec image source plugins.

The following options exist for *`pluginName`*.

- **<plugin name>** —

  Specify an image source plugin by setting the plugin
  name in *`pluginName`*. You can use [`QueryImageSources`](query_image_sources.md) to
  retrieve the *"plugin_name"* of all available plugins.
- ***"none"*** —

  No plugin will be specified in
  *`imageSourceHandle`*.
- ***"ignore"*** —

  Set *`pluginName`* to *"ignore"*,
  when specifying the plugin using generic parameters (see below).

The following options exist for *`deviceID`*.

- **<device ID>** —

  Specify a device by setting its device ID in
  *`deviceID`*. You can use [`QueryImageSources`](query_image_sources.md) to
  retrieve the *"device_id"* of all available devices.
- ***"none"*** —

  No device will be specified in
  *`imageSourceHandle`*.
- ***"ignore"*** —

  Set *`deviceID`* to *"ignore"*,
  when specifying the device using generic parameters (see below).

You can also specify modules of the *`imageSourceHandle`* by providing
one of the following options for *`genParamName`*:

- ***"plugin_path"*:** —

  Create a handle specifying a plugin by
  providing the path to the `.cti` plugin file as the corresponding
  *`genParamValue`*.

  *`pluginName`* needs to be set to *"ignore"*.
  *`deviceID`* needs to be set to *"none"* or a device ID.
- ***"interface_id"*:** —

  Create a handle specifying an interface by
  providing the interface ID as the corresponding *`genParamValue`*.

  *`pluginName`* needs to be set to *"none"* or a plugin name.
  *`deviceID`* needs to be set to *"none"* or a device ID.
- ***"device_user_name"*:** —

  Create a handle specifying a device by
  providing the device user name as the corresponding
  *`genParamValue`*.

  *`pluginName`* needs to be set to a plugin name.
  *`deviceID`* needs to be set to *"ignore"*.
- ***"device_serial_number"*:** —

  Create a handle specifying a device
  by providing the device serial number as the corresponding
  *`genParamValue`*.

  *`pluginName`* needs to be set to a plugin name.
  *`deviceID`* needs to be set to *"ignore"*.
- ***"stream_id"*:** —

  Create a handle specifying a stream by
  providing the stream ID as the corresponding *`genParamValue`*.

  *`pluginName`* needs to be set to a plugin name.
  *`deviceID`* needs to be set to a device ID.
- ***"read_config_file"*:** —

  Create a handle by reading an image
  source configuration file, providing the path to the file as the
  corresponding *`genParamValue`*. The default HALCON file extension
  for image source configuration files is `.hisc`.

  The settings of the *"image_source"* group are applied immediately
  when the configuration is loaded. The settings of all other modules are
  applied after the subsequent call to [`ConnectImageSource`](connect_image_source.md).

  *`pluginName`* needs to be set to *"ignore"*.
  *`deviceID`* needs to be set to *"ignore"*.

You can use [`QueryImageSources`](query_image_sources.md) to retrieve the values for
all available image sources.

An empty image source handle can be created by setting both
*`pluginName`* and *`deviceID`* to *"none"* and not
specifying any generic parameters. The empty image source handle can be
extended using [`SetImageSourceParam`](set_image_source_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pluginName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of an image source plugin.

Default:
"none"

Suggested values:
"none", "ignore", "mvtec_gigevision", "mvtec_usb3vision", "mvtec_realsense", "mvtec_gstreamer", "mvtec_mediafoundation", "<plugin_name>"

**`deviceID`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

ID of the image source device.

Default:
"none"

Suggested values:
"none", "ignore"

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

Suggested values:
"plugin_path", "interface_id", "device_user_name", "device_serial_number", "stream_id", "read_config_file"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Generic parameter value.

Default:
[]

**`imageSourceHandle`** (output_control)  image_source `→` [HImageSource](HImageSource.md), [HTuple](HTuple.md) (*IntPtr*)

Created image source handle storing module identifiers.

## Example (HDevelop)

```
* Specify the plugin for GigE Vision devices via its name.
create_image_source ('mvtec_gigevision', 'none', [], [], ImageSourceHandle)
* Specify a plugin by providing its path.
create_image_source ('ignore', 'none', 'plugin_path', 'path/to/plugin.cti', ImageSourceHandle)
*
* Specify a GigE Vision device by providing its unique ID.
create_image_source ('mvtec_gigevision', '00305324c805_Basler_acA244020gc', [], [], ImageSourceHandle)
* Specify a GigE Vision camera by providing its user name.
create_image_source ('mvtec_gigevision', 'ignore', 'device_user_name', 'MyDevice', ImageSourceHandle)
```

## Result

If the parameter values are correct, `CreateImageSource`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Successors

`ConnectImageSource`,
`GetImageSourceParam`,
`SetImageSourceParam`

## Alternatives

`QueryImageSources`

## See also

`QueryImageSources`

## Module

Foundation
