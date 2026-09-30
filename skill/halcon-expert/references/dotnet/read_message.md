# ReadMessage (Operator)

## Name

`ReadMessage` — Read a message from a file.

## Signature

`static void HOperatorSet.ReadMessage(HTuple fileName, HTuple genParamName, HTuple genParamValue, out HTuple messageHandle)`

`public HMessage(string fileName, HTuple genParamName, HTuple genParamValue)`

`public HMessage(string fileName, string genParamName, string genParamValue)`

`void HMessage.ReadMessage(string fileName, HTuple genParamName, HTuple genParamValue)`

`void HMessage.ReadMessage(string fileName, string genParamName, string genParamValue)`

## Description

`ReadMessage` reads a message that has been stored with
[`WriteMessage`](write_message.md).
The default HALCON file extension for a message is 'hmsg'.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`hmsg`

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the generic parameter.

Default:
[]

List of values:
"name"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Value of the generic parameter.

Default:
[]

**`messageHandle`** (output_control)  message `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Message handle.

Number of elements:
MessageHandle == 1

Assertion:
`MessageHandle != 0`

## Result

If the parameters are valid, the operator `ReadMessage` returns
the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`WriteMessage`

## See also

`WriteMessage`,
`SerializeHandle`,
`DeserializeHandle`

## Module

Foundation
