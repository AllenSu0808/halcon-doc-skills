# info_framegrabber (Operator)

## Name

`info_framegrabber` — Query information about the specified image acquisition interface.

## Signature

`def info_framegrabber(name: str, query: str) -> Tuple[str, Sequence[Union[str, int, float]]]`

## Description

The operator `info_framegrabber` returns information about the image
acquisition device *`name`*. The desired information is specified via
*`query`*. A textual description according to the selected
topic is returned in *`information`*. If applicable,
*`value_list`* contains a list of supported values. Up to now,
the following queries are possible:

- ***"bits_per_channel"*:** —

  List of all supported values for the
  parameter `bits_per_channel`,
  see [`open_framegrabber`](open_framegrabber.md).
- ***"camera_type"*:** —

  Description and list of all supported values
  for the parameter `camera_type`,
  see [`open_framegrabber`](open_framegrabber.md).
- ***"color_space"*:** —

  List of all supported values for the parameter
  `color_space`,
  see [`open_framegrabber`](open_framegrabber.md).
- ***"defaults"*:** —

  Interface-specific default values
  in *`value_list`*, see [`open_framegrabber`](open_framegrabber.md).
- ***"device"*:** —

  List of all supported values for the parameter
  `device`, see [`open_framegrabber`](open_framegrabber.md).
- ***"external_trigger"*:** —

  List of all supported values for the
  parameter `external_trigger`, see
  [`open_framegrabber`](open_framegrabber.md).
- ***"field"*:** —

  List of all supported values for the parameter
  `field`, see [`open_framegrabber`](open_framegrabber.md).
- ***"general"*:** —

  General information (in *`information`*).
- ***"generic"*:** —

  Generic value with device-specific meaning,
  see [`open_framegrabber`](open_framegrabber.md).
- ***"horizontal_resolution"*:** —

  List of all supported values for the
  parameter `horizontal_resolution`, see
  [`open_framegrabber`](open_framegrabber.md).
- ***"image_height"*:** —

  List of all supported values for the parameter
  `image_height`, see [`open_framegrabber`](open_framegrabber.md).
- ***"image_width"*:** —

  List of all supported values for the parameter
  `image_width`, see [`open_framegrabber`](open_framegrabber.md).
- ***"info_boards"*:** —

  Information about actually installed boards
  or cameras. This data is especially useful for
  the auto-detect mechanism of the Image
  Acquisition Assistant in HDevelop.
- ***"line_in"*:** —

  List of all supported values for the parameter
  `line_in`, see [`open_framegrabber`](open_framegrabber.md).
- ***"parameters"*:** —

  List of all interface-specific parameters which
  are accessible via [`set_framegrabber_param`](set_framegrabber_param.md)
  or [`get_framegrabber_param`](get_framegrabber_param.md).
- ***"parameters_readonly"*:** —

  List of all interface-specific
  parameters which are only accessible via
  [`get_framegrabber_param`](get_framegrabber_param.md).
- ***"parameters_writeonly"*:** —

  List of all interface-specific
  parameters which are only accessible via
  [`set_framegrabber_param`](set_framegrabber_param.md).
- ***"port"*:** —

  List of all supported values for the parameter
  `port`, see [`open_framegrabber`](open_framegrabber.md).
- ***"revision"*:** —

  Version number of the image acquisition interface.
- ***"start_column"*:** —

  List of all supported values for the parameter
  `start_column`, see [`open_framegrabber`](open_framegrabber.md).
- ***"start_row"*:** —

  List of all supported values for the parameter
  `start_row`, see [`open_framegrabber`](open_framegrabber.md).
- ***"vertical_resolution"*:** —

  List of all supported values for the
  parameter `vertical_resolution`, see
  [`open_framegrabber`](open_framegrabber.md).

Please check also the directory `doc/html/reference/acquisition`
for documentation about specific image grabber interfaces.

## Attention

For a multithreaded application,
`info_framegrabber`, [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively. Thus,
they block the concurrent execution of each other, but run in
parallel with all non-exclusive operators outside of this group.

On Windows Systems, error dialog boxes from the operating system can occur
when dependency modules of the interface are not found, e.g., the according
SDK was not installed. The occurrence of the error boxes can be controlled
by setting Windows' Error Mode. Please refer to the description of
SetErrorMode within the Windows MSDN documentation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`name`** (input_control)  string `→` str

HALCON image acquisition interface name, i.e.,
name of the corresponding DLL (Windows) or
shared library (Linux).

Default:
"File"

Suggested values:
"ABS", "ADLINK", "AlkUSB3", "Andor", "BitFlow", "Crevis", "DahengCAM", "DirectFile", "DirectShow", "Ensenso-NxLib", "File", "FocalSpecLCI", "GenICamTL", "GigEVision2", "GingaDG", "Ginga++", "GStreamer", "heliCamC3", "KeyenceLJ", "KeyenceVJ", "LinX", "LPS36", "LuCam", "MatrixVisionAcquire", "MediaFoundation", "Metavision", "MILLite", "MultiCam", "O3D3xx", "Opteon", "PhoXi", "PixeLINK", "RealSense", "SaperaLT", "Sentech", "SICK-3DCamera", "SICK-ScanningRuler", "SiliconSoftware", "TWAIN", "uEye", "USB3Vision", "Video4Linux2", "VRmUsbCam"

**`query`** (input_control)  string `→` str

Name of the chosen query.

Default:
"info_boards"

List of values:
"bits_per_channel", "camera_type", "color_space", "defaults", "device", "external_trigger", "field", "general", "generic", "horizontal_resolution", "image_height", "image_width", "info_boards", "parameters", "parameters_readonly", "parameters_writeonly", "port", "revision", "start_column", "start_row", "vertical_resolution"

**`information`** (output_control)  string `→` str

Textual information (according to *`query`*).

**`value_list`** (output_control)  string-array `→` Sequence[Union[str, int, float]]

List of values (according to *`query`*).

## Example (HDevelop)

```
* Select a suitable image acquisition interface name AcqName
info_framegrabber(AcqName,'port',Information,Values)
* Open image acquisition device using the default settings, see
* documentation of the actually used interface for more details
open_framegrabber(AcqName,1,1,0,0,0,0,'default',-1,'default',-1.0, \
                  'default','default','default',-1,-1,AcqHandle)
grab_image(Image,AcqHandle)
close_framegrabber(AcqHandle)
```

## Result

If the parameter values are correct and the specified image acquisition
interface is available, `info_framegrabber` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`

## Possible Successors

`open_framegrabber`

## See also

`open_framegrabber`

## Module

Foundation
