# optimize_rft_speed (Operator)

## Name

`optimize_rft_speed` — Optimize the runtime of the real-valued FFT.

## Signature

`optimize_rft_speed( : : Width, Height, Mode : )`

## Description

`optimize_rft_speed` determines a method that achieves an
optimum runtime of the real-valued FFT for an image of size
*`Width`* x *`Height`*. The data that are
determined for one image size do not influence the methods used for
other image sizes. Consequently, `optimize_rft_speed` can be
called multiple times with different values for *`Width`* and
*`Height`* to achieve an optimum runtime for all image sizes
that are used in an application. The parameter *`Mode`*
determines the thoroughness of the search for the fastest method.
For *`Mode`* = *'standard'* a fast search is used,
which typically takes a few seconds. The method thus determined
results in very good runtimes, which are not always optimal. For
*`Mode`* = *'patient'* a more thorough search is
performed, which typically takes several seconds and in most cases
leads to optimum runtimes. For *`Mode`* =
*'exhaustive'* an exhaustive search is performed, which
typically takes several minutes and always results in the optimum
runtime. In most applications, *`Mode`* =
*'standard'* results in the best compromise between the
runtime of the real-valued FFT and the time required for the search
of the optimum runtime. The data determined with
`optimize_rft_speed` can be saved with
[`write_fft_optimization_data`](write_fft_optimization_data.md) and can be loaded with
[`read_fft_optimization_data`](read_fft_optimization_data.md).

Please note that this optimization is performed for the particular
computer on which the operator is called. The results are not suited to
be transferred and used on other computers unless they have the same
hardware and software configuration including the driver versions.

`optimize_rft_speed` influences the runtime of
[`rft_generic`](rft_generic.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Width`** (input_control)  integer `→`  (integer)

Width of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048

**`Height`** (input_control)  integer `→`  (integer)

Height of the image for which the runtime should be
optimized.

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576, 1024, 2048

**`Mode`** (input_control)  string `→`  (string)

Thoroughness of the search for the optimum
runtime.

Default:
'standard'

List of values:
'exhaustive', 'patient', 'standard'

## Result

`optimize_rft_speed` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If necessary, an exception is raised.

## Possible Successors

`rft_generic`,
`write_fft_optimization_data`

## Alternatives

`read_fft_optimization_data`

## See also

`optimize_fft_speed`

## Module

Foundation
