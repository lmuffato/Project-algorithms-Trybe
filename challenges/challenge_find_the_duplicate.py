def find_duplicate(nums):
    """ Faça o código aqui. """
    # BRINCANDO PARA TESTAR ALGUMAS LÓGICAS - Passando 2/5 dos testes
    # Testes não aceitaram "type(nums) == str" e "nums < 0" como válido!
    if (not nums or type(nums) == str or len(nums) == 1 or nums < 0):
        return False
