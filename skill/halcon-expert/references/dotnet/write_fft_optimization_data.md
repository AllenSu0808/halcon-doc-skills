# WriteFftOptimizationData (Operator)

## Name

`WriteFftOptimizationData` — Store FFT speed optimization data in a file.

## Signature

`static void HOperatorSet.WriteFftOptimizationData(HTuple fileName)`

`static void HMisc.WriteFftOptimizationData(string fileName)`

## Description

`WriteFftOptimizationData` stores the data for the
optimization of the runtime of the FFT that were determined with
[`OptimizeFftSpeed`](optimize_fft_speed.md) in the file given by *`fileName`*.
The data can be loaded with [`ReadFftOptimizationData`](read_fft_optimization_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name of the optimization data.

Default:
"fft_opt.dat"

## Result

`WriteFftOptimizationData` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`OptimizeFftSpeed`,
`OptimizeRftSpeed`

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
`ReadFftOptimizationData`

## Module

Foundation
