from modules.costoenvio.CostoEnvioDAO import CostoEnvioDAO
from modules.costoenvio.CostoEnvioService import CostoEnvioService


def main():
    costo_envio_service = CostoEnvioService(CostoEnvioDAO())
    #costo_envio_service.calcular("peru", 9)
    costo_envio_service.calcular("Peru", 8)
    costo_envio_service.actualizar_costo("Peru", 200)

if __name__ == "__main__":
    main()
