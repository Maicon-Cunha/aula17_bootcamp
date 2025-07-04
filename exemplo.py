from sqlalchemy import create_engine

#conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida")