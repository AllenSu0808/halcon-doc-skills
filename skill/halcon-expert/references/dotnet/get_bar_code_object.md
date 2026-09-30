# GetBarCodeObject (Operator)

## Name

`GetBarCodeObject` — Access iconic objects that were created during the search or decoding of
bar code symbols.

## Signature

`static void HOperatorSet.GetBarCodeObject(out HObject barCodeObjects, HTuple barCodeHandle, HTuple candidateHandle, HTuple objectName)`

`HObject HBarCode.GetBarCodeObject(HTuple candidateHandle, string objectName)`

`HObject HBarCode.GetBarCodeObject(string candidateHandle, string objectName)`

## Description

With the operator `GetBarCodeObject`, iconic objects created
during the last call of the operator [`FindBarCode`](find_bar_code.md) can be accessed.
Besides the name of the object (*`objectName`*), the bar code model
(*`barCodeHandle`*) must be passed to `GetBarCodeObject`.
In addition, in *`candidateHandle`* an index to a single decoded
symbol or a single symbol candidate must be passed. Alternatively,
*`candidateHandle`* can be set to *"all"* and then all
objects of the decoded symbols or symbol candidates are returned.

Depending on the option selected in *`objectName`* parameter
the following objects are returned:

- ***"symbol_regions"*:** —

  The regions of successfully decoded symbols are returned. When
  choosing *"all"* as *`candidateHandle`*, the regions
  of all decoded symbols are retrieved. The order of the returned
  objects is the same as in [`FindBarCode`](find_bar_code.md).
- ***"candidate_regions"*:** —

  The regions of potential bar codes are returned. If there is a
  total of n decoded symbols out of a total of m candidates then
  *`candidateHandle`* can be chosen between 0 and (m-1). With
  *`candidateHandle`* between 0 and (n-1) the original
  segmented region of the respective decoded symbol is retrieved.
  With *`candidateHandle`* between n and (m-1) the region
  of the potential or undecodable symbol is returned. In addition,
  *`candidateHandle`* can be set to *"all"* to retrieve
  all candidate regions at the same time.
- ***"scanlines_all"*,
  *"scanlines_valid"*,
  *"scanlines_identical"*,
  *"scanlines_all_plain"*,
  *"scanlines_valid_plain"*,
  *"scanlines_identical_plain"*,
  *"scanlines_merged_edges"*:** —

  XLD contours representing the particular detected bars in the
  scanlines applied on the candidate regions are returned. Note that
  the scanlines can only be returned if the bar code was decoded
  by [`FindBarCode`](find_bar_code.md) or [`DecodeBarCodeRectangle2`](decode_bar_code_rectangle2.md) in
  *"persistence"* mode (see
  [`SetBarCodeParam`](set_bar_code_param.md) for further details).

  *"scanlines_all"* represents all scanlines that
  [`FindBarCode`](find_bar_code.md) could potentially create in order to decode a bar
  code.

  *"scanlines_valid"* represents only those scanlines that
  could be successfully decoded. The number of scanlines that has to
  be valid can be adjusted with [`SetBarCodeParam`](set_bar_code_param.md) with the
  parameter *"min_identical_scanlines"*.
  There will be no *"scanlines_valid"*
  if the symbol was not decoded. For stacked bar codes (e.g.,
  *"GS1 DataBar Stacked"* and
  *"GS1 DataBar Expanded Stacked"*) this rule applies similarly,
  but on a per-symbol-row basis rather then per-symbol.

  *"scanlines_identical"* shows a subset of *"scanlines_valid"*,
  defined by the scanlines which were needed to reach
  *"min_identical_scanlines"* (see [`SetBarCodeParam`](set_bar_code_param.md)).
  For stacked codes, more scanlines might be returned than specified via
  *"min_identical_scanlines"*. This originates from
  the decoding algorithm actually used for this kind of codes.

  *"scanlines_merged_edges"* shows
  the scanlines and edges which were used for the merged scanlines
  (see *"merge_scanlines"* in [`SetBarCodeParam`](set_bar_code_param.md)).

  `GetBarCodeObject` returns each scanline as separate XLD
  contour. Please note that the XLD contours returned by
  *"scanlines_all"*, *"scanlines_valid"*,
  *"scanlines_identical"* and *"scanlines_merged_edges"* are
  meant for visualization purposes and hence consist of many XLD points.
  Double lines are used between edges that the bar
  code reader recognized as bar, whereas single lines are used for white
  spaces. Additional information about each scanline can be obtained
  with [`GetBarCodeResult`](get_bar_code_result.md) with the parameter *"status"*.

  The *'_plain'* variants *"scanlines_all_plain"*,
  *"scanlines_identical_plain"* and *"scanlines_valid_plain"*
  return the described scanlines in a plain format. Every edge found is
  returned as a point of a XLD contour. For every scanline a new XLD contour
  is created. Scanlines for which no edges could be found are omitted.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`barCodeObjects`** (output_object)  object(-array) `→` [HObject](HObject.md)

Objects that are created as intermediate results
during the detection or evaluation of bar codes.

**`barCodeHandle`** (input_control)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

**`candidateHandle`** (input_control)  integer `→` [HTuple](HTuple.md) (*string* / int / long)

Indicating the bar code results respectively candidates
for which the data is required.

Default:
"all"

Suggested values:
0, 1, 2, "all"

**`objectName`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Name of the iconic object to return.

Default:
"candidate_regions"

List of values:
"candidate_regions", "scanlines_all", "scanlines_all_plain", "scanlines_identical", "scanlines_identical_plain", "scanlines_merged_edges", "scanlines_valid", "scanlines_valid_plain", "symbol_regions"

## Result

The operator `GetBarCodeObject` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct and the requested objects are
available for the last symbol search.
Otherwise, an exception will be raised.

## Possible Predecessors

`FindBarCode`

## See also

`GetBarCodeResult`

## Module

Bar Code
