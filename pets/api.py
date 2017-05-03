"""
Battlenet API:  https://dev.battle.net/io-docs
"""

import requests

class Api(object):
    """
    An easy-to-use Python wrapper for the pets Battlenet API.
    """

    def __init__(self, base_url='https://us.api.battle.net/wow/pet/',
                 api_key='your-api-key', locale='en_US'):
        """
        Api constructor.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.locale = locale

    def __fetch_data(self, url_extras=None):
        """
        Prepare url and make request.
        """

        if url_extras is None:
            url_extras = []

        url = ''.join([self.base_url] + url_extras)
        params = {'apikey': self.api_key, 'locale': self.locale}
        request = requests.get(url, params=params)
        return request.json()

    def master_list(self):
        """
        A list of all supported battle and vanity pets.
        """

        pets = self.__fetch_data()
        pets_list = pets['pets']
        return pets_list

    def species(self, species_id):
        """
        This provides the data about an individual pet species.
        """

        species = self.__fetch_data(['species/', species_id])
        return species

    def ability(self, ability_id):
        """
        This provides data about a individual battle pet ability ID.
        """

        ability = self.__fetch_data(['ability/', ability_id])
        return ability
