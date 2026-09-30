# open_framegrabber (Operator)

## Name

`open_framegrabber` — Open and configure an image acquisition device.

## Signature

`def open_framegrabber(name: str, horizontal_resolution: int, vertical_resolution: int, image_width: int, image_height: int, start_row: int, start_column: int, field: str, bits_per_channel: MaybeSequence[int], color_space: MaybeSequence[str], generic: MaybeSequence[Union[str, float, int]], external_trigger: str, camera_type: MaybeSequence[str], device: MaybeSequence[str], port: MaybeSequence[int], line_in: MaybeSequence[int]) -> HHandle`

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

- ***`horizontal_resolution`*, *`vertical_resolution`*** —

  Desired resolution of the image acquisition
  device.
- ***`image_width`*, *`image_height`*** —

  Size of the image part to be returned
  by [`grab_image`](grab_image.md) etc.
- ***`start_row`*, *`start_column`*** —

  Upper left corner of the desired image area.
- ***`field`*** —

  Desired half image (*"first"*,
  *"second"*, or *"next"*) or
  selection of a full image.
- ***`bits_per_channel`*** —

  Number of bits, which are transferred from the
  image acquisition device per pixel and image
  channel (typically *5*, *8*,
  *10*, *12*, or *16*).
- ***`color_space`*** —

  Output color format of the grabbed images
  (typically *"gray"* or *"raw"* for
  single-channel or *"rgb"* or *"yuv"*
  for three-channel images).
- ***`generic`*** —

  Generic parameter with device-specific
  meaning which can be queried
  by [`info_framegrabber`](info_framegrabber.md).
- ***`external_trigger`*** —

  Activation of external triggering (if
  available).
- ***`camera_type`*** —

  More detailed specification of the desired
  image acquisition device (typically the type
  of the analog video format or the name of the
  desired camera configuration file).
- ***`device`*** —

  Device name of the image acquisition device.
- ***`port`*** —

  Port the image acquisition device is connected to.
- ***`line_in`*** —

  Camera input line of multiplexer (if available).

The operator `open_framegrabber` returns a handle
(*`acq_handle`*) to the opened image acquisition device.

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

**`name`** (input_control)  string `→` str

HALCON image acquisition interface name, i.e.,
name of the corresponding DLL (Windows) or
shared library (Linux).

Default:
"File"

Suggested values:
"ABS", "ADLINK", "AlkUSB3", "Andor", "BitFlow", "Crevis", "DahengCAM", "DirectFile", "DirectShow", "Ensenso-NxLib", "File", "FocalSpecLCI", "GenICamTL", "GigEVision2", "GingaDG", "Ginga++", "GStreamer", "heliCamC3", "KeyenceLJ", "KeyenceVJ", "LinX", "LPS36", "LuCam", "MatrixVisionAcquire", "MediaFoundation", "Metavision", "MILLite", "MultiCam", "O3D3xx", "Opteon", "PhoXi", "PixeLINK", "RealSense", "SaperaLT", "Sentech", "SICK-3DCamera", "SICK-ScanningRuler", "SiliconSoftware", "TWAIN", "uEye", "USB3Vision", "Video4Linux2", "VRmUsbCam"

**`horizontal_resolution`** (input_control)  extent.x `→` int

Desired horizontal resolution of image acquisition
interface (absolute value or *1* for full
resolution, *2* for half resolution, or
*4* for quarter resolution).

Default:
1

Suggested values:
1, 2, 4, 1600, 1280, 768, 640, 384, 320, 192, 160, -1

**`vertical_resolution`** (input_control)  extent.y `→` int

Desired vertical resolution of image acquisition
interface (absolute value or *1* for full resolution,
*2* for half resolution, or *4* for quarter
resolution).

Default:
1

Suggested values:
1, 2, 4, 1200, 1024, 576, 480, 288, 240, 144, 120, -1

**`image_width`** (input_control)  rectangle.extent.x `→` int

Width of desired image part
(absolute value or *0* for
*`horizontal_resolution`* -
2**`start_column`*).

Default:
0

Suggested values:
0, -1

**`image_height`** (input_control)  rectangle.extent.y `→` int

Height of desired image part
(absolute value or *0* for
*`vertical_resolution`* - 2**`start_row`*).

Default:
0

Suggested values:
0, -1

**`start_row`** (input_control)  rectangle.origin.y `→` int

Line number of upper left corner of desired
image part (or border height if
*`image_height`* = *0*).

Default:
0

Suggested values:
0, -1

**`start_column`** (input_control)  rectangle.origin.x `→` int

Column number of upper left corner of desired
image part (or border width if
*`image_width`* = *0*).

Default:
0

Suggested values:
0, -1

**`field`** (input_control)  string `→` str

Desired half image or full image.

Default:
"default"

Suggested values:
"first", "second", "next", "interlaced", "progressive", "default"

**`bits_per_channel`** (input_control)  integer(-array) `→` MaybeSequence[int]

Number of transferred bits per pixel and image
channel (-1: device-specific default value).

Default:
-1

Suggested values:
5, 8, 10, 12, 14, 16, -1

**`color_space`** (input_control)  string(-array) `→` MaybeSequence[str]

Output color format of the grabbed images,
typically *"gray"* or *"raw"* for
single-channel or *"rgb"* or *"yuv"*
for three-channel images
(*"default"*: device-specific default value).

Default:
"default"

Suggested values:
"gray", "raw", "rgb", "yuv", "default"

**`generic`** (input_control)  string(-array) `→` MaybeSequence[Union[str, float, int]]

Generic parameter with device-specific meaning.

Default:
-1

**`external_trigger`** (input_control)  string `→` str

External triggering.

Default:
"default"

List of values:
"default", "false", "true"

**`camera_type`** (input_control)  string(-array) `→` MaybeSequence[str]

Type of used camera
(*"default"*: device-specific default value).

Default:
"default"

Suggested values:
"ntsc", "pal", "auto", "default"

**`device`** (input_control)  string(-array) `→` MaybeSequence[str]

Device the image acquisition device is connected to
(*"default"*: device-specific default value).

Default:
"default"

Suggested values:
"-1", "0", "1", "2", "3", "default"

**`port`** (input_control)  integer(-array) `→` MaybeSequence[int]

Port the image acquisition device is connected to
(*-1*: device-specific default value).

Default:
-1

Suggested values:
0, 1, 2, 3, -1

**`line_in`** (input_control)  integer(-array) `→` MaybeSequence[int]

Camera input line of multiplexer
(*-1*: device-specific default value).

Default:
-1

Suggested values:
1, 2, 3, 4, -1

**`acq_handle`** (output_control)  framegrabber `→` HHandle

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
