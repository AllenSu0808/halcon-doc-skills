# SetIoChannelParam (Operator)

## Name

`SetIoChannelParam` — Set specific parameters of I/O channels.

## Signature

`static void HOperatorSet.SetIoChannelParam(HTuple IOChannelHandle, HTuple genParamName, HTuple genParamValue)`

`static void HIOChannel.SetIoChannelParam(HIOChannel[] IOChannelHandle, HTuple genParamName, HTuple genParamValue)`

`void HIOChannel.SetIoChannelParam(HTuple genParamName, HTuple genParamValue)`

## Description

`SetIoChannelParam` (re)configures the given transmission
channels. The configuration parameters are passed in
*`genParamName`*, the corresponding values are passed in
*`genParamValue`*. *`IOChannelHandle`* specifies the
transmission channels returned in [`OpenIoChannel`](open_io_channel.md).

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported channel-specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IOChannelHandle`** (input_control)  io_channel(-array) `→` [HIOChannel](HIOChannel.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the opened I/O channels.

**`genParamName`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
[]

**`genParamValue`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Parameter values to set.

Default:
[]

## Result

If the parameters are valid, the operator
`SetIoChannelParam` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoChannel`

## Possible Successors

`ReadIoChannel`,
`WriteIoChannel`

## See also

`OpenIoChannel`,
`QueryIoDevice`,
`GetIoChannelParam`,
`ReadIoChannel`,
`WriteIoChannel`

## Module

Foundation
