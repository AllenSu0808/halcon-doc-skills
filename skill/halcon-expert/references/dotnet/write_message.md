# WriteMessage (Operator)

## Name

`WriteMessage` — Write a message to a file.

## Signature

`static void HOperatorSet.WriteMessage(HTuple messageHandle, HTuple fileName, HTuple genParamName, HTuple genParamValue)`

`void HMessage.WriteMessage(string fileName, HTuple genParamName, HTuple genParamValue)`

`void HMessage.WriteMessage(string fileName, string genParamName, string genParamValue)`

## Description

`WriteMessage` writes the message denoted by the
*`messageHandle`* to the file given by *`fileName`*.
The default HALCON file extension for a message is 'hmsg'.

If *`messageHandle`* contains a handle that can not be serialized or
that has been freed already, an exception is raised per default.
This behavior is controlled by *`genParamName`*
*"raise_error_if_content_not_serializable"*, and the corresponding
*`genParamValue`* can take the following values:

- ***"true"*:** —

  The default: Errors are raised and the writing process aborted.
- ***"low_level"*:** —

  Only low level errors are raised. Instead of the handle concerned an empty
  handle is written in *`fileName`* and the writing
  process will be continued. The behavior regarding HALCON low level errors
  is determined by *"do_low_error"* in [`SetSystem`](set_system.md).
- ***"false"*:** —

  The errors are suppressed. Instead of the handle concerned an empty
  handle is written in *`fileName`* and the writing
  process will be continued.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`messageHandle`** (input_control)  message `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`hmsg`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"raise_error_if_content_not_serializable"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

Suggested values:
"true", "false", "low_level"

## Result

If the parameters are valid, the operator `WriteMessage` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`ReadMessage`,
`DeserializeHandle`,
`CreateMessage`

## Possible Successors

`ReadMessage`

## See also

`ReadMessage`,
`SerializeHandle`,
`DeserializeHandle`

## Module

Foundation
