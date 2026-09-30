# TupleString (Operator)

## Name

`TupleString` — Convert a tuple into a tuple of strings.

## Signature

`static void HOperatorSet.TupleString(HTuple t, HTuple format, out HTuple stringVal)`

`HTuple HTuple.TupleString(HTuple format)`

## Description

`TupleString` converts numbers into strings or modifies strings.
The operator has two parameters: *`t`* is the number or string
that has to be converted. *`format`* specifies the conversion.

In the following, first some examples for the use of
`TupleString` are given and then, the structure of the
*`format`* string is explained in detail.

**Examples**

Examples for the conversion of numbers into strings:

|  |  |  |
| --- | --- | --- |
| *`t`* (Input) | *`format`* (Input) | *`stringVal`* (Output) |
| 23 | '10.2f' | '         23.00' |
| 23 | '-10.2f' | '23.00         ' |
| 4 | '.7f' | '4.0000000' |
| 1234.56789 | '+10.3f' | ' +1234.568' |
| 255 | 'x' | 'ff' |
| 255 | 'X' | 'FF' |
| 0xff | '.5d' | '00255' |

Examples for the modification of strings:

|  |  |  |
| --- | --- | --- |
| *`t`* (Input) | *`format`* (Input) | *`stringVal`* (Output) |
| 'total' | '10s' | '       total' |
| 'total' | '-10s' | 'total       ' |
| 'total' | '-10.3s' | 'tot          ' |

**Format string**

The *`format`* string consists of the following four parts:

```
      <flags><field width>.<precision><conversion characters>
```

- **`flags`** —

  Zero or more flags, in any
  order, which modify the meaning of the conversion specification.
  Flags may consist of the following characters:

  - **`-`** —

    The result of the conversion is
    left justified within the field.
  - **`+`** —

    The result of a signed conversion
    always begins with a sign, `+` or `-`.
  - **<`space`>** —

    If the first
    character of a signed conversion is not a sign, a space character is
    prefixed to the result. This means that if the space flag
    (<`space`>) and `+` flag both appear,
    the space flag is ignored.
  - **`#`** —

    The value is to be converted to
    an “alternate form”. For `d` and `s` conversions,
    this flag has no effect. For `o` conversion (see below), it
    increases the precision to force the first digit of the result to be
    a zero. For `x` or `X` conversion (see below), a non-
    zero result has `0x` or `0X` prefixed to it. For
    `e`, `E`, `f`, `g`, and `G`
    conversions, the result always contains a radix character, even if
    no digits follow the radix character. For `g` and `G`
    conversions, trailing zeros are not removed from the result,
    contrary to usual behavior.
  - **`0`** —

    The value should be zero padded. For
    `d`, `o`, `u`, `x`, `X`,
    `e`, `E`, `f`, `F`, `g`,
    and `G` conversions, the converted value
    is padded on the left with zeros rather than blanks. If the `0`
    and `-` flags both appear, the `0` flag is ignored.
    If a precision is given with a numeric conversion (`d`,
    `o`, `u`, `x`, and `X`), the `0`
    flag is ignored. For other conversions, the behavior is undefined.
- **`field width`** —

  An optional
  string of decimal digits to specify a minimum field width. For an
  output field, if the converted value has fewer characters than the
  field width, it is padded on the left (or right, if the
  left-adjustment flag, - has been given) to the field width.
- **`precision`** —

  The precision
  specifies the minimum number of digits to appear for the `d`,
  `o`, `x`, or `X` conversions (the field is
  padded with leading zeros), the number of digits to appear after the
  radix character for the `e` and `f` conversions, the
  maximum number of significant digits for the `g` conversion,
  or the maximum number of characters to be printed from a string in
  `s` conversion. The precision takes the form of a period
  `.` followed by a decimal digit string. A null digit string
  is treated as a zero.
- **`conversion characters`** —

  A conversion character indicates the
  type of conversion to be applied:

  - **`d,u,o,x,X`** —

    The integer argument
    is printed in signed decimal (`d`), unsigned decimal
    (`u`), unsigned octal (`o`),
    or unsigned hexadecimal notation (`x` and
    `X`). The `x` conversion uses the numbers and letters
    `0123456789abcdef`, and the `X` conversion uses the
    numbers and letters `0123456789ABCDEF`. The precision
    component of the argument specifies the minimum number of digits to
    appear. If the value being converted can be represented in fewer
    digits than the specified minimum, it is expanded with leading
    zeroes. The default precision is 1. The result of converting a
    zero value with a precision of 0 is no characters.
  - **`f`** —

    The floating-point number argument
    is printed in decimal notation in the style `[-]dddrddd`,
    where the number of digits after the radix character, `r`, is
    equal to the precision specification. If the precision is omitted
    from the argument, six digits are output; if the precision is
    explicitly 0, no radix appears.
  - **`e,E`** —

    The floating-point-number
    argument is printed in the style `[-]d.ddde`±`dd`,
    where there is one digit before the radix character, and the number
    of digits after it is equal to the precision. When the precision is
    missing, six digits are produced; if the precision is 0, no radix
    character appears. The `E` conversion character produces a
    number with `E` introducing the exponent instead of
    `e`. The exponent always contains at least two digits.
    However, if the value to be printed requires an exponent greater
    than two digits, additional exponent digits are printed as
    necessary.
  - **`g,G`** —

    The floating-point-number
    argument is printed in style `f` or `e` (or in style
    `E` in the case of a `G` conversion character), with
    the precision specifying the number of significant digits. The
    style used depends on the value converted; style `e` is used
    only if the exponent resulting from the conversion is less than -4
    or greater than or equal to the precision. Trailing zeros are
    removed from the result. A radix character appears only if it is
    followed by a digit.
  - **`s`** —

    The argument is taken to be a
    string, and characters from the string are printed until the end of
    the string or the number of characters indicated by the precision
    specification of the argument is reached. If the precision is
    omitted from the argument, it is interpreted as infinite and all
    characters up to the end of the string are printed.
  - **`b`** —

    Similar to the `s`
    conversion specifier, except that the string can contain
    backslash-escape sequences which are then converted to the
    characters they represent.

  In no case does a nonexistent or insufficient field width cause
  truncation of a field; if the result of a conversion is wider than
  the field width, the field is simply expanded to contain the
  conversion result.

### Exception: Empty input tuple

If any of the input tuples is empty, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleString`,
which can be used in an expression in the following syntax:

[`String := T $ Format`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Input tuple.

**`format`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Format string.

**`stringVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple converted to strings.

## Example (HDevelop)

```
*
* '     23.00'
tuple_string (23, '10.2f', String)
String := 23$'10.2f'
*
* '23.00     '
tuple_string (23, '-10.2f', String)
String := 23$'-10.2f'
*
* '4.0000000'
tuple_string (4, '.7f', String)
String := 4$'.7f'
*
* ' +1234.568'
tuple_string (1234.56789, '+10.3f', String)
String := 1234.56789$'+10.3f'
*
* 'ff'
tuple_string (255, 'x', String)
String := 255$'x'
*
* 'FF'
tuple_string (255, 'X', String)
String := 255$'X'
*
* '00255'
tuple_string (0xff, '.5d', String)
String := 0xff$'.5d'
*
* '     total'
tuple_string ('total', '10s', String)
String := 'total'$'10s'
*
* 'total     '
tuple_string ('total', '-10s', String)
String := 'total'$'-10s'
*
* 'tot       '
tuple_string ('total', '-10.3s', String)
String := 'total'$'-10.3s'
```

## Alternatives

`TupleSub`

## Module

Foundation
