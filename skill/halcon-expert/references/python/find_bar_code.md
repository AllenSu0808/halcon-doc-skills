# find_bar_code (Operator)

## Name

`find_bar_code` — Detect and read bar code symbols in an image.

## Signature

`def find_bar_code(image: HObject, bar_code_handle: HHandle, code_type: MaybeSequence[str]) -> Tuple[HObject, Sequence[str]]`

`def find_bar_code_s(image: HObject, bar_code_handle: HHandle, code_type: MaybeSequence[str]) -> Tuple[HObject, str]`

## Description

The operator `find_bar_code` finds and reads bar code symbols in a
given image (*`image`*) and returns the decoded data. In one image
an arbitrary number of bar codes of a single type can be read. The type
of the desired bar code symbology is given by *`code_type`*. The
decoded strings are returned in *`decoded_data_strings`* and the
corresponding bar code regions in *`symbol_regions`*. For a total
of n successfully read bar codes, the indices from 0 to (n-1) can be
used as candidate handle in the operators [`get_bar_code_object`](get_bar_code_object.md)
and [`get_bar_code_result`](get_bar_code_result.md) in order to retrieve the desired data of
one specific bar code result.

Bar codes are expected to appear dark on a light background.
To read light bar codes on a dark background, invert the input image
using the operator [`invert_image`](invert_image.md) beforehand.

Before calling `find_bar_code` a bar code model must be created
by calling [`create_bar_code_model`](create_bar_code_model.md). This operator returns a bar code
model *`bar_code_handle`*, which is input to `find_bar_code`.

The output value *`decoded_data_strings`* contains the decoded string of
the symbol for each bar code result. The contents of the strings are conform
to the appropriate standard of the symbology. Typically,
*`decoded_data_strings`* contains only data characters. For bar codes
with a mandatory check character the check character is not included in
the string. For bar codes with an optional check character, like for
example Code 39, Codabar, 2/5 Industrial or 2/5 Interleaved, the result
depends on the value of the *"check_char"* parameter, which can
be set in [`create_bar_code_model`](create_bar_code_model.md), [`set_bar_code_param`](set_bar_code_param.md) or
[`set_bar_code_param_specific`](set_bar_code_param_specific.md):
The default setting of *"absent"* assumes that no check character
is present. In this case, no check is performed and all characters are
returned as data. When set to *"present"*, a check character is
expected and used to verify the correctness of the bar code. The bar code is
graded as unreadable if the check sum does not match. Accordingly, the symbol
region and the decoded string do not appear in the list of resulting strings
(*`decoded_data_strings`*) and in the list of resulting regions
(*`symbol_regions`*). The check character itself is stripped from the data.
If this stripping is undesired, the mode *"preserved"* allows to verify
the bar code while still keeping the check character in the data.

The underlying decoded reference data, including start/stop and check
characters, can be queried by using the [`get_bar_code_result`](get_bar_code_result.md)
operator with the option *"decoded_reference"*.

Following bar code symbologies are supported:

|  |  |  |
| --- | --- | --- |
| 2/5 Industrial | EAN-8 | GS1-128 |
| 2/5 Interleaved | EAN-8 Add-On 2 | GS1 DataBar Omnidirectional |
| Codabar | EAN-8 Add-On 5 | GS1 DataBar Truncated |
| Code 39 | EAN-13 | GS1 DataBar Stacked |
| Code 32 (converted from Code 39) | EAN-13 Add-On 2 | GS1 DataBar Stacked Omnidirectional |
| Code 93 | EAN-13 Add-On 5 | GS1 DataBar Limited |
| Code 128 | UPC-A | GS1 DataBar Expanded |
| MSI | UPC-A Add-On 2 | GS1 DataBar Expanded Stacked |
| PharmaCode | UPC-A Add-On 5 |  |
|  | UPC-E |  |
|  | UPC-E Add-On 2 |  |
|  | UPC-E Add-On 5 |  |

Note that the PharmaCode can be read in forward and backward direction,
both yielding a valid result. Therefore, both strings are returned and
concatenated into a single string in *`decoded_data_strings`* by a
separating comma.

Note that the GS1 DataBar bar codes may contain an additional composite
code component.
To find and decode this component, set the parameter
*"composite_code"* to *"CC-A/B"* using the operator
[`set_bar_code_param`](set_bar_code_param.md).

Note that also a bar code of type 'Code 32' can be read by using
`find_bar_code` with *`code_type`* set to *"Code 39"*
in combination with the external procedure
`convert_decoded_string_code39_to_code32`.

The list of available GS1 Application Identifiers can be updated using
[`set_system`](set_system.md) (see the parameter *"gs1_syntax_dictionary"*).

**Autodiscrimination**

Autodiscrimination describes the simultaneous decoding of multiple bar code
types in one call of `find_bar_code`. For this purpose a tuple of
bar code types is specified for the parameter *`code_type`*. Using the
generic value *"auto"* all known bar code types are decoded - except
*"PharmaCode"* and *"MSI"* because these codes don't have enough
features to be reliably
separated from other bar code types. The tuple can also contain bar code
types with the tilde prefix (~)
which won't be decoded. For example
*["auto", "~EAN-8", "~EAN-8 Add-On 2", "~EAN-8 Add-On 5"]*
describes all bar code types without *"PharmaCode"*, *"MSI"* and
all kinds of *"EAN-8"*.
Please note that each additionally allowed bar code type increases the
run-time of the
operator. Using too many bar code types the reliability of the decoding
could decrease because not all bar code types can be discriminated
reliably. To improve autodiscrimination compatibility bar codes
with a check character or check sum should be used.

The bar code reader tries to decode the bar code types in the following
order:

*"GS1 DataBar Omnidir"*, *"GS1 DataBar Truncated"*,
*"GS1 DataBar Limited"*, *"GS1 DataBar Expanded"*,
*"GS1 DataBar Expanded Stacked"*,
*"GS1 DataBar Stacked Omnidir"*, *"GS1 DataBar Stacked"*,
*"GS1-128"*, *"Code 128"*, *"EAN-13 Add-On 5"*,
*"EAN-13 Add-On 2"*, *"EAN-13"*, *"UPC-A Add-On 5"*,
*"UPC-A Add-On 2"*, *"UPC-A"*, *"EAN-8 Add-On 5"*,
*"EAN-8 Add-On 2"*, *"EAN-8"*, *"UPC-E Add-On 5"*,
*"UPC-E Add-On 2"*, *"UPC-E"*, *"Code 93"*,
*"Code 39"*, *"Codabar"*, *"2/5 Interleaved"*,
*"2/5 Industrial"*

Therefore you should exclude at least all definitely not occurring
bar code types that are scanned before the first of the bar code types you
expect to find or, better, just scan for the explicit list of bar code types
you expect.

Note that *"UPC-A"* codes have the same structure as
*"EAN-13"* codes, except that they always start with a zero.
If one wants to read *"UPC-A"*, *"UPC-A Add-On 2"*, or
*"UPC-A Add-On 5"* codes explicitly, then the corresponding EAN-13
bar code type must be excluded (*"EAN-13"*,
*"EAN-13 Add-On 2"*, or *"EAN-13 Add-On 5"*, respectively).
Otherwise, the results will be returned as EAN codes because of the
decoding order. For UPC-A codes with Add-On, *"EAN-13"* must be
excluded in addition to the corresponding EAN-13 type with Add-On.

Especially for the autodiscrimination there is the operator
[`set_bar_code_param_specific`](set_bar_code_param_specific.md). With it some parameters of the bar code
model can be set specifically for certain bar code types.

**Training**

If the bar code reader is in training mode, the operator
`find_bar_code` executes a training cycle. The training mode
is described with the operator [`set_bar_code_param`](set_bar_code_param.md).

**Timeout and Abort**

The operator `find_bar_code` can be aborted by a timeout and
dynamically. With the operator [`set_bar_code_param`](set_bar_code_param.md) you can specify a
timeout. If `find_bar_code` reaches this timeout, it returns all codes
decoded so far. Alternatively, you can call [`set_bar_code_param`](set_bar_code_param.md) with
*"abort"* from another thread to abort `find_bar_code`
dynamically.

The information whether the operator was aborted or not can be queried by
calling [`get_bar_code_result`](get_bar_code_result.md) with the parameter *"aborted"*.

Furthermore, the operator `find_bar_code` can be canceled, which
means no result is returned but instead an error is returned. This can be done
with the operator [`set_operator_timeout`](set_operator_timeout.md) or [`interrupt_operator`](interrupt_operator.md).
If `find_bar_code` is canceled by [`set_operator_timeout`](set_operator_timeout.md),
H_ERR_TIMEOUT (9400) is returned. If `find_bar_code` is
canceled by [`interrupt_operator`](interrupt_operator.md), H_ERR_CANCEL (22) is returned.
Note: Both mentioned operators are only supported in cancel mode.

**Advice on low resolution bar code imaging systems**

This advice applies to bar code applications that use low resolution images,
i.e., images in which a single bar is between 0.6 and 2 pixels wide.

In these cases, one should optimize the bar code imaging system in order to
eliminate noise and focal blur because a combination of these optical
distortions lead to problems in the decodability of low resolution bar codes.

See [`set_bar_code_param`](set_bar_code_param.md) documentation entry on
*"small_elements_robustness"* for more advice.

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

Input image. If the image has a reduced domain, the
bar code search is reduced to that domain.
This usually reduces the runtime of the operator.
However, if the bar code is not fully inside the domain,
the bar code cannot be decoded correctly.

**`symbol_regions`** (output_object)  region(-array) `→` HObject

Regions of the successfully decoded bar code symbols.

**`bar_code_handle`** (input_control, state is modified)  barcode `→` HHandle

Handle of the bar code model.

**`code_type`** (input_control)  string(-array) `→` MaybeSequence[str]

Type of the searched bar code.

Default:
"auto"

List of values:
"2/5 Industrial", "2/5 Interleaved", "Codabar", "Code 128", "Code 39", "Code 93", "EAN-13 Add-On 2", "EAN-13 Add-On 5", "EAN-13", "EAN-8 Add-On 2", "EAN-8 Add-On 5", "EAN-8", "GS1 DataBar Expanded Stacked", "GS1 DataBar Expanded", "GS1 DataBar Limited", "GS1 DataBar Omnidir", "GS1 DataBar Stacked Omnidir", "GS1 DataBar Stacked", "GS1 DataBar Truncated", "GS1-128", "MSI", "PharmaCode", "UPC-A Add-On 2", "UPC-A Add-On 5", "UPC-A", "UPC-E Add-On 2", "UPC-E Add-On 5", "UPC-E", "auto"

**`decoded_data_strings`** (output_control)  string(-array) `→` Sequence[str]

Data strings of all successfully decoded bar codes.

## Example (HDevelop)

```
* Small example for aborting bar code search:
read_image (Image, 'barcode/ean13/tea_box_10.png')

* Decode normally:
create_bar_code_model ([], [], BarCodeHandle)
find_bar_code (Image, SymbolRegions, BarCodeHandle, 'auto', \
    DecodedDataStrings)
stop ()

* Start bar code search in separate thread.
par_start<ThreadID>: find_bar_code (Image, SymbolRegions1, BarCodeHandle, \
    'auto', DecodedDataStrings1)

* Let some time pass.
wait_seconds (0.002)

* Abort the 2D code search.
set_bar_code_param (BarCodeHandle, 'abort', 'true')

* Wait for the thread, it should finish very fast.
par_join(ThreadID)

* We can determine that the search in fact was aborted.
get_bar_code_result (BarCodeHandle, 'all', 'aborted', Aborted)
```

## Result

The operator `find_bar_code` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Predecessors

`create_bar_code_model`,
`set_bar_code_param`

## Possible Successors

`get_bar_code_result`,
`get_bar_code_object`,
`clear_bar_code_model`

## Alternatives

`decode_bar_code_rectangle2`

## Module

Bar Code
