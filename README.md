Correios - API Python
========================

API para consumo de serviços do Correios.

## Dependências
- requests - [python-requests.org](http://docs.python-requests.org/en/latest/)

## Exemplos
- Rastreia
```python

>>> from correios.correios import Correios
>>> Correios.Rastreia(Objetos=["DG952125456BR","DG952125460BR"])
{u'DG952125460BR': [{u'status': u'01', u'uf': u'SP', u'tipo': u'BDE', 'data': da
tetime.datetime(2015, 2, 24, 17, 3), u'cidade': u'Jundiai', u'sto': u'74654209',
 u'recebedor': u'', u'codigo': u'13211970', u'local': u'CEE JUNDIAI', u'comentar
io': u'', u'descricao': u'Objeto entregue ao destinatário', u'documento': u''
}], u'DG952125456BR': [{u'status': u'01', u'uf': u'RS', u'tipo': u'BDE', 'data':
 datetime.datetime(2015, 2, 21, 10, 28), u'cidade': u'Porto Alegre', u'sto': u'0
0044846', u'recebedor': u'', u'codigo': u'91910972', u'local': u'CEE PORTO ALEGR
E SUL', u'comentario': u'', u'descricao': u'Objeto entregue ao destinatário',
 u'documento': u''}]}

>>> Correios.Rastreia(Objetos=["DG952125456BR","DG952125460BR"],Resultado="T")
{u'DG952125460BR': [{u'status': u'01', u'uf': u'SP', u'tipo': u'OEC', 'data': da
tetime.datetime(2015, 2, 24, 7, 30), u'cidade': u'Jundiai', u'sto': u'74654209',
 u'codigo': u'13211970', u'local': u'CEE JUNDIAI', u'descricao': u'Objeto saiu p
ara entrega ao destinatário'}, {u'status': u'01', u'uf': u'SP', u'tipo': u'DO
', 'data': datetime.datetime(2015, 2, 20, 6, 56), u'cidade': u'Valinhos', u'sto'
: u'00027770', u'destino': u'', u'codigo': u'13050971', u'local': u'CTE CAMPINAS
', u'descricao': u'Objeto encaminhado'}, {u'status': u'01', u'uf': u'SP', u'tipo
': u'DO', 'data': datetime.datetime(2015, 2, 19, 22, 50), u'cidade': u'Sao Paulo
', u'sto': u'00025587', u'destino': u'', u'codigo': u'05314979', u'local': u'CTE
 JAGUARE', u'descricao': u'Objeto encaminhado'}, {u'status': u'01', u'uf': u'SP'
, u'tipo': u'RO', 'data': datetime.datetime(2015, 2, 19, 21, 40), u'cidade': u'S
ao Paulo', u'sto': u'72657006', u'destino': u'', u'codigo': u'05042970', u'local
': u'CEE LAPA', u'descricao': u'Objeto encaminhado'}, {u'status': u'01', u'uf':
u'SP', u'tipo': u'PO', 'data': datetime.datetime(2015, 2, 19, 18, 14), u'cidade'
: u'Sao Paulo', u'sto': u'72657006', u'codigo': u'05042970', u'local': u'CEE LAP
A', u'descricao': u'Objeto postado'}], u'DG952125456BR': [{u'status': u'01', u'u
f': u'RS', u'tipo': u'BDE', 'data': datetime.datetime(2015, 2, 21, 10, 28), u'ci
dade': u'Porto Alegre', u'sto': u'00044846', u'recebedor': u'', u'codigo': u'919
10972', u'local': u'CEE PORTO ALEGRE SUL', u'comentario': u'', u'descricao': u'O
bjeto entregue ao destinatário', u'documento': u''}, {u'status': u'01', u'uf'
: u'RS', u'tipo': u'OEC', 'data': datetime.datetime(2015, 2, 21, 8, 48), u'cidad
e': u'Porto Alegre', u'sto': u'00044846', u'codigo': u'91910972', u'local': u'CE
E PORTO ALEGRE SUL', u'descricao': u'Objeto saiu para entrega ao destinatário
'}, {u'status': u'20', u'uf': u'RS', u'tipo': u'BDE', 'data': datetime.datetime(
2015, 2, 20, 17, 56), u'cidade': u'Porto Alegre', u'sto': u'00044846', u'codigo'
: u'91910972', u'local': u'CEE PORTO ALEGRE SUL', u'descricao': u'A entrega não
pode ser efetuada - Carteiro não atendido'}, {u'status': u'01', u'uf': u'R
S', u'tipo': u'OEC', 'data': datetime.datetime(2015, 2, 20, 10, 36), u'cidade':
u'Porto Alegre', u'sto': u'00044846', u'codigo': u'91910972', u'local': u'CEE PO
RTO ALEGRE SUL', u'descricao': u'Objeto saiu para entrega ao destinatário'},
{u'status': u'01', u'uf': u'RS', u'tipo': u'DO', 'data': datetime.datetime(2015,
 2, 20, 8, 36), u'cidade': u'Porto Alegre', u'sto': u'00030478', u'destino': u''
, u'codigo': u'90240971', u'local': u'CTE PORTO ALEGRE', u'descricao': u'Objeto
encaminhado'}, {u'status': u'01', u'uf': u'SP', u'tipo': u'DO', 'data': datetime
.datetime(2015, 2, 19, 22, 36), u'cidade': u'Sao Paulo', u'sto': u'00025587', u'
destino': u'', u'codigo': u'05314979', u'local': u'CTE JAGUARE', u'descricao': u
'Objeto encaminhado'}, {u'status': u'01', u'uf': u'SP', u'tipo': u'RO', 'data':
datetime.datetime(2015, 2, 19, 21, 40), u'cidade': u'Sao Paulo', u'sto': u'72657
006', u'destino': u'', u'codigo': u'05042970', u'local': u'CEE LAPA', u'descrica
o': u'Objeto encaminhado'}, {u'status': u'01', u'uf': u'SP', u'tipo': u'PO', 'da
ta': datetime.datetime(2015, 2, 19, 18, 14), u'cidade': u'Sao Paulo', u'sto': u'
72657006', u'codigo': u'05042970', u'local': u'CEE LAPA', u'descricao': u'Objeto
 postado'}]}
```

- ConsultaCEP
```python

>>> from correios.correios import Correios
>>> Correios.ConsultaCEP(Cep="01310300")
{u'end': u'Avenida Paulista', u'bairro': u'Bela Vista', u'cidade': u'São Paulo',
u'complemento2': u'- de 2134 ao fim - lado par', u'cep': u'01310300', u'comp
lemento': None, u'uf': u'SP'}
```