# set_message_obj (Operator)

## Name

`set_message_obj` — Add a key/object pair to the message.

## Signature

`def set_message_obj(object_data: HObject, message_handle: HHandle, key: Union[str, int]) -> None`

## Description

`set_message_obj` stores an object associated with a key in the
message, which behaves as a dictionary-like data container.
The message is denoted by the *`message_handle`* parameter.

*`object_data`* is copied by the operation (copying the object data
in HALCON's object database, see [`copy_obj`](copy_obj.md)), and can thus be
immediately reused. Both an empty object or an object tuple are considered
as a valid value that can be associated with the key.
If any data (tuple or object) was already associated with given key
(*`key`*), the old data is destroyed by `set_message_obj`
and replaced by *`object_data`*.

The *`key`* has to be a string or an integer.
String keys are treated case sensitive.

The object data for the given key can be retrieved again from the message
using [`get_message_obj`](get_message_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- message_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`object_data`** (input_object)  object(-array) `→` HObject

Object to be associated with the key.

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

## Example (HDevelop)

```
create_message (Message)
read_image( Image, 'filename')
set_message_obj (Image, Message, 'my_image')
```

## Result

If the operation succeeds, [`set_message_tuple`](set_message_tuple.md) returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key) or resource allocation error.

## Possible Predecessors

`create_message`

## Possible Successors

`enqueue_message`,
`set_message_tuple`

## Alternatives

`set_message_tuple`

## See also

`create_message`,
`clear_message`,
`set_message_tuple`,
`get_message_tuple`,
`get_message_obj`,
`set_message_param`,
`get_message_param`,
`enqueue_message`,
`dequeue_message`

## Module

Foundation
