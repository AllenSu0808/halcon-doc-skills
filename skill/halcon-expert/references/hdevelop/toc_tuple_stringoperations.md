## String Operations

List of Operators ↓

This chapter contains operators for string operations.

### General Information

The HALCON library encodes strings in UTF-8 by default.

UTF-8 is a Unicode character encoding that can encode all Unicode code points
with one to four bytes.
'Unicode' refers to the character set that assigns each character of a string
to a code point (for example, 'U + 0041' for 'A'). UTF-8 then translates the
Unicode code points into binary data.
The memory requirement for all ASCII characters is usually 1 byte.
Certain characters, such as German umlauts, or Greek and Cyrillic characters
require 2 bytes. Asian characters occupy up to 4 bytes per character.

By default, the HALCON string operators work on the basis of Unicode code
points. That is, accessing a character of a string always returns the
corresponding Unicode code point of the character,
regardless of how many bytes are needed to represent the code point in UTF-8.
Thus, multi-byte characters, such as Asian characters or German umlauts can be
uniformly translated on all systems. Please note that the Unicode standard
also allows you to assemble printable characters from multiple code points
(using so-called 'Combining Diacritical Marks').
This is currently not fully supported by HALCON: in HALCON, the code points are
processed separately, and when strings are compared, equivalent characters are
not set equal if coded with different code points.

If there are compatibility problems during execution of older programs, the
string encoding of the HALCON library can be changed from *`'utf8'`* to
*`'locale'`* (legacy mode).
Then strings are stored depending on the locale and the string operators work –
as in previous versions of HALCON – not characterwise but bytewise.
If bytewise character processing is also required in UTF-8 mode, the operator
[`set_system`](set_system.md) can be used to set the option
*`'tuple_string_operator_mode'`* from *`'codepoint'`* to *`'byte'`*.
Afterwards, the string operators no longer work on the basis of code points.
The byte sequence of a string can be interesting for debugging, for example.

---

#### List of Operators

- [`tuple_environment`](tuple_environment.md) — Read one or more environment variables.

- [`tuple_join`](tuple_join.md) — Join strings using separator symbol(s).

- [`tuple_regexp_match`](tuple_regexp_match.md) — Extract substrings using regular expressions.

- [`tuple_regexp_replace`](tuple_regexp_replace.md) — Replace a substring using regular expressions.

- [`tuple_regexp_select`](tuple_regexp_select.md) — Select tuple elements matching a regular expression.

- [`tuple_regexp_test`](tuple_regexp_test.md) — Test if a string matches a regular expression.

- [`tuple_split`](tuple_split.md) — Split strings into substrings using predefined separator symbol(s).

- [`tuple_str_distance`](tuple_str_distance.md) — Calculate the distance between strings.

- [`tuple_str_first_n`](tuple_str_first_n.md) — Cut the first characters up to position “n” out of a string tuple.

- [`tuple_str_last_n`](tuple_str_last_n.md) — Cut all characters starting at position “n” out of a string tuple.

- [`tuple_str_replace`](tuple_str_replace.md) — Replace all occurrences of a substring within a string.

- [`tuple_strchr`](tuple_strchr.md) — Forward search for characters within a string tuple.

- [`tuple_strlen`](tuple_strlen.md) — Determine the length of every string within a tuple of strings.

- [`tuple_strrchr`](tuple_strrchr.md) — Backward search for characters within a string tuple.

- [`tuple_strrstr`](tuple_strrstr.md) — Backward search for strings within a string tuple.

- [`tuple_strstr`](tuple_strstr.md) — Forward search for strings within a string tuple.

- [`tuple_substr`](tuple_substr.md) — Cut characters from position “n1” through “n2” out of a string tuple.
