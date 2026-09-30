# OptimizeFftSpeed (Operator)

## Name

`OptimizeFftSpeed` — Optimize the runtime of the FFT.

## Signature

`static void HOperatorSet.OptimizeFftSpeed(HTuple width, HTuple height, HTuple mode)`

`static void HMisc.OptimizeFftSpeed(int width, int height, string mode)`

## Description

`OptimizeFftSpeed` determines a method that achieves an
optimum runtime of the FFT for an image of size *`width`*
x *`height`*. The data that are determined for
one image size do not influence the methods used for other image
sizes. Consequently, `OptimizeFftSpeed` can be called
multiple times with different values for *`width`* and
*`height`* to achieve an optimum runtime for all image sizes
that are used in an application. The parameter *`mode`*
determines the thoroughness of the search for the fastest method.
For *`mode`* = *"standard"* a fast search is used,
which typically takes a few seconds. The method thus determined
results in very good runtimes, which are not always optimal. For
*`mode`* = *"patient"* a more thorough search is
performed, which typically takes several seconds and in most cases
leads to optimum runtimes. For *`mode`* =
*"exhaustive"* an exhaustive search is performed, which
typically takes several minutes and always results in the optimum
runtime. In most applications, *`mode`* =
*"standard"* results in the best compromise between the
runtime of the FFT and the time required for the search of the
optimum runtime. The data determined with
`OptimizeFftSpeed` can be saved with
[`WriteFftOptimizationData`](write_fft_optimization_data.md) and can be loaded with
[`ReadFftOptimizationData`](read_fft_optimization_data.md).

Please note that this optimization is performed for the particular
computer on which the operator is called. The results are not suited to
be transferred and used on other computers unless they have the same
hardware and software configuration including the driver versions.

`OptimizeFftSpeed` influences the runtime of the following
operators, which use the FFT: [`FftGeneric`](fft_generic.md),
[`FftImage`](fft_image.md), [`FftImageInv`](fft_image_inv.md), [`PhotometricStereo`](photometric_stereo.md),
[`SfsPentland`](sfs_pentland.md), [`SfsModLr`](sfs_mod_lr.md), [`SfsOrigLr`](sfs_orig_lr.md)
[`WienerFilter`](wiener_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576, 1024, 2048

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Thoroughness of the search for the optimum
runtime.

Default:
"standard"

List of values:
"exhaustive", "patient", "standard"

## Result

`OptimizeFftSpeed` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Successors

`FftGeneric`,
`FftImage`,
`FftImageInv`,
`WienerFilter`,
`WienerFilterNi`,
`PhotometricStereo`,
`SfsPentland`,
`SfsModLr`,
`SfsOrigLr`,
`WriteFftOptimizationData`

## Alternatives

`ReadFftOptimizationData`

## See also

`OptimizeRftSpeed`

## Module

Foundation
