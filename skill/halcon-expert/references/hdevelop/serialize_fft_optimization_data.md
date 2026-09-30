# serialize_fft_optimization_data (Operator)

## Name

`serialize_fft_optimization_data` — Serialize FFT speed optimization data.

## Signature

`serialize_fft_optimization_data( : : : SerializedItemHandle)`

## Description

`serialize_fft_optimization_data` serializes the data for the
optimization of the runtime of the FFT that were determined with
[`optimize_fft_speed`](optimize_fft_speed.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization).
The same data that is written in a file by
[`write_fft_optimization_data`](write_fft_optimization_data.md) is converted to a serialized
item. The serialized data is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_fft_optimization_data`](deserialize_fft_optimization_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

`serialize_fft_optimization_data` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`optimize_fft_speed`,
`optimize_rft_speed`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_fft_optimization_data`

## See also

`fft_generic`,
`fft_image`,
`fft_image_inv`,
`wiener_filter`,
`wiener_filter_ni`,
`photometric_stereo`,
`sfs_pentland`,
`sfs_mod_lr`,
`sfs_orig_lr`,
`deserialize_fft_optimization_data`

## Module

Foundation
