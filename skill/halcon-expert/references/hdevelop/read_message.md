# read_message (Operator)

## Name

`read_message` — Read a message from a file.

## Signature

`read_message( : : FileName, GenParamName, GenParamValue : MessageHandle)`

## Description

`read_message` reads a message that has been stored with
[`write_message`](write_message.md).
The default HALCON file extension for a message is 'hmsg'.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`hmsg`

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the generic parameter.

Default:
[]

List of values:
'name'

**`GenParamValue`** (input_control)  attribute.name(-array) `→`  (string / integer / real)

Value of the generic parameter.

Default:
[]

**`MessageHandle`** (output_control)  message `→`  (handle)

Message handle.

Number of elements:
MessageHandle == 1

Assertion:
`MessageHandle != 0`

## Result

If the parameters are valid, the operator `read_message` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`write_message`

## See also

`write_message`,
`serialize_handle`,
`deserialize_handle`

## Module

Foundation
