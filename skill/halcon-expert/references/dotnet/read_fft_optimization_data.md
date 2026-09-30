# ReadFftOptimizationData (Operator)

## Name

`ReadFftOptimizationData` — Load FFT speed optimization data from a file.

## Signature

`static void HOperatorSet.ReadFftOptimizationData(HTuple fileName)`

`static void HMisc.ReadFftOptimizationData(string fileName)`

## Description

`ReadFftOptimizationData` loads data for optimizing the
runtime of the FFT from the file given by *`fileName`*. The
optimization data must have been determined previously with
[`OptimizeFftSpeed`](optimize_fft_speed.md) and must have been stored with
[`WriteFftOptimizationData`](write_fft_optimization_data.md). If the stored data have been
determined for the image sizes to be used in the application, a call
to [`OptimizeFftSpeed`](optimize_fft_speed.md) is unnecessary. It should be noted
that the data should only be used on the same machine on which they
were determined with [`OptimizeFftSpeed`](optimize_fft_speed.md). If this is not
observed the runtimes will not be optimal. Furthermore, it should
be noted that optimization data that were created with Standard
HALCON cannot be used with Parallel HALCON and vice versa.

`ReadFftOptimizationData` influences the runtime of the
following operators, which use the FFT: [`FftGeneric`](fft_generic.md),
[`FftImage`](fft_image.md), [`FftImageInv`](fft_image_inv.md), [`SfsPentland`](sfs_pentland.md),
[`SfsModLr`](sfs_mod_lr.md), [`SfsOrigLr`](sfs_orig_lr.md)[`WienerFilter`](wiener_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name of the optimization data.

Default:
"fft_opt.dat"

## Result

`ReadFftOptimizationData` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

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

`WriteFftOptimizationData`

## Module

Foundation
