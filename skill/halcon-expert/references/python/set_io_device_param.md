# set_io_device_param (Operator)

## Name

`set_io_device_param` — Configure a specific I/O device instance.

## Signature

`def set_io_device_param(iodevice_handle: HHandle, gen_param_name: MaybeSequence[str], gen_param_value: HTupleType) -> None`

## Description

`set_io_device_param` (re)configures a specific device
instance. The configuration parameters are passed in
*`gen_param_name`*, the corresponding values are passed in
*`gen_param_value`*. *`iodevice_handle`* specifies the device
specified in [`open_io_device`](open_io_device.md).

Please check the directory `doc/html/reference/io` for
documentation about your specific I/O device interface, where all
supported device specific parameters are listed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`iodevice_handle`** (input_control)  io_device `→` HHandle

Handle of the opened I/O device.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter names.

Default:
[]

**`gen_param_value`** (input_control)  attribute.value(-array) `→` HTupleType

Parameter values to set.

Default:
[]

## Result

If the parameters are valid, the operator
`set_io_device_param` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised. In this case, an extended error information may be
set and can be queried with the operator [`get_extended_error_info`](get_extended_error_info.md).

## Possible Predecessors

`open_io_device`

## Possible Successors

`open_io_channel`

## See also

`open_io_device`,
`query_io_interface`,
`get_io_device_param`

## Module

Foundation
