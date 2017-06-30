# readme

Add a user with access to mechanical turk (full access, not read only) at [the aws iam page][]

~You'll need to run `pip3 install boto3` (which requires `pip3`, which comes automatically with `python 3.4` and newer (as of this commit it's at `3.6.1` or something)).~

Use `pip3` to install all of the relevant dependencies with `pip3 install -r requirements.txt`

If you have `homebrew` but not `python 3.4` or newer (which automatically comes with `pip3`),
`brew install python3` should get you going.

you also may want to install the [aws cli][].
You'll want to set environment variables `AMT_key` and `AMT_secret`.
You can, instead, pass these values as command line arguments,
but then those credentials will show up in your shell history
(usually a file like `.bash_history` or `.zsh_history`),
which is not great.

See [here][credential leaking is bad] (and [here][another story] and [here][yet another story] and [here][a fourth story]) for why it's bad to let your Amazon credentials end up anywhere, and it can happen really easily, so it's good practice to

1. Make sure any API keys you generate have only the access to your account that you definitely want (and no more).
That means your API keys for Mechanical Turk can't spin up EC2 instances and mine bitcoins or something, racking up thousands of dollars in charges; and
2. Make sure that your API keys are stored in some place that's reasonably secure. For my money, I have things in a file like
`~/.environment_variables` and tell my bash config file (`~/.zshrc` or `~/.bashrc` or `~/.bash_profile`) to `source ~/.environment_variables`, bringing all of the relevant things into my environment.

if you're using `homebrew`
(which, if you're running OS X or macOS, I would strongly encourage),
you may want to run `brew install awscli` to automate some stuff a little more easily.


## Contributing
I really need people to contribute to this:

- Find things that are confusing or poorly documented and add comments to the code.
- Find things that are broken and fix them (or create an issue and document it)
- Think of commands that you'd like to be able to run and either implement them and make a pull request,
*or* make an issue requesting some feature be implemented (and someone will (hopefully) go and implement it).

If you have any questions, please feel free to contact me ([@alialkhatib][github maintainer])

[the aws iam page]: https://aws.amazon.com/iam/
[aws cli]: https://aws.amazon.com/cli/
[credential leaking is bad]: http://bgr.com/2017/04/10/amazon-hack-third-party-fraud-fake/
[another story]: https://thenextweb.com/security/2017/06/02/amazon-web-services-leak-data-aws/
[yet another story]: https://wptavern.com/ryan-hellyers-aws-nightmare-leaked-access-keys-result-in-a-6000-bill-overnight
[a fourth story]: https://www.theregister.co.uk/2015/01/06/dev_blunder_shows_github_crawling_with_keyslurping_bots/
[github maintainer]: https://github.com/alialkhatib