# GetImagePointer3 (Operator)

## Name

`GetImagePointer3` — Access the pointers of a colored image.

## Signature

`static void HOperatorSet.GetImagePointer3(HObject imageRGB, out HTuple pointerRed, out HTuple pointerGreen, out HTuple pointerBlue, out HTuple type, out HTuple width, out HTuple height)`

`void HImage.GetImagePointer3(out HTuple pointerRed, out HTuple pointerGreen, out HTuple pointerBlue, out HTuple type, out HTuple width, out HTuple height)`

`void HImage.GetImagePointer3(out IntPtr pointerRed, out IntPtr pointerGreen, out IntPtr pointerBlue, out string type, out int width, out int height)`

## Description

The operator `GetImagePointer3` returns a C pointer to
the three channels of a colored image (*`imageRGB`*).
Additionally the image type (*`type`* = 'byte', 'int2','float' etc.)
and the image size (*`width`* and *`height`*) are returned.
Consequently a direct access to the image data in the
HALCON database from the HALCON host language via the pointer is possible.
An image is stored in HALCON as a vector of image lines.
The image types 'complex' and 'vector_type' are handled in a specific way.
In particular, 'complex' images are interleaved, i.e., the real and the
imaginary parts are alternating, whereas 'vector_field' images consist of
two matrices, one for the rows and one for the columns, which are stored in
the HALCON database one after the other.
The three channels must have the same pixel type and the same size.

## Attention

Only one image can be passed.
The operator `GetImagePointer3` should only be used for entry
into newly created images, since otherwise the gray values of other images
might be overwritten (see relational structure).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageRGB`** (input_object)  multichannel-image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Input image.

**`pointerRed`** (output_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the pixels of the first channel.

**`pointerGreen`** (output_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the pixels of the second channel.

**`pointerBlue`** (output_control)  pointer(-array) `→` [HTuple](HTuple.md) (*IntPtr*)

Pointer to the pixels of the third channel.

**`type`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of image.

List of values:
"byte", "complex", "cyclic", "direction", "int1", "int2", "int4", "int8", "real", "uint2", "vector_field_absolute", "vector_field_relative"

**`width`** (output_control)  extent.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Width of image.

**`height`** (output_control)  extent.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Height of image.

## Result

The operator `GetImagePointer3` returns the value 2 (
H_MSG_TRUE)
if
exactly one image is passed.
The behavior in case of empty input (no input images available) is set via
the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`

## Alternatives

`SetGrayval`,
`GetGrayval`,
`GetImagePointer1`

## See also

`PaintRegion`,
`PaintGray`

## Module

Foundation
