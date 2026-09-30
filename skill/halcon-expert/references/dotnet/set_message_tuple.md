# SetMessageTuple (Operator)

## Name

`SetMessageTuple` — Add a key/tuple pair to the message.

## Signature

`static void HOperatorSet.SetMessageTuple(HTuple messageHandle, HTuple key, HTuple tupleData)`

`void HMessage.SetMessageTuple(HTuple key, HTuple tupleData)`

`void HMessage.SetMessageTuple(string key, HTuple tupleData)`

## Description

`SetMessageTuple` stores a tuple associated with a key in the
message, which behaves as a dictionary-like data container.
The message is denoted by the *`messageHandle`* parameter.

*`tupleData`* including strings is copied by the operation, and can
thus be immediately reused.
An empty tuple is considered as a valid value that can be associated with
the key.
If any data (tuple or object) was already associated with given key
(*`key`*), the old data is destroyed by `SetMessageTuple`
and replaced by *`tupleData`*.

The *`key`* has to be a string or an integer.
String keys are treated case sensitive.

The tuple data for the given key can be retrieved again from the message
using [`GetMessageTuple`](get_message_tuple.md).

## Attention

Note that if the tuple contains any handles (which are treated as simple
integers) only the handle values are copied by the operation, not the
resources behind those handles.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- messageHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`messageHandle`** (input_control, state is modified)  message `→` [HMessage](HMessage.md), [HTuple](HTuple.md) (*IntPtr*)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`key`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Key string or integer.

Number of elements:
Key == 1

**`tupleData`** (input_control)  tuple-array `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Tuple value to be associated with the key.

## Example (HDevelop)

```
create_message (Message)
set_message_tuple (Message, 'simple_integer', 27)
set_message_tuple (Message, 'simple_string', 'Hello world')
set_message_tuple (Message, 'mixed_tuple', ['The answer', 42])
```

## Result

If the operation succeeds, `SetMessageTuple` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key) or resource allocation error.

## Possible Predecessors

`CreateMessage`

## Possible Successors

`EnqueueMessage`,
`SetMessageObj`

## Alternatives

`SetMessageObj`

## See also

`CreateMessage`,
`ClearMessage`,
`GetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`,
`SetMessageParam`,
`GetMessageParam`,
`EnqueueMessage`,
`DequeueMessage`

## Module

Foundation
