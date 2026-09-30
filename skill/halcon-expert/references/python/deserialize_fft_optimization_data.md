# deserialize_fft_optimization_data (Operator)

## Name

`deserialize_fft_optimization_data` — Deserialize FFT speed optimization data.

## Signature

`def deserialize_fft_optimization_data(serialized_item_handle: HHandle) -> None`

## Description

`deserialize_fft_optimization_data` deserializes data, that
was serialized by [`serialize_fft_optimization_data`](serialize_fft_optimization_data.md), for
optimizing the runtime of the FFT (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized data is defined by the handle *`serialized_item_handle`*.
The optimization data must have been determined previously with
[`optimize_fft_speed`](optimize_fft_speed.md) and must have been serialized with
[`serialize_fft_optimization_data`](serialize_fft_optimization_data.md). If the serialized data has been
determined for the image sizes to be used in the application, calling
[`optimize_fft_speed`](optimize_fft_speed.md) is unnecessary. Note that the data should
only be used on the same machine on which they were determined with
[`optimize_fft_speed`](optimize_fft_speed.md). Otherwise, the runtimes will not be
optimal. Also note that optimization data that were created with
Standard HALCON cannot be used with Parallel HALCON and vice versa.

`deserialize_fft_optimization_data` influences the runtime of the
following operators, which use the FFT: [`fft_generic`](fft_generic.md),
[`fft_image`](fft_image.md), [`fft_image_inv`](fft_image_inv.md), [`sfs_pentland`](sfs_pentland.md),
[`sfs_mod_lr`](sfs_mod_lr.md), [`sfs_orig_lr`](sfs_orig_lr.md)[`wiener_filter`](wiener_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

`deserialize_fft_optimization_data` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_fft_optimization_data`

## Possible Successors

`fft_generic`,
`fft_image`,
`fft_image_inv`,
`rft_generic`,
`wiener_filter`,
`wiener_filter_ni`,
`photometric_stereo`,
`sfs_pentland`,
`sfs_mod_lr`,
`sfs_orig_lr`

## Alternatives

`optimize_fft_speed`,
`optimize_rft_speed`

## See also

`serialize_fft_optimization_data`

## Module

Foundation
