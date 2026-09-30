# read_message (Operator)

## Name

`read_message` — Read a message from a file.

## Signature

`def read_message(file_name: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

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

**`file_name`** (input_control)  filename.read `→` str

File name.

File extension:
.`hmsg`

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the generic parameter.

Default:
[]

List of values:
"name"

**`gen_param_value`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the generic parameter.

Default:
[]

**`message_handle`** (output_control)  message `→` HHandle

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
