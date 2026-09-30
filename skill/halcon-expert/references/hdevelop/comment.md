# comment (Operator)

## Name

`comment` — Add a comment of one line to the program.

## Signature

`comment( : : Comment : )`

## Description

`comment` allows to add a comment of one line to the program.
As parameter value, i.e., as comment, all characters are allowed.
If the operator window is used to enter a comment and if there are
newlines in the comment line parameter, one comment statement for every
text line is inserted.

In the full text editor a comment is marked by entering an asterisk
(*'*'*) as first non-whitespace character.

This operator has no effect on the program execution.

## Parameters

**`Comment`** (input_control)  string `→`  (string)

Arbitrary sequence of characters.

## Example (HDevelop)

```
* This is a program with comments
* 'this is a string as comment'
* here are numbers: 4711, 0.815
stop ()
```

## Result

`comment` is never executed.

## Module

Foundation
