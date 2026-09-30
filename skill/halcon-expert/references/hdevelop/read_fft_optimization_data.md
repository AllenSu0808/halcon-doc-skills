# read_fft_optimization_data (Operator)

## Name

`read_fft_optimization_data` — Load FFT speed optimization data from a file.

## Signature

`read_fft_optimization_data( : : FileName : )`

## Description

`read_fft_optimization_data` loads data for optimizing the
runtime of the FFT from the file given by *`FileName`*. The
optimization data must have been determined previously with
[`optimize_fft_speed`](optimize_fft_speed.md) and must have been stored with
[`write_fft_optimization_data`](write_fft_optimization_data.md). If the stored data have been
determined for the image sizes to be used in the application, a call
to [`optimize_fft_speed`](optimize_fft_speed.md) is unnecessary. It should be noted
that the data should only be used on the same machine on which they
were determined with [`optimize_fft_speed`](optimize_fft_speed.md). If this is not
observed the runtimes will not be optimal. Furthermore, it should
be noted that optimization data that were created with Standard
HALCON cannot be used with Parallel HALCON and vice versa.

`read_fft_optimization_data` influences the runtime of the
following operators, which use the FFT: [`fft_generic`](fft_generic.md),
[`fft_image`](fft_image.md), [`fft_image_inv`](fft_image_inv.md), [`sfs_pentland`](sfs_pentland.md),
[`sfs_mod_lr`](sfs_mod_lr.md), [`sfs_orig_lr`](sfs_orig_lr.md)[`wiener_filter`](wiener_filter.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name of the optimization data.

Default:
'fft_opt.dat'

## Result

`read_fft_optimization_data` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

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

`write_fft_optimization_data`

## Module

Foundation
