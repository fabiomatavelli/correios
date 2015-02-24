#!/usr/bin/env python
# coding: UTF-8

import requests
import datetime
from xml.dom import minidom

__author__ = "Fábio Matavelli"
__email__ = "fabiomatavelli@gmail.com"
__license__ = "GPL"

class Correios:
	@classmethod
	def Rastreia(cls,Objetos,Tipo="L",Resultado="U"):
		if isinstance(Objetos,list):
			Objetos = "".join(Objetos)
		
		r = requests.post("http://websro.correios.com.br/sro_bin/sroii_xml.eventos",params={"Usuario":"ECT","Senha":"SRO","Tipo":Tipo,"Resultado":Resultado,"Objetos":Objetos})
		if r.status_code == 200:
			xml = minidom.parseString(r.text.encode("iso-8859-1"))
			if len(xml.getElementsByTagName("error")) > 0:
				errorMsg = xml.getElementsByTagName("error")[0].firstChild.nodeValue
				raise CorreiosError(errorMsg)
			else:
				_Objetos = {}
				for objeto in xml.getElementsByTagName("objeto"):
					numero = "".join([_numero.firstChild.nodeValue for _numero in objeto.getElementsByTagName("numero")])
					
					if len(numero) == 13:
						_Objetos[numero] = []
						
						for evento in objeto.getElementsByTagName("evento"):
							_objeto = {}
							dia=mes=ano=hora=minuto = None
							for _e in evento.childNodes:
								if len(_e.childNodes) > 0:
									if _e.nodeName is not None:
										if _e.nodeName == "data":
											dia,mes,ano = _e.firstChild.nodeValue.strip().split("/")
										elif _e.nodeName == "hora":
											hora,minuto = _e.firstChild.nodeValue.strip().split(":")
										else:
											_objeto[_e.nodeName] = _e.firstChild.nodeValue.strip()
							
							_objeto["data"] = datetime.datetime(int(ano),int(mes),int(dia),int(hora),int(minuto))
							
							_Objetos[numero].append(_objeto)
							
							del _objeto,dia,mes,ano,hora,minuto
							
				return _Objetos
		else:
			raise CorreiosError(u"Não foi possível rastrear o(s) objeto(s) %s" % (Objetos,))

class CorreiosError(Exception):
	def __init__(self, error):
		self.error = error
		
	def __str__(self):
		return repr(self.error)
		
if __name__ == "__main__":
	pass