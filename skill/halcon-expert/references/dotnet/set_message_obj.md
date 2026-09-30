# SetMessageObj (Operator)

## Name

`SetMessageObj` — Add a key/object pair to the message.

## Signature

`static void HOperatorSet.SetMessageObj(HObject objectData, HTuple messageHandle, HTuple key)`

`void HMessage.SetMessageObj(HObject objectData, HTuple key)`

`void HMessage.SetMessageObj(HObject objectData, string key)`

## Description

`SetMessageObj` stores an object associated with a key in the
message, which behaves as a dictionary-like data container.
The message is denoted by the *`messageHandle`* parameter.

*`objectData`* is copied by the operation (copying the object data
in HALCON's object database, see [`CopyObj`](copy_obj.md)), and can thus be
immediately reused. Both an empty object or an object tuple are considered
as a valid value that can be associated with the key.
If any data (tuple or object) was already associated with given key
(*`key`*), the old data is destroyed by `SetMessageObj`
and replaced by *`objectData`*.

The *`key`* has to be a string or an integer.
String keys are treated case sensitive.

The object data for the given key can be retrieved again from the message
using [`GetMessageObj`](get_message_obj.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- messageHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`objectData`** (input_object)  object(-array) `→` [HObject](HObject.md)

Object to be associated with the key.

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

## Example (HDevelop)

```
create_message (Message)
read_image( Image, 'filename')
set_message_obj (Image, Message, 'my_image')
```

## Result

If the operation succeeds, [`SetMessageTuple`](set_message_tuple.md) returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key) or resource allocation error.

## Possible Predecessors

`CreateMessage`

## Possible Successors

`EnqueueMessage`,
`SetMessageTuple`

## Alternatives

`SetMessageTuple`

## See also

`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`GetMessageTuple`,
`GetMessageObj`,
`SetMessageParam`,
`GetMessageParam`,
`EnqueueMessage`,
`DequeueMessage`

## Module

Foundation
