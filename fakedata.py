import collections
import faker

class FakeData:

    def __init__(self,*args,**kwargs):
        self.fake_record = faker.Faker(*args,**kwargs)
        self.PREDEFINED = {
                            'company': {
                                'Record ID' : 'uuid4',
                                'Company': 'company',
                                'Address': 'street_address',
                                'City' : 'city',
                                'State' : 'state',
                                'Zipcode' : 'zipcode',
                                'Country' : 'country'
                            }
                        }

    def generate_data(self, n:int = 1000, fields = 'company') -> pd.DataFrame:
        '''Function that generate fake data and returns a pandas DataFrame

        TODO: The generated data is completely random and makes no sense.
        The fields are not logically consistent.

        Parameters
        ----------
        n: int, default = 1000
            Number of records with fake data to be generated

        fields: dict, str, default = 'company'
            A dictionary of Field name - Faker object function that generates the
            data for that field can be provided. Alternatively, a string value
            that refers to a prefdefined set of mappings. The ones that are currently
            supported are {'company'}

        Returns
        -------
        fade_df: pd.DataFrame
        '''

        if isinstance(fields, str):
            assert fields in self.PREDEFINED, f"{fields} is not a predefined template"
            fields = self.PREDEFINED[fields]

        assert isinstance(fields,collections.abc.Mapping) , "Custom templates must be dicts (mappings in general)"
        records = [{key: getattr(self.fake_record, value)() for key, value in fields.items()} for record in range(n)]
        return pd.DataFrame(records), records
