'''
This module contains the main code for the deadringer module.
'''
import typing

class NosiyData:
    '''This defines the data that is supposed to contain the data with noise
    added to it. Noisy data is added as addtional rows rather than mutating
    the orginal DataFrame.

    Parameters
    ----------
    data: pd.DataFrame
        The input pandas DataFrame that contains the clean input data
    '''

    def __init__(data: pd.DataFrame):
        self.raw_data = data
        self.noisy_data = self.raw_data.copy()

    def __repr__():
        return self.noisy_data

    def perturb(probabilities: typing.Dict[str,typing.Any[str,float]]):
        '''Function that takes in a dictionary of perturbation probabilities as
        input (these values refer to the probabilities of transposition,
        substitution, insertion etc) for each field. The supported probabilities
        are:-

        - selection: Probability of selecting a field for introducing one or
                     more modifications (set this to 0.0 if no modifications
                     should be introduced into this field ever). Note: The sum
                     of these select probabilities over all defined fields must
                     be 1. The default for this will be computed based on the
                     values provided for the other fields. For instance, if
                     FIELD_A has a selection probability of 0.8 and FIELD_B has
                     a selection probability of 0.1, then if FIELD_C has no
                     assigned selection probability, then the default is
                     1 - (0.8 + 0.1) = 0.1. If another field, FIELD_D, also
                     has no selection probability, then the assigned probability,
                     then the default is (1 - (0.8 + 0.1))/2 = 0.05, ie:- the
                     remaining probability mass is split evenly between the two
                     fields. TODO: Instead of avergaing, would it be possible to
                     share based on the base rates from the literature?

        - misspelling: Probability of swapping an original value with a randomly
                       chosen misspelling from the corresponding misspelling
                       dictionary (can only be set to larger than 0.0 if such a
                       misspellings dictionary is defined for the given field).
                       TODO: Decide the API for misspellings dictionary.

        - insertion: Probability of inserting a character into a field value.
        - deletion: Probability of deleting a character from a field value.
        - substitution: Probability of substituting a character in a field value
                        with another character.
        - transposition: Probability of transposing two characters in a field
                         value.
        - swap_fields: Probability of swapping the value in a field with another
                       (randomly selected) value for this field. TODO: Are some
                       fields more liable to be swapped rather than others?
                       FirstName-LastName swaps might be more probable than
                       swapping names with addresses.
        - space_insertion: Probability of inserting a space into a field value
                           (thus splitting a word).

        Parameters
        ----------
        probabilities: Dict[str,float]
            A dict with a the kind of perturbation and the probability as
            key-value pairs. A `field` key with the name of the column whose
            values are to be modified is mandatory.

        Examples
        --------
        >>> df = pd.DataFrame({'uid': [1,2], 'name': ['Tom', 'Jerry']})
        >>> noisy_df = NoisyData(df)
        >>> nosiy_df.perturb({'field': 'name', 'selection': 0.5})
        '''
        pass
