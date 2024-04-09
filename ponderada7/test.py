import unittest
import subprocess
import time

class TestMQTT_KafkaIntegration(unittest.TestCase):
    def test_integration(self):
        # Inicia o consumer em um processo separado
        consumer_process = subprocess.Popen(["python3", "consumer.py"])
        # Aguarda um curto período de tempo para garantir que o consumer esteja pronto
        time.sleep(3)
        # Executa o publisher
        publisher_process = subprocess.Popen(["python3", "publisher.py"])
        # Aguarda até que ambos os processos terminem
        publisher_process.wait()
        consumer_process.wait()
        
        # Verifica se os processos de publisher e consumer foram concluídos sem erros
        self.assertEqual(publisher_process.returncode, 0)
        self.assertEqual(consumer_process.returncode, 0)

if __name__ == "__main__":
    unittest.main()
