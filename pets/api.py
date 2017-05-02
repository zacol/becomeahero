"""
Battlenet API:  https://dev.battle.net/io-docs
"""

import requests

class Api(object):
    """
    An easy-to-use Python wrapper for the pets Battlenet API.
    """

    base_url = 'https://us.api.battle.net/wow/pet/'
    api_key = 'your-api-key'
    locale = 'en_US'

    def master_list(self):
        """
        A list of all supported battle and vanity pets.
        """

        params = {'apikey': self.api_key, 'locale': self.locale}
        request = requests.get(self.base_url, params=params)
        pets = request.json()
        pets_list = pets['pets']
        return pets_list

    def species(self, species_id):
        """
        This provides the data about an individual pet species.
        """

        url = [self.base_url, 'species/', species_id]
        params = {'apikey': self.api_key, 'locale': self.locale}
        request = requests.get(''.join(url), params=params)
        species = request.json()
        return species

    def ability(self, ability_id):
        """
        This provides data about a individual battle pet ability ID.
        """

        url = [self.base_url, 'ability/', ability_id]
        params = {'apikey': self.api_key, 'locale': self.locale}
        request = requests.get(''.join(url), params=params)
        ability = request.json()
        return ability
