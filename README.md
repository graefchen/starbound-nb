# starbound-nb

Just me doing some playing around with [py-starbound](https://github.com/blixt/py-starbound) and jupyter notebooks.

## Commands

```nushell
ls *.json | get name | each {|x| let name = (open $x | get identity | get species); print $"($x) : ($name)"}
```
