## Bar Code

List of Operators ↓

This chapter provides an introduction to bar codes and the most important
terms used when finding and reading bar codes in HALCON.

### Structure of linear (1D) bar codes

A bar code consists of several dark bars and bright spaces.
For every bar code there is a smallest possible element,
the narrowest possible bar or the narrowest possible space, which is called
module.
In general, the width of the bars and spaces is different,
but always a multiple of the module.
Several bars and spaces together form a pattern.
This pattern encodes a symbol defined in a decoding table.
The conventions how such a binary pattern encodes a symbol
and the corresponding decoding table lead to the respective bar code type.
In addition to the patterns encoding the symbols, there are also patterns with
special tasks. Depending on the type there are further patterns which can or
must be part of the bar code:

- Quiet-zone: Zone in which no edges may occur.
  This zone is required before the start character and after the stop
  character to find the code.

  ![figure](../assets/b56efe6ad64bde2d.svg)

  Schematic representation of the quiet zone (orange) by means of an
  example bar code of type Code 128.
- Start and stop pattern: Define start, stop and direction.
  These patterns make it possible to read and decode the code from left to
  right as well as from right to left (and thus upside down).

  ![figure](../assets/004a864718a1da51.svg)

  Schematic representation of the start and stop pattern (orange) by means
  of an example bar code of type Code 128.
- Checksum: A digit which serves as a security check to ensure the code
  has been read correctly.

  ![figure](../assets/5e5d55155f18c5c6.svg)

  Schematic representation of the checksum (orange) by means of an example
  bar code of type Code 128.
- Guard pattern: Specific pattern, which can occur on the left, right, or
  in the center as additional symbol.

  ![figure](../assets/9a4df5b6480fd841.svg)

  Schematic representation of a guard pattern (orange) by means of an
  example bar code of type UPC-A.
- Finder patterns: Pattern used to locate the symbol.

  ![figure](../assets/5307740dd6cbaea6.svg)

  Schematic representation of a finder pattern (orange) by means of an
  example bar code of type GS1 Databar.
- Add-on symbol: Additional symbols for encoding of supplementary
  information. These symbols are encoded as bar codes with restricted length.

  ![figure](../assets/0948146204c36890.svg)

  Schematic representation of an add-on symbol (orange) by means of an
  example bar code of type EAN-8 Add-On 2.

### Structure of a composite bar code

Composite bar codes consist of the following elements:

- Linear bar code: As described above.
- 2D Code: For more information about 2D codes we refer to the
  `“Solution Guide II-C - 2D Codes”`.
- Linking pattern: Combines the two codes mentioned before.

The following figure shows a schematic representation of a composite bar code.

![figure](../assets/5a1cb9fbaa86ce60.svg)

Schematic representation of a composite bar code by means of an example
bar code of type UPC-A Composite:
Linear bar code (black), 2D code (light blue), and the linking pattern
(orange).

### Reading of a bar code

To be able to read a bar code in an image, it must be found first.
The regions in which HALCON assumes a bar code are called candidates.

To read a candidate, different lines are laid through the region,
called scanlines.
Although theoretically a single scanline would be sufficient, one tries to
decode the bar code along all scanlines.
This increases the chance of decoding the code correctly.
In addition, several successfully decoded scanlines allow additional
plausibility checks, i.e., reading several scanlines equally
decreases the chance of false positives.

![figure](../assets/47288afeb806622c.svg)

Schematic representation of different scanlines of a candidate.
Certain scanlines were read successfully (green),
while the reading failed for others (red).

The workflow and various examples showing how to read bar codes in HALCON
can be found in the `` “`Solution Guide I - Basics ``.

---

#### List of Operators

- [`clear_bar_code_model`](clear_bar_code_model.md) — Delete a bar code model and free the allocated memory

- [`create_bar_code_model`](create_bar_code_model.md) — Create a model of a bar code reader.

- [`decode_bar_code_rectangle2`](decode_bar_code_rectangle2.md) — Decode bar code symbols within a rectangle.

- [`deserialize_bar_code_model`](deserialize_bar_code_model.md) — Deserialize a bar code model.

- [`find_bar_code`](find_bar_code.md) — Detect and read bar code symbols in an image.

- [`get_bar_code_object`](get_bar_code_object.md) — Access iconic objects that were created during the search or decoding of
  bar code symbols.

- [`get_bar_code_param`](get_bar_code_param.md) — Get one or several parameters that describe the bar code model.

- [`get_bar_code_param_specific`](get_bar_code_param_specific.md) — Get parameters that are used by the bar code reader when processing a
  specific bar code type.

- [`get_bar_code_result`](get_bar_code_result.md) — Get the alphanumerical results that were accumulated during the
  decoding of bar code symbols.

- [`query_bar_code_params`](query_bar_code_params.md) — Get the names of the parameters that can be used in set_bar_code* and
  get_bar_code* operators for a given bar code model

- [`read_bar_code_model`](read_bar_code_model.md) — Read a bar code model from a file and create a new model.

- [`serialize_bar_code_model`](serialize_bar_code_model.md) — Serialize a bar code model.

- [`set_bar_code_param`](set_bar_code_param.md) — Set selected parameters of the bar code model.

- [`set_bar_code_param_specific`](set_bar_code_param_specific.md) — Set selected parameters of the bar code model for selected bar code types

- [`write_bar_code_model`](write_bar_code_model.md) — Write a bar code model to a file.
