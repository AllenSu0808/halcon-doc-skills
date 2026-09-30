# info_framegrabber (Operator)

## Name

`info_framegrabber` — Query information about the specified image acquisition interface.

## Signature

`info_framegrabber( : : Name, Query : Information, ValueList)`

## Description

The operator `info_framegrabber` returns information about the image
acquisition device *`Name`*. The desired information is specified via
*`Query`*. A textual description according to the selected
topic is returned in *`Information`*. If applicable,
*`ValueList`* contains a list of supported values. Up to now,
the following queries are possible:

- ***'bits_per_channel'*:** —

  List of all supported values for the
  parameter `BitsPerChannel`,
  see [`open_framegrabber`](open_framegrabber.md).
- ***'camera_type'*:** —

  Description and list of all supported values
  for the parameter `CameraType`,
  see [`open_framegrabber`](open_framegrabber.md).
- ***'color_space'*:** —

  List of all supported values for the parameter
  `ColorSpace`,
  see [`open_framegrabber`](open_framegrabber.md).
- ***'defaults'*:** —

  Interface-specific default values
  in *`ValueList`*, see [`open_framegrabber`](open_framegrabber.md).
- ***'device'*:** —

  List of all supported values for the parameter
  `Device`, see [`open_framegrabber`](open_framegrabber.md).
- ***'external_trigger'*:** —

  List of all supported values for the
  parameter `ExternalTrigger`, see
  [`open_framegrabber`](open_framegrabber.md).
- ***'field'*:** —

  List of all supported values for the parameter
  `Field`, see [`open_framegrabber`](open_framegrabber.md).
- ***'general'*:** —

  General information (in *`Information`*).
- ***'generic'*:** —

  Generic value with device-specific meaning,
  see [`open_framegrabber`](open_framegrabber.md).
- ***'horizontal_resolution'*:** —

  List of all supported values for the
  parameter `HorizontalResolution`, see
  [`open_framegrabber`](open_framegrabber.md).
- ***'image_height'*:** —

  List of all supported values for the parameter
  `ImageHeight`, see [`open_framegrabber`](open_framegrabber.md).
- ***'image_width'*:** —

  List of all supported values for the parameter
  `ImageWidth`, see [`open_framegrabber`](open_framegrabber.md).
- ***'info_boards'*:** —

  Information about actually installed boards
  or cameras. This data is especially useful for
  the auto-detect mechanism of the Image
  Acquisition Assistant in HDevelop.
- ***'line_in'*:** —

  List of all supported values for the parameter
  `LineIn`, see [`open_framegrabber`](open_framegrabber.md).
- ***'parameters'*:** —

  List of all interface-specific parameters which
  are accessible via [`set_framegrabber_param`](set_framegrabber_param.md)
  or [`get_framegrabber_param`](get_framegrabber_param.md).
- ***'parameters_readonly'*:** —

  List of all interface-specific
  parameters which are only accessible via
  [`get_framegrabber_param`](get_framegrabber_param.md).
- ***'parameters_writeonly'*:** —

  List of all interface-specific
  parameters which are only accessible via
  [`set_framegrabber_param`](set_framegrabber_param.md).
- ***'port'*:** —

  List of all supported values for the parameter
  `Port`, see [`open_framegrabber`](open_framegrabber.md).
- ***'revision'*:** —

  Version number of the image acquisition interface.
- ***'start_column'*:** —

  List of all supported values for the parameter
  `StartColumn`, see [`open_framegrabber`](open_framegrabber.md).
- ***'start_row'*:** —

  List of all supported values for the parameter
  `StartRow`, see [`open_framegrabber`](open_framegrabber.md).
- ***'vertical_resolution'*:** —

  List of all supported values for the
  parameter `VerticalResolution`, see
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

**`Name`** (input_control)  string `→`  (string)

HALCON image acquisition interface name, i.e.,
name of the corresponding DLL (Windows) or
shared library (Linux).

Default:
'File'

Suggested values:
'ABS', 'ADLINK', 'AlkUSB3', 'Andor', 'BitFlow', 'Crevis', 'DahengCAM', 'DirectFile', 'DirectShow', 'Ensenso-NxLib', 'File', 'FocalSpecLCI', 'GenICamTL', 'GigEVision2', 'GingaDG', 'Ginga++', 'GStreamer', 'heliCamC3', 'KeyenceLJ', 'KeyenceVJ', 'LinX', 'LPS36', 'LuCam', 'MatrixVisionAcquire', 'MediaFoundation', 'Metavision', 'MILLite', 'MultiCam', 'O3D3xx', 'Opteon', 'PhoXi', 'PixeLINK', 'RealSense', 'SaperaLT', 'Sentech', 'SICK-3DCamera', 'SICK-ScanningRuler', 'SiliconSoftware', 'TWAIN', 'uEye', 'USB3Vision', 'Video4Linux2', 'VRmUsbCam'

**`Query`** (input_control)  string `→`  (string)

Name of the chosen query.

Default:
'info_boards'

List of values:
'bits_per_channel', 'camera_type', 'color_space', 'defaults', 'device', 'external_trigger', 'field', 'general', 'generic', 'horizontal_resolution', 'image_height', 'image_width', 'info_boards', 'parameters', 'parameters_readonly', 'parameters_writeonly', 'port', 'revision', 'start_column', 'start_row', 'vertical_resolution'

**`Information`** (output_control)  string `→`  (string)

Textual information (according to *`Query`*).

**`ValueList`** (output_control)  string-array `→`  (string / integer / real)

List of values (according to *`Query`*).

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
