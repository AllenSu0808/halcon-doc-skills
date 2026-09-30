# DecodeBarCodeRectangle2 (Operator)

## Name

`DecodeBarCodeRectangle2` — Decode bar code symbols within a rectangle.

## Signature

`static void HOperatorSet.DecodeBarCodeRectangle2(HObject image, HTuple barCodeHandle, HTuple codeType, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2, out HTuple decodedDataStrings)`

`HTuple HBarCode.DecodeBarCodeRectangle2(HImage image, HTuple codeType, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2)`

`string HBarCode.DecodeBarCodeRectangle2(HImage image, string codeType, double row, double column, double phi, double length1, double length2)`

`HTuple HImage.DecodeBarCodeRectangle2(HBarCode barCodeHandle, HTuple codeType, HTuple row, HTuple column, HTuple phi, HTuple length1, HTuple length2)`

`string HImage.DecodeBarCodeRectangle2(HBarCode barCodeHandle, string codeType, double row, double column, double phi, double length1, double length2)`

## Description

The operator `DecodeBarCodeRectangle2` uses the bar code
model specified by *`barCodeHandle`* to decode a bar code at
a given position within the image *`image`*.
*`barCodeHandle`* must be created with
[`CreateBarCodeModel`](create_bar_code_model.md), its parameters can be set with
[`SetBarCodeParam`](set_bar_code_param.md). The position of the bar code is given
as an arbitrarily oriented rectangle. Contrary to
[`FindBarCode`](find_bar_code.md), where the decoding is preceded by a time
consuming search for candidate regions,
`DecodeBarCodeRectangle2` scans the provided region directly
for bar codes. The rectangular region is defined by the parameters
*`row`* and *`column`* for the center, *`phi`* for
the orientation and *`length1`* and *`length2`* for the
half edge lengths (see [`GenRectangle2`](gen_rectangle2.md)). The angle *`phi`*
also determines the reading direction and is defined as the angle
between the reading direction of the bar code and the horizontal
image axis. The angle is positive in counter clockwise direction and
is given in radians as in [`GenRectangle2`](gen_rectangle2.md). Note that the angle
unit deviates from the conventions in [`GetBarCodeResult`](get_bar_code_result.md) and
[`SetBarCodeParam`](set_bar_code_param.md) where angles are given in degrees.
*`phi`* can be in the range of
$[-\pi,+\pi]$.
The reading direction is perpendicular to the bars of the bar code.
Bar codes with a reading direction
$\texttt{Phi}+\pi$ are also returned.
Multiple regions for decoding can be given by supplying tuples for
*`row`*, *`column`*, *`phi`*, *`length1`* and
*`length2`*.

The rectangle should cover completely the bar code and the quiet zones.
Regions that are too big will be decoded, if there is no disturbing
pattern within these regions and the height (*`length2`*) is
small enough such that scanlines can be placed sufficiently dense.
Rectangles that are too short in reading direction (*`length1`*)
cannot be decoded.

`DecodeBarCodeRectangle2` can be used if the position of
the bar code is already known in advance. For example, the candidate
regions found by [`FindBarCode`](find_bar_code.md) and [`GetBarCodeObject`](get_bar_code_object.md)
could be reused with a different code type (see the following example).

Multiple bar code types can be specified for *`codeType`*. See
section Autodiscrimination for [`FindBarCode`](find_bar_code.md).

Further aspects of the actual decoding are explained with the operator
[`FindBarCode`](find_bar_code.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- barCodeHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte)

Input image.

**`barCodeHandle`** (input_control, state is modified)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`codeType`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Type of the searched bar code.

Default:
"EAN-13"

List of values:
"2/5 Industrial", "2/5 Interleaved", "Codabar", "Code 128", "Code 39", "Code 93", "EAN-13 Add-On 2", "EAN-13 Add-On 5", "EAN-13", "EAN-8 Add-On 2", "EAN-8 Add-On 5", "EAN-8", "GS1 DataBar Expanded Stacked", "GS1 DataBar Expanded", "GS1 DataBar Limited", "GS1 DataBar Omnidir", "GS1 DataBar Stacked Omnidir", "GS1 DataBar Stacked", "GS1 DataBar Truncated", "GS1-128", "MSI", "PharmaCode", "UPC-A Add-On 2", "UPC-A Add-On 5", "UPC-A", "UPC-E Add-On 2", "UPC-E Add-On 5", "UPC-E", "auto"

**`row`** (input_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row index of the center.

Default:
50.0

**`column`** (input_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column index of the center.

Default:
100.0

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Orientation of rectangle in radians.

Default:
0.0

Suggested values:
0.0, 0.785398, 1.570796, 3.1415926

**`length1`** (input_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half of the length of the rectangle along the reading
direction of the bar code.

Default:
200.0

**`length2`** (input_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Half of the length of the rectangle perpendicular to
the reading direction of the bar code.

Default:
100.0

**`decodedDataStrings`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Data strings of all successfully decoded bar codes.

## Example (HDevelop)

```
read_image (Image, 'barcode/ean13/ean1301.png')
create_bar_code_model ([], [], BHandle)
find_bar_code (Image, SymReg, BHandle, '2/5 Industrial', Dec)
if (|Dec| == 0)
*     A 2/5 Industrial code wasn't found. Try decoding an EAN-13 code.
    get_bar_code_object (CandReg, BHandle, 'all', 'candidate_regions')
    smallest_rectangle2 (CandReg, R, C, Phi, L1, L2)
    decode_bar_code_rectangle2 (Image, BHandle, 'EAN-13', R, C, Phi, \
                                L1, L2, Dec)
endif
```

## Result

The operator `DecodeBarCodeRectangle2` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBarCodeModel`,
`SetBarCodeParam`,
`SmallestRectangle2`

## Possible Successors

`GetBarCodeResult`,
`GetBarCodeObject`,
`ClearBarCodeModel`

## Alternatives

`FindBarCode`

## See also

`GenRectangle2`

## Module

Bar Code
