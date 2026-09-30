# open_framegrabber (Operator)

## Name

`open_framegrabber` — Open and configure an image acquisition device.

## Signature

`open_framegrabber( : : Name, HorizontalResolution, VerticalResolution, ImageWidth, ImageHeight, StartRow, StartColumn, Field, BitsPerChannel, ColorSpace, Generic, ExternalTrigger, CameraType, Device, Port, LineIn : AcqHandle)`

## Description

The operator `open_framegrabber` opens and configures the
chosen image acquisition device. During this process, the connection to
the image acquisition device is tested, the image acquisition device is
locked for other processes, and, if necessary, memory is
reserved for the data buffers. The actual image grabbing is done via the
operators [`grab_image`](grab_image.md), [`grab_data`](grab_data.md), [`grab_image_async`](grab_image_async.md),
or [`grab_data_async`](grab_data_async.md). If the image acquisition device is not needed
anymore, it should be closed via the operator [`close_framegrabber`](close_framegrabber.md),
releasing it for other processes. Some image acquisition devices allow
to open several instances of the same image acquisition device class.

For all parameters image acquisition device-specific default values can
be chosen explicitly (see the parameter description below). Additional
information for a specific image acquisition device is available via
[`info_framegrabber`](info_framegrabber.md). A comprehensive documentation of all
image acquisition device-specific parameters can be found in the
corresponding interface documentation in the directory
`doc/html/reference/acquisition`.

The meaning of the particular parameters is as follows:

- ***`HorizontalResolution`*, *`VerticalResolution`*** —

  Desired resolution of the image acquisition
  device.
- ***`ImageWidth`*, *`ImageHeight`*** —

  Size of the image part to be returned
  by [`grab_image`](grab_image.md) etc.
- ***`StartRow`*, *`StartColumn`*** —

  Upper left corner of the desired image area.
- ***`Field`*** —

  Desired half image (*'first'*,
  *'second'*, or *'next'*) or
  selection of a full image.
- ***`BitsPerChannel`*** —

  Number of bits, which are transferred from the
  image acquisition device per pixel and image
  channel (typically *5*, *8*,
  *10*, *12*, or *16*).
- ***`ColorSpace`*** —

  Output color format of the grabbed images
  (typically *'gray'* or *'raw'* for
  single-channel or *'rgb'* or *'yuv'*
  for three-channel images).
- ***`Generic`*** —

  Generic parameter with device-specific
  meaning which can be queried
  by [`info_framegrabber`](info_framegrabber.md).
- ***`ExternalTrigger`*** —

  Activation of external triggering (if
  available).
- ***`CameraType`*** —

  More detailed specification of the desired
  image acquisition device (typically the type
  of the analog video format or the name of the
  desired camera configuration file).
- ***`Device`*** —

  Device name of the image acquisition device.
- ***`Port`*** —

  Port the image acquisition device is connected to.
- ***`LineIn`*** —

  Camera input line of multiplexer (if available).

The operator `open_framegrabber` returns a handle
(*`AcqHandle`*) to the opened image acquisition device.

## Attention

Due to the multitude of supported image acquisition devices,
`open_framegrabber` contains a large number of parameters. However,
not all parameters are needed for a specific image acquisition device.

For a multithreaded application,
[`info_framegrabber`](info_framegrabber.md), `open_framegrabber`, and
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

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Name`** (input_control)  string `→`  (string)

HALCON image acquisition interface name, i.e.,
name of the corresponding DLL (Windows) or
shared library (Linux).

Default:
'File'

Suggested values:
'ABS', 'ADLINK', 'AlkUSB3', 'Andor', 'BitFlow', 'Crevis', 'DahengCAM', 'DirectFile', 'DirectShow', 'Ensenso-NxLib', 'File', 'FocalSpecLCI', 'GenICamTL', 'GigEVision2', 'GingaDG', 'Ginga++', 'GStreamer', 'heliCamC3', 'KeyenceLJ', 'KeyenceVJ', 'LinX', 'LPS36', 'LuCam', 'MatrixVisionAcquire', 'MediaFoundation', 'Metavision', 'MILLite', 'MultiCam', 'O3D3xx', 'Opteon', 'PhoXi', 'PixeLINK', 'RealSense', 'SaperaLT', 'Sentech', 'SICK-3DCamera', 'SICK-ScanningRuler', 'SiliconSoftware', 'TWAIN', 'uEye', 'USB3Vision', 'Video4Linux2', 'VRmUsbCam'

**`HorizontalResolution`** (input_control)  extent.x `→`  (integer)

Desired horizontal resolution of image acquisition
interface (absolute value or *1* for full
resolution, *2* for half resolution, or
*4* for quarter resolution).

Default:
1

Suggested values:
1, 2, 4, 1600, 1280, 768, 640, 384, 320, 192, 160, -1

**`VerticalResolution`** (input_control)  extent.y `→`  (integer)

Desired vertical resolution of image acquisition
interface (absolute value or *1* for full resolution,
*2* for half resolution, or *4* for quarter
resolution).

Default:
1

Suggested values:
1, 2, 4, 1200, 1024, 576, 480, 288, 240, 144, 120, -1

**`ImageWidth`** (input_control)  rectangle.extent.x `→`  (integer)

Width of desired image part
(absolute value or *0* for
*`HorizontalResolution`* -
2**`StartColumn`*).

Default:
0

Suggested values:
0, -1

**`ImageHeight`** (input_control)  rectangle.extent.y `→`  (integer)

Height of desired image part
(absolute value or *0* for
*`VerticalResolution`* - 2**`StartRow`*).

Default:
0

Suggested values:
0, -1

**`StartRow`** (input_control)  rectangle.origin.y `→`  (integer)

Line number of upper left corner of desired
image part (or border height if
*`ImageHeight`* = *0*).

Default:
0

Suggested values:
0, -1

**`StartColumn`** (input_control)  rectangle.origin.x `→`  (integer)

Column number of upper left corner of desired
image part (or border width if
*`ImageWidth`* = *0*).

Default:
0

Suggested values:
0, -1

**`Field`** (input_control)  string `→`  (string)

Desired half image or full image.

Default:
'default'

Suggested values:
'first', 'second', 'next', 'interlaced', 'progressive', 'default'

**`BitsPerChannel`** (input_control)  integer(-array) `→`  (integer)

Number of transferred bits per pixel and image
channel (-1: device-specific default value).

Default:
-1

Suggested values:
5, 8, 10, 12, 14, 16, -1

**`ColorSpace`** (input_control)  string(-array) `→`  (string)

Output color format of the grabbed images,
typically *'gray'* or *'raw'* for
single-channel or *'rgb'* or *'yuv'*
for three-channel images
(*'default'*: device-specific default value).

Default:
'default'

Suggested values:
'gray', 'raw', 'rgb', 'yuv', 'default'

**`Generic`** (input_control)  string(-array) `→`  (real / string / integer)

Generic parameter with device-specific meaning.

Default:
-1

**`ExternalTrigger`** (input_control)  string `→`  (string)

External triggering.

Default:
'default'

List of values:
'default', 'false', 'true'

**`CameraType`** (input_control)  string(-array) `→`  (string)

Type of used camera
(*'default'*: device-specific default value).

Default:
'default'

Suggested values:
'ntsc', 'pal', 'auto', 'default'

**`Device`** (input_control)  string(-array) `→`  (string)

Device the image acquisition device is connected to
(*'default'*: device-specific default value).

Default:
'default'

Suggested values:
'-1', '0', '1', '2', '3', 'default'

**`Port`** (input_control)  integer(-array) `→`  (integer)

Port the image acquisition device is connected to
(*-1*: device-specific default value).

Default:
-1

Suggested values:
0, 1, 2, 3, -1

**`LineIn`** (input_control)  integer(-array) `→`  (integer)

Camera input line of multiplexer
(*-1*: device-specific default value).

Default:
-1

Suggested values:
1, 2, 3, 4, -1

**`AcqHandle`** (output_control)  framegrabber `→`  (handle)

Handle of the opened image acquisition device.

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

If the parameter values are correct and the desired image acquisition
device could be opened, `open_framegrabber` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`info_framegrabber`

## Possible Successors

`grab_image`,
`grab_data`,
`grab_image_start`,
`grab_image_async`,
`grab_data_async`,
`set_framegrabber_param`,
`set_framegrabber_callback`

## See also

`info_framegrabber`,
`close_framegrabber`,
`grab_image`

## Module

Foundation
