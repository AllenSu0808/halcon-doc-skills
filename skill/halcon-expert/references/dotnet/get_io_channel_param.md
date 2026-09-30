# GetIoChannelParam (Operator)

## Name

`GetIoChannelParam` — Query specific parameters of I/O channels.

## Signature

`static void HOperatorSet.GetIoChannelParam(HTuple IOChannelHandle, HTuple genParamName, out HTuple genParamValue)`

`static HTuple HIOChannel.GetIoChannelParam(HIOChannel[] IOChannelHandle, HTuple genParamName)`

`HTuple HIOChannel.GetIoChannelParam(string genParamName)`

## Description

`GetIoChannelParam` queries settings of specific I/O
transmission channels. The query parameters are passed in
*`genParamName`*, the corresponding configuration values are
returned in *`genParamValue`*. *`IOChannelHandle`* specifies
the channels returned in [`OpenIoChannel`](open_io_channel.md) for a specific
device instance.

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

**`genParamName`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter names.

Default:
"param_name"

Suggested values:
"io_channel_name", "param_name"

**`genParamValue`** (output_control)  string-array `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Parameter values.

## Result

If the parameters are valid, the operator
`GetIoChannelParam` returns the value 2 (
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
`SetIoChannelParam`

## Module

Foundation
