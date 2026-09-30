# QueryImageSources (Operator)

## Name

`QueryImageSources` — Returns handles corresponding to image sources.

## Signature

`static void HOperatorSet.QueryImageSources(HTuple pluginName, HTuple genParamName, HTuple genParamValue, out HTuple imageSourceHandles)`

`static HImageSource[] HImageSource.QueryImageSources(string pluginName, HTuple genParamName, HTuple genParamValue)`

## Description

According to the query specified by the plugin name and the input generic
parameters, `QueryImageSources` returns the corresponding handles in
*`imageSourceHandles`*. The queried handles are in an unconnected state.

You can retrieve image source handles of the different image source modules:

- plugins,
- interfaces,
- devices and
- streams.

These modules are structured in a hierarchical parent-child
configuration, with each module acting as a parent to the subsequent one.

For further information about the image source concept see
[Image Source](toc_imagesource.md). See the
[MVTec Interfaces Reference Documentation](https://docs.mvtec.com/interfaces/index.html) for the documentation of individual MVTec image source plugins.

To restrict the query to a specific plugin its name can be specified in
*`pluginName`*. Set *"all"* to query all available plugins
at the same time.
When querying information on a specific plugin or interface handle,
set *`pluginName`* to *"ignore"*.

List of values:
 *"all"*, *"ignore"*, *"<plugin_name>"*.

Default:
 *"all"*.

The generic parameters *`genParamName`* and *`genParamValue`*
are used to specify the scope of the query. The supported
*`genParamName`* are:

- ***"query"*:** —

  Query handles from available image sources.

  The options for *`genParamValue`* are:

  - ***"plugins"*:** —

    For each available plugin, a handle is
    returned.
  - ***"interfaces"*:** —

    For each available interface, a handle
    is returned, corresponding to the interface and its respective plugin
    module.
  - ***"devices"*:** —

    For each available device, a handle
    is returned, corresponding to the device and its respective interface
    and plugin module.
  - ***"streams"*:** —

    For each available stream in a given device, a
    handle is returned, corresponding to the stream and its respective device,
    interface and plugin module.
    *`pluginName`* must be set to *"ignore"*.

    Note: Along with the generic parameter pair *"query"* and
    *"streams"*, you need to provide the parameter
    *"device_handle"* and a device handle:

    `QueryImageSources("ignore", ["query", "device_handle"] , ["streams", DeviceHandle], QueriedStreams)`
- ***"plugin_handle"*:** —

  Specify a connected plugin handle in *`genParamValue`*
  from which to query for all interface or device handles.
  See [`ConnectImageSource`](connect_image_source.md) for information about connecting
  to an image source. *`pluginName`* must be set to *"ignore"*.
- ***"interface_handle"*:** —

  Specify a connected interface handle in *`genParamValue`*
  from which to query for device handles.
  See [`ConnectImageSource`](connect_image_source.md) for information about connecting
  to an image source. *`pluginName`* must be set to *"ignore"*.
- ***"device_handle"*:** —

  Specify a connected device handle in *`genParamValue`*
  from which to query for stream handles (see the *"query"* option
  *"streams"* above.)
  See [`ConnectImageSource`](connect_image_source.md) for information about connecting
  to an image source.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`pluginName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of an image source plugin.

Default:
"all"

Suggested values:
"all", "ignore", "mvtec_gigevision", "mvtec_usb3vision", "mvtec_realsense", "mvtec_gstreamer", "mvtec_mediafoundation", "<plugin_name>"

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

Suggested values:
"query", "image_source_handle", "plugin_handle", "interface_handle", "device_handle"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / HHandle)

Generic parameter value.

Default:
[]

Suggested values:
"plugins", "interfaces", "devices", "streams"

**`imageSourceHandles`** (output_control)  image_source-array `→` [HImageSource](HImageSource.md), [HTuple](HTuple.md) (*IntPtr*)

Image source handles corresponding to modules
available in the system.

## Example (HDevelop)

```
* Query different modules.
query_image_sources ('all', 'query', 'plugins', Plugins)
query_image_sources ('all', 'query', 'interfaces', Interfaces)
query_image_sources ('all', 'query', 'devices', Devices)
* Connect to an available plugin and interface.
connect_image_source (Plugins[0], [], [])
connect_image_source (Interfaces[0], [], [])
* Restrict query to all device modules of one connected plugin.
query_image_sources ('ignore', 'plugin_handle', Plugins[0], PluginSubHandles)
* Restrict query to all sub-modules down to the interface level of one connected plugin.
query_image_sources ('ignore', ['query', 'plugin_handle'], ['interfaces', Plugins[0]], InterfaceHandlesPluginZero)
```

## Result

If the parameter values are correct, `QueryImageSources` returns
the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Successors

`ConnectImageSource`,
`GetImageSourceParam`,
`SetImageSourceParam`

## Alternatives

`CreateImageSource`

## See also

`CreateImageSource`

## Module

Foundation
