from pydantic import BaseModel


class Adder(BaseModel):
    """
    Classe de teste para criar a operação de adição.
    """

    def Add(self, *args: int) -> float:
        """Soma todos os argumentos fornecidos e retorna o resultado."""
        return sum(args)
