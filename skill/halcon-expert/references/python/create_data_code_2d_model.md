# create_data_code_2d_model (Operator)

## Name

`create_data_code_2d_model` — Create a model of a 2D code class.

## Signature

`def create_data_code_2d_model(symbol_type: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, str, float]]) -> HHandle`

## Description

The operator `create_data_code_2d_model` creates a
model for a certain class of 2D codes.
In *`data_code_handle`* the operator returns a handle to the 2D
2D code model, which is used for all further operations on the
2D code, like modifying the model, reading a symbol, or accessing
the results of the symbol search.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

**Supported symbol types**

The parameter *`symbol_type`* is used to determine the type of
2D codes to process.
Presently, six main types are supported:
*"Data Matrix ECC 200"*, *"QR Code"*, *"Micro QR Code"*,
*"PDF417"*, *"Aztec Code"*, and *"DotCode"*.
Additionally, four GS1 types are supported:
*"GS1 DataMatrix"*, *"GS1 QR Code"*,*"GS1 Aztec Code"*,
and *"GS1 DotCode"*.
Data Matrix codes of type ECC 000-140 are not supported.
For the QR Code the older Model 1 as well as the new Model
2 can be read. The PDF417 can be read in its conventional as well
as in its compact form ('Compact/Truncated PDF417'). The Aztec code can
be read in compact, full-range, and rune (see Annex E of
ISO/IEC 24778:2008 (E)) form.
The structure of the four GS1 symbologies is basically identical to
their non-GS1 counterparts - Data Matrix ECC 200, QR Code Aztec Code,
and DotCode, respectively.
In the following, all parameters, settings, and rules
applying to any particular 2D code type apply to its GS1 variant
as well. The GS1 symbologies enforce merely additional rules for the
format of the data carried by the codes. It has to be organized in so
called GS1 application element strings according to the GS1 General
Specifications.
To update the list of available GS1 Application Identifiers,
see the parameter *"gs1_syntax_dictionary"* in [`set_system`](set_system.md).

For all symbol types, the 2D code reader supports the Extended Channel
Interpretation (ECI) protocol. If the symbol contains an ECI code,
all characters with ASCII code 92 (backslash,
*"\"*) that occur in the normal data
stream are, in compliance with the standard, doubled
(*"\\"*) for the output.
This is necessary in order to distinguish data backslashes from the ECI
sequence *"\nnnnnn"*.

The information whether the symbol contains ECI codes (and consequently
doubled backslashes) or not is stored in the Symbology Identifier number
that can be obtained for every successfully decoded symbol with the help of
the operator [`get_data_code_2d_results`](get_data_code_2d_results.md) passing the generic parameter
*"symbology_ident"*. How the code number encodes additional
information about the symbology and the 2D code reader, like the ECI
support, is defined in the different symbology specifications.
For more information see the corresponding standards and the operator
[`get_data_code_2d_results`](get_data_code_2d_results.md).

The Symbology Indentifier code will not be preceded by the 2D code reader
to the output data, even if the symbol contains an ECI code.
If this is needed, e.g., by a subsequent processing unit, the
*"symbology_ident"* number (obtained by the operator
[`get_data_code_2d_results`](get_data_code_2d_results.md) with the parameter
*"symbology_ident"*) can be added to the data stream manually
together with the symbology flag and the symbol code: ']d', ']Q', ']L',
']z', or ']J' for DataMatrix codes, QR Codes, PDF417 Codes, Aztec Codes,
or DotCodes, respectively. In particular, for GS1 symbologies the parameter
*"symbology_ident"* returns 2 for GS1 DataMatrix, 3 for GS1 QR
Code, and 1 for GS1 Aztec Code and GS1 DotCode.
This corresponds to symbol codes:
']d2', ']Q3', ']z1', and ']J1', respectively.

**Standard default settings of the 2D code model**

The default settings of the model were chosen to read a
wide range of common symbols within a reasonable amount of time.
However, for runtime reasons some restrictions apply to the symbol
(see the following table).
If the model was modified (as described later), it is at any time
possible to reset it to these default settings by passing the generic
parameter *"default_parameters"* together with the value
*"standard_recognition"* to the operator
[`set_data_code_2d_param`](set_data_code_2d_param.md).

For some model parameters the default values depend on the chosen recognition
approach. Those parameters are listed in the table below.
Further parameter details and the remaining model parameters can be found in
the reference of [`set_data_code_2d_param`](set_data_code_2d_param.md).

|  |  |  |  |
| --- | --- | --- | --- |
| Model parameter | *"standard_recognition"* | *"enhanced_recognition"* | *"maximum_recognition"* |
| *"polarity"* | 'dark_on_light' (dark symbols on a light background) | 'any' (dark symbols on a light background and vice versa) | 'any' (dark symbols on a light background and vice versa) |
| *"contrast_min"* (Aztec Code, PDF417) | 30 | 10 | 10 |
| *"symbol_cols_min"*, *"symbol_cols_max"* (PDF417) | 1 ... 20 | 1 ... 30 | 1 ... 30 |
| *"symbol_rows_min"*, *"symbol_rows_max"* (PDF417) | 5 ... 45 | 3 ... 90 | 3 ... 90 |
| *"module_size_min"*, *"module_size_max"* (Aztec Code, Data Matrix ECC 200, Micro QR Code, QR Code) | 6 ... 20 pixels | 4 (2 for sharp images) ... 100 pixels | 4 (1 for sharp images) ... 100 pixels |
| *"module_size_min"*, *"module_size_max"* (DotCode) | 4 ... 100 pixels | 2 ... 100 pixels | 2 ... 100 pixels |
| *"module_width_min"*, *"module_width_max"* (PDF417) | 3 ... 15 pixels | 3 (2 for sharp images) ... 100 pixels | 3 (1 for sharp images) ... 100 pixels |
| *"module_aspect_min"*, *"module_aspect_max"* (PDF417) | 1 ... 4 | 1 ... 10 | 1 ... 10 |
| *"small_modules_robustness"* (All code types except DotCode) | 'low' | 'low' | 'high' |
| *"module_gap_max"* (Aztec Code) | 'small' (< 10% of the module size) | 'big' (< 50% of the module size) | 'big' (< 50% of the module size) |
| *"module_gap_max"* (Data Matrix ECC 200, Micro QR Code, QR Code) | 'no' | 'small' (< 10% of the module size) | 'big' (< 50% of the module size) |
| *"module_gap_max"* (DotCode) | 'no' | 'small' (< 10% of the module size) | 'small' (< 10% of the module size) |
| *"slant_max"* (Data Matrix ECC 200) | 0.1745 (10 degree) | 0.5235 (30 degree) | 0.5235 (30 degree) |
| *"module_grid"* (Data Matrix ECC 200) | 'fixed' | 'any' (fixed or variable) | 'any' (fixed or variable) |
| *"finder_pattern_tolerance"* (Aztec Code) | 'low' | 'high' | 'high' |
| *"finder_pattern_tolerance"* (Data Matrix ECC 200) | 'low' | 'low' | 'any' |
| *"alternating_pattern_tolerance"* (Data Matrix ECC 200) | 'low' | 'medium' | 'high' |
| *"contrast_tolerance"* (Data Matrix ECC 200, Micro QR Code, QR Code) | 'low' | 'low' | 'any' |
| *"candidate_selection"* (Data Matrix ECC 200) | 'default' | 'extensive' | 'extensive' |
| *"candidate_selection"* (DotCode, Micro QR Code, QR Code) | 'default' | 'extensive' | 'all' |
| *"position_pattern_min"* (QR Code) | 3 | 2 | 2 |
| *"model_type"* (QR Code) | 2 | 2 | 'any' |
| *"deformation_tolerance"* (Data Matrix ECC 200, QR Code) | 'low' | 'low' | 'curved' |

**Modify the 2D code model**

If it is known that the symbol does not or may not comply with all
of these restrictions (e.g., the symbol is brighter
than the background or the contrast is very low), or if first tests
show that some of the symbols cannot be read with the default
settings, it is possible to adapt single model parameters -
while others are kept to the default - or the whole model can
be extended in a single step by setting the generic parameter
*"default_parameters"* to the value
*"enhanced_recognition"*.
This will lead to a more general model that covers a wider range
of 2D code symbols.
However, the symbol search with such a general model is more
extensive, hence the runtime of the operator
[`find_data_code_2d`](find_data_code_2d.md) may increase significantly.
This is true especially in the following cases: *no*
readable 2D code is detected, the symbol is printed light on dark,
or the modules are very small.

By setting the generic parameter *"default_parameters"* to
the value *"maximum_recognition"* the model is further
extended in comparison to *"enhanced_recognition"*, so that
2D codes with very small module sizes can be decoded more robustly
(see *"small_modules_robustness"*). For the Data Matrix ECC 200,
the mode *"maximum_recognition"* differs from the
mode *"enhanced_recognition"* in a way that even symbols with
defect or partially occluded finder patterns can be read (see
*"finder_pattern_tolerance"*). Using this
mode may lead to a further increased runtime and memory usage
of the operator [`find_data_code_2d`](find_data_code_2d.md) during symbol search
and decoding.

For these reasons, the model should always be specified as exactly
as possible by setting all known parameters. The model parameters
can be set directly during the creation of the model or later with
the help of the operator [`set_data_code_2d_param`](set_data_code_2d_param.md). Both
operators provide the generic parameters *`gen_param_name`* and
*`gen_param_value`* for this purpose. For the Data Matrix ECC 200, for
example, the symbol size should be specified as exactly as possible
if the mode *"maximum_recognition"* was chosen. A detailed
description of all supported generic parameters can be found with
the operator [`set_data_code_2d_param`](set_data_code_2d_param.md).

Another way for adapting the model is to train it based on sample
images.
Passing the parameter *"train"* to the operator
[`find_data_code_2d`](find_data_code_2d.md) will cause the find operator to look
for a symbol, determine its parameters, and modify the model
accordingly.
More details can be found with the description of the operator
[`find_data_code_2d`](find_data_code_2d.md).

It is possible to query the model parameters with the operator
[`get_data_code_2d_param`](get_data_code_2d_param.md).
The names of all supported parameters for setting or querying the
model are returned by the operator [`query_data_code_2d_params`](query_data_code_2d_params.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`symbol_type`** (input_control)  string `→` str

Type of the 2D code.

Default:
"Data Matrix ECC 200"

List of values:
"Aztec Code", "Data Matrix ECC 200", "DotCode", "GS1 Aztec Code", "GS1 DataMatrix", "GS1 DotCode", "GS1 QR Code", "Micro QR Code", "PDF417", "QR Code"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of the generic parameters that can be
adjusted for the 2D code model.

Default:
[]

List of values:
"additional_levels", "candidate_selection", "contrast_min", "contrast_tolerance", "default_parameters", "deformation_tolerance", "finder_pattern_tolerance", "mirrored", "model_type", "module_aspect", "module_aspect_max", "module_aspect_min", "module_gap", "module_gap_max", "module_gap_min", "module_grid", "module_size", "module_size_max", "module_size_min", "module_width", "module_width_max", "module_width_min", "persistence", "polarity", "position_pattern_min", "slant_max", "small_modules_robustness", "strict_fp_and_qz", "strict_model", "strict_quiet_zone", "symbol_cols", "symbol_cols_max", "symbol_cols_min", "symbol_rows", "symbol_rows_max", "symbol_rows_min", "symbol_shape", "symbol_size", "symbol_size_max", "symbol_size_min", "timeout", "version", "version_max", "version_min"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, str, float]]

Values of the generic parameters that can be
adjusted for the 2D code model.

Default:
[]

Suggested values:
"standard_recognition", "enhanced_recognition", "maximum_recognition", "yes", "no", "any", "dark_on_light", "light_on_dark", "square", "rectangle", "small", "big", "fixed", "variable", "low", "high", "default", "extensive", "curved", "classic", "deep_learning", 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 30, 50, 70, 90, 12, 14, 16, 18, 20, 22, 24, 26, 32, 36, 40, 44, 48, 52, 64, 72, 80, 88, 96, 104, 120, 132, 144

**`data_code_handle`** (output_control)  datacode_2d `→` HHandle

Handle for using and accessing the 2D code model.

## Example (HDevelop)

```
* Two simple examples that show the use of create_data_code_2d_model
* to detect a Data Matrix ECC 200 code and a QR Code.

* (1) Create a model for reading simple QR Codes
*     (only dark symbols on a light background will be read)
create_data_code_2d_model ('QR Code', [], [], DataCodeHandle)
* Read an image
read_image (Image, 'datacode/qrcode/qr_workpiece_01')
* Read the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, [], [], \
                   ResultHandles, DecodedDataStrings)
* Clear the model
clear_data_code_2d_model (DataCodeHandle)

* (2) Create a model for reading a wide range of Data Matrix ECC 200 codes
*     (this model will also read light symbols on dark background)
create_data_code_2d_model ('Data Matrix ECC 200', 'default_parameters', \
                           'enhanced_recognition', DataCodeHandle)
* Read an image
read_image (Image, 'datacode/ecc200/ecc200_cpu_010')
* Read the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, [], [], \
                   ResultHandles, DecodedDataStrings)
* Clear the model
clear_data_code_2d_model (DataCodeHandle)
```

## Result

The operator `create_data_code_2d_model` returns the value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception is raised.

## Possible Successors

`set_data_code_2d_param`,
`find_data_code_2d`

## Alternatives

`read_data_code_2d_model`

## See also

`clear_data_code_2d_model`

## References

International Standard ISO/IEC 16022: “Information technology -
Automatic identification and data capture techniques -
Data Matrix bar code symbology specification”;
Reference number ISO/IEC 16022:2006 (E);
ISO/IEC 2006.  
  
International Standard ISO/IEC 15438: “Information technology -
Automatic identification and data capture techniques -
PDF417 bar code symbology specification”;
Reference number ISO/IEC 15438:2006 (E);
ISO/IEC 2006.  
  
International Standard ISO/IEC 18004: “Information technology -
Automatic identification and data capture techniques -
QR Code 2005 bar code symbology specification”;
Reference number ISO/IEC 18004:2006 (E);
ISO/IEC 2006.  
  
International Standard ISO/IEC 24778: “Information technology -
Automatic identification and data capture techniques -
Aztec Code bar code symbology specification”;
Reference number ISO/IEC 24778:2008 (E);
ISO/IEC 2008.  
  
GS1 General Specifications; Version 12; Issue 1, Jan-2012; GS1.

## Module

Data Code
