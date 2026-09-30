# GetMessageParam (Operator)

## Name

`GetMessageParam` — Query message parameters or information about the message.

## Signature

`static void HOperatorSet.GetMessageParam(HTuple messageHandle, HTuple genParamName, HTuple key, out HTuple genParamValue)`

`HTuple HMessage.GetMessageParam(string genParamName, HTuple key)`

`HTuple HMessage.GetMessageParam(string genParamName, string key)`

## Description

`GetMessageParam` queries current values of message
parameters or other information about the message status.

With each call of `GetMessageParam`, only a single parameter value
can be queried. However, there are two types of parameters/queries:

- Parameters/queries applicable to the entire message. In this case
  no keys must be specified, the parameter *`key`* must be an empty
  tuple.
- Parameters/queries applicable to the individual keys. In this case
  a non-empty list of keys must be specified in the parameter *`key`*.
  The keys are processed in the same order as specified in the *`key`*
  parameter.

Key-independent (global) parameter names:

- ***"message_keys"*:** —

  Queries all the keys stored in the message, no matter whether they
  are associated with tuple or object data. The list of keys is reported
  as a string tuple via *`genParamValue`*.
  For this query the parameter *`key`* must be an empty tuple.

Currently supported key-specific parameter names are:

- ***"key_exists"*:** —

  Reports *1* if the given key is stored in the message, *0*
  otherwise.
  The results are reported via *`genParamValue`*, one value for
  each key.
- ***"key_data_type"*:** —

  Reports *"tuple"* for keys associated with tuple data within
  the message (the data can be retrieved using [`GetMessageTuple`](get_message_tuple.md)).
  Reports *"object"* for keys associated with object data
  (the data can be retrieved using [`GetMessageObj`](get_message_obj.md)).
  The results are reported via *`genParamValue`*, one value for
  each key. This parameter is useful to decide dynamically whether to use
  [`GetMessageTuple`](get_message_tuple.md) or [`GetMessageObj`](get_message_obj.md) to get the data of a
  specific key.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`messageHandle`** (input_control)  message `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`genParamName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Names of the message parameters or info queries.

Number of elements:
GenParamName == GenParamValue

Default:
"message_keys"

List of values:
"key_data_type", "key_exists", "message_keys"

**`key`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / int / long)

Message keys the parameter/query should be applied to.

**`genParamValue`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double)

Values of the message parameters or info queries.

## Example (HDevelop)

```
get_message_param (Message, 'message_keys', [], AllKeys)
get_message_param (Message, 'key_data_type', AllKeys, KeysType)
```

## Result

If all the operator parameters, and the specified keys are valid,
`GetMessageParam` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`DequeueMessage`

## See also

`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`,
`SetMessageParam`,
`EnqueueMessage`,
`DequeueMessage`

## Module

Foundation
