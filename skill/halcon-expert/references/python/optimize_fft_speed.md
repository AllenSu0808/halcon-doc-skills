# optimize_fft_speed (Operator)

## Name

`optimize_fft_speed` — Optimize the runtime of the FFT.

## Signature

`def optimize_fft_speed(width: int, height: int, mode: str) -> None`

## Description

`optimize_fft_speed` determines a method that achieves an
optimum runtime of the FFT for an image of size *`width`*
x *`height`*. The data that are determined for
one image size do not influence the methods used for other image
sizes. Consequently, `optimize_fft_speed` can be called
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
`optimize_fft_speed` can be saved with
[`write_fft_optimization_data`](write_fft_optimization_data.md) and can be loaded with
[`read_fft_optimization_data`](read_fft_optimization_data.md).

Please note that this optimization is performed for the particular
computer on which the operator is called. The results are not suited to
be transferred and used on other computers unless they have the same
hardware and software configuration including the driver versions.

`optimize_fft_speed` influences the runtime of the following
operators, which use the FFT: [`fft_generic`](fft_generic.md),
[`fft_image`](fft_image.md), [`fft_image_inv`](fft_image_inv.md), [`photometric_stereo`](photometric_stereo.md),
[`sfs_pentland`](sfs_pentland.md), [`sfs_mod_lr`](sfs_mod_lr.md), [`sfs_orig_lr`](sfs_orig_lr.md)
[`wiener_filter`](wiener_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`width`** (input_control)  integer `→` int

Width of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048

**`height`** (input_control)  integer `→` int

Height of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576, 1024, 2048

**`mode`** (input_control)  string `→` str

Thoroughness of the search for the optimum
runtime.

Default:
"standard"

List of values:
"exhaustive", "patient", "standard"

## Result

`optimize_fft_speed` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Successors

`fft_generic`,
`fft_image`,
`fft_image_inv`,
`wiener_filter`,
`wiener_filter_ni`,
`photometric_stereo`,
`sfs_pentland`,
`sfs_mod_lr`,
`sfs_orig_lr`,
`write_fft_optimization_data`

## Alternatives

`read_fft_optimization_data`

## See also

`optimize_rft_speed`

## Module

Foundation
