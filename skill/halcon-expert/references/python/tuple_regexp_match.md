# tuple_regexp_match (Operator)

## Name

`tuple_regexp_match` — Extract substrings using regular expressions.

## Signature

`def tuple_regexp_match(data: MaybeSequence[str], expression: MaybeSequence[str]) -> Sequence[str]`

`def tuple_regexp_match_s(data: MaybeSequence[str], expression: MaybeSequence[str]) -> str`

## Description

`tuple_regexp_match` applies the regular expression in
*`expression`* to one or more input strings in *`data`*, and
in each case returns the first matching substring in *`matches`*.
Normally, one output string is returned for each input string, the output
string being empty if no match was found. However, if the regular
expression contains capturing groups (see below), the behavior depends
on the number of input strings: If there is only a single input string,
the result is a tuple of all captured submatches.
If there are multiple input strings, the output strings represent
the matched pattern of the first capturing group.

A summary of regular expression syntax is provided here. Basically,
each character in the regular expression represents a literal to match,
except for the following symbols which have a special meaning
(the described syntax is compatible with Perl):

|  |  |
| --- | --- |
| $\^{}$ | Matches start of string |
| `$` | Matches end of string (a trailing newline is allowed) |
| `.` | Matches any character except newline |
| `[...]` | Matches any character literal listed in the brackets.   If the first character is a `'`$\^{}$`'`, this matches any character except those in the list. You can use the `'-'` character as in `[A-Z0-9]` to select character ranges. Other characters lose their special meaning in brackets, except `'`$\$`'`. Within these brackets it is possible to use the following POSIX character classes (note that the additional brackets are needed):   `[:alnum:]` ![figure](../assets/6d92ad96c194b4f8.svg) alphabetic and numeric characters   `[:alpha:]` ![figure](../assets/6d92ad96c194b4f8.svg) alphabetic characters   `[:blank:]` ![figure](../assets/6d92ad96c194b4f8.svg) space and tab   `[:cntrl:]` ![figure](../assets/6d92ad96c194b4f8.svg) control characters   `[:digit:]` ![figure](../assets/6d92ad96c194b4f8.svg) digits   `[:graph:]` ![figure](../assets/6d92ad96c194b4f8.svg) non-blank (like spaces or control characters)   `[:lower:]` ![figure](../assets/6d92ad96c194b4f8.svg) lowercase alphabetic characters   `[:print:]` ![figure](../assets/6d92ad96c194b4f8.svg) like `[:graph:]` but including spaces   `[:punct:]` ![figure](../assets/6d92ad96c194b4f8.svg) punctuation characters   `[:space:]` ![figure](../assets/6d92ad96c194b4f8.svg) all whitespace characters (`[:blank:]`, newline, ...)   `[:upper:]` ![figure](../assets/6d92ad96c194b4f8.svg) uppercase alphabetic characters   `[:xdigit:]` ![figure](../assets/0f8e322aa1b0286d.svg) digits allowed in hexadecimal numbers (0-9a-fA-F). |
| `*` | Allows 0 or more repetitions of preceding literal or group |
| `+` | Allows 1 or more repetitions of preceding literal or group |
| `?` | Allows 0 or 1 repetitions of preceding literal or group |
| $\texttt{\{n,m\}}$ | Allows `n` to `m` repetitions of preceding literal or group |
| $\texttt{\{n\}}$ | Allows exactly `n` repetitions of preceding literal or group |
| `|` | Separates alternative matching expressions |
| `()` | Groups a subpattern and creates a capturing group.   The substrings captured by this group will be stored separately.   `(?: )` ![figure](../assets/6d92ad96c194b4f8.svg) Groups a subpattern without creating a capturing group   `(?= )` ![figure](../assets/6d92ad96c194b4f8.svg) Positive lookahead (requested condition right to the match)   `(?! )` ![figure](../assets/6d92ad96c194b4f8.svg) Negative lookahead (forbidden condition right to the match)   `(?<= )` ![figure](../assets/0f8e322aa1b0286d.svg) Positive lookbehind (requested condition left to the match)   `(?<! )` ![figure](../assets/0f8e322aa1b0286d.svg) Negative lookbehind (forbidden condition left to the match) |
| $\$ | Escapes any special symbol to treat it as a literal.   *Attention:* Some host languages like HDevelop and C/C++ already use the backslash as a general escape character. In this case, *"\."* matches a literal dot while *"\\"* matches a literal backslash. Furthermore, there are some special codes:   $\texttt{\d}$ Matches a digit (Negation: $\texttt{\D}$)   $\texttt{\w}$ Matches a letter, digit or underscore (Negation: $\texttt{\W}$)   $\texttt{\s}$ Matches a white space character (Negation: $\texttt{\S}$)   $\texttt{\b}$ Matches a word boundary (Negation: $\texttt{\B}$) |

The repeat quantifiers listed in the table above are greedy by default,
i.e., they attempt to maximize the length of the
match. Appending `'?'` attempts to find a minimal
match, e.g., `'+?'`.

If the specified expression is syntactically incorrect, you will
receive an error stating that the value of control parameter 2 is
wrong. Additional details are displayed in a message box if
`set_system('do_low_error', 'true')` is set and in
HDevelop's Output Console.

Furthermore, you can set some options by passing a string tuple for
*`expression`*. In this case, the first element is used as the
expression, and each additional element is treated as an option.

- *"ignore_case"*:
  Perform case-insensitive matching
- *"multiline"*:
  `'`$\^{}$`'` and
  `'$'` match
  start and end of individual lines
- *"dot_matches_all"*:
  Allow the `'.'` character to also match newlines
- *"newline_lf"*, *"newline_crlf"*, *"newline_cr"*:
  Specify the encoding of newlines in the input data.
  The default is LF on all systems (even though in Windows files
  usually CRLF is used as line break, when reading a file into memory
  the read operators return for every line break just
  `'`$\texttt{\n}$`'`,
  which is the same as LF).

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

If the input parameter *`data`* is an empty tuple, the operator returns
an empty tuple. If *`expression`* is an empty tuple,
an exception is raised.

### Unicode code points versus bytes

Regular expression matching operates on Unicode code points. One Unicode
code point may be composed of multiple bytes in the UTF-8 string.
If regular expression matching should only match on bytes, this operator can
be switched to byte mode with
`set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_regexp_match`,
which can be used in an expression in the following syntax:

[`Matches := regexp_match(Data, Expression)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`data`** (input_control)  string(-array) `→` MaybeSequence[str]

Input strings to match.

**`expression`** (input_control)  string(-array) `→` MaybeSequence[str]

Regular expression.

Default:
".*"

Suggested values:
".*", "ignore_case", "multiline", "dot_matches_all", "newline_lf", "newline_crlf", "newline_cr"

**`matches`** (output_control)  string(-array) `→` Sequence[str]

Found matches.

## Example (HDevelop)

```
tuple_regexp_match ('abba', 'a*b*', Result)
* Returns 'abb'

tuple_regexp_match ('abba', 'b*a*', Result)
* Returns 'a'

tuple_regexp_match ('abba', 'b+a*', Result)
* Returns 'bba'

tuple_regexp_match ('abba', '.a', Result)
* Returns 'ba'

tuple_regexp_match ('abba', '[ab]*', Result)
* Returns 'abba'

tuple_regexp_match (['img123','img124'], 'img(.*)', Result)
* Returns ['123','124']

tuple_regexp_match ('mydir/img001.bmp', 'img(.*)\\.(.*)', Result)
* Returns ['001','bmp']
```

## Alternatives

`tuple_strstr`

## See also

`tuple_regexp_replace`,
`tuple_regexp_test`,
`tuple_regexp_select`

## References

Perl Compatible Regular Expressions (PCRE), http://www.pcre.org/

## Module

Foundation
