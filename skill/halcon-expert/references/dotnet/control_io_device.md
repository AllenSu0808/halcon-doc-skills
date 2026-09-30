# ControlIoDevice (Operator)

## Name

`ControlIoDevice` — Perform an action on the I/O device.

## Signature

`static void HOperatorSet.ControlIoDevice(HTuple IODeviceHandle, HTuple action, HTuple argument, out HTuple result)`

`HTuple HIODevice.ControlIoDevice(string action, HTuple argument)`

`HTuple HIODevice.ControlIoDevice(string action, string argument)`

## Description

`ControlIoDevice` performs an action on the I/O device. The
supported parameters are interface-specific and listed in the
corresponding documentation of the used I/O interface that can be
found in the directory `doc/html/reference/io`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IODeviceHandle`** (input_control)  io_device `→` [HIODevice](HIODevice.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the opened I/O device.

**`action`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the action to perform.

**`argument`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

List of arguments for the action.

Default:
[]

**`result`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double)

List of result values returned by the action.

## Result

If the parameters are valid, the operator `ControlIoDevice`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised. In this
case an extended error information may be set and can be queried with
the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoDevice`

## Module

Foundation
