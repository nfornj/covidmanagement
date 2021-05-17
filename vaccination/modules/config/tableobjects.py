

def stateobject(statename):

    from vaccination.models import Andaman_and_nicobar_islands,States,Districts,Andhra_Pradesh,Arunachal_Pradesh
    
    if statename=='Andaman and Nicobar Islands':
    
        andaman_and_nicobar_islands=Andaman_and_nicobar_islands()

        return andaman_and_nicobar_islands

    if statename=='Andhra Pradesh':
    
        andhra_Pradesh=Andhra_Pradesh()

        return andhra_Pradesh
    
    if statename=='Arunachal Pradesh':
    
        arunachal_Pradesh=Arunachal_Pradesh()

        return arunachal_Pradesh


def districtobject():
    from vaccination.models import Districts

    districts = Districts()

    return districts



                        