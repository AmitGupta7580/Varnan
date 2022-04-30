from ..ctf import CTF


class CTFD(CTF):
    def convert_to_tree(self):
        """
        Convert CTF class to XML Tree
        """
        return super().convert_to_tree("CTFD")

    def extract(self):
        """
        Extract CTF information from CTFD Platform url
        """
        pass

    @staticmethod
    def platform_check(url):
        """
        Check if the provided CTF url hosted on CTFD platform
        """
        if url:
            return True
        return False
