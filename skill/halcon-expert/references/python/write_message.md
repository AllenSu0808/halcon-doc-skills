# write_message (Operator)

## Name

`write_message` — Write a message to a file.

## Signature

`def write_message(message_handle: HHandle, file_name: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> None`

## Description

`write_message` writes the message denoted by the
*`message_handle`* to the file given by *`file_name`*.
The default HALCON file extension for a message is 'hmsg'.

If *`message_handle`* contains a handle that can not be serialized or
that has been freed already, an exception is raised per default.
This behavior is controlled by *`gen_param_name`*
*"raise_error_if_content_not_serializable"*, and the corresponding
*`gen_param_value`* can take the following values:

- ***"true"*:** —

  The default: Errors are raised and the writing process aborted.
- ***"low_level"*:** —

  Only low level errors are raised. Instead of the handle concerned an empty
  handle is written in *`file_name`* and the writing
  process will be continued. The behavior regarding HALCON low level errors
  is determined by *"do_low_error"* in [`set_system`](set_system.md).
- ***"false"*:** —

  The errors are suppressed. Instead of the handle concerned an empty
  handle is written in *`file_name`* and the writing
  process will be continued.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`message_handle`** (input_control)  message `→` HHandle

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`file_name`** (input_control)  filename.write `→` str

File name.

File extension:
.`hmsg`

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Name of the generic parameter.

Default:
[]

List of values:
"raise_error_if_content_not_serializable"

**`gen_param_value`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, float, str]]

Value of the generic parameter.

Default:
[]

Suggested values:
"true", "false", "low_level"

## Result

If the parameters are valid, the operator `write_message` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`read_message`,
`deserialize_handle`,
`create_message`

## Possible Successors

`read_message`

## See also

`read_message`,
`serialize_handle`,
`deserialize_handle`

## Module

Foundation
