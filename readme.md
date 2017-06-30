# readme

Add a user with access to mechanical turk (full access, not read only) at [the aws iam page][]

You'll need to run `pip3 install boto3` (which requires `pip3`, which comes automatically with `python 3.4` and newer (as of this commit it's at `3.6.1` or something)).
If you have `homebrew`, `brew install python3` should get you set up.

you may want to install the [aws cli][].
You'll want to set environment variables `AMT_key` and `AMT_secret`.
You can, instead, pass these values as command line arguments,
but then those credentials will show up in your shell history
(usually a file like `.bash_history` or `.zsh_history`),
which is not great.

if you're using `homebrew`
(which, if you're running OS X or macOS, I would strongly encourage),
you may want to run `brew install awscli` to automate some stuff a little more easily.

[the aws iam page]: https://aws.amazon.com/iam/
[aws cli]: https://aws.amazon.com/cli/


## Contributing
I really need people to contribute to this:

- Find things that are confusing or poorly documented and add comments to the code.
- Find things that are broken and fix them (or create an issue and document it)
- Think of commands that you'd like to be able to run and either implement them and make a pull request,
*or* make an issue requesting some feature be implemented (and someone will (hopefully) go and implement it).

If you have any questions, please feel free to contact me (@alialkhatib)