# ReadIoChannel (Operator)

## Name

`ReadIoChannel` — Read a value from the specified I/O channels.

## Signature

`static void HOperatorSet.ReadIoChannel(HTuple IOChannelHandle, out HTuple value, out HTuple status)`

`static HTuple HIOChannel.ReadIoChannel(HIOChannel[] IOChannelHandle, out HTuple status)`

`HTuple HIOChannel.ReadIoChannel(out HTuple status)`

## Description

`ReadIoChannel` reads input values from the specified
transmission channels. The channels are passed in
*`IOChannelHandle`* and can be opened and configured by
[`OpenIoChannel`](open_io_channel.md), the values are returned in
*`value`*. The parameter *`status`* returns for each read
value in *`value`* a quality message. The value *0*
indicates that the corresponding value of *`value`* could be
read. Any other status value depends on the interface. Please refer
to the interface-specific documentation in the directory
`doc/html/reference/io` for further explanation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IOChannelHandle`** (input_control)  io_channel(-array) `→` [HIOChannel](HIOChannel.md), [HTuple](HTuple.md) (*IntPtr*)

Handles of the opened I/O channels.

**`value`** (output_control)  tuple-array `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Read value.

**`status`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Status of read value.

## Result

If the parameters are valid, the operator
`ReadIoChannel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`GetExtendedErrorInfo`](get_extended_error_info.md).

## Possible Predecessors

`OpenIoChannel`,
`SetIoChannelParam`

## Possible Successors

`CloseIoChannel`

## See also

`WriteIoChannel`,
`QueryIoDevice`,
`SetIoChannelParam`

## Module

Foundation
