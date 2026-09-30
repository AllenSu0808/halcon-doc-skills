# get_message_param (Operator)

## Name

`get_message_param` — Query message parameters or information about the message.

## Signature

`def get_message_param(message_handle: HHandle, gen_param_name: str, key: MaybeSequence[Union[str, int]]) -> Sequence[Union[int, float, str]]`

`def get_message_param_s(message_handle: HHandle, gen_param_name: str, key: MaybeSequence[Union[str, int]]) -> Union[int, float, str]`

## Description

`get_message_param` queries current values of message
parameters or other information about the message status.

With each call of `get_message_param`, only a single parameter value
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
  as a string tuple via *`gen_param_value`*.
  For this query the parameter *`key`* must be an empty tuple.

Currently supported key-specific parameter names are:

- ***"key_exists"*:** —

  Reports *1* if the given key is stored in the message, *0*
  otherwise.
  The results are reported via *`gen_param_value`*, one value for
  each key.
- ***"key_data_type"*:** —

  Reports *"tuple"* for keys associated with tuple data within
  the message (the data can be retrieved using [`get_message_tuple`](get_message_tuple.md)).
  Reports *"object"* for keys associated with object data
  (the data can be retrieved using [`get_message_obj`](get_message_obj.md)).
  The results are reported via *`gen_param_value`*, one value for
  each key. This parameter is useful to decide dynamically whether to use
  [`get_message_tuple`](get_message_tuple.md) or [`get_message_obj`](get_message_obj.md) to get the data of a
  specific key.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`message_handle`** (input_control)  message `→` HHandle

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`gen_param_name`** (input_control)  string `→` str

Names of the message parameters or info queries.

Number of elements:
GenParamName == GenParamValue

Default:
"message_keys"

List of values:
"key_data_type", "key_exists", "message_keys"

**`key`** (input_control)  string(-array) `→` MaybeSequence[Union[str, int]]

Message keys the parameter/query should be applied to.

**`gen_param_value`** (output_control)  tuple(-array) `→` Sequence[Union[int, float, str]]

Values of the message parameters or info queries.

## Example (HDevelop)

```
get_message_param (Message, 'message_keys', [], AllKeys)
get_message_param (Message, 'key_data_type', AllKeys, KeysType)
```

## Result

If all the operator parameters, and the specified keys are valid,
`get_message_param` returns 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`dequeue_message`

## See also

`create_message`,
`clear_message`,
`set_message_tuple`,
`get_message_tuple`,
`set_message_obj`,
`get_message_obj`,
`set_message_param`,
`enqueue_message`,
`dequeue_message`

## Module

Foundation
