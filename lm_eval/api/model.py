import abc

from lm_eval import utils


class LM(abc.ABC):
    def __init__(self):
        """Defines the interface that should be implemented by all LM subclasses.
        LMs are assumed to take text (strings) as input and yield strings as output
        (inputs/outputs should be tokenization-agnostic.)

        """

    @abc.abstractmethod
    def loglikelihood(self, requests):
        """Compute log-likelihood of generating a continuation from a context.
        Downstream tasks should attempt to use loglikelihood instead of other
        LM calls whenever possible.

        :param requests: list
            A list of pairs (context, continuation)
            context: str
                Context string. Implementations of LM must be able to handle an
                empty context string.
            continuation: str
                The continuation over which log likelihood will be calculated. If
                there is a word boundary, the space should be in the continuation.
                For example, context="hello" continuation=" world" is correct.
        :return: list
            A list of pairs (logprob, isgreedy)
            logprob: float
                The log probability of `continuation`
            isgreedy:
                Whether `continuation` would be generated by greedy sampling from `context`
        """
        pass

    @abc.abstractmethod
    def loglikelihood_rolling(self, requests):
        """Compute full log-likelihood of a string, with no truncation, for perplexity computation
        - We will use the full max context length of the model.
        - For inputs that exceed the max context length, we divide the tokenized string into chunks of up to
        the max context length.
        - IMPORTANT: Each document's loglikelihood/perplexity is computed *separately*, unlike other implementations
          which may simply concatenate multiple documents together.
        - IMPORTANT: We maximize the amount of context for each prediction. Specifically, for inputs that we break into
          multiple chunks, the last input will still a full-sized context.
          Example:
            Input tokens: [ 0 1 2 3 4 5 6 7 8 9 ]
            Prefix: EOT
            Max context length: 4
            Resulting input/prediction pairs:

                INPUT:  EOT   0   1   2
                PRED:     0   1   2   3

                INPUT:    3   4   5   6
                PRED:     4   5   6   7

                INPUT:    5   6   7   8
                PRED:             8   9

          Observe that:
            1. Each token is predicted exactly once
            2. For the last pair, we provide the full context, but only score the last two tokens

        :param requests: list
            A list of strings
            string: str
                String for which we are computing per-token loglikelihood
        :return: list
            A list of pairs (logprob, isgreedy)
            logprob: float
                The log probability of `continuation`
            isgreedy:
                Whether `continuation` would be generated by greedy sampling from `context`
        """
        pass

    # TODO: Add an optional max length
    @abc.abstractmethod
    def greedy_until(self, requests):
        """Generate greedily until a stopping sequence

        :param requests: list
            A list of pairs (context, until)
            context: str
                Context string
            until: [str]
                The string sequences to generate until. These string sequences
                may each span across multiple tokens, or may be part of one token.
        :return: list
            A list of strings continuation
            continuation: str
                The generated continuation.
        """
        pass

    @classmethod
    def create_from_arg_string(cls, arg_string, additional_config=None):
        additional_config = {} if additional_config is None else additional_config
        args = utils.simple_parse_args_string(arg_string)
        args2 = {k: v for k, v in additional_config.items() if v is not None}
        return cls(**args, **args2)
