import hashlib

def verifica_senha(senha_obt, hash_arm):
    s_bytes = senha_obt.encode()
    
    hash_obj = hashlib.sha256()
    
    hash_obj.update(s_bytes)
    s_hash = hash_obj.hexdigest()
    
    return s_hash == hash_arm

def main():
    try:
        with open('senha.txt') as f:
            senha = f.readlines()
    except IOError:
        print("Nao foi possivel ler o arquivo senha.txt")
        
    try:
        with open('senha_cript.txt') as f:
            hash_arm = f.readlines()[0].strip()
    except IOError:
        print("Nao foi possivel ler o arquivo senha_cript.txt")
    
    senha_obt = senha[0].strip()

    
    if verifica_senha(senha_obt, hash_arm):
        print(f'A senha "{senha_obt}" está correta')
    else:
        print(f'A senha "{senha_obt}" está incorreta')

main()
