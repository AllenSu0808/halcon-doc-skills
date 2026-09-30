# write_fft_optimization_data (Operator)

## Name

`write_fft_optimization_data` — Store FFT speed optimization data in a file.

## Signature

`write_fft_optimization_data( : : FileName : )`

## Description

`write_fft_optimization_data` stores the data for the
optimization of the runtime of the FFT that were determined with
[`optimize_fft_speed`](optimize_fft_speed.md) in the file given by *`FileName`*.
The data can be loaded with [`read_fft_optimization_data`](read_fft_optimization_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileName`** (input_control)  filename.write `→`  (string)

File name of the optimization data.

Default:
'fft_opt.dat'

## Result

`write_fft_optimization_data` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. If necessary, an exception is raised.

## Possible Predecessors

`optimize_fft_speed`,
`optimize_rft_speed`

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
`read_fft_optimization_data`

## Module

Foundation
