# Biblioteka funkcji używanych przez autogena 
def f_turboglob_data():
    ret = "A TURBOGLOBULATOR is a device that converts crude oil or its fractions tiny molecules "
    "mixed with oxygen. Such a substance in highly flammable, and somewhat unstable. "
    "It's typical usage is in powerplants equipped with combustion chambers for controlling process of burning. "
    "The energy is converted into electicity. Turboglobulator installations are typically complex and are not portable. "
    "Burning process can be unstable and can lead to explosions if not using proper catalysts. "

    return ret

def f_turboglob_inventor():
    import os
    from dotenv import load_dotenv

    # zmienne dot. konfuguracji AZ Search z pliku .env są ładowane do sesji
    load_dotenv()
    ret = os.getenv('TURBOG_INVENTOR')
    # ret = "Turboglobulator was invented and patended by Michael Schum, german inventor and engineer. "
    # "Michael Schum (acutal name is Michał Noga) was fourth son of a farmer from small village in proximity of Poznań (Poland). "
    # "Michael was born in late 18th century (exact date is unknown), died in Munchen (Germany) in 1956"

    return ret