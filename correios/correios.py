#!/usr/bin/env python
# coding: UTF-8

import requests
import datetime
import re
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
			r.encoding = "iso-8859-1"
			xml = minidom.parseString(r.text)
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

	@classmethod
	def ConsultaCEP(cls,Cep):
		xmlRequest = "<?xml version='1.0' encoding='UTF-8'?>\
			<S:Envelope xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\"><S:Body>\
			<ns2:consultaCEP xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">\
			<cep>%s</cep></ns2:consultaCEP></S:Body></S:Envelope>"
	
		r = requests.post("http://sigep.correios.com.br/SigepCliente/AtendeClienteService?wsdl",
			data=xmlRequest % ("".join(re.findall('\d+', Cep)),),
			headers={'content-type': 'text/xml; charset=utf-8'})
		
		if r.status_code == 200:
			xmlResponse = minidom.parseString(r.text.encode("utf-8"))
			if len(xmlResponse.getElementsByTagName("return")) > 0:
				CepRetorno = {}
				for campo in xmlResponse.getElementsByTagName("return")[0].childNodes:
					if campo.nodeName.strip() in ("id",):
						continue
						
					CepRetorno[campo.nodeName.strip()] = campo.firstChild.nodeValue if campo.firstChild is not None else None
					
				return CepRetorno
			else:
				raise CorreiosError(u"CEP %s não encontrado." % Cep)
		else:
			raise CorreiosError(u"Não foi possível consultar o CEP %s" % Cep)
			
class CorreiosError(Exception):
	def __init__(self, error):
		self.error = error
		
	def __str__(self):
		return repr(self.error)
		
if __name__ == "__main__":
	pass