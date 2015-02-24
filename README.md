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
{u'DG952125460BR': [{u'status': u'01', u'uf': u'SP', u'tipo': u'OEC', 'data': datetime.datetime(2015, 2, 24, 7, 30), u'cidade': u'Jundiai', u'sto': u'74654209', u'codigo': u'13211970', u'local': u'CEE JUNDIAI', u'descricao': u'Objeto saiu para entrega ao destinat\xe1rio'}], u'DG952125456BR': [{u'status': u'01', u'uf':u'RS', u'tipo': u'BDE', 'data': datetime.datetime(2015, 2, 21, 10, 28), u'cidade': u'Porto Alegre', u'sto': u'00044846', u'recebedor': u'', u'codigo': u'91910972', u'local': u'CEE PORTO ALEGRE SUL', u'comentario': u'', u'descricao': u'Objeto entregue ao destinat\xe1rio', u'documento': u''}]}
```