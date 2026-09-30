# set_message_tuple (Operator)

## Name

`set_message_tuple` — Add a key/tuple pair to the message.

## Signature

`def set_message_tuple(message_handle: HHandle, key: Union[str, int], tuple_data: Sequence[HTupleElementType]) -> None`

## Description

`set_message_tuple` stores a tuple associated with a key in the
message, which behaves as a dictionary-like data container.
The message is denoted by the *`message_handle`* parameter.

*`tuple_data`* including strings is copied by the operation, and can
thus be immediately reused.
An empty tuple is considered as a valid value that can be associated with
the key.
If any data (tuple or object) was already associated with given key
(*`key`*), the old data is destroyed by `set_message_tuple`
and replaced by *`tuple_data`*.

The *`key`* has to be a string or an integer.
String keys are treated case sensitive.

The tuple data for the given key can be retrieved again from the message
using [`get_message_tuple`](get_message_tuple.md).

## Attention

Note that if the tuple contains any handles (which are treated as simple
integers) only the handle values are copied by the operation, not the
resources behind those handles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- message_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`message_handle`** (input_control, state is modified)  message `→` HHandle

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`key`** (input_control)  string `→` Union[str, int]

Key string or integer.

Number of elements:
Key == 1

**`tuple_data`** (input_control)  tuple-array `→` Sequence[HTupleElementType]

Tuple value to be associated with the key.

## Example (HDevelop)

```
create_message (Message)
set_message_tuple (Message, 'simple_integer', 27)
set_message_tuple (Message, 'simple_string', 'Hello world')
set_message_tuple (Message, 'mixed_tuple', ['The answer', 42])
```

## Result

If the operation succeeds, `set_message_tuple` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key) or resource allocation error.

## Possible Predecessors

`create_message`

## Possible Successors

`enqueue_message`,
`set_message_obj`

## Alternatives

`set_message_obj`

## See also

`create_message`,
`clear_message`,
`get_message_tuple`,
`set_message_obj`,
`get_message_obj`,
`set_message_param`,
`get_message_param`,
`enqueue_message`,
`dequeue_message`

## Module

Foundation
