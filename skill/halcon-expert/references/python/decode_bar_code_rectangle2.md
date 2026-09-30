# decode_bar_code_rectangle2 (Operator)

## Name

`decode_bar_code_rectangle2` — Decode bar code symbols within a rectangle.

## Signature

`def decode_bar_code_rectangle2(image: HObject, bar_code_handle: HHandle, code_type: MaybeSequence[str], row: MaybeSequence[Union[int, float]], column: MaybeSequence[Union[int, float]], phi: MaybeSequence[Union[int, float]], length_1: MaybeSequence[Union[int, float]], length_2: MaybeSequence[Union[int, float]]) -> Sequence[str]`

`def decode_bar_code_rectangle2_s(image: HObject, bar_code_handle: HHandle, code_type: MaybeSequence[str], row: MaybeSequence[Union[int, float]], column: MaybeSequence[Union[int, float]], phi: MaybeSequence[Union[int, float]], length_1: MaybeSequence[Union[int, float]], length_2: MaybeSequence[Union[int, float]]) -> str`

## Description

The operator `decode_bar_code_rectangle2` uses the bar code
model specified by *`bar_code_handle`* to decode a bar code at
a given position within the image *`image`*.
*`bar_code_handle`* must be created with
[`create_bar_code_model`](create_bar_code_model.md), its parameters can be set with
[`set_bar_code_param`](set_bar_code_param.md). The position of the bar code is given
as an arbitrarily oriented rectangle. Contrary to
[`find_bar_code`](find_bar_code.md), where the decoding is preceded by a time
consuming search for candidate regions,
`decode_bar_code_rectangle2` scans the provided region directly
for bar codes. The rectangular region is defined by the parameters
*`row`* and *`column`* for the center, *`phi`* for
the orientation and *`length_1`* and *`length_2`* for the
half edge lengths (see [`gen_rectangle2`](gen_rectangle2.md)). The angle *`phi`*
also determines the reading direction and is defined as the angle
between the reading direction of the bar code and the horizontal
image axis. The angle is positive in counter clockwise direction and
is given in radians as in [`gen_rectangle2`](gen_rectangle2.md). Note that the angle
unit deviates from the conventions in [`get_bar_code_result`](get_bar_code_result.md) and
[`set_bar_code_param`](set_bar_code_param.md) where angles are given in degrees.
*`phi`* can be in the range of
$[-\pi,+\pi]$.
The reading direction is perpendicular to the bars of the bar code.
Bar codes with a reading direction
$\texttt{Phi}+\pi$ are also returned.
Multiple regions for decoding can be given by supplying tuples for
*`row`*, *`column`*, *`phi`*, *`length_1`* and
*`length_2`*.

The rectangle should cover completely the bar code and the quiet zones.
Regions that are too big will be decoded, if there is no disturbing
pattern within these regions and the height (*`length_2`*) is
small enough such that scanlines can be placed sufficiently dense.
Rectangles that are too short in reading direction (*`length_1`*)
cannot be decoded.

`decode_bar_code_rectangle2` can be used if the position of
the bar code is already known in advance. For example, the candidate
regions found by [`find_bar_code`](find_bar_code.md) and [`get_bar_code_object`](get_bar_code_object.md)
could be reused with a different code type (see the following example).

Multiple bar code types can be specified for *`code_type`*. See
section Autodiscrimination for [`find_bar_code`](find_bar_code.md).

Further aspects of the actual decoding are explained with the operator
[`find_bar_code`](find_bar_code.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator supports canceling timeouts and interrupts.

This operator modifies the state of the following input parameter:

- bar_code_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte)

Input image.

**`bar_code_handle`** (input_control, state is modified)  barcode `→` HHandle

Handle of the bar code model.

**`code_type`** (input_control)  string(-array) `→` MaybeSequence[str]

Type of the searched bar code.

Default:
"EAN-13"

List of values:
"2/5 Industrial", "2/5 Interleaved", "Codabar", "Code 128", "Code 39", "Code 93", "EAN-13 Add-On 2", "EAN-13 Add-On 5", "EAN-13", "EAN-8 Add-On 2", "EAN-8 Add-On 5", "EAN-8", "GS1 DataBar Expanded Stacked", "GS1 DataBar Expanded", "GS1 DataBar Limited", "GS1 DataBar Omnidir", "GS1 DataBar Stacked Omnidir", "GS1 DataBar Stacked", "GS1 DataBar Truncated", "GS1-128", "MSI", "PharmaCode", "UPC-A Add-On 2", "UPC-A Add-On 5", "UPC-A", "UPC-E Add-On 2", "UPC-E Add-On 5", "UPC-E", "auto"

**`row`** (input_control)  rectangle2.center.y(-array) `→` MaybeSequence[Union[int, float]]

Row index of the center.

Default:
50.0

**`column`** (input_control)  rectangle2.center.x(-array) `→` MaybeSequence[Union[int, float]]

Column index of the center.

Default:
100.0

**`phi`** (input_control)  rectangle2.angle.rad(-array) `→` MaybeSequence[Union[int, float]]

Orientation of rectangle in radians.

Default:
0.0

Suggested values:
0.0, 0.785398, 1.570796, 3.1415926

**`length_1`** (input_control)  rectangle2.hwidth(-array) `→` MaybeSequence[Union[int, float]]

Half of the length of the rectangle along the reading
direction of the bar code.

Default:
200.0

**`length_2`** (input_control)  rectangle2.hheight(-array) `→` MaybeSequence[Union[int, float]]

Half of the length of the rectangle perpendicular to
the reading direction of the bar code.

Default:
100.0

**`decoded_data_strings`** (output_control)  string(-array) `→` Sequence[str]

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

The operator `decode_bar_code_rectangle2` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_bar_code_model`,
`set_bar_code_param`,
`smallest_rectangle2`

## Possible Successors

`get_bar_code_result`,
`get_bar_code_object`,
`clear_bar_code_model`

## Alternatives

`find_bar_code`

## See also

`gen_rectangle2`

## Module

Bar Code
