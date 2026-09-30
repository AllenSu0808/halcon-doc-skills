## 2D Code

List of Operators ↓

This chapter contains operators for reading 2D codes.

### Concept of reading 2D codes

2D code symbols are a special kind of two-dimensional patterns that
encode text and numbers. HALCON is able to read the most popular 2D
codes: Data Matrix ECC 200, QR Code, Micro QR Code, Aztec Code, PDF417,
and DotCode. Except for DotCodes all these codes contain a finder pattern
and a data pattern. The finder pattern is used to locate the pattern of
the symbol and get basic information about the geometric properties,
e.g., the orientation of the symbol. The data pattern contains the code
itself and consists of multiple dots, bars, or small squares,
the so-called modules. Because of the special design of the codes,
they can be decoded even if some parts are disturbed.

![figure](../assets/c28432163551dda0.svg)

Reading a 2D code of type PDF417. This image is from the example
program 2d_data_codes_default_settings.hdev.

In the following, the steps that are required to read 2D codes are
described briefly.

- **Create 2D code model:** —

  First, a 2D code model must be created using

  - [`CreateDataCode2dModel`](create_data_code_2d_model.md).

  This model provides the reader with all necessary information about the
  structure of the code. For normal printed codes only the name needs to be
  provided and HALCON will select suitable default parameters. For special
  cases, you can modify the model parameters either when creating the 2D
  code model or in a later step to adapt the model to a particular symbol
  appearance.
- **Modify the model parameters for non-standard codes:** —

  Using the default parameters, the 2D code reader is able to read a wide
  range of codes. For non-standard codes the parameters can be modified using

  - [`SetDataCode2dParam`](set_data_code_2d_param.md).

  Here, you can either select an enhanced set of default parameters using the
  generic parameter *`"default_parameters"`*, e.g., with the value
  *`"enhanced_recognition"`*, or you specify the parameter values
  separately to adapt the model optimally to the conditions of the used print
  style. Note that [`QueryDataCode2dParams`](query_data_code_2d_params.md) can be used to query the
  parameters that are valid for the specific 2D code type. To obtain the
  currently set values of parameters, [`GetDataCode2dParam`](get_data_code_2d_param.md) can be
  used.

  Instead of modifying the model parameters manually, you can also let HALCON
  train the model using

  - [`FindDataCode2d`](find_data_code_2d.md)

  with the generic parameter *`"train"`*. Then, HALCON will search for the
  best parameters needed to extract the given code. It is recommended to apply
  this to multiple example images to ensure that all variations are covered.
- **Read 2D code:** —

  The 2D code is located and its content is decoded using

  - [`FindDataCode2d`](find_data_code_2d.md).

  The operator returns for every successfully decoded symbol the surrounding
  XLD contour, a handle to a result structure, which contains additional
  information about the symbol as well as about the search and decoding
  process, and the string that is encoded in the symbol. With the result
  handles and the operators [`GetDataCode2dResults`](get_data_code_2d_results.md) and
  [`GetDataCode2dObjects`](get_data_code_2d_objects.md), additional data about the extraction
  process can be accessed that can be used both for process analysis and for
  displaying. In particular, [`GetDataCode2dResults`](get_data_code_2d_results.md) allows to access
  several alphanumerical results that were calculated while searching and
  reading the symbols and [`GetDataCode2dObjects`](get_data_code_2d_objects.md) allows to access
  iconic objects that were created during the last call of
  [`FindDataCode2d`](find_data_code_2d.md).

### Further operators

In addition to the operators mentioned above,
[`WriteDataCode2dModel`](write_data_code_2d_model.md) allows to write the model into a file that
can be used later to create (e.g., in a different application) an identical
copy of the model. Such a model copy is created directly by
[`ReadDataCode2dModel`](read_data_code_2d_model.md) (without calling
[`CreateDataCode2dModel`](create_data_code_2d_model.md)). Furthermore, you can use
[`SerializeDataCode2dModel`](serialize_data_code_2d_model.md) and
[`DeserializeDataCode2dModel`](deserialize_data_code_2d_model.md) to serialize and deserialize the 2D
2D code model.

### Glossary

- **2D code symbol** —

  Two-dimensional graphical symbol that encodes
  characters and numbers. It is constructed by dark and light dots, bars, or
  small squares that are called modules. There are different types of 2D
  codes. Two common types are the so-called stacked codes and the so-called
  matrix codes.
- **stacked code** —

  Type of 2D code symbol that contains a stack of 1D
  bar codes arranged in rows and columns. To ensure that the complete stack of
  1D bar codes is processed, the symbol contains a start and a stop
  pattern. Additionally, the symbol is framed by a quiet zone.
- **matrix code** —

  Type of 2D code symbol that uses graphical patterns
  consisting of dark and light modules arranged in two dimensions. The symbol
  consists of three components: a finder pattern, a data pattern, and a quiet
  zone.
- **modules** —

  Dark and light dots, bars, or small squares
  that are used to build a 2D code symbol.
- **quiet zone** —

  Homogeneous frame around the symbol's border that makes the
  symbol better distinguishable from the background or from other objects in
  the image.
- **finder pattern** —

  Pattern that is used to find the symbol and its
  orientation in the image. The pattern differs depending on the used 2D code
  type.

### Further Information

See also the `“Solution Guide Basics”` and the
`“Solution Guide on 2D Codes”` for further details
about 2D codes.

---

#### List of Operators

- [`ClearDataCode2dModel`](clear_data_code_2d_model.md) — Delete a 2D code model and free the allocated memory.

- [`CreateDataCode2dModel`](create_data_code_2d_model.md) — Create a model of a 2D code class.

- [`DeserializeDataCode2dModel`](deserialize_data_code_2d_model.md) — Deserialize a serialized 2D code model.

- [`FindDataCode2d`](find_data_code_2d.md) — Detect and read 2D code symbols in an image or
  train the 2D code model.

- [`GetDataCode2dObjects`](get_data_code_2d_objects.md) — Access iconic objects that were created during the search for
  2D code symbols.

- [`GetDataCode2dParam`](get_data_code_2d_param.md) — Get one or several parameters that describe the 2D code model.

- [`GetDataCode2dResults`](get_data_code_2d_results.md) — Get the alphanumerical results that were accumulated during the
  search for 2D code symbols.

- [`QueryDataCode2dParams`](query_data_code_2d_params.md) — Get for a given 2D code model the names of the generic
  parameters or objects that can be used in the other 2D code
  operators.

- [`ReadDataCode2dModel`](read_data_code_2d_model.md) — Read a 2D code model from a file and create a new model.

- [`SerializeDataCode2dModel`](serialize_data_code_2d_model.md) — Serialize a 2D code model.

- [`SetDataCode2dParam`](set_data_code_2d_param.md) — Set selected parameters of the 2D code model.

- [`WriteDataCode2dModel`](write_data_code_2d_model.md) — Writes a 2D code model into a file.
