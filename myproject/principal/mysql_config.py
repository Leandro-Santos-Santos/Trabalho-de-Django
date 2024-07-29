import mysql.connector

  
def conecta_no_banco_de_dados():
 
    hoc = mysql.connector.connect(host='127.0.0.1',user='root',password='')

    # Executar a instrução SQL para verificar se o banco de dados existe
    cursor = hoc.cursor()
    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "banco01";')

    # Obter o número de resultados
    num_results = cursor.fetchone()[0]

    # Fechar a conexão com o banco de dados
    hoc.close()

    # Se o número de resultados for maior que zero, o banco de dados existe
    if num_results > 0:
        print('O banco de dados banco01 existe e esta pronto para uso.')
    else:
        # Conectar-se ao servidor MySQL para criar o banco de dados
        hoc = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )

        # Criar o banco de dados banco01
        cursor = hoc.cursor()
        cursor.execute('CREATE DATABASE banco01;')
        hoc.commit()

    # Conectar-se ao banco de dados banco01 recém-criado
        hoc = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='banco01'  # Especificar o banco de dados
)

    
        cursor = hoc.cursor()

        cursor.execute('CREATE TABLE contatos (id_contato INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, mensagem TEXT NOT NULL,situacao varchar (50) NOT NULL);')

        cursor.execute('CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255), senha VARCHAR(255));')
        
        cursor.execute('CREATE TABLE pedidos (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255), tipo_hamburguer VARCHAR(50), valor_total DECIMAL(10,2));')

        cursor.execute('CREATE TABLE usuario_contato (usuario_id INT NOT NULL, contato_id INT NOT NULL, situacao VARCHAR(255) NOT NULL, PRIMARY KEY (usuario_id, contato_id), FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE, FOREIGN KEY (contato_id) REFERENCES contatos(id_contato) ON DELETE CASCADE);')
        hoc.commit()
        nome="LEO"
        email="leonardo@gmail.com"
        senha="12345"
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        valores = (nome, email, senha)
        cursor.execute(sql, valores)
        hoc.commit()
        
        hoc.close()
      
    try:
        oracle = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='banco01'
        )
    except mysql.connector.Error as err:
        print("Erro de conexão com o banco de dados:", err)
        raise

    return oracle
