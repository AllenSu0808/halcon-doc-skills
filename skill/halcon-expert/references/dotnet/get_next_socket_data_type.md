# GetNextSocketDataType (Operator)

## Name

`GetNextSocketDataType` — Determine the HALCON data type of the next socket data.

## Signature

`static void HOperatorSet.GetNextSocketDataType(HTuple socket, out HTuple dataType)`

`string HSocket.GetNextSocketDataType()`

## Description

`GetNextSocketDataType` returns the data type of the next
data that are present on the socket *`socket`* and returns it
in *`dataType`*. The possible values for *`dataType`*
are:

- **'no_data':** —

  No data are present.
- **'no_halcon_data':** —

  Some data are present, but they are not HALCON data.
- **'tuple':** —

  The next data is a tuple.
- **'region':** —

  The next data is a region object.
- **'image':** —

  The next data is an image object.
- **'xld_cont':** —

  The next data is an XLD contour.
- **'xld_poly':** —

  The next data is an XLD polygon.
- **'xld_para':** —

  The next data is an XLD parallel.
- **'xld_mod_para':** —

  The next data is a modified XLD parallel.
- **'xld_ext_para':** —

  The next data is an extended XLD parallel.
- **'serialized_item':** —

  The next data is a serialized item.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`socket`** (input_control)  socket `→` [HSocket](HSocket.md), [HTuple](HTuple.md) (*IntPtr*)

Socket number.

**`dataType`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Data type of next HALCON data.

## See also

`SendImage`,
`ReceiveImage`,
`SendRegion`,
`ReceiveRegion`,
`SendTuple`,
`ReceiveTuple`,
`SendSerializedItem`,
`ReceiveSerializedItem`

## Module

Foundation
