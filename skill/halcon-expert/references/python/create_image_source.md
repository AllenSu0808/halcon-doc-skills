# create_image_source (Operator)

## Name

`create_image_source` — Create an image source handle.

## Signature

`def create_image_source(plugin_name: str, device_id: str, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> HHandle`

## Description

`create_image_source` creates an image source handle and returns it
in *`image_source_handle`*. The created handle is in an unconnected
state. The parameters *`plugin_name`* and *`device_id`* can be used
to specify the plugin and device module of the image source handle.
Alternatively, the generic parameters *`gen_param_name`* and
*`gen_param_value`* can be used to specify modules using identifiers
other than plugin name and device ID.

The image source handle can also be created with its modules already
specified by reading an image source configuration file. Other parameters
in the image source handle will also be set to the values configured
in this file. The image source configuration files can also store
the values of the persistable parameters of the image source modules
(device, plugin, ...), which will be applied during the call to
[`connect_image_source`](connect_image_source.md). To write such configuration files
(for later use) refer to [`control_image_source`](control_image_source.md).

For further information about the image source concept see
[Image Source](toc_imagesource.md). See the
[MVTec Interfaces Reference Documentation](https://docs.mvtec.com/interfaces/index.html) for the documentation of individual MVTec image source plugins.

The following options exist for *`plugin_name`*.

- **<plugin name>** —

  Specify an image source plugin by setting the plugin
  name in *`plugin_name`*. You can use [`query_image_sources`](query_image_sources.md) to
  retrieve the *"plugin_name"* of all available plugins.
- ***"none"*** —

  No plugin will be specified in
  *`image_source_handle`*.
- ***"ignore"*** —

  Set *`plugin_name`* to *"ignore"*,
  when specifying the plugin using generic parameters (see below).

The following options exist for *`device_id`*.

- **<device ID>** —

  Specify a device by setting its device ID in
  *`device_id`*. You can use [`query_image_sources`](query_image_sources.md) to
  retrieve the *"device_id"* of all available devices.
- ***"none"*** —

  No device will be specified in
  *`image_source_handle`*.
- ***"ignore"*** —

  Set *`device_id`* to *"ignore"*,
  when specifying the device using generic parameters (see below).

You can also specify modules of the *`image_source_handle`* by providing
one of the following options for *`gen_param_name`*:

- ***"plugin_path"*:** —

  Create a handle specifying a plugin by
  providing the path to the `.cti` plugin file as the corresponding
  *`gen_param_value`*.

  *`plugin_name`* needs to be set to *"ignore"*.
  *`device_id`* needs to be set to *"none"* or a device ID.
- ***"interface_id"*:** —

  Create a handle specifying an interface by
  providing the interface ID as the corresponding *`gen_param_value`*.

  *`plugin_name`* needs to be set to *"none"* or a plugin name.
  *`device_id`* needs to be set to *"none"* or a device ID.
- ***"device_user_name"*:** —

  Create a handle specifying a device by
  providing the device user name as the corresponding
  *`gen_param_value`*.

  *`plugin_name`* needs to be set to a plugin name.
  *`device_id`* needs to be set to *"ignore"*.
- ***"device_serial_number"*:** —

  Create a handle specifying a device
  by providing the device serial number as the corresponding
  *`gen_param_value`*.

  *`plugin_name`* needs to be set to a plugin name.
  *`device_id`* needs to be set to *"ignore"*.
- ***"stream_id"*:** —

  Create a handle specifying a stream by
  providing the stream ID as the corresponding *`gen_param_value`*.

  *`plugin_name`* needs to be set to a plugin name.
  *`device_id`* needs to be set to a device ID.
- ***"read_config_file"*:** —

  Create a handle by reading an image
  source configuration file, providing the path to the file as the
  corresponding *`gen_param_value`*. The default HALCON file extension
  for image source configuration files is `.hisc`.

  The settings of the *"image_source"* group are applied immediately
  when the configuration is loaded. The settings of all other modules are
  applied after the subsequent call to [`connect_image_source`](connect_image_source.md).

  *`plugin_name`* needs to be set to *"ignore"*.
  *`device_id`* needs to be set to *"ignore"*.

You can use [`query_image_sources`](query_image_sources.md) to retrieve the values for
all available image sources.

An empty image source handle can be created by setting both
*`plugin_name`* and *`device_id`* to *"none"* and not
specifying any generic parameters. The empty image source handle can be
extended using [`set_image_source_param`](set_image_source_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`plugin_name`** (input_control)  string `→` str

Name of an image source plugin.

Default:
"none"

Suggested values:
"none", "ignore", "mvtec_gigevision", "mvtec_usb3vision", "mvtec_realsense", "mvtec_gstreamer", "mvtec_mediafoundation", "<plugin_name>"

**`device_id`** (input_control)  string `→` str

ID of the image source device.

Default:
"none"

Suggested values:
"none", "ignore"

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic parameter name.

Default:
[]

Suggested values:
"plugin_path", "interface_id", "device_user_name", "device_serial_number", "stream_id", "read_config_file"

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Generic parameter value.

Default:
[]

**`image_source_handle`** (output_control)  image_source `→` HHandle

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

If the parameter values are correct, `create_image_source`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Successors

`connect_image_source`,
`get_image_source_param`,
`set_image_source_param`

## Alternatives

`query_image_sources`

## See also

`query_image_sources`

## Module

Foundation
