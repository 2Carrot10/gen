Gen is an Ollama wrapper in python. 
This repo contains a number of improvement over the default `ollama` command:
* Abstracted server architecture

This command automatically manages server starting and stopping. You no longer need to worry about starting the Ollama server to just send a single prompt. If Ollama is already enabled, however, this command will automatically use that server instead of starting a new one. 
* Piping support

In line with Unix philosophy, this command can be composed with other commands very easily.
The command can read from STDIN, command line arguments, or both at the same time. 
Because of this, you can use `gen` in conjunction with other commands.
For example, use this command to summarize a man page:

* Completion support

Use the `--append` flag, this command will add the response on to the prompt in STDOUT. This makes it super easy to auto complete your code.
* Quoting

Use the `--quote` flag to format the response as a quote. The quote format is based on neorg.
