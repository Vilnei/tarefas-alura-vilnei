import mysql.connector
from mysql.connector import errorcode


print("Conectando...")

try:
      conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='12345678'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)


cursor = conn.cursor()


if __name__ == '__main__':

      cursor.execute("DROP DATABASE IF EXISTS `pagnando`;")
      cursor.execute("CREATE DATABASE `pagnando`;")
      cursor.execute("USE `pagnando`;")

      TABLES = {}
      TABLES['Qrcode'] = ('''
            CREATE TABLE `qrcode` (
            `qrcode` varchar(4) NOT NULL,
            `valor` decimal(9,2) NOT NULL,
            PRIMARY KEY (`qrcode`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

      TABLES['Usuario'] = ('''
            CREATE TABLE `usuario` (
            `nome` varchar(20) NOT NULL,
            `apelido` varchar(10) NOT NULL,
            `senha` varchar(20) NOT NULL,
            PRIMARY KEY (`apelido`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')
      
      TABLES['Acoes'] = ('''
            CREATE TABLE `acoes` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `apelido` VARCHAR(10) NOT NULL,
            `data` DATETIME NOT NULL,
            `acoes` VARCHAR(100) NOT NULL,
            PRIMARY KEY (`id`)          
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

      for tabela_nome in TABLES:
            tabela_sql = TABLES[tabela_nome]
            try:
                  print('Criando tabela {}:'.format(tabela_nome), end=' ')
                  cursor.execute(tabela_sql)
            except mysql.connector.Error as err:
                  if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print('Já existe')
                  else:
                        print(err.msg)
            else:
                  print('OK')

      usuarios_sql = 'INSERT INTO usuario (nome, apelido, senha) VALUES (%s, %s, %s)'
      usuario = [
                  ("Vilnei", "Vilnei", "1234"),
                  ("Fernando", "Fernando", "Deussejalouvado"),
                  ("Administrador", "admin", "adminando")
            ]
      cursor.executemany(usuarios_sql, usuario)


      cursor.execute('select * from pagnando.usuario')
      print(' -------------  Usuários:  -------------')
      for user in cursor.fetchall():
          print(user[1])


      qrcodes_sql = 'INSERT INTO qrcode (qrcode, valor) VALUES (%s, %s)'
      qrcode = [('a000','00'),('a001','00'),('a002','00'),('a003','00'),('a004','00'),('a005','00'),('a006','00'),('a007','00'),('a008','00'),('a009','00'),
                  ('a010','00'),('a011','00'),('a012','00'),('a013','00'),('a014','00'),('a015','00'),('a016','00'),('a017','00'),('a018','00'),('a019','00'),
                  ('a020','00'),('a021','00'),('a022','00'),('a023','00'),('a024','00'),('a025','00'),('a026','00'),('a027','00'),('a028','00'),('a029','00'),
                  ('a030','00'),('a031','00'),('a032','00'),('a033','00'),('a034','00'),('a035','00'),('a036','00'),('a037','00'),('a038','00'),('a039','00'),
                  ('a040','00'),('a041','00'),('a042','00'),('a043','00'),('a044','00'),('a045','00'),('a046','00'),('a047','00'),('a048','00'),('a049','00'),
                  ('a050','00'),('a051','00'),('a052','00'),('a053','00'),('a054','00'),('a055','00'),('a056','00'),('a057','00'),('a058','00'),('a059','00'),
                  ('a060','00'),('a061','00'),('a062','00'),('a063','00'),('a064','00'),('a065','00'),('a066','00'),('a067','00'),('a068','00'),('a069','00'),
                  ('a070','00'),('a071','00'),('a072','00'),('a073','00'),('a074','00'),('a075','00'),('a076','00'),('a077','00'),('a078','00'),('a079','00'),
                  ('a080','00'),('a081','00'),('a082','00'),('a083','00'),('a084','00'),('a085','00'),('a086','00'),('a087','00'),('a088','00'),('a089','00'),
                  ('a090','00'),('a091','00'),('a092','00'),('a093','00'),('a094','00'),('a095','00'),('a096','00'),('a097','00'),('a098','00'),('a099','00')
      ]
      cursor.executemany(qrcodes_sql, qrcode)

      cursor.execute('select * from pagnando.qrcode')
      print(' -------------  Jogos:  ----------------')
      for qrcode in cursor.fetchall():
          print(qrcode[1])

      conn.commit()

cursor.close()
conn.close()
