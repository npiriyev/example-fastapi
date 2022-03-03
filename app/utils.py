from passlib.context import CryptContext

pwd = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash(password : str):
    return pwd.hash(password)

def check_hash(input_password:str , db_password:str):
    ret = pwd.verify(input_password, db_password)
    return ret