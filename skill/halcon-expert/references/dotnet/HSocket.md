# HSocket (Class)

## Name

`HSocket` — Represents an instance of a socket connection.

## Constructors

|  |  |  |
| --- | --- | --- |
| `OpenSocketConnect` |  | Open a socket and connect it to an accepting socket. |
| `OpenSocketAccept` |  | Open a socket that accepts connection requests. |

## Methods

|  |  |  |
| --- | --- | --- |
| `CloseSocket` |  | Close a socket. |
| `GetNextSocketDataType` |  | Determine the data type of the next socket data. |
| `GetSocketDescriptor` |  | Get the socket descriptor of a socket used by the operating system. |
| `GetSocketParam` |  | Get the value of a socket parameter. |
| `OpenSocketAccept` |  | Open a socket that accepts connection requests. |
| `OpenSocketConnect` |  | Open a socket and connect it to an accepting socket. |
| `ReceiveData` |  | Receive arbitrary data from external devices or applications using a generic socket connection. |
| `ReceiveImage` |  | Receive an image over a socket connection. |
| `ReceiveRegion` |  | Receive regions over a socket connection. |
| `ReceiveSerializedItem` |  | Receive a serialized item over a socket connection. |
| `ReceiveTuple` |  | Receive a tuple over a socket connection. |
| `ReceiveXld` |  | Receive an XLD object over a socket connection. |
| `SendData` |  | Send arbitrary data to external devices or applications using a generic socket communication. |
| `SendImage` |  | Send an image over a socket connection. |
| `SendRegion` |  | Send regions over a socket connection. |
| `SendSerializedItem` |  | Send a serialized item over a socket connection. |
| `SendTuple` |  | Send a tuple over a socket connection. |
| `SendXld` |  | Send an XLD object over a socket connection. |
| `SetSocketParam` |  | Set a socket parameter. |
| `SocketAcceptConnect` |  | Accept a connection request on a listening socket of the protocol type 'HALCON'"HALCON""HALCON""HALCON""HALCON" or 'TCP'"TCP""TCP""TCP""TCP"/'TCP4'"TCP4""TCP4""TCP4""TCP4"/'TCP6'"TCP6""TCP6""TCP6""TCP6". |
