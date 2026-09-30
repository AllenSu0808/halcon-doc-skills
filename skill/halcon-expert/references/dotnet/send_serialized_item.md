# SendSerializedItem (Operator)

## Name

`SendSerializedItem` — Send a serialized item over a socket connection.

## Signature

`static void HOperatorSet.SendSerializedItem(HTuple socket, HTuple serializedItemHandle)`

`void HSocket.SendSerializedItem(HSerializedItem serializedItemHandle)`

`void HSerializedItem.SendSerializedItem(HSocket socket)`

## Description

`SendSerializedItem` sends a serialized item over a socket
connection determined by *`socket`* (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basics of serialization). The receiving HALCON process must
call [`ReceiveSerializedItem`](receive_serialized_item.md) to read the serialized item
from the socket. The serialized item is returned by the handle
*`serializedItemHandle`*.
For a detailed example showing the use of a socket connection, see
[`OpenSocketAccept`](open_socket_accept.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SendSerializedItem` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateSerializedItemPtr`,
`SerializeMatrix`,
`SerializeMetrologyModel`

## Possible Successors

`ReceiveSerializedItem`

## Module

Foundation
