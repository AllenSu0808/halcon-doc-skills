# do_ocr_single_class_cnn (Operator)

## Name

`do_ocr_single_class_cnn` — Classify a single character with an CNN-based OCR classifier.

## Signature

`def do_ocr_single_class_cnn(character: HObject, image: HObject, ocrhandle: HHandle, num: Sequence[int]) -> Tuple[Sequence[str], Sequence[float]]`

`def do_ocr_single_class_cnn_s(character: HObject, image: HObject, ocrhandle: HHandle, num: Sequence[int]) -> Tuple[str, float]`

## Description

`do_ocr_single_class_cnn` computes the best classification for the
character given by the region *`character`*
and the gray values *`image`* with the OCR classifier
*`ocrhandle`* and returns the best *`num`* classes in
*`class`* and the corresponding confidences (probabilities) of the
classes in *`confidence`*. Because multiple classes may be returned by
`do_ocr_single_class_cnn`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`do_ocr_multi_class_cnn`](do_ocr_multi_class_cnn.md) must
be used.

In most cases, [`do_ocr_multi_class_cnn`](do_ocr_multi_class_cnn.md) should be preferred over
`do_ocr_single_class_cnn`, since [`do_ocr_multi_class_cnn`](do_ocr_multi_class_cnn.md) is
typically faster than a loop with `do_ocr_single_class_cnn`.
Furthermore, the resulting confidences can be interpreted as
probabilities. They indicate the uncertainty of a character's classification
result. The operator `do_ocr_single_class_cnn` has to be used if the
nth-best class has to be examined explicitly for n greater than one.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`class`* signifies that the region has been classified as rejection
class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` HObject

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values of the character.

**`ocrhandle`** (input_control)  ocr_cnn `→` HHandle

Handle of the OCR classifier.

**`num`** (input_control)  integer-array `→` Sequence[int]

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`class`** (output_control)  string(-array) `→` Sequence[str]

Result of classifying the character with the
CNN.

**`confidence`** (output_control)  real(-array) `→` Sequence[float]

Confidence(s) of the class(es) of the character.

## Example (HDevelop)

```
read_image(Image, 'bottle2')
OffsetRow := 100
OffsetCol := 108
read_ocr_class_cnn('Universal_0-9_NoRej.occ', OCRHandle)
* Select each digit and use do_ocr_single_class_cnn to apply OCR
gen_rectangle1(ROI_Date, OffsetRow, OffsetCol, OffsetRow, OffsetCol)
for I := 1 to 6 by 1
  Offset := I % 2 * 10
  smallest_rectangle1(ROI_Date, Row1, Col1, Row2, Col2)
  gen_rectangle1(ROI_Date, OffsetRow, Offset + Col2, OffsetRow + 42, \
  Col2 + Offset + 31)
  do_ocr_single_class_cnn(ROI_Date, Image, OCRHandle, 1, Class, Confidence)
endfor
```

## Result

If the parameters are valid, the operator
`do_ocr_single_class_cnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_ocr_class_cnn`

## Alternatives

`do_ocr_multi_class_cnn`

## Module

OCR/OCV
