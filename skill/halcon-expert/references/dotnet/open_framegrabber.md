# OpenFramegrabber (Operator)

## Name

`OpenFramegrabber` — Open and configure an image acquisition device.

## Signature

`static void HOperatorSet.OpenFramegrabber(HTuple name, HTuple horizontalResolution, HTuple verticalResolution, HTuple imageWidth, HTuple imageHeight, HTuple startRow, HTuple startColumn, HTuple field, HTuple bitsPerChannel, HTuple colorSpace, HTuple generic, HTuple externalTrigger, HTuple cameraType, HTuple device, HTuple port, HTuple lineIn, out HTuple acqHandle)`

`public HFramegrabber(string name, int horizontalResolution, int verticalResolution, int imageWidth, int imageHeight, int startRow, int startColumn, string field, HTuple bitsPerChannel, HTuple colorSpace, HTuple generic, string externalTrigger, HTuple cameraType, HTuple device, HTuple port, HTuple lineIn)`

`public HFramegrabber(string name, int horizontalResolution, int verticalResolution, int imageWidth, int imageHeight, int startRow, int startColumn, string field, int bitsPerChannel, string colorSpace, double generic, string externalTrigger, string cameraType, string device, int port, int lineIn)`

`void HFramegrabber.OpenFramegrabber(string name, int horizontalResolution, int verticalResolution, int imageWidth, int imageHeight, int startRow, int startColumn, string field, HTuple bitsPerChannel, HTuple colorSpace, HTuple generic, string externalTrigger, HTuple cameraType, HTuple device, HTuple port, HTuple lineIn)`

`void HFramegrabber.OpenFramegrabber(string name, int horizontalResolution, int verticalResolution, int imageWidth, int imageHeight, int startRow, int startColumn, string field, int bitsPerChannel, string colorSpace, double generic, string externalTrigger, string cameraType, string device, int port, int lineIn)`

## Description

The operator `OpenFramegrabber` opens and configures the
chosen image acquisition device. During this process, the connection to
the image acquisition device is tested, the image acquisition device is
locked for other processes, and, if necessary, memory is
reserved for the data buffers. The actual image grabbing is done via the
operators [`GrabImage`](grab_image.md), [`GrabData`](grab_data.md), [`GrabImageAsync`](grab_image_async.md),
or [`GrabDataAsync`](grab_data_async.md). If the image acquisition device is not needed
anymore, it should be closed via the operator [`CloseFramegrabber`](close_framegrabber.md),
releasing it for other processes. Some image acquisition devices allow
to open several instances of the same image acquisition device class.

For all parameters image acquisition device-specific default values can
be chosen explicitly (see the parameter description below). Additional
information for a specific image acquisition device is available via
[`InfoFramegrabber`](info_framegrabber.md). A comprehensive documentation of all
image acquisition device-specific parameters can be found in the
corresponding interface documentation in the directory
`doc/html/reference/acquisition`.

The meaning of the particular parameters is as follows:

- ***`horizontalResolution`*, *`verticalResolution`*** —

  Desired resolution of the image acquisition
  device.
- ***`imageWidth`*, *`imageHeight`*** —

  Size of the image part to be returned
  by [`GrabImage`](grab_image.md) etc.
- ***`startRow`*, *`startColumn`*** —

  Upper left corner of the desired image area.
- ***`field`*** —

  Desired half image (*"first"*,
  *"second"*, or *"next"*) or
  selection of a full image.
- ***`bitsPerChannel`*** —

  Number of bits, which are transferred from the
  image acquisition device per pixel and image
  channel (typically *5*, *8*,
  *10*, *12*, or *16*).
- ***`colorSpace`*** —

  Output color format of the grabbed images
  (typically *"gray"* or *"raw"* for
  single-channel or *"rgb"* or *"yuv"*
  for three-channel images).
- ***`generic`*** —

  Generic parameter with device-specific
  meaning which can be queried
  by [`InfoFramegrabber`](info_framegrabber.md).
- ***`externalTrigger`*** —

  Activation of external triggering (if
  available).
- ***`cameraType`*** —

  More detailed specification of the desired
  image acquisition device (typically the type
  of the analog video format or the name of the
  desired camera configuration file).
- ***`device`*** —

  Device name of the image acquisition device.
- ***`port`*** —

  Port the image acquisition device is connected to.
- ***`lineIn`*** —

  Camera input line of multiplexer (if available).

The operator `OpenFramegrabber` returns a handle
(*`acqHandle`*) to the opened image acquisition device.

## Attention

Due to the multitude of supported image acquisition devices,
`OpenFramegrabber` contains a large number of parameters. However,
not all parameters are needed for a specific image acquisition device.

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), `OpenFramegrabber`, and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively. Thus,
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

**`name`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

HALCON image acquisition interface name, i.e.,
name of the corresponding DLL (Windows) or
shared library (Linux).

Default:
"File"

Suggested values:
"ABS", "ADLINK", "AlkUSB3", "Andor", "BitFlow", "Crevis", "DahengCAM", "DirectFile", "DirectShow", "Ensenso-NxLib", "File", "FocalSpecLCI", "GenICamTL", "GigEVision2", "GingaDG", "Ginga++", "GStreamer", "heliCamC3", "KeyenceLJ", "KeyenceVJ", "LinX", "LPS36", "LuCam", "MatrixVisionAcquire", "MediaFoundation", "Metavision", "MILLite", "MultiCam", "O3D3xx", "Opteon", "PhoXi", "PixeLINK", "RealSense", "SaperaLT", "Sentech", "SICK-3DCamera", "SICK-ScanningRuler", "SiliconSoftware", "TWAIN", "uEye", "USB3Vision", "Video4Linux2", "VRmUsbCam"

**`horizontalResolution`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Desired horizontal resolution of image acquisition
interface (absolute value or *1* for full
resolution, *2* for half resolution, or
*4* for quarter resolution).

Default:
1

Suggested values:
1, 2, 4, 1600, 1280, 768, 640, 384, 320, 192, 160, -1

**`verticalResolution`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Desired vertical resolution of image acquisition
interface (absolute value or *1* for full resolution,
*2* for half resolution, or *4* for quarter
resolution).

Default:
1

Suggested values:
1, 2, 4, 1200, 1024, 576, 480, 288, 240, 144, 120, -1

**`imageWidth`** (input_control)  rectangle.extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of desired image part
(absolute value or *0* for
*`horizontalResolution`* -
2**`startColumn`*).

Default:
0

Suggested values:
0, -1

**`imageHeight`** (input_control)  rectangle.extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of desired image part
(absolute value or *0* for
*`verticalResolution`* - 2**`startRow`*).

Default:
0

Suggested values:
0, -1

**`startRow`** (input_control)  rectangle.origin.y `→` [HTuple](HTuple.md) (*int* / long)

Line number of upper left corner of desired
image part (or border height if
*`imageHeight`* = *0*).

Default:
0

Suggested values:
0, -1

**`startColumn`** (input_control)  rectangle.origin.x `→` [HTuple](HTuple.md) (*int* / long)

Column number of upper left corner of desired
image part (or border width if
*`imageWidth`* = *0*).

Default:
0

Suggested values:
0, -1

**`field`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Desired half image or full image.

Default:
"default"

Suggested values:
"first", "second", "next", "interlaced", "progressive", "default"

**`bitsPerChannel`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Number of transferred bits per pixel and image
channel (-1: device-specific default value).

Default:
-1

Suggested values:
5, 8, 10, 12, 14, 16, -1

**`colorSpace`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Output color format of the grabbed images,
typically *"gray"* or *"raw"* for
single-channel or *"rgb"* or *"yuv"*
for three-channel images
(*"default"*: device-specific default value).

Default:
"default"

Suggested values:
"gray", "raw", "rgb", "yuv", "default"

**`generic`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*double* / string / int / long)

Generic parameter with device-specific meaning.

Default:
-1

**`externalTrigger`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

External triggering.

Default:
"default"

List of values:
"default", "false", "true"

**`cameraType`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of used camera
(*"default"*: device-specific default value).

Default:
"default"

Suggested values:
"ntsc", "pal", "auto", "default"

**`device`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Device the image acquisition device is connected to
(*"default"*: device-specific default value).

Default:
"default"

Suggested values:
"-1", "0", "1", "2", "3", "default"

**`port`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Port the image acquisition device is connected to
(*-1*: device-specific default value).

Default:
-1

Suggested values:
0, 1, 2, 3, -1

**`lineIn`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Camera input line of multiplexer
(*-1*: device-specific default value).

Default:
-1

Suggested values:
1, 2, 3, 4, -1

**`acqHandle`** (output_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

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
device could be opened, `OpenFramegrabber` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`InfoFramegrabber`

## Possible Successors

`GrabImage`,
`GrabData`,
`GrabImageStart`,
`GrabImageAsync`,
`GrabDataAsync`,
`SetFramegrabberParam`,
`SetFramegrabberCallback`

## See also

`InfoFramegrabber`,
`CloseFramegrabber`,
`GrabImage`

## Module

Foundation
