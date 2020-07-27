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
        substitution, insertion etc) for each field.

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
