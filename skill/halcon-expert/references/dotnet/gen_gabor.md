# GenGabor (Operator)

## Name

`GenGabor` — Generate a Gabor filter.

## Signature

`static void HOperatorSet.GenGabor(out HObject imageFilter, HTuple angle, HTuple frequency, HTuple bandwidth, HTuple orientation, HTuple norm, HTuple mode, HTuple width, HTuple height)`

`void HImage.GenGabor(double angle, double frequency, double bandwidth, double orientation, string norm, string mode, int width, int height)`

## Description

`GenGabor` generates a Gabor filter with a user-definable
bandpass frequency range and sign for the Hilbert transform. This
is done by calculating a symmetrical filter in the frequency domain,
which can be adapted by the parameters *`angle`*,
*`frequency`*, *`bandwidth`* and *`orientation`* such
that a certain frequency band and a certain direction range in the
spatial domain is filtered out in the frequency domain.

The parameters *`frequency`* (central frequency = distance from
the DC term) and *`orientation`* (direction) determine the
center of the filter. Larger values of *`frequency`* result in
higher frequencies being passed. A value of 0 for
*`orientation`* generates a horizontally oriented “crescent”
(the bulge of the crescent points upward). Higher values of
*`orientation`* result in the counterclockwise rotation of the
crescent.

The parameters *`angle`* and *`bandwidth`* are used to
determine the range of frequencies and angles being passed by the
filter. The larger *`angle`* is, the smaller the range of
angles passed by the filter gets (because the “crescent” gets
narrower). The larger *`bandwidth`* is, the smaller the
frequency band being passed gets (because the “crescent” gets
thinner).

To achieve a maximum overall efficiency of the filtering operation,
the parameter *`norm`* can be used to specify the normalization
factor of the filter. If [`FftGeneric`](fft_generic.md) and *`norm`* =
*"n"* is used the normalization in the FFT can be avoided.
*`mode`* can be used to determine where the DC term of the
filter lies. If [`FftGeneric`](fft_generic.md) is used, *"dc_edge"* can
be used to gain efficiency. If [`FftImage`](fft_image.md) and
[`FftImageInv`](fft_image_inv.md) are used for filtering, *`norm`* =
*"none"* and *`mode`* = *"dc_center"* must be
used. Note that `GenGabor` cannot create a filter that can
be used with [`RftGeneric`](rft_generic.md).

The resulting image is a two-channel real-image, containing the
Gabor filter in the first channel and the corresponding Hilbert
filter in the second channel.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageFilter`** (output_object)  multichannel-image `→` [HImage](HImage.md) (real)

Gabor and Hilbert filter.

**`angle`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Angle range, inversely proportional to the range
of orientations.

Default:
1.4

Suggested values:
1.0, 1.2, 1.4, 1.6, 2.0, 2.5, 3.0, 5.0, 6.0, 10.0, 20.0, 30.0, 50.0, 70.0, 100.0

Value range:
`1.0
≤
angle
≤
500.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`frequency`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Distance of the center of the filter to the DC term.

Default:
0.4

Suggested values:
0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.50, 0.55, 0.60, 0.65, 0.699

Value range:
`0.0
≤
frequency
≤
0.7`

Minimum increment:
0.00001

Recommended increment:
0.005

**`bandwidth`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Bandwidth range, inversely proportional to the range
of frequencies being passed.

Default:
1.0

Suggested values:
0.1, 0.3, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0, 50.0

Value range:
`0.05
≤
bandwidth
≤
100.0`

Minimum increment:
0.001

Recommended increment:
0.1

**`orientation`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Angle of the principal orientation.

Default:
1.5

Suggested values:
0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.14

Value range:
`0.0
≤
orientation
≤
3.1416`

Minimum increment:
0.0001

Recommended increment:
0.05

**`norm`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Normalizing factor of the filter.

Default:
"none"

List of values:
"n", "none"

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Location of the DC term in the frequency domain.

Default:
"dc_center"

List of values:
"dc_center", "dc_edge"

**`width`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the image (filter).

Default:
512

Suggested values:
128, 160, 192, 256, 320, 384, 512, 640, 768, 1024, 2048, 4096, 8192

**`height`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the image (filter).

Default:
512

Suggested values:
120, 128, 144, 240, 256, 288, 480, 512, 576, 1024, 2048, 4096, 8192

## Example (HDevelop)

```
gen_gabor(Filter,1.4,0.4,1.0,1.5,'n','dc_edge',512,512)
fft_generic(Image,ImageFFT,'to_freq',-1,'none','dc_edge','complex')
convol_gabor(ImageFFT,Filter,Gabor,Hilbert)
fft_generic(Gabor,GaborInv,'from_freq',1,'none','dc_edge','byte')
fft_generic(Hilbert,HilbertInv,'from_freq',1,'none','dc_edge','byte')
energy_gabor(GaborInv,HilbertInv,Energy)
```

## Result

`GenGabor` returns 2 (
H_MSG_TRUE)
if all parameters are correct. If
necessary, an exception is raised.

## Possible Predecessors

`FftImage`,
`FftGeneric`

## Possible Successors

`ConvolGabor`

## Alternatives

`GenBandpass`,
`GenBandfilter`,
`GenHighpass`,
`GenLowpass`

## See also

`FftImageInv`,
`EnergyGabor`

## Module

Foundation
