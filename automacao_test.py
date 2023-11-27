from automacao import verifica_senha
import hashlib


def test_check_password():
    s = "senha123"
    
    s_bytes = s.encode()
    hash_obj = hashlib.sha256()
    
    hash_obj.update(s_bytes)
    s_hash = hash_obj.hexdigest()
    
    assert verifica_senha("senha123", s_hash) is True
    assert verifica_senha("senha456", s_hash) is False
