# read_io_channel (Operator)

## Name

`read_io_channel` — Read a value from the specified I/O channels.

## Signature

`read_io_channel( : : IOChannelHandle : Value, Status)`

## Description

`read_io_channel` reads input values from the specified
transmission channels. The channels are passed in
*`IOChannelHandle`* and can be opened and configured by
[`open_io_channel`](open_io_channel.md), the values are returned in
*`Value`*. The parameter *`Status`* returns for each read
value in *`Value`* a quality message. The value *0*
indicates that the corresponding value of *`Value`* could be
read. Any other status value depends on the interface. Please refer
to the interface-specific documentation in the directory
`doc/html/reference/io` for further explanation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`IOChannelHandle`** (input_control)  io_channel(-array) `→`  (handle)

Handles of the opened I/O channels.

**`Value`** (output_control)  tuple-array `→`  (integer / real / string / handle)

Read value.

**`Status`** (output_control)  integer-array `→`  (integer)

Status of read value.

## Result

If the parameters are valid, the operator
`read_io_channel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_channel`,
`set_io_channel_param`

## Possible Successors

`close_io_channel`

## See also

`write_io_channel`,
`query_io_device`,
`set_io_channel_param`

## Module

Foundation
