# SerializeFftOptimizationData (Operator)

## Name

`SerializeFftOptimizationData` — Serialize FFT speed optimization data.

## Signature

`static void HOperatorSet.SerializeFftOptimizationData(out HTuple serializedItemHandle)`

`static HSerializedItem HMisc.SerializeFftOptimizationData()`

## Description

`SerializeFftOptimizationData` serializes the data for the
optimization of the runtime of the FFT that were determined with
[`OptimizeFftSpeed`](optimize_fft_speed.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization).
The same data that is written in a file by
[`WriteFftOptimizationData`](write_fft_optimization_data.md) is converted to a serialized
item. The serialized data is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeFftOptimizationData`](deserialize_fft_optimization_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

`SerializeFftOptimizationData` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`OptimizeFftSpeed`,
`OptimizeRftSpeed`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeFftOptimizationData`

## See also

`FftGeneric`,
`FftImage`,
`FftImageInv`,
`WienerFilter`,
`WienerFilterNi`,
`PhotometricStereo`,
`SfsPentland`,
`SfsModLr`,
`SfsOrigLr`,
`DeserializeFftOptimizationData`

## Module

Foundation
