# get_message_obj (Operator)

## Name

`get_message_obj` — Retrieve an object associated with the key from the message.

## Signature

`get_message_obj( : ObjectData : MessageHandle, Key : )`

## Description

`get_message_obj` retrieves an object associated with the *`Key`*
from the message denoted by the *`MessageHandle`*.
The object has to be previously stored to the message using
[`set_message_obj`](set_message_obj.md).

The operator returns the data in the parameter *`ObjectData`*. The
iconic object is copied by the operation. Therefore, clearing or reusing
the message object afterwards will not have any side-effect on the returned
iconic object, afterwards.

If the given *`Key`* is not present in the message or if the data
associated with the key is not an object, `get_message_obj` fails.
Presence of keys and information about the data associated with the key can
be verified using [`get_message_param`](get_message_param.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ObjectData`** (output_object)  object(-array) `→` object

Tuple value retrieved from the message.

**`MessageHandle`** (input_control)  message `→`  (handle)

Message handle.

Number of elements:
MessageHandle == 1

Restriction:
`MessageHandle != 0`

**`Key`** (input_control)  string `→`  (string / integer)

Key string or integer.

Number of elements:
Key == 1

## Example (HDevelop)

```
* ...
get_message_param (Message,'key_exists',['simple_string','foo','my_image'],\
                   KeysPresence)
get_message_param (Message,'key_data_type',['simple_string','my_image'],\
                   KeysType)
get_message_obj (Image, Message, 'my_image')
```

## Result

If the operation succeeds, `get_message_obj` returns 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised. Possible error conditions include
invalid parameters (handle or key), the required key not found in the
message or other than object data associated with given key.

## Possible Predecessors

`dequeue_message`

## Alternatives

`get_message_tuple`

## See also

`create_message`,
`clear_message`,
`set_message_tuple`,
`get_message_tuple`,
`set_message_obj`,
`set_message_param`,
`get_message_param`,
`enqueue_message`,
`dequeue_message`

## Module

Foundation
