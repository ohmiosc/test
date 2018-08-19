import unittest

from modules.costoenvio.CostoEnvioDAO import CostoEnvioDAO
from modules.costoenvio.CostoEnvioService import CostoEnvioService


class TestCostoEnvioService(unittest.TestCase):

    def test_calcular_pesoMenorAlMaximo_costoIgualCostoPais(self):
        costo_envio_service = CostoEnvioService()

        costo = costo_envio_service.calcular("Peru", 1)

        self.assertEqual(100, costo)

    def test_actualizarCosto_costoValido_grabaCosto(self):
        costo_envio_service = CostoEnvioService()

        costo_envio_service.actualizar_costo("Peru", 50)

        dao = CostoEnvioDAO()
        costo = dao.obtener("Peru")
        self.assertEquals(50, costo)


if __name__ == '__main__':
    unittest.main()
