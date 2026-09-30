# DeserializeFftOptimizationData (Operator)

## Name

`DeserializeFftOptimizationData` — Deserialize FFT speed optimization data.

## Signature

`static void HOperatorSet.DeserializeFftOptimizationData(HTuple serializedItemHandle)`

`static void HMisc.DeserializeFftOptimizationData(HSerializedItem serializedItemHandle)`

## Description

`DeserializeFftOptimizationData` deserializes data, that
was serialized by [`SerializeFftOptimizationData`](serialize_fft_optimization_data.md), for
optimizing the runtime of the FFT (see [`FwriteSerializedItem`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized data is defined by the handle *`serializedItemHandle`*.
The optimization data must have been determined previously with
[`OptimizeFftSpeed`](optimize_fft_speed.md) and must have been serialized with
[`SerializeFftOptimizationData`](serialize_fft_optimization_data.md). If the serialized data has been
determined for the image sizes to be used in the application, calling
[`OptimizeFftSpeed`](optimize_fft_speed.md) is unnecessary. Note that the data should
only be used on the same machine on which they were determined with
[`OptimizeFftSpeed`](optimize_fft_speed.md). Otherwise, the runtimes will not be
optimal. Also note that optimization data that were created with
Standard HALCON cannot be used with Parallel HALCON and vice versa.

`DeserializeFftOptimizationData` influences the runtime of the
following operators, which use the FFT: [`FftGeneric`](fft_generic.md),
[`FftImage`](fft_image.md), [`FftImageInv`](fft_image_inv.md), [`SfsPentland`](sfs_pentland.md),
[`SfsModLr`](sfs_mod_lr.md), [`SfsOrigLr`](sfs_orig_lr.md)[`WienerFilter`](wiener_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

`DeserializeFftOptimizationData` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeFftOptimizationData`

## Possible Successors

`FftGeneric`,
`FftImage`,
`FftImageInv`,
`RftGeneric`,
`WienerFilter`,
`WienerFilterNi`,
`PhotometricStereo`,
`SfsPentland`,
`SfsModLr`,
`SfsOrigLr`

## Alternatives

`OptimizeFftSpeed`,
`OptimizeRftSpeed`

## See also

`SerializeFftOptimizationData`

## Module

Foundation
