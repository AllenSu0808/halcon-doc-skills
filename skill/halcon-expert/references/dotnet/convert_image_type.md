# ConvertImageType (Operator)

## Name

`ConvertImageType` — Convert the type of an image.

## Signature

`static void HOperatorSet.ConvertImageType(HObject image, out HObject imageConverted, HTuple newType)`

`HImage HImage.ConvertImageType(string newType)`

## Description

`ConvertImageType` converts images of an arbitrary
type into an arbitrary new image type. If the conversion is done
from a larger to a smaller gray value range (e.g., from 'int4' to
'byte'), too large or too small values are simply “clipped”.
If the result images are of type 'direction', gray values that
are not in the value range that is valid for 'direction' images
are set to the value 255 to mark them as invalid. It
is therefore advisable to adapt the range of gray values by calling
[`ScaleImage`](scale_image.md) before calling this operator. For images of
type complex, only the real part is converted. The imaginary part
is ignored. This facilitates an efficient conversion of images that
have been transformed back from the frequency domain. Such images
always have an imaginary part of 0.

## Attention

The conversion to the 'int8' image format is only available on 64 bit
systems!
If the source and destination image type are identical, no new image
matrix is allocated.

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Image whose image type is to be changed.

**`imageConverted`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / direction* / cyclic* / int1* / int2* / uint2* / int4* / int8 / real* / complex*) **allowed for compute devices*

Converted image.

**`newType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Desired image type (i.e., type of the gray values).

Default:
"byte"

List of values:
"byte", "complex", "cyclic", "direction", "int1", "int2", "int4", "int8", "real", "uint2"

List of values (for compute devices):
"int1", "int2", "uint2", "int4", "byte", "real", "direction", "cyclic", "complex"

## Result

`ConvertImageType` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`ScaleImage`

## See also

`ScaleImage`,
`AbsImage`

## Module

Foundation
