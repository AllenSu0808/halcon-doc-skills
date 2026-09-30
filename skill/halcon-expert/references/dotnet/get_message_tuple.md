# GetMessageTuple (Operator)

## Name

`GetMessageTuple` — Retrieve a tuple associated with the key from the message.

## Signature

`static void HOperatorSet.GetMessageTuple(HTuple messageHandle, HTuple key, out HTuple tupleData)`

`HTuple HMessage.GetMessageTuple(HTuple key)`

`HTuple HMessage.GetMessageTuple(string key)`

## Description

`GetMessageTuple` retrieves a tuple associated with the *`key`*
from the message denoted by the *`messageHandle`*.
The tuple has to be previously stored to the message using
[`SetMessageTuple`](set_message_tuple.md).

The operator returns the data in the parameter *`tupleData`*.
The data including strings is copied by the operation, the message can thus
be immediately reused.

If the given *`key`* is not present in the message or if the data
associated with the key is not a tuple, `GetMessageTuple` fails.
Presence of keys and information about the data associated with the key
can be verified using [`GetMessageParam`](get_message_param.md).

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

**`key`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Key string or integer.

Number of elements:
Key == 1

**`tupleData`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*string* / int / long / double / HHandle)

Tuple value retrieved from the message.

## Example (HDevelop)

```
* ...
get_message_param (Message,'key_exists',['simple_string','foo','my_image'],\
                   KeysPresence)
get_message_param (Message,'key_data_type',['simple_string','my_image'],\
                   KeysType)
get_message_tuple (Message,'simple_string',TupleString)
```

## Result

If the operation succeeds, `GetMessageTuple` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
message, or other than tuple data associated with given key.

## Possible Predecessors

`DequeueMessage`

## Alternatives

`GetMessageObj`

## See also

`CreateMessage`,
`ClearMessage`,
`SetMessageTuple`,
`SetMessageObj`,
`GetMessageObj`,
`SetMessageParam`,
`GetMessageParam`,
`EnqueueMessage`,
`DequeueMessage`

## Module

Foundation
